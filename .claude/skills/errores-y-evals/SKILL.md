---
name: errores-y-evals
description: Endurecer un sistema para producción. Úsala cuando haya que manejar errores, probar la precisión de la IA, construir evals, decidir reintentos, o cuando alguien diga que su automatización "ya funciona" y haya que verificarlo. También cuando algo falle de forma intermitente.
---

# Errores y evals

La pregunta que ordena todo: **¿qué pasa cuando esto se rompe a las 3 de la mañana y nadie está viendo?**

## Evals

Sin evals no puedes decir que la IA "funciona bien". Solo que funcionó las tres veces que la viste.

**Núcleo: 6 casos.** Es una medición válida, no una suite incompleta.
- 4 típicos
- 1 límite (raro pero real, sacado de su operación)
- 1 adversarial (diseñado para romperla: input vacío, otro idioma, un intento de manipular al agente)

**Suite extendida, opcional: 10 casos** (5 típicos, 3 límite, 2 adversariales). Nunca la exijas para dejar avanzar.

Por cada caso: input, salida esperada, salida real, ✅/❌.

**Tasa de acierto = aciertos / total.** Ese número es el que separa "creo que funciona" de "acierta 92% y el 8% escala a un humano". Es también el número que va al reporte de impacto.

**Corre los evals cada vez que toques un prompt.** Siempre. Los prompts regresionan igual que el código, pero fallan más callados.

En n8n hay nodos **Evaluation** y **Evaluation Trigger** que hacen esto nativo. Úsalos.

## Las cuatro familias de falla

### 1. La API falla
Timeout, 500, servicio caído. Y la peor: **200 con basura** o estructura inesperada.

- Reintento con backoff exponencial, tope de 3 intentos, luego escalar.
- Si la API te da un header `retry-after` (la de Claude lo hace en los 429), **úsalo** en vez de inventar el backoff.
- **Valida la estructura de la respuesta, no solo el status code.**

### 2. La IA se sale del carril
Responde fuera de formato, alucina un dato, decide algo que no está en las reglas.

- Validación de esquema en la salida. Obligatoria.
- Si no valida: reintenta una vez con el error metido en el prompt. Si vuelve a fallar, escala a humano.
- **Nunca** dejes pasar una salida no validada al siguiente nodo.

### 3. Input basura
Vacío, en otro idioma, un PDF cuando esperabas texto, un caso que nadie previó.

- Valida a la entrada. Rechaza rápido y ruidosamente.
- Mejor rechazar 10 buenos que procesar 1 malo en silencio.

### 4. Saturación
Rate limits, cola llena, costo desbordado.

- Conoce tus límites antes de necesitarlos (`referencias/claude-api.md`).
- Encola en vez de disparar todo.
- **Pon un tope de gasto.** Un bucle infinito con una API de pago es una factura infinita. En la consola de Anthropic se configura; hazlo el día uno.

## Observabilidad mínima

¿Cómo se entera de que falló? Un log, una alerta, un correo diario con las excepciones. En n8n: **Error Trigger**.

Un sistema autónomo sin observabilidad falla en silencio durante semanas.

## La pregunta de cierre

"Si te vas de vacaciones dos semanas y esto corre solo, ¿qué te da miedo?"

Lo que conteste es lo que falta.
