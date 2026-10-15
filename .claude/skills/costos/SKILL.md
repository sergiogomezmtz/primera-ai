---
name: costos
description: Calcular y optimizar lo que cuesta correr una automatización con IA. Úsala cuando se hable de tokens, presupuesto, ROI, elección de modelo por costo, o cuando alguien pregunte "¿cuánto me va a costar esto?". También al preparar un reporte de impacto.
---

# Costos

**Lee `referencias/claude-api.md` antes de citar cualquier precio. Nunca de memoria.**

## Los cuatro descuentos, en orden de impacto

1. **Prompt caching.** Un cache hit cuesta 10% del input. Y —lo que casi nadie sabe— **los tokens leídos de cache no cuentan para tu rate limit**. No es solo un descuento: es un multiplicador de throughput. Cachea lo que se repite: system prompt, definiciones de herramientas, documentos de contexto.

2. **Batch API — 50% de descuento.** Asíncrono, ≤24h, sin diferencia de calidad. Si el proceso no es en tiempo real (enriquecer datos, procesar documentos, análisis nocturno), no usarlo es tirar la mitad del dinero.

3. **Rutear por modelo.** Haiku 5.5 para clasificar/extraer/rutear/resumir. Sonnet 5.5 para el grueso. Opus 5.5 solo donde el razonamiento lo justifique. Con los precios vigentes (9 oct 2026) la diferencia es **20× entre Haiku 5.5 y Sonnet 5.5** y solo **2× entre Sonnet 5.5 y Opus 5.5**: el ahorro grande está en mandar lo simple a Haiku, no en evitar Opus. En n8n el **Model Selector** lo hace dentro del mismo flujo.

4. **Recortar contexto y output.** El output cuesta 5x el input. Baja `max_tokens` cuando la salida debe ser corta.

Se acumulan: batch + caching juntos.

## Costos que la gente olvida y luego duelen

- **Las definiciones de herramientas se cobran en cada llamada.** Solo por incluir `tools` se agregan cientos de tokens de sistema, más los esquemas de tus herramientas. En cada request.
- **Extended thinking** se cobra como output.
- **Haiku 5.5 tiene dos precios.** Arriba de 100k tokens de prompt (contando cache) la petición entera paga 5× más ($0.50/$2.50). Un clasificador barato al que alguien le mete el manual completo deja de ser barato.
- **Tokenizador nuevo.** Desde Opus 4.7, el mismo texto produce ~35% más tokens (1M tokens pasó de ~750k a ~555k palabras). Un cálculo hecho a ojo con la intuición de un modelo anterior se queda corto por un tercio.
- **El bucle infinito.** Un agente que reintenta sin tope con una API de pago es una factura sin tope. **Tope de gasto en la consola. El día uno.**

## Cómo estimar de verdad

1. Tokens por ejecución (input + output). No lo adivines: **corre 5 ejecuciones reales y mide.** El campo `usage` de la respuesta te lo da.
2. Ejecuciones por mes.
3. Multiplica por el precio del modelo.
4. **Súmale**: tokens de definiciones de herramientas, reintentos (asume 10-15%), llamadas fallidas.
5. Súmale lo que no son tokens: licencia de n8n, hosting, vector DB, web search ($10 / 1,000 búsquedas).

Ese último punto es donde casi todos los ROI se caen.

## ROI honesto

**ROI = (horas ahorradas × costo hora) − costo de operación del sistema.** Anualizado. Con los supuestos escritos, no escondidos.

Un ROI que ignora el costo de operar el sistema no es un ROI. Es marketing.

Y si sale negativo, **eso también es un hallazgo válido**. Es más valioso que un número inflado. Ayúdale a presentarlo, no a maquillarlo.
