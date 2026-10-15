---
description: Corre los evals del proyecto y devuelve la tasa de acierto, con su modo y su suite declarados
---

Un sistema sin evals "funciona" — hasta que alguien te pregunta cuánto acierta y no tienes un número. Carga la skill `errores-y-evals`.

Tu objetivo: correr los casos de `evals.md` y devolver **un número, no una opinión**, con dos etiquetas: la **suite** que se midió y el **modo** de medición.

## Suite: qué cuenta como válida

| Suite | Casos | Reparto | Etiqueta en `evals.md` |
|---|---|---|---|
| **Núcleo** | 6 | 4 típicos, 1 límite, 1 adversarial | `núcleo · 6 casos` — **medición válida y completa para la cohorte** |
| **Extendida** | 10 | 5 típicos, 3 límite, 2 adversariales | `extendida · 10 casos` |
| Cualquier otra | — | — | `parcial` + qué falta (por ejemplo, "falta el caso adversarial") |

El núcleo **no** es una suite incompleta. Nunca pidas los 10 casos para dejar avanzar a nadie: ofrece la extendida como extensión, una vez.

## Modo: qué se midió

- **Escritorio** (S2–S3): la decisión de IA sola, con el prompt más reciente de `prompts.md`.
- **Sistema** (S4): el flujo completo, con reglas, validación y escalamiento, tal como corre. Si no hay forma de correr el flujo completo (falta el runner, la herramienta o la autenticación), escribe `BLOQUEADO: <qué falta>` en lugar de una tasa. Nunca simules una corrida de sistema.
- **Importado** (ruta visual): la persona trae salidas reales de n8n, Make u otra herramienta (export del nodo de evaluación o una tabla pegada). No corras nada: compara esas salidas contra la esperada y cuenta.

## Qué hacer

**0. Rescate: si falta un prerequisito, constrúyelo — no te bloquees.** Antes de correr necesitas un `evals.md` con casos llenos y, en modo escritorio, un `prompts.md` con al menos un v0. Si falta algo, entra en modo rescate, en este orden:

- **Falta `prompts.md`:** el prompt v0 casi siempre ya existe disperso en `proyecto.md`, `reglas.md` o `flujo.md` (la instrucción de la decisión de IA, el formato de salida). Ensámblalo tú, márcalo como v0, escríbelo en `proyectos/<nombre>/prompts.md` y muestra lo que armaste. El v0 NO tiene que ser bueno — tiene que existir para poder medirlo.
- **Falta `decisiones.md`:** reconstrúyelo desde `reglas.md` y `flujo.md`, clasificando cada paso como if / IA / herramienta / humano, y confirma con el humano cuál es la decisión de IA a evaluar.
- **Faltan casos:** NO los inventes tú y no pidas todos de golpe. Guía de uno en uno con la receta de `proyectos/GUIA-escribir-evals.md`: propón TÚ un borrador de input realista basado en el proyecto, y que el humano lo corrija y fije la salida esperada. El borrador del input puede ser tuyo; **la salida esperada es siempre del humano.** Al llegar a 6 casos con reparto 4/1/1, corre: es el núcleo.

**1. Ubica el proyecto.** Busca en `proyectos/`. Si hay varios, pregunta cuál. Lee su `evals.md` y, en modo escritorio, su `prompts.md` — usa la versión más reciente del prompt. **Nunca corras contra un prompt vacío o inexistente.**

**2. Declara suite y modo** antes de correr, con la tabla de arriba.

**3. Corre cada caso** tal como lo haría el sistema en el modo declarado. Guarda la salida cruda de cada caso: es la evidencia.

**4. Compara contra la verdad, sin preguntarte a ti mismo.** La salida esperada ya está escrita en `evals.md`, fijada por un humano. Compara el campo —no "se ve bien", el campo— contra esa verdad. Marca ✅ o ❌. **Nunca regeneres la salida esperada ni te preguntes si acertaste.**

**5. Llena y cuenta.** Agrega una columna con la versión (`v0`, `v1`…) y el modo, con sus ✅/❌. No sobrescribas la corrida anterior: el valor está en el diff entre versiones. Calcula la tasa = aciertos / total.

**6. Diagnostica los fallos, pero no los arregles.** Por cada ❌, di en qué escalón cae, en orden: regla ambigua → falta un dato o un ejemplo límite → era un `if` → el modelo. La decisión de qué cambiar es del humano, no tuya.

## Reglas

**Verificación externa, siempre.** La verdad vive en `evals.md`, no en tu juicio. Si para saber si un caso acertó tendrías que opinar, el eval está mal escrito — dilo, no lo adivines.

**No inventes salidas esperadas. Nunca.** Los borradores de input sí, siempre que el humano los valide como realistas.

**Un prompt, una columna.** Cada versión deja su propia columna. Correr `/eval` después de cada cambio no es opcional: es la única forma de cachar una regresión antes que producción.

**Condición de salida.** Los casos puntuados, la tasa, la suite y el modo escritos en `evals.md`. Ahí acabas — ni sigues optimizando ni te pones a arreglar prompts.

## Escribe

Actualiza `proyectos/<nombre>/evals.md`: la columna de esta corrida, la tasa con su etiqueta (por ejemplo, `v0 · escritorio · núcleo 6 casos: 4/6`) y la salida cruda de al menos un fallo. No toques la salida esperada de ninguna fila.

## Antes de cerrar

Di la tasa en una línea, con su suite y su modo. Señala el eval que más **duele** —el fallo cuyo costo en producción es más alto— para orientar por dónde atacar primero. Recuérdale: si toca el prompt, vuelve a correr `/eval`.
