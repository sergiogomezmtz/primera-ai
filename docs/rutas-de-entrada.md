# Rutas de entrada

Esta página es la fuente canónica para decidir **qué hacer primero**. No empieces por la herramienta: empieza por la evidencia que puedes producir hoy.

## Decide en 30 segundos

| Ruta | Elige esta ruta si… | Primer resultado |
|---|---|---|
| **Ruta 1 — Ya tengo algo construido** | Traes una automatización, prototipo o sistema en Cowork, Make, n8n, Claude Code u otra herramienta. | Una falla o cuello de botella que vale la pena medir. |
| **Ruta 2 — Quiero descubrir qué agentizar** | Tienes un proceso, idea o problema real, pero todavía no sabes qué decisión delegar. | Proceso acotado, decisión candidata y tres casos ancla. |
| **Ruta 3 — Camino dorado opcional** | No tienes proceso claro, estás bloqueado técnicamente o quieres ver un ejemplo antes de decidir. | Entendimiento del contrato y transferencia explícita hacia la Ruta 2. |

> **Ruta 2 es la ruta común principal. Ruta 3 es un andamio opcional, no un requisito ni una salida final.**

## Ruta 1 — Ya tengo algo construido

1. No vuelvas a construir desde cero.
2. Elige una sola falla, decisión difícil o cuello de botella.
3. Reúne la evidencia disponible: corrida, prompt, traza, queja, costo o handoff.
4. Usa `/rumbo` solo para fijar foco y alcance si todavía están difusos.
5. Llega a S2 con una decisión que puedas medir y tres casos ancla.

**Tracks habituales:** Construir, Endurecer o Productificar/escalar.

## Ruta 2 — Quiero descubrir qué agentizar

1. Describe el proceso actual en una frase.
2. Nombra quién lo ejecuta, qué entra y qué resultado debe salir.
3. Separa pasos deterministas, decisiones ambiguas, herramientas y acciones humanas.
4. Elige una sola decisión candidata; todo lo demás queda fuera por ahora.
5. Define una salida verificable y tres casos: típico, límite y adversarial.
6. Usa `/rumbo` después de esta conversación si necesitas fijar la ruta formal.

**Checkpoint:** puedes explicar qué vas a medir y qué no vas a construir todavía.

## Ruta 3 — Camino dorado opcional

1. Abre [`ejemplo/README.md`](../ejemplo/README.md).
2. Entiende el caso común antes de ejecutar comandos.
3. Identifica `if`, IA, salida estructurada, validación y humano.
4. Corre la versión offline o recorre `casos.json` en papel.
5. Responde las cinco preguntas de comprensión.
6. Regresa a la Ruta 2: elige un proceso propio o declara que continuarás con el caso común.

El camino dorado enseña el contrato:

```text
if → IA solo para ambigüedad → salida estructurada → validación → humano
```

**No es una prueba de que un modelo real sea bueno.** Es una calibración del harness y del criterio de diseño.

## Qué ruta no debes tomar

- No ejecutes `/rumbo` automáticamente si aún no puedes explicar el proceso o el caso.
- No instales Node/NPM si tu proyecto no los necesita.
- No conviertas un bloqueo de instalación en el objetivo de la sesión.
- No uses el camino dorado para evitar indefinidamente elegir una decisión real.
- No regreses al onboarding a quien ya trae evidencia suficiente.

## Criterio común de llegada a S2

Cualquiera de las tres rutas llega al mismo núcleo:

- proceso o caso en una frase;
- una sola decisión;
- salida esperada verificable;
- tres casos ancla;
- siguiente paso y fallback.

La suite de seis casos, la línea base y `/eval` pertenecen a la continuidad posterior cuando ya existe suelo operativo.

## Si algo falla

| Situación | Ruta inmediata |
|---|---|
| Falta Python | Ruta 2 en papel o Ruta 3 con `casos.json` |
| Claude Code no inicia | Cowork, ZIP o Ruta 3 offline |
| Ya existe un sistema | Ruta 1; no reinicies el curso |
| No hay proceso claro | Ruta 3 primero; después Ruta 2 |
| Hay demasiadas ideas | Ruta 2: elige una y declara las demás fuera de alcance |
