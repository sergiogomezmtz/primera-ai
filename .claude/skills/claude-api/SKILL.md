---
name: claude-api
description: Construir directamente contra la API de Claude. Úsala cuando se escriba código que llama a Claude, se elija modelo, se implemente tool use, prompt caching, batch processing o salida estructurada, o cuando haya que decidir entre la API y un nodo visual.
---

# Claude API

**Lee `referencias/claude-api.md` antes de citar precios, modelos o límites. Nunca de memoria.**

## Elegir modelo

| Tarea | Modelo |
|---|---|
| Clasificar, extraer, rutear, resumir | **Haiku 5.5** (`claude-haiku-5-5`) |
| El grueso de la producción | **Sonnet 5.5** (`claude-sonnet-5-5`) |
| Razonamiento complejo, coding agéntico de larga duración | **Opus 5.5** (`claude-opus-5-5`) |
| Máxima capacidad disponible | **Fable 5.1** (`claude-fable-5-1`) |

Empieza por el más barato que resuelva la tarea. Sube solo si los evals te obligan. Casi nadie necesita Opus para clasificar correos, y casi todo el mundo lo intenta.

Dos cosas que cambiaron con esta generación (verificado 9 oct 2026): el salto caro ya no es Sonnet→Opus (2×), es **Haiku→Sonnet (20×)**; y Haiku 5.5 se encarece 5× cuando el prompt pasa de 100k tokens, así que no le metas corpus enteros. Haiku 4.5 sigue vivo pero tiene fecha de retiro: no lo uses para nada nuevo.

## Salida estructurada

El primer camino es **Structured Outputs** (GA, verificado 9 oct 2026): la API compila tu JSON Schema a una gramática y el modelo **no puede** emitir tokens fuera de ella. Se acabó el "pídele JSON y reza".

```json
"output_config": {
  "format": {
    "type": "json_schema",
    "schema": { "type": "object", "properties": {...}, "required": [...], "additionalProperties": false }
  }
}
```

Para herramientas, lo mismo con **`strict: true`** en la definición: el `input` del `tool_use` cumple el `input_schema` siempre, y el nombre de la herramienta siempre es válido. Se pueden combinar en una misma petición.

**Lo que la gramática no te garantiza:**
- `stop_reason: "refusal"` → 200, cobrado, y el texto puede no cumplir el esquema.
- `stop_reason: "max_tokens"` → JSON truncado. Sube `max_tokens`.
- Capitalización de `enum`: compara sin distinguir mayúsculas.
- Subconjunto de JSON Schema: sin recursión, sin `minimum`/`maximum`, sin `minLength`/`maxLength`; `additionalProperties: false` obligatorio. Lo que no cabe en el esquema va al `description` del campo.

**Tu validación cambia de capa.** Ya no validas sintaxis: la API lo hace. Validas **contenido** con un checker tuyo: que el RFC exista en el padrón, que el total cuadre con la orden de compra, que la categoría sea coherente con el texto, que `confianza: alta` no venga con `razonamiento` vacío. Eso ninguna gramática lo garantiza, y es donde el sistema se rompe en silencio.

Segundo camino, solo para modelos sin soporte o SDKs que no lo exponen: pedir JSON y validar el esquema tú, con un reintento metiendo el error al prompt.

Nunca dejes pasar una salida sin pasar por el checker.

## Prompt caching — el que más rinde

Cachea lo que se repite entre llamadas: system prompt, definiciones de herramientas, documentos de contexto largos.

- Cache hit = 10% del precio del input.
- **Los tokens de cache no cuentan para el rate limit ITPM.** Es un multiplicador de throughput, no solo un descuento.
- Se paga solo con una lectura (cache de 5 min).

Si tu sistema manda el mismo system prompt de 3,000 tokens en cada llamada y no lo estás cacheando, estás pagando de más y limitándote sin razón.

## Batch API

50% de descuento, resultados en ≤24h, sin diferencia de calidad. **Solo cambia el tiempo.**

Si el proceso no es en tiempo real —enriquecer registros, procesar documentos, análisis nocturno, generar contenido en cola— y no está en batch, está tirando la mitad del dinero.

## Tool use

Recuerda: **las definiciones de herramientas se cobran en cada llamada.** Los nombres, descripciones y esquemas van en el input todas las veces. 20 herramientas con esquemas largos es un impuesto permanente.

Herramientas del servidor con costo propio: web search ($10 / 1,000 búsquedas), code execution (1,550 h gratis/mes, luego $0.05/h; gratis si va junto a web search o web fetch). Web fetch no cuesta extra más allá de los tokens — pero usa `max_content_tokens` o un PDF grande te mete 125,000 tokens de golpe.

## Errores

- **429** → respeta el header `retry-after`. No inventes el backoff.
- **4xx** → no reintentes. No se arregla insistiendo.
- **5xx** → reintento con backoff, tope 3.
- **Pon un tope de gasto en la consola.** Un agente en loop con una API de pago es una factura sin techo.

## ¿API o nodo visual?

Si cabe en n8n, hazlo en n8n. La API directa es para cuando necesitas control que el nodo no te da: caching fino, batch, streaming, tool use complejo, o lógica que no se dibuja.
