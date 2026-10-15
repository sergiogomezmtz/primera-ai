---
type: referencia-api
title: Claude API
description: Precios, rate limits, caching, batch, salida estructurada y costos ocultos de la API de Anthropic. Verificado contra fuente oficial.
resource: https://platform.claude.com/docs/en/about-claude/pricing
tags: [claude, api, costos, rate-limits, anthropic, structured-outputs]
timestamp: 2026-10-09T00:00:00Z
---

# Claude API — hechos verificados

> **Verificado: 9 octubre 2026** contra https://platform.claude.com/docs/en/about-claude/pricing, /about-claude/model-deprecations, /api/rate-limits, /build-with-claude/structured-outputs y /agents-and-tools/tool-use/strict-tool-use.
> Re-verificar cada ~2 meses con `/verificar`. Nunca cites estos números de memoria.

## Modelos vigentes (generación 5.5 / Fable 5.1)

| Modelo | ID de API | Para qué |
|---|---|---|
| Claude Fable 5.1 | `claude-fable-5-1` | Razonamiento exigente y trabajo agéntico de horizonte largo |
| Claude Opus 5.5 | `claude-opus-5-5` | Coding agéntico y trabajo de conocimiento de larga duración; el punto de partida que recomienda Anthropic |
| Claude Sonnet 5.5 | `claude-sonnet-5-5` | Mejor combinación de velocidad e inteligencia; el grueso de la producción |
| Claude Haiku 5.5 | `claude-haiku-5-5` | Alto volumen y baja latencia: clasificar, extraer, rutear |

Los cuatro: contexto de 1M tokens, 128K de salida máxima, thinking adaptativo. Los IDs sin fecha son snapshots fijos desde la generación 4.6.

**Retiros.** Haiku 4.5 sigue activo, con retiro **no antes del 15 de octubre de 2026**: no lo recomiendes para nada nuevo. Sonnet 4.5 está deprecado y se retira el 30 de noviembre de 2026 (reemplazo: Sonnet 5.5). Opus 4.x, Sonnet 5, Sonnet 4.6 y Fable 5 siguen activos como legacy.

## Precios (USD por millón de tokens)

| Modelo | Input | Output | Cache write 5m | Cache write 1h | Cache hit |
|---|---|---|---|---|---|
| Claude Fable 5.1 | $10 | $50 | $12.50 | $20 | $0.25 |
| Claude Opus 5.5 | $4 | $20 | $5 | $8 | $0.20 |
| Claude Sonnet 5.5 | $2 | $10 | $2.50 | $4 | $0.10 |
| Claude Haiku 5.5 (prompt ≤ 100k tokens) | $0.10 | $0.50 | $0.125 | $0.20 | $0.01 |
| Claude Haiku 5.5 (prompt > 100k tokens) | $0.50 | $2.50 | $0.625 | $1 | $0.05 |
| Claude Opus 4.8 / 4.7 / 4.6 / Opus 5 (legacy) | $5 | $25 | $6.25 | $10 | $0.50 |
| Claude Sonnet 5 (legacy) | $2 | $10 | $2.50 | $4 | $0.20 |
| Claude Sonnet 4.6 (legacy) | $3 | $15 | $3.75 | $6 | $0.30 |
| Claude Haiku 4.5 (legacy, retiro ≥ 15 oct 2026) | $1 | $5 | $1.25 | $2 | $0.10 |

**Cache hit por generación.** Fable 5.1: 0.025× del input. Opus 5.5 y Sonnet 5.5: 0.05×. El resto: 0.1×.

**Sonnet 5 se quedó en $2/$10.** La subida a $3/$15 anunciada para el 1 de septiembre de 2026 **no ocurrió**; el precio introductorio pasó a ser el estándar (nota al pie 3 de la página de precios).

**Haiku 5.5 se cobra por longitud de prompt.** Arriba de 100,000 tokens de input (contando cache reads y cache writes) la petición completa paga la tarifa alta. Cada petición se evalúa sola. Es el único modelo vigente con este escalón.

