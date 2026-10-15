---
name: harness-y-loops
description: Diseñar el andamio que rodea al modelo. Úsala cuando el sistema llame al LLM más de una vez, cuando haya un agente que itera, cuando una tarea no quepa en una sola ventana de contexto, o cuando el agente se pierda, se declare terminado antes de tiempo, entre en loops o se quede sin contexto a media tarea. También cuando alguien quiera "mejorar el agente" y la respuesta real sea cambiar el andamio, no el modelo.
---

# Harness y loop engineering

**Lee `referencias/harness.md` para las fuentes.**

## La tesis

El modelo es **una llamada**. El harness es **todo lo demás**: qué entra al contexto, qué herramientas existen, cuándo para el loop, quién verifica que funcionó, qué se reintenta, qué escala a humano.

**El harness importa más que el modelo.** Un modelo bueno con un harness ingenuo pierde contra un modelo mediano con un harness bien diseñado. Cuando alguien te diga "el agente no funciona, ¿cambio a Opus?", casi siempre la respuesta es: no, arregla el harness.

Anthropic lo probó con el caso más favorable posible: un modelo frontera, en el Claude Agent SDK, en loop, con compactación de contexto, y el prompt "construye un clon de claude.ai". **Falló.** No por el modelo — por falta de andamio.

## El loop, completo

```
observar → planear → actuar → VERIFICAR → repetir
                                   ↑
                        aquí es donde casi todos fallan
```

La mayoría construye `observar → actuar → repetir`. Sin verificación, el loop no sabe si avanzó. Y un modelo **siempre** cree que avanzó.

## Los dos modos de falla de todo loop largo

Vienen del artículo de Anthropic, y los vas a ver en cualquier agente que corra más de una sesión:

**1. Quiere hacerlo todo de un jalón.** Se le acaba el contexto a media implementación y deja la cosa a medias, sin documentar. La siguiente sesión tiene que adivinar qué pasó y se gasta el tiempo reparando en vez de avanzando.

**2. Se declara victorioso antes de tiempo.** Una sesión posterior mira alrededor, ve que hay progreso, y anuncia que terminó. Con features sin construir.

**La compactación de contexto no basta.** Comprime, pero no le pasa instrucciones limpias al siguiente. Este es el punto que casi todo el mundo se salta.

## La solución: dos agentes, un solo harness

No son dos sistemas. Es el **mismo harness con distinto primer prompt**.

**Agente inicializador** (corre una vez, la primera):
- Escribe la **lista de features** — el spec expandido, exhaustivo
- Crea el **archivo de progreso**
- Inicializa git y hace el primer commit
- Escribe un **`init.sh`** que levanta el entorno

**Agente de trabajo** (cada sesión posterior):
- Se orienta (protocolo abajo)
- Escoge **una sola feature**
- La construye, la **verifica de verdad**, la marca
- Deja el entorno limpio: commit + actualiza el progreso

## Los cuatro artefactos

### 1. Lista de features (JSON, no Markdown)

Detalle no obvio y verificado: **usa JSON**. El modelo es menos propenso a sobreescribir o "arreglar" un JSON que un Markdown. Con Markdown se pone creativo.

```json
{
  "category": "functional",
  "description": "El botón de nuevo chat crea una conversación limpia",
  "steps": ["Navegar a la interfaz", "Clic en 'New Chat'", "Verificar que aparece en el sidebar"],
  "passes": false
}
```

Todas empiezan en `false`. El agente **solo puede cambiar el campo `passes`**. Y dilo con fuerza en el prompt: *"Es inaceptable borrar o editar features. Hacerlo lleva a funcionalidad rota o faltante."* El lenguaje fuerte aquí funciona.

Esta lista es el ancla contra el modo de falla #2. Un agente no puede declarar victoria si hay 47 features en `false`.

### 2. Archivo de progreso

Qué se hizo, qué se decidió, qué está roto, qué sigue. Lo escribe cada sesión al terminar. Lo lee cada sesión al empezar.

Es el turno de guardia: cada ingeniero llega sin memoria del turno anterior. La bitácora es lo único que los une.

### 3. Git

Commits descriptivos por feature. No es higiene: es **la máquina de revertir**. El agente puede volver a un estado que funcionaba cuando rompe algo. Sin git, un mal paso contamina todo lo que sigue.

### 4. `init.sh`

Levanta el entorno con un comando. Ahorra tokens en cada sesión — el agente no tiene que redescubrir cómo se corre el sistema, todas las veces.

