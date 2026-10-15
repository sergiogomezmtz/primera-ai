# Ruta de la cohorte

Esta ruta convierte el repositorio en una experiencia de trabajo de 2.5 horas por sesión. La primera sesión técnica de la cohorte es la **Sesión 2 — Panorama de Agent Engineering Q4-2026 y primera medición**. La doctrina sigue viviendo en `CLAUDE.md`; este archivo responde una pregunta distinta: **¿qué hacemos en clase, en qué orden y qué queda listo?**

## Resultado del curso

Al terminar, cada Aprendedor(a) debe poder tomar una automatización real y responder con evidencia:

1. **Qué parte es una regla, qué parte necesita IA y qué parte debe seguir siendo humana.**
2. **Cómo sabe que el sistema terminó bien sin preguntarle al modelo.**
3. **Cuánto acierta sobre una suite de casos conocidos.**
4. **Qué ocurre cuando falla, se sale de alcance o intenta una acción irreversible.**
5. **Cómo lo corre otra persona sin depender del autor.**

No es obligatorio construir un agente autónomo. **Justificar un workflow con un solo paso de IA, o decidir no automatizar todavía, también es un resultado válido.**

El mapa completo de salida está en [`Competencias de Agentic AI`](../docs/competencias.md). La guía de la primera sesión está en [`Sesión 2 — Panorama y primera medición`](S2-panorama-y-evals.md).

## Cómo entrarás

La herramienta no decide la ruta pedagógica. Primero elige una de estas tres entradas:

| Ruta | Úsala si… | Debes demostrar primero |
|---|---|---|
| **1 — Ya tengo algo construido** | Traes automatización, prototipo o sistema | Una falla, cuello de botella o decisión difícil |
| **2 — Quiero descubrir qué agentizar** | Traes proceso o idea, pero no diseño | Proceso acotado, decisión candidata y salida verificable |
| **3 — Camino dorado opcional** | Falta claridad, entorno o confianza | Comprensión del contrato y transferencia hacia Ruta 2 |

Después eliges el medio: **visual** (n8n, Make, Cowork) o **código/API** (Claude Code, Python, TypeScript). El contrato no cambia: entrada, decisión, salida, validación y escalamiento.

La fuente canónica de las tres rutas es [`Rutas de entrada`](../docs/rutas-de-entrada.md).

## Núcleo y extensión

### Núcleo: todas las personas

- Un proceso acotado o el caso común del `ejemplo/`.
- Una sola decisión de IA.
- Seis casos: cuatro típicos, uno límite y uno adversarial. **Es una medición válida, no una suite incompleta.**
- Una salida esperada fijada por la persona.
- Un análisis de un fallo.
- Un criterio de éxito verificable.
- Una matriz mínima de permisos, escalamiento y observabilidad.

### Extensión: para quien termina antes

- Suite extendida de diez casos: cinco típicos, tres límite y dos adversariales.
- Calibración de `confianza` por categoría.
- Corrida end-to-end con datos reales anonimizados.
- Costo por corrida y proyección mensual.
- Loop con cuatro paradas, solo si el flujo realmente itera.
- S5, multiagente: comparación de agente único contra Nest o Swarm. Es extensión avanzada, no requisito común.

La extensión no se usa para avanzar más rápido el calendario ni para convertir el núcleo en una carrera.

## Preflight antes de clase

La continuidad técnica vive en la [Ruta de preparación y continuidad de la Sesión 2](../docs/ruta-continuidad-s2.md). No repitas aquí la instalación: elige ruta, verifica solo sus dependencias y conserva un fallback.

Si algún paso falla, lleva la captura o el mensaje de error; **no intentes resolverlo durante los primeros minutos de clase**. El camino dorado offline o en papel conserva el aprendizaje sin credenciales reales.

## Sesión 2 — Panorama y primera medición

Esta es la primera sesión técnica. La reunión anterior fue de bienvenida y contexto, así que aquí sí se presenta el panorama, se abre Claude Code y se usa el Agente Mentor. La sesión no presupone experiencia técnica ni exige que todas las personas construyan lo mismo.

Consulta la [guía técnica de evals](S2-evals.md) solo para la continuidad posterior; no es una puerta de entrada ni un requisito para comenzar S2.

**Objetivo:** salir con una ruta elegida, el repositorio abierto o un fallback documentado, un proceso/caso, una decisión de IA y tres casos ancla. La suite de seis casos cierra la primera medición después de la sesión.

| Tiempo | Actividad | Checkpoint |
|---:|---|---|
| 0–30 min | Plenaria: Panorama Q4-2026, vocabulario y rutas según experiencia | Cada persona sabe qué track le corresponde |
| 30–65 min | Teoría aplicada: decisión, contrato, eval, 4/1/1 y diagnóstico | Todas las personas entienden el caso común |
| 65–75 min | Break | Bloqueos anotados, no soporte improvisado |
| 75–85 min | Abrir repositorio y Claude Code; confirmar Mentor | Repo abierto o fallback activo |
| 85–100 min | Elegir track y proceso/caso | Una ruta y un proceso |
| 100–115 min | Definir una decisión de IA y qué queda fuera | Contrato inicial |
| 115–135 min | Fijar tres casos ancla | Típico, límite y adversarial con salida esperada |
| 135–145 min | Extensión para quien va rápido: tres casos restantes o `/eval` | Suite parcial o línea base |
| 145–150 min | Cierre y siguiente paso | Entregable mínimo y fecha de los seis casos |