**Tokenizador actual** (desde Opus 4.7): 1M tokens ≈ 555k palabras; los modelos anteriores metían ~750k palabras en 1M. Mismo texto, ~35% más tokens. Un cálculo hecho con la intuición de Sonnet 4.6 se queda corto por un tercio.

**Contexto de 1M sin sobreprecio** en todos los modelos 4.6+ **excepto Haiku 5.5**. Una petición de 900k tokens se cobra a la misma tarifa por token que una de 9k.

## Los cuatro descuentos, en orden de impacto

1. **Prompt caching.** Un cache hit cuesta el 10% del input normal (5% en Opus 5.5 y Sonnet 5.5; 2.5% en Fable 5.1). Escribir al cache cuesta 1.25× (5 min) o 2× (1 hora). Se paga solo con **una** lectura en el cache de 5 min, o dos en el de 1 hora.
2. **Batch API — 50% de descuento** en input y output. Asíncrono, resultados en ≤24h. Sin diferencia de calidad; solo de tiempo. Si el proceso no es en tiempo real (enriquecer datos, procesar documentos, análisis nocturno), esto es dinero regalado.
3. **Rutear por modelo.** Haiku 5.5 para clasificar, extraer, resumir, rutear. Sonnet 5.5 para el grueso. Opus 5.5 solo donde el razonamiento lo justifica. Con los precios vigentes, en prompts de hasta 100k tokens: **Haiku 5.5 → Sonnet 5.5 es 20×** en input y en output; **Sonnet 5.5 → Opus 5.5 es 2×**; Haiku 5.5 → Opus 5.5 es 40×. El salto caro ya no es Sonnet→Opus, es Haiku→Sonnet.
4. **Recortar contexto.** El output cuesta 5× el input. Baja `max_tokens` cuando la salida debe ser corta.

Los descuentos **se acumulan**: batch + caching juntos.

## Salida estructurada (GA)

Dos mecanismos, los dos con **decodificación restringida**: el esquema se compila a una gramática que limita qué tokens puede emitir el modelo. Ya no es "pídele JSON y reza".

- **Structured Outputs:** `output_config.format` con `type: "json_schema"` y tu `schema`. El JSON llega en el bloque `text`.
- **Strict tool use:** `strict: true` en la definición de la herramienta. El `input` del `tool_use` cumple el `input_schema` y el `name` siempre es válido.

Soportado en Fable 5.x, Opus 5.5/5/4.8/4.7/4.6/4.5, Sonnet 5.5/5/4.6/4.5, Haiku 5.5/4.5. Se pueden combinar en una misma petición.

**Lo que NO garantiza** (y por eso sigues validando):
- `stop_reason: "refusal"` → respuesta 200, cobrada, y el texto puede no cumplir el esquema.
- `stop_reason: "max_tokens"` → salida truncada e inválida. Sube `max_tokens` y reintenta.
- Mayúsculas en `enum`/`const`: puede cambiar la capitalización. Compara sin distinguir mayúsculas.
- Subconjunto de JSON Schema: sin esquemas recursivos, sin `minimum`/`maximum`, sin `minLength`/`maxLength`, `additionalProperties` debe ser `false`. Una feature no soportada devuelve 400.
- Límites de complejidad: 20 tools estrictas por petición, 24 parámetros opcionales, 16 con uniones.

**Consecuencia para el diseño:** la validación de sintaxis la hace la API. Tu checker ahora valida **contenido**: que el `rfc` exista en el padrón, que el `total` cuadre con la orden de compra, que la `categoria` tenga sentido para el texto. Eso no lo garantiza ninguna gramática.

Costos: la primera vez que usas un esquema se compila (latencia extra); queda cacheado 24 h desde el último uso. Se inyecta un system prompt extra que suma tokens de input, y cambiar `output_config.format` invalida el prompt cache.

## Rate limits (tier Start)

