---
name: rumbo
description: Assessment de entrada al curso; se usa cuando la persona escribe /rumbo. Fija qué quiere construir, mide con evidencia dónde está y decide su ruta.
disable-model-invocation: true
---

# /rumbo — assessment de entrada

## Propósito

Fijar **qué quiere construir** la persona, medir **con evidencia** dónde está, y decidir **su ruta** para el curso.

Durante el assessment **no se enseña: se mide.** No expliques conceptos, no corrijas su diseño, no propongas mejoras. Eso viene después, en `ACOMPANAMIENTO.md`. Aquí solo preguntas, verificas y calificas.

**Una pregunta a la vez.** Espera la respuesta antes de la siguiente. Duración objetivo: 35 minutos.

Argumentos: `$ARGUMENTS`. Si empieza con `prueba`, ve directo a la sección **Modo prueba** al final de este archivo antes de hacer nada.

---

## Momento 1 · Predicción (3 min)

Antes de cualquier evidencia, la persona se autocalifica de **0 a 3** en diez dimensiones. Pídele los diez números en una sola respuesta, en este orden y con estos nombres exactos:

`objetivos`, `delegacion`, `contexto`, `evaluacion`, `harness`, `loop`, `gobernanza`, `mejora`, `producto`, `economia`.

Una línea de contexto por dimensión, sin más:

| Dimensión | De qué va |
|---|---|
| objetivos | Decir cuándo el sistema terminó bien, de forma que un tercero lo verifique |
| delegacion | Decidir qué es un `if`, qué es IA, qué es una herramienta y qué sigue siendo humano |
| contexto | Decidir qué ve el modelo y qué no, y por qué |
| evaluacion | Tener casos con salida esperada y una tasa de acierto |
| harness | Saber qué capa revisar cuando falla, y con qué evidencia |
| loop | Diseñar iteraciones con cuatro paradas con números |
| gobernanza | Permisos mínimos, tope de gasto, aprobación antes de lo irreversible, secretos fuera del repo |
| mejora | Cambiar un prompt midiendo antes y después |
| producto | Que otra persona lo pueda correr sin ti |
| economia | Saber cuánto cuesta una corrida y un mes |

Escribe los diez números en el frontmatter `prediccion` de `rumbo.md` (plantilla más abajo) y **pide un commit antes de seguir**: `git add rumbo.md && git commit -m "rumbo: predicción"`. La predicción se fija antes de la evidencia para que no se acomode después.

---

## Momento 2 · Rumbo (10 min)

Seis preguntas, **una a la vez**:

1. **¿Qué quieres que exista en 4 semanas que hoy no existe?** Un artefacto observable, en una frase. ("Un workflow que clasifique tickets y los asigne" sí; "entender mejor la IA" no.)
2. **¿Quién lo va a usar?** `yo` | `equipo` | `internos` | `clientes`
3. **¿Qué tienes hoy?** `nada` | `prototipo` | `corre-para-mi` | `corre-para-otros`
4. **¿Qué número va a demostrar que funcionó, y cuánto vale hoy?** "NO SÉ" vale **si dice cómo lo va a medir esta semana**.
5. **¿Qué te frena?** `datos` | `reglas` | `permisos` | `proceso` | `expectativa` | `distribucion` | `confianza` | `costo`
6. **¿Qué NO vas a hacer en este curso?**

Mientras escuchas, separa en tus notas **hechos** (lo que dijo y se puede comprobar), **inferencias** (lo que tú deduces) y **faltantes** (lo que no contestó). Los tres van al final de `rumbo.md`.

**Si trae dos procesos, pide que elija uno antes de seguir.** No continúes con dos. Anota cuál eligió y cuál dejó.

---

## Momento 3 · Evidencia (20 min)

Diez sondas sobre **su sistema**, o sobre **su proceso** si no tiene sistema. Pide que pegue o señale archivos: export de n8n o Make, prompts, repo, hojas. **Verifica cada ruta que te dé con `ls`** antes de calificar.

