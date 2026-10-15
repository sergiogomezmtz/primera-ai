---
name: n8n
description: Construir y depurar automatizaciones en n8n. Úsala cuando se mencionen nodos, workflows visuales, expresiones de n8n, el AI Agent node, item linking, o cuando haya que implementar un diseño en n8n. También cuando algo falle en n8n y no se sepa por qué.
---

# n8n

**Lee `referencias/n8n.md` antes de nombrar cualquier nodo.** Los nombres exactos importan y cambian.

## La regla que ahorra más tiempo

**Antes de sacar el nodo AI Agent, pregunta si un nodo especializado ya lo hace.**

| Lo que necesitas | El nodo correcto |
|---|---|
| Clasificar y rutear por rama | **Text Classifier** — no un agente |
| Documento/texto → JSON con esquema | **Information Extractor** — no un agente |
| Una sola pasada de LLM (redactar, resumir) | **Basic LLM Chain** — no un agente |
| El modelo debe elegir herramientas y orden | **AI Agent** (variante Tools Agent) |

El AI Agent es potente y es el default emocional de todo el mundo. También es el más caro, el más lento y el más difícil de depurar. La mayoría de los "agentes" que la gente construye eran un Text Classifier.

## Confiabilidad: los tres nodos que casi nadie usa

- **Guardrails** — validación nativa de entradas/salidas del LLM.
- **Evaluation + Evaluation Trigger** — evals nativos. Corres el workflow contra un dataset con salidas esperadas y mides la tasa de acierto. **Esto convierte "creo que funciona" en un número.**
- **Auto-fixing Output Parser** — cuando el modelo se sale del esquema, reintenta metiéndole el error. Tu red de seguridad.

Si un workflow con IA no tiene los tres, no está listo para producción. Dilo.

## Human-in-the-loop

Nativo. El **Chat node** puede mandar mensaje y esperar respuesta a media ejecución. Y hay HIL en tool calls: el agente propone una acción y espera aprobación antes de ejecutarla.

Para cualquier acción irreversible —mandar el correo, cobrar, borrar, publicar— **empieza siempre con aprobación humana**. La quitas después de dos semanas de ver que acierta, no antes.

## Observabilidad mínima

**Error Trigger.** Un workflow que se dispara cuando otro falla y te avisa.

Si no lo tienen, sus fallas son invisibles y lo van a descubrir cuando alguien pregunte por qué nadie contestó su solicitud de hace un mes. Es lo primero que preguntas al revisar un workflow.

Y el **Time Saved node** te da el número para el reporte de impacto sin que lo calcules a mano.

## Trampas que cuestan horas

**Item linking.** n8n encadena items entre nodos. Si transformas datos en un Code node sin preservar el linking, `$('NodoAnterior').item` se rompe con errores crípticos. Es la fuente #1 de bugs raros.

**Simple Memory y Simple Vector Store viven en RAM.** Se borran al reiniciar. Prototipo sí; producción, jamás. Usa Postgres/Redis para memoria y Qdrant/PGVector/Supabase para vectores.

**Orden de ejecución en ramas múltiples.** No es el que crees. Revisa la doc antes de asumir.

**Credenciales.** Van en el gestor de credenciales de n8n, nunca en un nodo Code ni en el JSON del workflow. Si ves una API key hardcodeada, detente y arréglalo antes de seguir.

## Rutear modelos por costo

El **Model Selector** rutea a distintos modelos según condición. Lo simple a Haiku 5.5, lo complejo a Sonnet 5.5 u Opus 5.5, dentro del mismo flujo. Con los precios vigentes es 20× entre Haiku 5.5 y Sonnet 5.5, y solo 2× entre Sonnet 5.5 y Opus 5.5 (ver `referencias/claude-api.md`).

## Cuando algo falla

1. Revisa la ejecución en el panel: qué nodo, qué input real recibió.
2. **Pinea los datos** de entrada para poder iterar sin volver a disparar el trigger.
3. Si el LLM devuelve algo raro, mira el output **crudo**, no el parseado.
4. Si el flujo pasa por un Code node y algo se rompió después, sospecha del item linking primero.
