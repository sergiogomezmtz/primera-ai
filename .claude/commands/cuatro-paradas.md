---
description: Diseña y ejecuta un loop de trabajo-verificación con cuatro condiciones de parada explícitas.
---

# /cuatro-paradas

> Antes se llamaba `/loop`. Se renombró porque Claude Code trae un `/loop` integrado (repite un prompt en intervalos) y los dos chocaban.

Tu trabajo es convertir un paso repetitivo del flujo del usuario en un **loop que corre solo y para solo**.

Un loop sin condición de parada no es un loop: es una fuga de presupuesto.

## Antes de empezar

Lee estos archivos del proyecto activo en `proyectos/<proyecto>/`:

- `flujo.md` — el diagrama con cada paso clasificado IF / IA / humano
- `evals.md` — los casos de prueba y la tasa de acierto actual
- `alcance.md` — qué es "terminado" y qué queda fuera

Si falta alguno, dilo y detente. No inventes el contexto.

## Fase 1 — Identificar el candidato

Del `flujo.md`, encuentra el paso donde **hoy el humano es el bucle**: el que se repite hasta que algo queda bien, y el criterio de "bien" ya está escrito en algún lado.

Propón **un solo candidato** y justifica en dos líneas por qué ese y no otro. Espera confirmación del usuario.

Si ningún paso califica —porque ninguno tiene criterio verificable— dilo directamente: el problema no es que falte un loop, es que falta un criterio. Regrésalo a `/eval`.

Si el flujo termina en una sola pasada, **no fuerces un loop**. La salida válida es "no necesito loop": pídele que escriba en `harness.md` la razón y el checker que verifica la salida sin el modelo, y detente. Esa decisión cuenta como evidencia de criterio.

## Fase 2 — Las cuatro paradas

Un loop necesita las cuatro. Si falta una, el loop no se escribe.

Para cada una, exige un **valor concreto**. Si el usuario responde con una frase cualitativa, no la aceptes: pídele el número.

### 1. Éxito

La condición que, al cumplirse, termina el loop con resultado bueno.

**Contrato:** debe ser verificable **sin preguntarle al modelo**. Un `if`, un parser, un schema, una comparación contra la salida esperada de un eval. Si la única forma de saber si terminó bien es preguntarle al mismo modelo que lo hizo, no es una condición de éxito.

**Rechaza:** "cuando el resultado sea correcto", "cuando quede bien redactado".
**Acepta:** "cuando el JSON valide contra el schema y los 4 campos obligatorios no vengan vacíos".

### 2. Presupuesto

El tope duro. Dos números, ambos obligatorios:

- **Iteraciones máximas:** cuántas vueltas antes de rendirse.
- **Costo máximo:** en tokens o en pesos.

Recuérdale al usuario la aritmética: si cada vuelta tiene 95% de confiabilidad, el loop no mejora indefinidamente. Más vueltas no es más calidad; a partir de cierto punto es solo más gasto.

**Rechaza:** "las que necesite".
**Acepta:** "máximo 5 iteraciones o $8 MXN, lo que ocurra primero".

### 3. No-progreso

El loop puede estar gastando presupuesto sin acercarse a nada. Necesitas detectarlo antes de agotar el tope.

Define: **cuántas iteraciones consecutivas sin cambio material** cuentan como estancamiento, y **qué se compara** para saber si hubo cambio (¿el output completo? ¿un campo? ¿el número de errores del validador?).

**Rechaza:** "cuando ya no avance".
**Acepta:** "3 iteraciones seguidas donde el validador reporta el mismo número de errores".

### 4. Escalamiento

Qué dispara la salida hacia un humano **antes** de agotar presupuesto. Mínimo tres disparadores, y al menos uno de cada tipo:

- **Fuera de alcance:** el caso no se parece a nada de `alcance.md`
- **Acción irreversible:** el siguiente paso manda, borra, cobra o firma
- **Umbral de riesgo:** un monto, un cliente, una categoría que siempre pasa por ojos humanos

Y di **a quién** escala y **por qué canal**. "A alguien del equipo" no es un destinatario.

## Fase 3 — Escribir la especificación

Escribe `proyectos/<proyecto>/loop.md` usando `proyectos/PLANTILLA-loop.md`.

Reglas:

- Las cuatro paradas van con sus valores numéricos, no con la descripción de la parada.
- El paso de verificación va **explícito y separado** del paso de trabajo. Si en tu especificación el mismo paso hace y revisa, no hay verificación: hay una opinión.
- Todo lo que pueda ser un `if`, es un `if`. No mandes al modelo a decidir algo que una condición resuelve.

## Fase 4 — Correr contra un caso real

Ejecuta el loop **una vez**, contra un caso real de `evals.md` — de preferencia uno de los que falló.

Captura la traza en `proyectos/<proyecto>/trazas/<fecha>-<caso>.md`:

- Cuántas iteraciones corrió
- Qué cambió entre una y otra
- **Por cuál de las cuatro paradas salió**
- Cuánto costó

## Fase 5 — Leer la traza

Una sola pregunta al usuario: **¿salió por donde esperabas?**

- Salió por presupuesto → tu condición de éxito probablemente es inalcanzable, no estricta.
- Salió por no-progreso en la primera revisión → el paso de verificación no está midiendo nada útil.
- Salió por éxito en la primera vuelta → no necesitabas un loop; necesitabas un prompt.
- Salió por escalamiento con un caso que sí estaba en alcance → tu disparador está mal calibrado.

Propón **un solo ajuste**. Uno. El que más mueva la aguja. Que el usuario lo aplique y vuelva a correr.

## Al terminar

Recuérdale al usuario que haga commit. La traza es evidencia: es lo que hace que la siguiente sesión pueda comparar contra algo en vez de empezar de cero.
