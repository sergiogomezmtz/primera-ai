# S4 — Guion del facilitador

**Objetivo:** que otra persona pueda operar el sistema con límites claros, reconocer una falla y saber qué hacer.

**Guía técnica:** [`curso/S4-gobernanza.md`](../curso/S4-gobernanza.md)
**Cierre:** [`proyectos/CHECKLIST-demo.md`](../proyectos/CHECKLIST-demo.md) y [`proyectos/PLANTILLA-handoff.md`](../proyectos/PLANTILLA-handoff.md)

## Agenda de 150 minutos

| Minutos | Tú haces | El Aprendedor(a) produce | Pregunta de transición |
|---:|---|---|---|
| 0–20 | Recuperas permisos y acciones irreversibles | Riesgo principal identificado | “¿Qué puede hacer el sistema que no debería hacer solo?” |
| 20–45 | Corres `/auditar` y limitas el foco | Hasta tres hallazgos prioritarios | “¿Cuál duele más en producción?” |
| 45–75 | Acompañas permisos mínimos y tope de gasto | Matriz de gobernanza | “¿Cuál es el límite duro fuera del prompt?” |
| 75–100 | Diseñas aprobación humana y observabilidad | Gate + señal de falla | “¿Cómo te enteras si falla?” |
| 100–120 | Corres `/eval` en modo sistema/importado o declaras BLOQUEADO | Tasa o bloqueo honesto | “¿Qué mide el sistema completo?” |
| 120–140 | Pides una mejora guiada por evidencia | Antes/después | “¿Qué arreglaste y qué podría haber roto?” |
| 140–150 | Haces demo por parejas y handoff | Evidencia de operación | “¿Puede tu pareja correr una prueba sin ti?” |

## Qué debe verse en la demo

1. Una entrada normal.
2. Una entrada límite o adversarial.
3. La verificación externa.
4. El límite humano antes de una acción irreversible.
5. La señal de falla y el plan de recuperación.
6. El handoff que permite a la pareja operar una prueba.

## Frases útiles

- “El límite duro vive en el entorno, no solo en el prompt.”
- “Human-in-the-loop no significa aprobar cada paso; significa reservar la aprobación para lo irreversible.”
- “Si el flujo completo no corre, `BLOQUEADO` es mejor que una tasa inventada.”
- “La demo no evalúa la cantidad de archivos; evalúa criterio, evidencia y operabilidad.”

## Señales de atasco

| Señal | Intervención |
|---|---|
| Lista muchos guardrails sin decidir ninguno | Pide un permiso, un costo, un gate y una alerta concretos |
| Quiere conectar datos reales sensibles | Devuelve al dataset sintético o anonimizado |
| Confunde tasa de prompt con tasa de sistema | Pide separar modo escritorio, sistema e importado |
| El handoff es una descripción | Pide una prueba de humo y una acción de recuperación |
| La pareja no puede operar | Trata la falla como evidencia del producto, no como culpa de la pareja |

## Extensión para avanzados

Solo después del cierre común:

- completar suite extendida;
- medir costo y confianza;
- mejorar el harness;
- comparar agente único y multiagente;
- justificar una arquitectura S5.