**Entregable de la sesión:** track, proceso/caso, una decisión, tres casos ancla con salidas esperadas y siguiente paso. `proyecto.md`, `flujo.md`, `alcance.md`, `decisiones.md`, `reglas.md` y `evals.md` se completan según la ruta, no como requisito uniforme de los primeros 150 minutos.

**Evidencia, no solo archivos:** la persona puede explicar por qué la decisión es `if`, IA, herramienta o humana, y qué salida esperaría en cada caso ancla. Quien termine la suite añade la tasa `aciertos/6` y la salida cruda de un fallo.

## Sesión 3 — Fallas, verificación y loops

Consulta también la [guía completa de S3](S3-loops.md).

**Objetivo:** distinguir una falla del modelo de una falla de contexto, herramienta o harness.

| Tiempo | Actividad | Checkpoint |
|---:|---|---|
| 0–15 min | Recuperación de la línea base | Comparar número y casos fallidos |
| 15–40 min | Diagnóstico por capas y harness | Nombrar la capa rota y la evidencia |
| 40–55 min | Decidir si hace falta un loop | “No necesito loop” es una salida válida, con su razón escrita |
| 55–85 min | Con loop: `/cuatro-paradas` con números. Sin loop: escribir la verificación externa del paso | Cuatro paradas con números, o un checker que no le pregunta al modelo |
| 85–105 min | Correr una traza, o la suite con el checker | Trabajo y verificación separados |
| 105–135 min | Aplicar un solo ajuste (v0 → v1) y volver a correr `/eval` | Número antes y después |
| 135–150 min | Guardar evidencia y cerrar | `diagnostico.md`, `harness.md`, `evals.md` con v1 y, si aplica, `loop.md` |

**Entregable:** diagnóstico de una falla, una verificación externa y una mejora medida. Solo hay `loop.md` si el flujo realmente necesita iterar.

**Evidencia, no solo archivos:** la capa nombrada con lo que descartó las otras, la comparación v0 → v1 sobre los mismos seis casos, y la traza o la corrida del checker.

## Sesión 4 — Gobernanza, handoff y defensa

Consulta también la [guía completa de S4](S4-gobernanza.md).

**Objetivo:** que otra persona pueda operar el sistema con límites claros.

| Tiempo | Actividad | Checkpoint |
|---:|---|---|
| 0–20 min | Recuperación sobre permisos y acciones irreversibles | Identificar el mayor riesgo |
| 20–45 min | `/auditar`: encontrar el teatro | Los tres hallazgos que más duelen (de máximo cinco) |
| 45–75 min | Permisos mínimos y tope de gasto | Matriz de gobernanza |
| 75–100 min | Human-in-the-loop y Error Trigger | Acción irreversible y señal de falla |
| 100–120 min | Corrida end-to-end con `/eval` | Tasa del sistema, no solo del prompt |
| 120–140 min | Una mejora guiada por evidencia | Comparación antes/después |
| 140–150 min | Demo por parejas y handoff | Preguntas de defensa respondidas |

**Entregable final:** paquete de ejecución con README corto, evals, evidencia de una corrida, gobernanza, limitaciones y qué hacer si falla.

**Evidencia, no solo archivos:** la tasa del sistema en modo sistema (o `BLOQUEADO` con lo que falta), una falla provocada y cómo te enteraste, y tu pareja corriendo una prueba con tu handoff sin ayuda.

## Si algo falla en clase

| Falla | No hagas | Haz esto |
|---|---|---|
| No instala Claude Code | Convertir la clase en soporte técnico | Usa el camino dorado offline |
| Tampoco hay Python | Esperar a que alguien lo instale | Recorre el camino dorado en papel con `ejemplo/casos.json` |
| `/eval` no corre | Inventar la tasa | Corre los casos en tu herramienta o a mano y cuenta contra la salida esperada |
| No autentica una API | Pegar una llave en un archivo | Usa datos sintéticos y deja el punto de integración documentado |
| No existe un proceso real | Inventar una línea base | Trabaja el caso común y marca la transferencia como siguiente paso |
| La herramienta visual no responde | Cambiar de plataforma a mitad de sesión | Completa el contrato y los evals con el formato local |
| Agent Teams no arranca | Depurarlo durante el taller | Usa la conclusión preparada y discute el juicio arquitectónico |

## Criterio de salida

No se evalúa cuántos comandos ejecutaste. Se evalúa si puedes defender estas cinco respuestas:

1. ¿Dónde usas IA y por qué no un `if`?
2. ¿Qué caso te da más miedo?
3. ¿Cómo sabes que funcionó sin preguntarle al modelo?
4. ¿Qué acción nunca dejarías automática?
5. Si tú desapareces mañana, ¿quién lo corre?