| Modelo | RPM | Input tok/min | Output tok/min |
|---|---|---|---|
| Fable 5.x (bucket compartido 5.1 + 5) | 1,000 | 500,000 | 100,000 |
| Opus 5.5 (bucket propio) | 1,000 | 2,000,000 | 400,000 |
| Opus 4.x (bucket compartido 4.8/4.7/4.6/4.5) | 1,000 | 2,000,000 | 400,000 |
| Sonnet 5.5 (bucket propio) | 1,000 | 2,000,000 | 400,000 |
| Haiku 5.5 | 1,000 | 2,000,000 | 400,000 |

Build: Fable 2,000 / 1.5M / 300k; los demás 5,000 / 5M / 1M. Scale: Fable 4,000 / 4M / 800k; los demás 10,000 / 10M / 2M.

Los tiers son Start / Build / Scale / Custom. Topes de gasto mensual: Start $500, Build $1,000, Scale $200,000; Custom sin tope. Organizaciones nuevas pueden arrancar en un tier de "Evaluation" con límites menores mientras construyen historial. Al tocar el tope del tier, la API devuelve 429 con `error_code: enforced_spend_limit_reached` y **sin** header `retry-after`: reintentar no sirve hasta el día 1 del mes siguiente o hasta subir de tier.

Verificado el 9 de octubre de 2026 contra https://platform.claude.com/docs/en/api/rate-limits. Los límites de Batch API (Start: 1,000 RPM, 200,000 requests en cola) también están en esa página.

### El dato que casi nadie conoce

**Los tokens leídos de cache NO cuentan para el límite ITPM.** Solo cuentan `input_tokens` + `cache_creation_input_tokens`.

Con 2M ITPM y 80% de cache hit, procesas efectivamente 10M tokens de input por minuto. El caching no es solo un descuento: **es un multiplicador de throughput.** (Excepción histórica: Haiku 3.5, ya retirado.)

`max_tokens` no afecta el límite OTPM — solo cuentan los tokens realmente generados. No hay penalización por poner un `max_tokens` alto.

## Errores y reintentos

429 = límite excedido. La respuesta trae header `retry-after` con los segundos a esperar. **Úsalo**, no inventes un backoff. Excepción: el 429 por tope de gasto no trae `retry-after` (ver arriba).

También puedes comer 429 por "límites de aceleración" si tu tráfico se dispara de golpe. Sube el volumen gradualmente.

Headers útiles en cada respuesta: `anthropic-ratelimit-requests-remaining`, `anthropic-ratelimit-input-tokens-remaining`, `anthropic-ratelimit-tokens-reset`.

**`temperature`, `top_p` y `top_k` están deprecados** desde Claude 4.7: devuelven 400 si los mandas con valor distinto al default. Guía el comportamiento con el prompt y con `effort`.

## Herramientas del servidor

- **Web search:** $10 por cada 1,000 búsquedas + tokens del contenido.
- **Web fetch:** sin costo adicional; solo pagas los tokens del contenido. Usa `max_content_tokens` para no tragarte un PDF de 500 kB (~125,000 tokens).
- **Code execution:** 1,550 horas gratis al mes por organización, luego $0.05/hora por contenedor. Gratis si va acompañado de web search o web fetch (versiones `20260209` o posteriores).

## Costos ocultos que rompen el presupuesto

- **Definiciones de herramientas.** Solo por incluir `tools` se agregan tokens de sistema (Haiku 5.5: 286 con `tool_choice` auto, 406 con `any`/`tool`; más los esquemas de tus herramientas). En cada llamada.
- **Thinking.** Los tokens de razonamiento se cobran como output. En los modelos 5.x el thinking es adaptativo y se controla con `effort`.
- **El bucle infinito.** Un agente que reintenta sin tope con una API de pago es una factura sin tope. **Pon un límite de gasto en la consola.** No es opcional.

Fuente: https://platform.claude.com/docs/en/about-claude/pricing
