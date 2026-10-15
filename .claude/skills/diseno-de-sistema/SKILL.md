---
name: diseno-de-sistema
description: Decidir la arquitectura de una automatización. Úsala cuando haya que elegir entre agente y workflow, decidir dónde va IA y dónde va un if, mapear un proceso, o cuando alguien describa lo que quiere construir y todavía no exista diseño. Es la primera skill de casi cualquier proyecto.
---

# Diseño de sistema

El cuello de botella de estas personas no es programar. Es esto.

## Paso 1 — El proceso real

Antes de dibujar nada, entiende el proceso **como es hoy**, no como debería ser. Con sus parches, sus correos y su hoja de cálculo escondida.

Cuatro preguntas que filtran lo que no vale la pena automatizar:
- ¿Con qué frecuencia ocurre? (mensual → no vale)
- ¿Cuánto tiempo consume cada vez?
- ¿Qué pasa si sale mal? (nada → no es crítico)
- ¿Tiene acceso a los sistemas que toca? (si depende de TI, muere)

Si el proceso es raro, de bajo volumen o de bajo riesgo, **dilo**. Automatizarlo da una demo bonita y un ROI de cero.

## Paso 2 — Clasifica cada paso

Recorre el flujo y marca cada paso:

| Tipo | Cuándo | Costo |
|---|---|---|
| **Condición dura** (`if`) | La regla se puede escribir | Gratis, instantáneo, determinista |
| **Decisión con IA** | Hay ambigüedad real: lenguaje libre, contexto, criterio | Caro, lento, no determinista |
| **Humano** | Error irreversible o de alto costo | Lento, pero a veces obligatorio |

**Si puedes escribirlo como un `if`, que sea un `if`.** Repítelo. Es la corrección más frecuente que vas a hacer.

## Paso 3 — ¿Workflow o agente?

**La prueba de 30 segundos:** ¿puedes dibujar el diagrama de flujo completo?

- **Sí** → workflow. Determinista, depurable, barato. Es la respuesta correcta el 80% de las veces.
- **Hay una caja que dice "aquí depende"** → *esa caja* necesita un agente. El resto no.

Casi todos los "agentes" en producción son workflows con un paso de LLM. Está bien.

Un agente le da al modelo el poder de elegir herramientas y orden. Eso es potencia y es riesgo: se puede equivocar de orden, entrar en loops, gastar sin control. Solo dáselo cuando el camino no se pueda predecir.

## Paso 4 — Corta el alcance

Los proyectos no mueren por lo que incluyen. Mueren por lo que se les fue metiendo.

Fuerza una lista explícita de **fuera de alcance**. Y una definición de terminado que sea verificable.

## Paso 5 — Escalamiento

¿Cuándo el sistema para y le pregunta a un humano?

Si la respuesta es "nunca", una de dos: el sistema es frágil, o el proceso no era crítico. Ambas son problema.

Para acciones irreversibles (mandar el correo, cobrar, borrar, publicar) → **human-in-the-loop siempre**, al menos en las primeras semanas.

## Paso 6 — Línea base

Mide el proceso manual **antes** de tocarlo: tiempo por ejecución, ejecuciones por semana, tasa de error actual, costo estimado.

Toma dos horas y no se puede recuperar después. Sin esto, cualquier afirmación de impacto es inventada.

## Entregable

- Diagrama Mermaid del flujo, con las condicionales visibles
- Tabla de reglas de decisión: input → condición → acción → ¿escala a humano?
- Contrato de alcance: dentro / fuera / definición de terminado
- Línea base

Todo a `proyectos/<nombre>/`.
