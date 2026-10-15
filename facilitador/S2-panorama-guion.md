# Guion del facilitador — Sesión 2

## Propósito

Esta es la primera sesión técnica de la cohorte. La reunión anterior fue de bienvenida, contexto y orientación; no se presupone que el grupo haya recibido S1 técnica.

El objetivo no es que todas las personas construyan lo mismo. Es que todas salgan con una **decisión observable** y una ruta de trabajo acorde con lo que traen.

> **Mínimo común:** repositorio abierto o fallback activo, Mentor identificado, una decisión de IA, tres casos ancla y una duda concreta.

La suite de seis casos —4 típicos, 1 límite y 1 adversarial— es la entrega inmediata que cierra S2; no la uses como barrera de entrada durante el laboratorio.

## Agenda de 150 minutos

| Tiempo | Tu intervención | Producción de los Aprendedores(as) | Pregunta de control |
|---:|---|---|---|
| 0–5 | Da la bienvenida técnica y presenta el objetivo: pasar de idea a decisión medible | Escuchan la promesa y anotan qué traen | “¿Qué vienes a descubrir, construir, endurecer o escalar?” |
| 5–15 | Explica el panorama Q4-2026: el modelo genera; el sistema organiza, verifica y limita | Vocabulario común | “¿Qué parte de tu problema no debería resolver un LLM?” |
| 15–25 | Distingue workflow, chatbot y agente; introduce `if`, IA, herramienta y humano | Clasifican mentalmente un proceso | “¿Dónde decide realmente tu sistema?” |
| 25–30 | Presenta las tres rutas: sistema existente, descubrir qué agentizar y camino dorado opcional | Eligen su punto de entrada | “¿Qué evidencia puedes producir hoy?” |
| 30–40 | Define eval como input + salida esperada | Entienden qué significa medir | “¿Quién fija la salida correcta?” |
| 40–50 | Presenta 4/1/1 y la regla de cambiar una cosa a la vez | Preparan el tipo de casos que buscarán | “¿Cuál sería tu caso límite?” |
| 50–60 | Muestra el camino dorado: `if → IA → salida estructurada → validación → humano` | Identifican las capas | “¿Dónde se detiene el sistema?” |
| 60–65 | Explica tasa como señal y conecta un fallo con S3 | Entienden el siguiente paso | “¿Qué no nos dice todavía una tasa?” |
| 65–75 | Break | Pausa; anotan bloqueos sin convertirlos en soporte | — |
| 75–85 | Abre el repo y Claude Code en pantalla; muestra el prompt de inspección | Abren su copia o activan fallback | “¿Ves tu carpeta y el nombre del repo?” |
| 85–100 | Circula por los tracks y pide una pregunta a la vez | Definen proceso, estado y ruta | “¿Qué evidencia tienes hoy?” |
| 100–115 | Ayuda a elegir una sola decisión de IA | Escriben la decisión y lo que queda fuera | “¿Por qué IA y no `if`?” |
| 115–135 | Pide tres casos ancla; propone formatos, no respuestas | 1 típico, 1 límite, 1 adversarial con salida esperada | “¿Podrías verificar esa salida sin preguntarle al modelo?” |
| 135–145 | Quien está listo comienza los tres casos restantes o `/eval`; quien no, consolida su nota | Suite parcial o evidencia mínima | “¿Qué sigue después de hoy?” |
| 145–150 | Cierra con ronda rápida y explica la entrega de seis casos | Cada persona verbaliza su siguiente paso | “¿Qué vas a medir primero?” |

Si la teoría ocupa 45 minutos, termina el bloque teórico en el minuto 75 y reduce el laboratorio a 65 minutos. Conserva los tres casos ancla; mueve la suite completa a la entrega inmediata.

## Los cuatro tracks

### Descubrir

La persona tiene un proceso o idea, pero no una automatización. Esta es la Ruta 2: pide usuario, entrada, pasos, decisión y resultado. Si no puede acotar, ofrece el camino dorado como Ruta 3 y después regresa a Ruta 2.

### Construir

