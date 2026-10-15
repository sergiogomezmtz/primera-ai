# Patrón 03 — Human-in-the-loop

**El agente propone. El humano aprueba. Solo entonces se ejecuta.**

Obligatorio en cualquier acción irreversible: mandar el correo, cobrar, borrar, publicar, firmar.

## Por qué no es opcional

El costo del error es **asimétrico**. Ahorras 30 segundos y pierdes un cliente. Ninguna tasa de acierto justifica una acción irreversible automática en las primeras semanas.

Y es tu defensa real contra inyección de prompt. Si el agente lee contenido externo (correos, formularios, web), ese contenido puede traer instrucciones. El prompt no te protege. El humano en el bucle sí.

## Estructura

```
Trigger
   ↓
Agente / LLM genera la propuesta
   ↓
Formatear para revisión        ← que el humano entienda en 5 segundos qué va a pasar
   ↓
Chat node: "enviar y esperar respuesta"   ← o Slack / correo con botones
   ↓
├─ Aprobado    → ejecutar la acción
├─ Editado     → ejecutar la versión editada
└─ Rechazado   → log + no ejecutar
   ↓
Registrar la decisión          ← ESTO es lo que casi nadie hace
```

En n8n es nativo: el **Chat node** con *Send a message and wait for response*, y human-in-the-loop en los tool calls del agente.

## El paso que todos se saltan

**Registrar cada decisión humana.** Aprobado / editado / rechazado, y qué cambió cuando editaron.

Eso te da dos cosas:
1. **Tu dataset de evals, gratis.** Los rechazos son tus casos límite reales. Los edits te dicen exactamente en qué se equivoca el modelo.
2. **El criterio para quitar el humano.** Cuando la tasa de aprobación sin edición sea alta y estable durante semanas, puedes automatizar. Con datos, no con corazonada.

Sin este registro, el humano se queda en el bucle para siempre y el ROI nunca llega.

## Cómo se presenta la propuesta

El humano va a aprobar 40 de estas al día. Si le toma 2 minutos entender cada una, no ahorraste nada — moviste el trabajo.

- Lo importante primero. La acción exacta que se va a ejecutar, en una línea.
- El razonamiento del agente, colapsado.
- Un botón. Dos si acaso.

Si la revisión toma más de 15 segundos, el diseño está mal.

## Cuándo quitarlo

Nunca "porque ya confío". Solo con el número: tasa de aprobación sin edición, sostenida, sobre un volumen que importe.

Y aun entonces: en las acciones más caras, se queda. Para siempre.