| # | Dimensión | Sonda | Nivel 3 = |
|---|---|---|---|
| 1 | objetivos | "Escribe en una línea cuándo tu sistema terminó bien." | Un tercero lo verifica sin preguntarle al modelo ni a la persona. |
| 2 | delegacion | "Etiqueta cinco pasos de tu flujo: IF, IA, herramienta o humano." | Cada etiqueta tiene razón y no queda un IF disfrazado sin detectar. |
| 3 | contexto | "Muestra el contexto que hoy recibe el modelo. ¿Qué dejaste fuera y por qué?" | Cada pieza tiene razón y algo quedó fuera a propósito. |
| 4 | evaluacion | "¿Cuánto acierta y sobre cuántos casos? Muestra el archivo." | Tasa, n y casos con salida esperada fijada antes de correr. |
| 5 | harness | "Si tu sistema inventó un dato, ¿qué capa revisas primero y con qué evidencia descartas las otras?" | Va de abajo hacia arriba (harness → framework → contexto → modelo) y nombra la evidencia de cada descarte. |
| 6 | loop | "¿Algo itera? Dame sus cuatro paradas con números." | Las cuatro con número y el éxito se verifica sin el modelo. |
| 7 | gobernanza | "Acciones irreversibles y quién las aprueba; tu tope de gasto; dónde viven tus llaves." | Tope verificado en consola, gate antes de lo irreversible, secretos fuera del repo. |
| 8 | mejora | "El último cambio que hiciste a un prompt: ¿qué número medías antes y después?" | Antes y después con la misma suite. |
| 9 | producto | "Si mañana no estás: ¿quién lo corre, cómo sabe si funcionó y qué hace si no?" | Otra persona lo corre con un onboarding escrito y un paquete de ejecución. |
| 10 | economia | "¿Cuánto cuesta una corrida y un mes? ¿Medido o estimado?" | Costo por corrida medido y proyección mensual con supuestos escritos. |

### Escala única

| Nivel | Significa |
|---|---|
| **0** | No lo puede mostrar ni describir. "NO SÉ" vale y **no penaliza**: es un 0 honesto. |
| **1** | Lo describe, pero no hay artefacto. |
| **2** | Hay artefacto, pero un tercero no podría verificarlo: le falta número, criterio o fecha. |
| **3** | Un tercero lo verifica sin preguntarle al modelo ni a la persona. |

**Regla dura:** sin una ruta de archivo que exista (verifícala con `ls`) o evidencia pegada en la conversación, **el máximo es 1**. "Sí lo tengo" no es evidencia. "Está en mi repo" sin ruta no es evidencia. Una ruta que `ls` no encuentra no es evidencia.

Para cada dimensión anota en la tabla del mapa **qué evidencia viste**: la ruta del archivo o la cita textual. Si no viste nada, escribe "ninguna".

### Seguridad

Si aparece una **credencial** (API key, token, contraseña, cadena de conexión con password) en algo que pegó o en un archivo que leíste:

1. **No la escribas en ningún archivo**, ni en `rumbo.md`, ni en la bitácora, ni en tus notas. Ni completa ni parcial.
2. Dile que la **rote** ahora, y que la saque del archivo donde estaba (variable de entorno o `.env`, que ya está en `.gitignore`).
3. Califica **gobernanza con máximo 1**, diga lo que diga y muestre lo que muestre. Una llave en un export es la evidencia de que los secretos no viven fuera del repo.
4. En la columna de evidencia escribe solo: "credencial encontrada en <ruta o 'texto pegado'>; se pidió rotarla".

---

## Ruteo

**Es un `if`, no una opinión.** Aplícalo en este orden y detente en la primera regla que aplique:

1. Si la pregunta 1 **no describe un artefacto observable**, o la pregunta 4 **no tiene número ni forma de medirlo** → `todavia-no`.
2. Si `estado_actual` es `nada` o `prototipo` → `construir`.
3. Si `estado_actual` es `corre-para-mi` y `usuario_final` es `yo` → `endurecer`.
4. Si `estado_actual` es `corre-para-mi` y `usuario_final` es `equipo`, `internos` o `clientes` → `productificar`.
5. Si `estado_actual` es `corre-para-otros` → `escalar`.

Los niveles de evidencia **no cambian la ruta**. La ruta sale de lo que quiere y de lo que tiene; la evidencia decide cómo se le acompaña.

**`brecha_mayor`** = la dimensión con mayor diferencia `prediccion − evidencia`. Si hay empate, gana la de **menor evidencia**. Si persiste el empate, la que aparece primero en la lista de diez.

---

## Salida

Escribe `rumbo.md` **en la raíz del repo** con esta plantilla exacta. Llena todos los campos; ninguno queda vacío.

```markdown
---
nombre:
fecha:
ruta: construir | endurecer | productificar | escalar | todavia-no
usuario_final: yo | equipo | internos | clientes
estado_actual: nada | prototipo | corre-para-mi | corre-para-otros
prediccion: {objetivos: 0, delegacion: 0, contexto: 0, evaluacion: 0, harness: 0, loop: 0, gobernanza: 0, mejora: 0, producto: 0, economia: 0}
evidencia: {objetivos: 0, delegacion: 0, contexto: 0, evaluacion: 0, harness: 0, loop: 0, gobernanza: 0, mejora: 0, producto: 0, economia: 0}
brecha_mayor:
---
# Mi rumbo
**En cuatro semanas va a existir:**
**Lo va a usar:**
**Lo voy a saber porque:** [métrica] pasa de [hoy] a [meta]
**Fuera de alcance:**
**Supuesto más riesgoso:**
## Mapa: predicción contra evidencia
| Dimensión | Me puse | Demostré | Evidencia (archivo o cita) |
## Cómo me va a acompañar el agente
## Qué llevo a S2
```

