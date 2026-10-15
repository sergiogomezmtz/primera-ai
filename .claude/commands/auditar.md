---
description: Revisión crítica — qué parte de tu sistema es teatro
---

Audita la automatización. Lee todo lo que haya en `proyectos/<nombre>/`, más el código y las configuraciones que existan.

Tu trabajo aquí **no es ayudar**. Es encontrar lo que está mal antes de que lo encuentre un cliente, o el sistema cayéndose un martes a las 3 de la mañana.

Sé duro. Esta persona puede con la verdad y la necesita ahora, no después.

## Qué buscar

**Teatro.** ¿Qué parte funciona solo en la demo? Datos limpios, caso perfecto, humano al volante sin admitirlo.

**Línea base fantasma.** ¿Los números de "antes" están medidos o inventados? Si son inventados, el ROI es humo.

**IA donde iba un `if`.** ¿Dónde está pagando tokens, latencia y no-determinismo por algo que una condición resolvía mejor?

**`if` donde iba IA.** Lo contrario también existe. Reglas rígidas para ambigüedad real: falla en silencio en todos los casos que no previó.

**Agente donde iba workflow.** ¿Se puede dibujar el diagrama completo? Entonces el agente es un lujo caro y no determinista.

**Camino feliz.** ¿Qué falla no está manejada? De las cuatro familias (API cae / IA se sale del carril / input basura / saturación), ¿cuáles faltan?

**Sin evals.** ¿Puede decir la tasa de acierto con un número? Si no, "funciona bien" es una opinión.

**Sin observabilidad.** ¿Cómo se entera de que falló? Si no hay Error Trigger ni alerta, las fallas son invisibles.

**Sin tope de gasto.** ¿Hay límite en la consola? Un loop con API de pago es una factura sin techo.

**Acción irreversible sin humano.** Manda correos, cobra, borra o publica sin aprobación. Riesgo asimétrico.

**Credenciales expuestas.** En el repo, en un nodo Code, en el JSON del workflow.

**Fragilidad de conocimiento.** ¿Hay partes del sistema que no entiende? Si tú las generaste y las aceptó sin preguntar, eso es deuda. Señálalo y explícaselas.

## Formato

Máximo 5 hallazgos, ordenados por lo que más le va a doler.

Por cada uno:
- **Qué está mal** — una línea, directa
- **Cuándo te va a cobrar** — en producción, en la demo, la primera semana
- **Qué hacer** — concreto, hoy

Si algo está genuinamente bien hecho, dilo. Una línea, sin fiesta.

Escribe el resultado en `proyectos/<nombre>/auditoria-<fecha>.md`.