## El protocolo de orientación

Cada sesión arranca igual. Suena trivial. No lo es:

1. `pwd` — dónde estoy
2. Leer el archivo de progreso y el `git log`
3. Leer la lista de features → escoger **la de mayor prioridad que no esté hecha**
4. Correr `init.sh` y hacer una **prueba de humo** end-to-end

El paso 4 es el que nadie pone y el que más salva. Si la sesión anterior dejó algo roto, lo detectas **antes** de construir encima. Si en vez de eso empiezas una feature nueva, empeoras el problema.

## Verificación: la parte que decide todo

**El modelo marca cosas como terminadas sin haberlas probado de verdad.** Escribe el código, corre un unit test, hace un `curl` — y no se da cuenta de que la feature no funciona end-to-end.

**La verdad no puede venir del modelo.** Tiene que venir de algo externo:
- Corre el test, no le preguntes si pasaría
- Consulta la base de datos, no le preguntes si escribió
- Abre el navegador, no le preguntes si se ve bien
- Llama la API, no le preguntes si respondería

En el caso de Anthropic, darle automatización de navegador (Puppeteer vía MCP) y decirle *"prueba como lo haría un humano"* cambió el resultado dramáticamente. El agente encontró bugs que eran invisibles desde el código.

**Regla: la condición de parada del loop debe ser verificable por algo que no sea el modelo.** Si tu única señal de éxito es que el modelo dijo "listo", no tienes un sistema. Tienes un optimista.

## Condiciones de parada

Todo loop necesita las cuatro. Si falta una, el loop es un riesgo:

| Tipo | Qué es | Sin esto |
|---|---|---|
| **Éxito** | Condición verificable externamente | El agente no sabe que terminó, o cree que terminó |
| **Presupuesto** | Tope de iteraciones, tokens, dinero, tiempo | Factura sin techo |
| **Sin progreso** | Detecta que se está repitiendo | Loop infinito elegante |
| **Escalamiento** | Cuándo para y pregunta | Adivina y ejecuta |

La de **sin progreso** es la más olvidada: el agente reintenta lo mismo con variaciones cosméticas y nunca avanza. Detecta la repetición (mismo tool call, mismo error, N veces) y **rompe el loop**. No lo dejes descubrirlo solo.

## Contexto: presupuesto, no cubeta

El contexto es un **recurso finito y curado**, no un cajón donde se va acumulando todo. Lo que entra al contexto es una decisión de diseño en cada iteración.

**Context rot:** un error de la iteración 3 se queda en el contexto y contamina las iteraciones 4 a 20. El modelo lo sigue viendo y lo sigue tomando en cuenta.

Tres palancas:
- **Externalizar estado a archivos.** El sistema de archivos es la memoria. Lo que importa se escribe; el contexto es de trabajo, no de almacén.
- **Aislar con sub-agentes.** Una subtarea con contexto limpio no arrastra la basura de la tarea principal. Es la palanca más fuerte, y es de **topología**, no de modelo.
- **Podar.** Resultados de herramientas viejos, intentos fallidos ya superados. Fuera.

## La "altitud" correcta del prompt de sistema

Hay una zona Goldilocks entre dos fallas:

- **Muy bajo:** lógica if-else durísima hardcodeada en el prompt. Frágil, imposible de mantener.
- **Muy alto:** guía vaga que asume contexto compartido y no da señales concretas.

Lo correcto: **específico para guiar, flexible para que el modelo aplique criterio.** Si te encuentras escribiendo `if` dentro de un prompt, o el prompt es un `if`, o el `if` debería estar en el código.

## Dónde vive tu harness

Los participantes ya usan harnesses aunque no los llamen así:

- **Un workflow de n8n es un harness determinista.** Tú fijas el orden. El modelo solo decide dentro de las cajas que le diste.
- **LangGraph es un harness con estado durable.** Checkpointers, HIL, reintentos condicionales, grafos cíclicos.
- **Claude Code + este repo es un harness.** `CLAUDE.md` es el prompt de sistema, `.claude/skills/` son capacidades bajo demanda, `referencias/` es el estado externalizado, `proyectos/` es el archivo de progreso.

Cuando alguien pregunte "¿cómo hago mi agente más confiable?", la respuesta casi nunca es el modelo. Es una de estas tres: **acota el paso, verifica externamente, o pon el estado en disco.**
