# Patrones

Siete formas. Casi toda automatización de negocio es una de estas, o una composición de dos.

Antes de diseñar desde cero, pregúntate cuál de estas es. Ahorra semanas.

| Patrón | Cuándo | Nodo/pieza clave |
|---|---|---|
| **01 · Clasificar y rutear** | Llega algo, hay que decidir a dónde va | Text Classifier — **no un agente** |
| **02 · Extraer** | Documento/texto → JSON estructurado | Information Extractor |
| **03 · Human-in-the-loop** | El agente propone, el humano aprueba | Chat node / HIL en tool calls |
| **04 · RAG interno** | Responder desde documentos propios | Vector store + retriever |
| **05 · Watcher** | Vigilar algo, actuar cuando cambia | Trigger + estado + condición |
| **06 · Enriquecer** | Tomar un registro, completarlo, escribirlo | Batch API |
| **07 · Loop agéntico** | La tarea no cabe en una pasada ni en una ventana | Harness: progreso + verificación externa |

## El patrón que la gente cree que necesita

Un **agente autónomo con herramientas**, que decide solo qué hacer.

Rara vez es lo correcto. Antes de construirlo, aplica la prueba: *¿puedes dibujar el diagrama de flujo completo?* Si sí, es un workflow. Combina dos de los patrones de arriba y te ahorras el no-determinismo, el costo y el debugging a ciegas.

Cuando de verdad lo necesites — la tarea no cabe en una pasada, el camino no se puede predecir — ve al **patrón 07**. Y constrúyelo con harness, no con esperanza.
