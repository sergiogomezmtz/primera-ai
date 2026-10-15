---
description: Arrancar una automatización nueva — del proceso al diseño
---

Nueva automatización. Carga la skill `diseno-de-sistema`.

Tu objetivo: que salgan de esta sesión con **un** proceso elegido, mapeado, acotado y medido. Y con el patrón identificado. O con un veredicto honesto de que todavía no toca automatizarlo.

## Conduce así

**1. El proceso.** ¿Qué proceso manual quieren automatizar? Casi nunca traen uno solo, o traen uno vago. Corta.

Filtra con: frecuencia, tiempo que consume, qué pasa si sale mal, si tienen acceso a los sistemas. Si el proceso es raro o de bajo riesgo, **dilo**: da demo bonita y ROI cero.

**2. El flujo actual, como es hoy.** Con sus parches. Clasifica cada paso: **IF** (condición dura) / **IA** (decisión con ambigüedad real) / **herramienta** (una API o un nodo lo resuelve sin decidir nada) / **humano**.

**3. El patrón.** Mira `patrones/`. Casi seguro es uno de los siete, o dos combinados. Si es así, no diseñen desde cero — ahí está la estructura.

**4. ¿Workflow o agente?** Prueba de 30 segundos: ¿pueden dibujar el diagrama completo? Si sí, es un workflow. No le pongan un agente encima.

**5. Línea base.** Tiempo por ejecución, ejecuciones por semana, tasa de error actual. **No los dejes salir sin esto.** Si no tienen los números, dales una forma barata de medirlos esta semana. Un cronómetro y una hoja durante tres días basta.

**6. Alcance.** Lista explícita de qué queda dentro y qué queda fuera. Y una definición de terminado que un tercero pueda verificar sin preguntarle al modelo ni a la persona.

## Los cuatro veredictos

Al cerrar el punto 1 (y revísalo otra vez después del 5), el proceso cae en uno de estos. Dilo con esas palabras:

1. **Workflow.** Se puede dibujar completo. Es la respuesta el 80% de las veces.
2. **Workflow con un paso de IA.** Hay una sola caja con ambigüedad real. Ahí va el modelo; el resto son `if`.
3. **Agente.** Hay un tramo donde el camino no se puede predecir. Solo ese tramo lleva agente, con sus cuatro paradas.
4. **No automatizar todavía.** El proceso no pasa los filtros: es raro, es de bajo riesgo, no tienen acceso a los sistemas, no hay línea base, o nadie sabe decir qué es "terminado". **Es una salida válida y es la más barata.** Escribe por qué y qué tendría que cambiar para volver a intentarlo.

## Escribe

Crea `proyectos/<nombre>/` con cinco archivos. Ninguno es opcional:

- `proyecto.md` — copia de `proyectos/PLANTILLA.md`, llena. Incluye el veredicto y la línea base.
- `flujo.md` — diagrama Mermaid del proceso actual y del propuesto.
- `alcance.md` — tres secciones: **Dentro**, **Fuera**, y **Definición de terminado** (verificable por un tercero: un archivo que existe, un número que cuadra, un registro que aparece).
- `decisiones.md` — las **tres decisiones más difíciles** del diseño con su alternativa descartada, y la tabla de **cada paso clasificado IF / IA / herramienta / humano** con una línea de razón por paso.
- `reglas.md` — tabla: input → condición → acción → ¿escala a humano?

Si el veredicto es "no automatizar todavía", escribe solo `proyecto.md` con el veredicto y la razón. No generes archivos que nadie va a leer.

## Antes de cerrar

Diles en una línea qué es lo más probable que salga mal en este proyecto. Sé específico. Ya viste el proceso.