Reglas de llenado:

- En el frontmatter, `ruta`, `usuario_final` y `estado_actual` llevan **un solo valor**, no la lista de opciones.
- `prediccion` y `evidencia` llevan los diez números, en ese orden, con esos nombres.
- La tabla del mapa tiene **exactamente diez filas**, una por dimensión, en el orden de la lista.
- **Supuesto más riesgoso:** la inferencia tuya que, si está mal, tira el proyecto. Una frase.
- Después de "Qué llevo a S2" agrega una sección `## Notas del assessment` con tres listas: **Hechos**, **Inferencias**, **Faltantes**. Si pidió elegir entre dos procesos, dilo ahí.

### Cómo me va a acompañar el agente

Según el **nivel de evidencia** de cada dimensión, lista las dimensiones en cada modo:

- **Nivel 0–1 → Enseñar.** El agente explica el mecanismo en corto, con un ejemplo, y hace una sola pregunta.
- **Nivel 2 → Retar.** El agente no explica: pide la evidencia que falta (el número, el archivo, el criterio).
- **Nivel 3 → Revisar como par.** El agente no guía: señala riesgos y contradicciones; la persona conduce.

Escríbelo así: `Enseñar: objetivos, contexto, …` · `Retar: …` · `Revisar como par: …`. Si un modo queda vacío, escribe "ninguna".

### Qué llevo a S2

Según la ruta:

- `construir` → proceso o caso acotado, una decisión candidata y **3 casos ancla recordados, no inventados** (típico, límite y adversarial), con la salida esperada de cada uno. Los 6 casos núcleo son continuidad posterior; los 10 de la suite extendida son opcionales.
- `endurecer` → el **export o prompt actual**, una decisión difícil y **3 casos reales** (típico, límite y adversarial); 6 si quiere cerrar el núcleo y 10 si quiere la extendida.
- `productificar` → el **export**, el **nombre de quien lo va a correr** sin la persona y una decisión concreta que esa persona pueda verificar con 3 casos ancla.
- `escalar` → el **costo real de un mes** (consola o factura), una decisión de producción y **3 casos ancla**; 6 para el núcleo y 10 para la extendida.
- `todavia-no` → el **mapa del proceso** con hechos, inferencias y faltantes separados; después vuelve a Ruta 2 para elegir una decisión y tres casos ancla.

### Al cerrar

1. Muestra el frontmatter completo en la conversación.
2. Pide que se lo entregue a **León tal cual**, sin editarlo.
3. Agrega una línea a `bitacora.md` en la raíz (créala si no existe): `AAAA-MM-DD · /rumbo · ruta: <ruta> · brecha_mayor: <dimensión> · sigue: lo que dice "Qué llevo a S2"`.
4. Pide el commit: `git add rumbo.md bitacora.md && git commit -m "rumbo: assessment de entrada"`.

---

## Modo prueba

Se invoca con `/rumbo prueba <ruta-al-fixture>`. Sirve para correr el assessment contra respuestas fijas y comparar la salida contra lo esperado, sin que nadie conteste en vivo.

En modo prueba:

1. **No preguntes nada.** Lee el archivo de la ruta dada. Trae las respuestas de los tres momentos y una sección de **seguimiento** con las respuestas a las preguntas que harías si fuera en vivo (por ejemplo, cuál proceso elige si trae dos). Úsalas como si la persona las hubiera dicho.
2. Aplica **exactamente** las mismas reglas: la escala, la regla dura (verifica cada ruta de evidencia con `ls` desde la raíz del repo), la regla de seguridad, el ruteo y el cálculo de `brecha_mayor`.
3. Escribe la salida en **`.claude/skills/rumbo/fixtures/salidas/<nombre>.md`**, donde `<nombre>` es el nombre del archivo del fixture sin extensión (`F01.md` → `salidas/F01.md`). Misma plantilla que `rumbo.md`. **Nunca escribas en la raíz** ni toques `rumbo.md` ni `bitacora.md`.
4. **No pidas commits** y no hagas ninguno.
5. Si el fixture trae dos procesos, aplica la regla: pide elegir uno (en modo prueba, toma la elección de la sección de seguimiento) y deja constancia en `## Notas del assessment`: "Traía dos procesos (A y B). Se pidió elegir uno. Eligió A."
6. Si el fixture o su evidencia contiene una credencial, aplica la regla de seguridad tal cual: la llave **no aparece en el archivo de salida**, se registra que se pidió rotarla, y gobernanza queda en máximo 1.
7. Al terminar, imprime en la conversación solo el frontmatter de la salida y la ruta donde quedó.