La persona tiene un prototipo o automatización personal. Pide que etiquete un flujo como `if`, IA, herramienta o humano y que elija una sola decisión.

### Endurecer

La persona trae un sistema que ya funciona, pero no mide o falla. Esta es la Ruta 1: pide una ejecución, una falla o un prompt actual. No la regreses al camino dorado salvo que lo necesite para explicar el contrato.

### Productificar / escalar

La persona ya lo usa con otras personas. Pide identificar quién lo opera, qué costo o riesgo limita el crecimiento y qué evidencia falta para que otro lo corra. No la regreses a construir desde cero.

## Prompt visible para iniciar Claude Code

```text
Lee CLAUDE.md y ACOMPANAMIENTO.md.
Dime qué repositorio abrí, qué hace el Agente Mentor y qué comandos del proyecto están disponibles.
No edites archivos todavía.
```

Después, por track:

```text
Hazme una pregunta a la vez.
Ayúdame a elegir entre descubrir, construir, endurecer o productificar/escalar.
No inventes mi proceso, mis casos ni mis salidas esperadas.
Si todavía no tengo un proceso acotado, usa el camino dorado como andamio.
```

## Rescates rápidos

| Señal | Intervención |
|---|---|
| No tiene repo | Comparte la plantilla; si tarda, camino dorado offline. |
| Claude Code no inicia | Captura el error y continúa con el ejemplo; no conviertas la sesión en instalación. |
| No entiende “camino dorado” | Abre `ejemplo/README.md`, lee “Qué vas a hacer aquí” y señala el diagrama. |
| Trae tres proyectos | Pide elegir uno; los otros quedan anotados como fuera de alcance. |
| Quiere construir un agente completo | Pregunta cuál es la única decisión que debe tomar. |
| No puede escribir una salida esperada | Reduce la decisión a una categoría, sí/no, valor o escalamiento verificable. |
| Ya tiene sistema avanzado | No lo regreses al onboarding; usa su falla o cuello de botella como caso. |
| Instalación bloqueada | Fallback: tabla manual con `casos.json`, nota y oficina de ayuda posterior. |

## Qué no hacer

- No presentar una revisión histórica del campo como objetivo de esta sesión.
- No asumir que S1 técnica ya ocurrió.
- No exigir `/arrancar` a quien ya trae automatización.
- No exigir seis casos antes de que la persona entienda el caso común.
- No usar diez casos como puerta de entrada.
- No dejar que el Mentor invente las salidas esperadas.
- No resolver tú la decisión por la persona.

## Cierre uniforme

Antes de cerrar, verifica que cada persona pueda decir: **estoy en esta ruta · mi siguiente paso es este · si me bloqueo haré esto · si termino antes haré esta extensión**.

## Cierre uniforme

Antes de cerrar, verifica que cada persona pueda decir: **estoy en esta ruta · mi siguiente paso es este · si me bloqueo haré esto · si termino antes haré esta extensión**.

## Cierre uniforme

Antes de cerrar, verifica que cada persona pueda decir: **estoy en esta ruta · mi siguiente paso es este · si me bloqueo haré esto · si termino antes haré esta extensión**.

## Cierre uniforme

Antes de cerrar, verifica que cada persona pueda decir: **estoy en esta ruta · mi siguiente paso es este · si me bloqueo haré esto · si termino antes haré esta extensión**.

## Cierre uniforme

Antes de cerrar, verifica que cada persona pueda decir: **estoy en esta ruta · mi siguiente paso es este · si me bloqueo haré esto · si termino antes haré esta extensión**.

## Cierre mínimo

Antes de cerrar, verifica que cada persona tenga al menos:

- ruta o track elegido;
- repositorio abierto o fallback documentado;
- proceso/caso en una frase;
- una decisión de IA;
- tres casos ancla con salida esperada;
- siguiente paso para cerrar los seis casos.

Si no tiene proceso propio, el camino dorado es un cierre válido. Si ya tiene sistema, una falla o cuello de botella documentado es una mejor evidencia que una nueva idea.
