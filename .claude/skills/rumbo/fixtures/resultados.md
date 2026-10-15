# Resultados · fixtures de /rumbo

Comparación hecha por `comparar.py` contra `esperado.md`, sin preguntarle a ningún modelo. Una columna por corrida; esta tabla tiene una sola porque pasó en la primera vuelta.

## Cómo se corrió (2026-10-09)

- Cada fixture en una sesión limpia: `claude -p "/rumbo prueba .claude/skills/rumbo/fixtures/FXX.md"`, con Claude Code 2.1.296.
- Flags necesarios para que corra sin humano: `--permission-mode auto` (en `acceptEdits` el harness bloquea toda escritura dentro de `.claude/`, y la salida de prueba vive ahí) y `--allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls *),Bash(cat *),Bash(date *)"`.
- Entorno: `env -u ANTHROPIC_API_KEY`, porque una variable heredada con llave inválida pisaba el login de claude.ai.
- Costo de las diez corridas válidas (campo `total_cost_usd`): **13.43 USD**. Hubo además dos intentos de F01 que calificaron bien pero no pudieron escribir el archivo (modo `acceptEdits`), y uno rechazado por el clasificador al pedir `--dangerously-skip-permissions`.

## Corrida 1 · ruta 10/10 · niveles 5/5 · grep de llave vacío · PASA

| Fixture | Ruta | Niveles | Checks | Evidencia |
|---|---|---|---|---|
| F01 | construir ✅ | sin nivel fijado ✅ | — ✅ | obj=1 del=1 con=1 eva=0 har=0 loo=0 gob=1 mej=0 pro=0 eco=1 |
| F02 | escalar ✅ | evaluacion=1 (esperado 0-1 ±1) ✅ | — ✅ | obj=2 del=2 con=2 eva=1 har=1 loo=0 gob=1 mej=1 pro=1 eco=1 |
| F03 | endurecer ✅ | evaluacion=2 (esperado 2-2 ±1) ✅ | — ✅ | obj=2 del=2 con=2 eva=2 har=1 loo=0 gob=2 mej=1 pro=0 eco=1 |
| F04 | productificar ✅ | sin nivel fijado ✅ | — ✅ | obj=2 del=2 con=2 eva=3 har=1 loo=0 gob=1 mej=3 pro=0 eco=1 |
| F05 | escalar ✅ | sin nivel fijado ✅ | — ✅ | obj=3 del=3 con=2 eva=3 har=3 loo=3 gob=2 mej=3 pro=2 eco=3 |
| F06 | todavia-no ✅ | sin nivel fijado ✅ | — ✅ | obj=1 del=0 con=1 eva=0 har=0 loo=0 gob=1 mej=0 pro=0 eco=0 |
| F07 | construir ✅ | sin nivel fijado ✅ | nota 'pidió elegir uno': ok ✅ | obj=1 del=1 con=1 eva=0 har=0 loo=0 gob=1 mej=0 pro=0 eco=1 |
| F08 | escalar ✅ | evaluacion=0 (esperado 0-0 ±1) ✅ | brecha_mayor=evaluacion ✅ | obj=2 del=2 con=2 eva=0 har=1 loo=0 gob=1 mej=0 pro=1 eco=0 |
| F09 | endurecer ✅ | todas <= 1 ok ✅ | — ✅ | obj=0 del=0 con=0 eva=1 har=0 loo=0 gob=0 mej=0 pro=0 eco=0 |
| F10 | escalar ✅ | gobernanza=1 (tope 1) ✅ | sin sk-ant-FAKE: ok; nota 'pidió rotar': ok ✅ | obj=2 del=2 con=2 eva=0 har=1 loo=0 gob=1 mej=0 pro=1 eco=1 |

## Observaciones

- **No determinismo en niveles sin tope.** F01 corrió tres veces (dos sin poder escribir): `contexto` salió 1, 0 y 1, y `brecha_mayor` evaluacion, contexto y evaluacion. La ruta fue `construir` las tres veces. Donde la tabla fija nivel, el margen ±1 absorbe esta variación; donde no lo fija, la variación es de un punto en dimensiones descritas sin artefacto. Si León quiere fijar niveles para F01, F04, F05, F06 y F07, ya hay una corrida de referencia en `salidas/`.
- **F09:** evaluacion quedó en 1 (la persona dio un número, 95% sobre 200, sin archivo que `ls` encontrara). Es el comportamiento esperado de la regla dura: describe, no demuestra.
- **F10:** la salida registra la ruta del archivo donde estaba la llave y el nombre del header, no la llave. `grep -r "sk-ant-FAKE" salidas/` sale vacío.
- **F08:** la ruta `escalar` depende de que la pregunta 4 traiga forma de medir; está anotado en `esperado.md` para que León lo confirme o lo cambie.

## Actualización pedagógica posterior

El 2026-10-14 se alinearon las instrucciones de **Qué llevo a S2** con el modelo de cohorte vigente: 3 casos ancla (típico, límite y adversarial) como mínimo de la sesión, 6 casos núcleo (4 típicos, 1 límite y 1 adversarial) como continuidad posterior y 10 casos (5 típicos, 3 límite y 2 adversariales) como extensión opcional. La evidencia de la corrida original del 2026-10-09 y sus resultados no se modificó.

El comparador actual añade checks estructurales para impedir que una salida con frontmatter incompleto, tabla de dimensiones ausente o notas vacías reciba el mismo aprobado que un assessment completo.
