# Diagnóstico por capas — <nombre del proyecto>

**Fecha:** <YYYY-MM-DD>
**Fuente:** los casos que fallaron en `evals.md` + la falla que traías del prework

---

## Las cuatro preguntas, en orden

Se diagnostica **de abajo hacia arriba**. Lo barato y probable se revisa primero.

| # | Capa | La pregunta |
|---|---|---|
| 1 | **Harness** | ¿Recordó, verificó, se detuvo, escaló? |
| 2 | **Framework** | ¿Pudo hacerlo, con la forma correcta? |
| 3 | **Contexto** | ¿Tuvo la información, en el momento correcto? |
| 4 | **Modelo** | ¿Es capaz? |

La primera que responda **«no»** es tu capa.

---

## Tabla de fallas

| Caso | Síntoma observado | Capa | Evidencia |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

### Cómo se llena la columna de evidencia

**No es evidencia:**
- «se siente como el modelo»
- «creo que no entendió»
- «a veces sí funciona»

**Sí es evidencia:**
- «le di el dato explícito en el prompt y aun así falló» → descarta contexto
- «el archivo existía pero nunca se cargó» → confirma contexto
- «llamó a la herramienta con un parámetro que no existe» → confirma framework
- «volvió a hacer lo que ya había hecho en la corrida anterior» → confirma harness

---

## Regla de escritura

> **Nadie escribe «modelo» en la columna de capa** sin haber descartado las otras tres por escrito, aquí mismo.

Si crees que una falla es del modelo, agrégala abajo con sus tres descartes:

**Caso:**
- Descarté harness porque:
- Descarté framework porque:
- Descarté contexto porque:

---

## Referencia de síntomas

| Síntoma | Capa probable |
|---|---|
| Se queda a media tarea, olvida lo hecho | Harness · sin estado en disco |
| Declara terminado sin terminar | Harness · sin éxito verificable |
| Repite un error que ya corregiste | Harness · sin memoria durable |
| Gasta sin parar | Harness · sin condición de salida |
| Acierta en tus pruebas, falla en real | Contexto · lo real trae algo que no viste |
| Alucina un dato que sí está en un archivo | Contexto · no cargado, o enterrado |
| Usa la herramienta mal, inventa parámetros | Framework |
| Falla el razonamiento con todo lo demás en orden | Modelo |
