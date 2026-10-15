# Loop — <nombre del proyecto>

**Paso del flujo que automatiza:** <copiar el nombre exacto del paso desde flujo.md>
**Fecha:** <YYYY-MM-DD>

---

## El ciclo

| # | Tipo | Qué hace |
|---|------|----------|
| 1 | trabajo | |
| 2 | verificación | |
| 3 | decisión | ¿cumple éxito? → salir · ¿no? → volver a 1 |

> El paso de verificación **no puede ser** el mismo que el de trabajo.
> Si lo es, no tienes verificación: tienes una opinión.

---

## Las cuatro paradas

### 1. Éxito

**Condición:**
**Se verifica con:** <if / schema / parser / comparación contra eval — NUNCA "le pregunto al modelo">

### 2. Presupuesto

**Iteraciones máximas:**
**Costo máximo:** <tokens o $MXN>
**Qué pasa al agotarse:** <guarda el mejor intento / descarta / notifica>

### 3. No-progreso

**Iteraciones consecutivas sin cambio material:**
**Qué se compara entre iteraciones:**
**Qué pasa al detectarse:**

### 4. Escalamiento

| Disparador | Tipo | A quién | Por qué canal |
|---|---|---|---|
| | fuera de alcance | | |
| | acción irreversible | | |
| | umbral de riesgo | | |

---

## Aritmética

**Pasos de IA dentro del loop:** n = <número>
**Confiabilidad de una vuelta:** 0.95^n = <resultado>
**Iteraciones máximas:** <número>

> Si una vuelta está por debajo de 85%, más iteraciones no lo arreglan.
> Quita un paso antes de subir el presupuesto.

---

## Trazas

| Fecha | Caso | Iteraciones | Salió por | Costo |
|---|---|---|---|---|
| | | | | |
