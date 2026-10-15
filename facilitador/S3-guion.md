# S3 — Guion del facilitador

**Objetivo:** que cada Aprendedor(a) distinga una falla del modelo de una falla de contexto, herramienta o harness, y justifique si necesita iteración.

**Guía técnica:** [`curso/S3-loops.md`](../curso/S3-loops.md)
**Comando:** `/cuatro-paradas`

## Agenda de 150 minutos

| Minutos | Tú haces | El Aprendedor(a) produce | Pregunta de transición |
|---:|---|---|---|
| 0–15 | Recuperas la línea base de S2 | Número y casos fallidos | “¿Qué evidencia tenemos?” |
| 15–40 | Modelas diagnóstico por capas | `diagnostico.md` y `harness.md` | “¿Qué capa descartaste primero?” |
| 40–55 | Abres la decisión loop/no-loop | Justificación de una ruta | “¿Hay iteración real o solo falta un checker?” |
| 55–85 | Acompañas `/cuatro-paradas` o el checker externo | Cuatro paradas o verificación | “¿Dónde está el número?” |
| 85–105 | Pides una traza o una corrida del checker | Evidencia de salida | “¿Por qué terminó?” |
| 105–135 | Pides un solo ajuste y nueva corrida | Comparación v0 → v1 | “¿Qué cambió y qué quedó igual?” |
| 135–150 | Cierras evidencia y siguiente paso | `diagnostico.md`, `harness.md`, `evals.md` y `loop.md` si aplica | “¿Qué no vas a automatizar?” |

## Dos rutas válidas

### Sin loop

El Aprendedor(a) escribe:

```text
No necesito loop porque __________________.
```

Después produce un checker que verifica sin preguntarle al modelo y corre los seis casos.

### Con loop

El Aprendedor(a) debe fijar con números:

- éxito;
- presupuesto;
- no-progreso;
- escalamiento.

No aceptes “hasta que quede bien” ni “las vueltas que necesite”.

## Frases útiles

- “Un loop no es un requisito; es una hipótesis sobre la forma del proceso.”
- “Antes de culpar al modelo, revisa harness, framework y contexto.”
- “Una condición de éxito que pregunta al mismo modelo no es verificación externa.”
- “Una sola modificación nos enseña más que cinco cambios simultáneos.”

## Señales de atasco

| Señal | Intervención |
|---|---|
| Construye un loop porque lo pide el título | Pide dibujar primero una sola pasada completa |
| Usa criterios cualitativos | Solicita iteraciones, costo, errores o umbral concreto |
| Llama “modelo” a todo fallo | Pide evidencia que descarte harness, framework y contexto |
| No puede correr una traza | Usa el camino dorado offline y conserva la especificación |
| Quiere arreglar todos los casos | Selecciona el fallo que más duele y cambia una cosa |

## Cierre mínimo

El Aprendedor(a) debe poder mostrar:

- la capa diagnosticada;
- evidencia que descarte las otras;
- una decisión loop/no-loop;
- una traza o corrida de checker;
- comparación v0 → v1 sobre los mismos seis casos.
