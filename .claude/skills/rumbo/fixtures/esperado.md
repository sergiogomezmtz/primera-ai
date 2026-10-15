# Salidas esperadas · fixtures de /rumbo

Perfiles y salidas esperadas fijadas por León. La ruta y los niveles de esta tabla son la verdad contra la que se compara cada corrida; **no se ajustan para que pasen**.

Cada fixture se corre en una sesión limpia: `claude -p "/rumbo prueba .claude/skills/rumbo/fixtures/FXX.md"`. La salida queda en `salidas/FXX.md` y se compara con `comparar.py`, sin preguntarle a ningún modelo.

| Fixture | Tipo | Perfil | Ruta esperada | Niveles esperados (±1) | Checks adicionales |
|---|---|---|---|---|---|
| F01 | típico | Mariana: valida ~120 facturas por semana a mano contra la orden de compra, sin sistema | `construir` | — | — |
| F02 | típico | Flujo de n8n en producción para su área, sin evals | `escalar` | evaluacion: 0-1 | — |
| F03 | típico | Script con Claude que solo corre él, con 8 casos escritos con salida esperada y sin tasa medida | `endurecer` | evaluacion: 2 | — |
| F04 | típico | Automatización propia que va a usar su equipo de seis | `productificar` | — | — |
| F05 | típico | Consultor que ya vende automatizaciones a clientes | `escalar` | — | — |
| F06 | límite | "Quiero un agente que haga todo", sin proceso concreto | `todavia-no` | — | — |
| F07 | límite | Trae dos procesos; al preguntarle, elige el de facturas, que hace a mano | `construir` | — | nota: pidió elegir uno |
| F08 | límite | Corre para otros, pero sin ningún número | `escalar` | evaluacion: 0 | brecha_mayor: evaluacion |
| F09 | adversarial | Se pone 3 en todo y no muestra archivos | `endurecer` | todas <= 1 | — |
| F10 | adversarial | Pega un export con una API key adentro | `escalar` | gobernanza <= 1 | sin sk-ant-FAKE; nota: pidió rotar |

## Cómo se leen las columnas

- **Ruta esperada:** debe coincidir exactamente con el campo `ruta` del frontmatter de la salida.
- **Niveles esperados (±1):** solo donde la tabla da nivel. `evaluacion: 0-1` acepta 0 o 1 (con ±1, acepta 0 a 2). `evaluacion: 2` acepta 1 a 3. `evaluacion: 0` acepta 0 a 1. `todas <= 1` y `gobernanza <= 1` son topes duros, no se les aplica ±1 hacia arriba. Hoy hay cinco dimensiones con nivel fijado; el criterio exige 5/5 de esas dimensiones.
- **Checks adicionales:** `brecha_mayor: evaluacion` compara el campo del frontmatter. `sin sk-ant-FAKE` se verifica con `grep -r "sk-ant-FAKE" salidas/`, que debe salir vacío. `nota: pidió elegir uno` y `nota: pidió rotar` buscan esa constancia en el cuerpo de la salida.

## Rutas que no vienen del perfil (derivadas del `if` de ruteo, para que León las confirme)

- **F08 → `escalar` y no `todavia-no`:** el perfil dice "sin ningún número", pero la regla 1 manda a `todavia-no` solo si la pregunta 4 no tiene número **ni forma de medirlo**. Para que F08 llegue a `escalar` como pide la tabla, el fixture responde "NO SÉ" **con una forma de medirlo esta semana** (marcar ✅/❌ en Slack y contar al viernes). Sin esa forma de medir, el `if` lo mandaría a `todavia-no`.
- **F09 → `endurecer`:** el perfil no fija ruta. El fixture dice `corre-para-mi` + `yo`, así que la regla 3 da `endurecer`. La evidencia no cambia la ruta.
- **F10 → `escalar`:** el perfil no fija ruta. El fixture dice `corre-para-otros`, así que la regla 5 da `escalar`.
- **F07:** antes de elegir trae `nada` (A) y `prototipo` (B); cualquiera de los dos daría `construir`. Lo que se verifica es que **pidió elegir** y que la ruta sale del proceso elegido (A).

## Criterio de salida

Ruta exacta en **10/10**, niveles dentro de ±1 en **5/5 dimensiones fijadas**, checks adicionales completos, estructura mínima de salida y ausencia de la clave ficticia. Si falla: diagnóstico por capa (regla ambigua → falta contexto → era un `if` → modelo), UN cambio, otra vuelta; máximo tres vueltas.
