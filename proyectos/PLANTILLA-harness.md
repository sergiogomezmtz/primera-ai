# Inventario de harness — <nombre del proyecto>

**Fecha:** <YYYY-MM-DD>

Qué tiene tu sistema hoy, en cada capa, y qué le falta.
La columna que importa es la última.

---

## 1 · Modelo

| Qué existe | Dónde vive | Qué falta |
|---|---|---|
| | | |

---

## 2 · Contexto

| Qué existe | Dónde vive | Qué falta |
|---|---|---|
| | | |

> Dónde suele vivir: `.claude/skills/` · `referencias/` · tu `reglas.md` y `alcance.md`

---

## 3 · Framework y herramientas

| Qué existe | Dónde vive | Qué falta |
|---|---|---|
| | | |

> Dónde suele vivir: `patrones/`

---

## 4 · Harness

| Qué existe | Dónde vive | Qué falta |
|---|---|---|
| | | |

> Dónde suele vivir: `CLAUDE.md` · `.claude/commands/` · `proyectos/` · `trazas/`

Preguntas para llenar esta capa:

- ¿Dónde queda el **estado** entre una corrida y otra?
- ¿Qué paso hace la **verificación**, y es distinto al que hace el trabajo?
- ¿Cuál es la **condición de salida**, y es verificable sin preguntarle al modelo?
- ¿Qué **memoria durable** impide que repita un error ya corregido?

---

## Regla de cierre

> **Cada capa termina con al menos un hueco nombrado.**
> Si no le falta nada a ninguna capa, tu sistema nunca ha corrido solo.

---

## El hueco que atacas primero

**Capa:**
**Hueco:**
**Por qué este y no otro:**

> Este es el mapa de tus próximas dos semanas, no una autocrítica.
