## Sesión 3 — Loops: el sistema que corre solo y para solo

En la Sesión 2 mediste tu decisión de IA. La Sesión 3 responde dos preguntas: **qué capa está rota** y **si tu sistema necesita iterar**. Si la respuesta es sí, convierte el paso donde HOY el humano es el bucle — revisar, corregir, volver a revisar — en un loop que trabaja, se verifica y se detiene sin que nadie lo esté viendo. Si es no, lo demuestras con una verificación externa y sigues.

La idea central viene de la doctrina (`CLAUDE.md` §11): un loop sin condición de parada verificable no es automatización — es una fuga de presupuesto con un optimista adentro. Todo loop necesita **cuatro paradas**:

| # | Parada | La pregunta que responde |
|---|---|---|
| 1 | **Éxito** | ¿Cómo sabe que terminó BIEN — sin preguntarle al modelo? |
| 2 | **Presupuesto** | ¿Cuántas vueltas / cuánto dinero antes de rendirse? |
| 3 | **No-progreso** | ¿Cómo detecta que da vueltas sin avanzar? |
| 4 | **Escalamiento** | ¿Qué casos van a un humano ANTES de agotar presupuesto? |

Falta una y el loop es un riesgo (§11). Las cuatro con números concretos, o el loop no se escribe.

### Decisión de la cohorte: quizá no necesitas un loop

Antes de construirlo, intenta dibujar el flujo completo. Si termina en una pasada o si el ciclo existe solo porque el prompt está mal delimitado, escribe en `harness.md`: **"No necesito loop porque ___"**, y sigue por el Paso 2b. Esa salida cuenta como evidencia de criterio; no se exige un `loop.md` a quien no tiene iteración real.

### En clase: 150 minutos

| Minutos | Bloque de la [Ruta de la cohorte](00-ruta-de-la-cohorte.md) | Paso de esta guía |
|---:|---|---|
| Antes | Preflight | Paso 0 |
| 0–15 | Recuperación de la línea base | Tu `evals.md` de S2 |
| 15–40 | Diagnóstico por capas y harness | Paso 1 |
| 40–55 | Decidir si hace falta un loop | La decisión de arriba |
| 55–85 | Con loop: `/cuatro-paradas` con números. Sin loop: escribir el checker | Paso 2 (fases 1–3) o Paso 2b (puntos 1–2) |
| 85–105 | Correr una traza, o la suite con el checker | Paso 2 (fases 4–5) y Paso 3, o Paso 2b (punto 3) |
| 105–135 | Un solo ajuste (v0 → v1) y nueva corrida | Paso 4 |
| 135–150 | Guardar evidencia | Commit |

**Ruta visual.** Las cuatro paradas existen igual en n8n o Make. Presupuesto: un contador en un nodo `IF` dentro del loop. No-progreso: comparar la salida con la de la vuelta anterior. Escalamiento: una rama a aprobación humana. Éxito: un nodo que valida contra el esquema, no contra la opinión del modelo. Añade un Error Trigger para enterarte cuando algo truene.

**Si falla la herramienta.** Escribe las cuatro paradas, o tu "no necesito loop", en `harness.md` con números, y corre la verificación sobre el camino dorado offline. El criterio se puede demostrar sin la integración.

---

### Puente desde S2 — si solo tienes el checkpoint mínimo

La Sesión 2 puede cerrarse correctamente con una ruta, un proceso o caso, una decisión, tres casos ancla, sus salidas esperadas, un siguiente paso y un fallback. Eso todavía no garantiza que existan `evals.md`, `flujo.md` y `alcance.md` en `proyectos/<tu-proyecto>/`.

Antes de correr `/cuatro-paradas`, comprueba qué tienes:

```bash
ls proyectos/<tu-proyecto>/
```

Si falta `evals.md`, completa primero la continuidad de S2: seis casos recordados de tu operación, con 4 típicos, 1 límite y 1 adversarial. Los diez casos son opcionales. Usa `proyectos/PLANTILLA-evals.md` y conserva las salidas esperadas que fijaste tú.

Si falta `flujo.md` o `alcance.md`, dentro de Claude Code o Cowork escribe:

```text
Lee el checkpoint de S2 en proyectos/<tu-proyecto>/rumbo.md o en la nota que te indique,
junto con proyectos/<tu-proyecto>/evals.md y cualquier evidencia existente.

Hazme una pregunta a la vez si falta información.
No inventes pasos, contexto, herramientas ni criterios de terminado.
Cuando yo confirme que hay suficiente evidencia, crea únicamente:
- proyectos/<tu-proyecto>/flujo.md: pasos del proceso, clasificados como IF, IA, herramienta o humano.
- proyectos/<tu-proyecto>/alcance.md: qué significa terminado y qué queda fuera.

Detente si no puedes justificar un dato con mi checkpoint o mis casos.
```

Revisa ambos archivos antes de continuar. Si todavía falta una decisión, una salida esperada o un límite, no ejecutes el loop: completa esa evidencia primero o usa el fallback documentado. `/cuatro-paradas` sigue siendo estricto y debe detenerse si el contexto no alcanza.

---

### Paso 0 — Trae `/cuatro-paradas` y su plantilla a TU repo 📍 EN LA TERMINAL

> Este comando se llamaba `/loop` en Q3. Se renombró porque Claude Code trae un `/loop` integrado (corre un prompt en intervalos) y los dos chocaban. Si en tu repo todavía tienes `.claude/commands/loop.md`, bórralo y trae el nuevo.

Igual que en la Sesión 2: tu repo es una foto del día que lo creaste, y `/cuatro-paradas` se publicó después. Parado en tu repo (`pwd` para ubicarte, `cd` a tu carpeta), verifica:

```bash
ls .claude/commands/
```

Si aparece `cuatro-paradas.md`, salta al Paso 1. Si NO, copia y pega estas dos líneas (cada una completa):

```bash
curl -o .claude/commands/cuatro-paradas.md https://raw.githubusercontent.com/nabolom/agentic-ai-automation-mentor-agent-2026/main/.claude/commands/cuatro-paradas.md
curl -o proyectos/PLANTILLA-loop.md https://raw.githubusercontent.com/nabolom/agentic-ai-automation-mentor-agent-2026/main/proyectos/PLANTILLA-loop.md
```

Confirma y guarda en tu repo:

```bash
ls .claude/commands/          # debe aparecer cuatro-paradas.md
ls proyectos/                 # debe aparecer PLANTILLA-loop.md

git add .claude/commands/cuatro-paradas.md proyectos/PLANTILLA-loop.md
git commit -m "sesion 3: comando /cuatro-paradas y plantilla de loops"
git push
```

**Importante:** si Claude Code estaba abierto, ciérralo (`Ctrl+C`) y vuelve a entrar (`claude`) — los comandos nuevos solo se detectan al arrancar.

---

### Paso 1 — Diagnostica antes de construir 📍 EN CLAUDE CODE

Antes de escribir un loop, nombra la capa donde tu sistema falla hoy. Un loop mal ubicado automatiza el paso equivocado.

Copia las dos plantillas a tu proyecto:

```
cp proyectos/PLANTILLA-diagnostico.md proyectos/<tu-proyecto>/diagnostico.md
cp proyectos/PLANTILLA-harness.md proyectos/<tu-proyecto>/harness.md
```

Si no las tienes todavía, tráelas igual que `/cuatro-paradas`:

```
curl -o proyectos/PLANTILLA-diagnostico.md https://raw.githubusercontent.com/nabolom/agentic-ai-automation-mentor-agent-2026/main/proyectos/PLANTILLA-diagnostico.md
curl -o proyectos/PLANTILLA-harness.md https://raw.githubusercontent.com/nabolom/agentic-ai-automation-mentor-agent-2026/main/proyectos/PLANTILLA-harness.md
```

**`diagnostico.md`** — toma los casos que fallaron en tu `evals.md` y clasifícalos por capa. La columna que cuesta es *evidencia*: «se siente como el modelo» no es evidencia; «le di el dato explícito y aun así falló» sí lo es. Nadie escribe «modelo» sin descartar las otras tres capas por escrito.

**`harness.md`** — inventario de las cuatro capas de tu sistema: qué existe, dónde vive, qué falta. Cada capa termina con al menos un hueco nombrado. Si no le falta nada a ninguna, tu sistema nunca ha corrido solo.

Las cuatro capas se diagnostican **de abajo hacia arriba** — harness, framework, contexto, modelo — porque lo barato y probable se revisa primero. El marco completo está en `referencias/harness.md`.

```
git add proyectos/
git commit -m "sesion 3: diagnostico por capas e inventario de harness"
git push
```

---

### Paso 2 — Corre `/cuatro-paradas` en tu proyecto 📍 EN CLAUDE CODE

**Prerequisitos:** `/cuatro-paradas` lee tu `flujo.md`, tu `evals.md` y tu `alcance.md`. Si falta alguno, el comando se detiene y te lo dice — S2 es el suelo de esta sesión. Con el núcleo de 6 casos basta; no necesitas la suite extendida para seguir.

```
/cuatro-paradas
```

El comando trabaja en cinco fases, y te va a exigir números — no te aceptes a ti mismo respuestas cualitativas:

| Fase | Qué pasa | Tu papel |
|---|---|---|
| 1 | Identifica EL paso candidato de tu `flujo.md` (uno solo) | Confirmar o corregir |
| 2 | Te exige las cuatro paradas con valores concretos | Dar números: "máx 5 iteraciones o $8 MXN", no "las que necesite" |
| 3 | Escribe la especificación en `proyectos/<tu-proyecto>/loop.md` | Revisar que verificación y trabajo sean pasos SEPARADOS |
| 4 | Corre el loop UNA vez contra un caso real de tus evals | Mirar la traza que queda en `trazas/` |
| 5 | Te pregunta: ¿salió por donde esperabas? | Aplicar UN ajuste y volver a correr |

Si en la Fase 1 el comando concluye que ningún paso itera, acepta la salida "no necesito loop" y sigue por el Paso 2b.

---

### Paso 2b — Sin loop: escribe la verificación externa 📍 EN CLAUDE CODE

Si tu flujo termina en una pasada, no construyas un loop para cumplir. Demuestra que sabes cuándo terminó bien sin preguntarle al modelo:

1. En `harness.md`, escribe **"No necesito loop porque ___"** con la razón concreta.
2. Escribe el **checker**: la condición que verifica la salida sin el modelo (un `if`, un esquema, una comparación contra la salida esperada).
3. Corre `/eval` sobre tus seis casos y guarda el resultado. Esa corrida es tu evidencia, igual que la traza de un loop.

```bash
git add proyectos/
git commit -m "sesion 3: no necesito loop - checker y corrida"
git push
```

---

### Paso 3 — Lee la traza como diagnóstico 📍 EN CLAUDE CODE

La traza dice **por cuál de las cuatro paradas salió** el loop, y cada salida es un diagnóstico distinto:

| Salió por… | Significa |
|---|---|
| Presupuesto | Tu condición de éxito probablemente es inalcanzable, no estricta |
| No-progreso en la primera revisión | Tu verificación no está midiendo nada útil |
| Éxito en la primera vuelta | No necesitabas un loop — necesitabas un prompt |
| Escalamiento con un caso que SÍ estaba en alcance | Tu disparador está mal calibrado |

Un ajuste a la vez — el que más mueva la aguja. Corre de nuevo. Y commit después de cada corrida, porque la traza es evidencia: es lo que hace que la Sesión 4 pueda comparar contra algo en vez de empezar de cero.

```bash
git add proyectos/
git commit -m "loop: primera traza - salio por <parada>"
git push
```

---

### Paso 4 — Un ajuste medido 📍 EN CLAUDE CODE

Con loop o sin él, cierras igual: toma el fallo que diagnosticaste en S2 (o el que mostró la traza), aplica **un solo** ajuste siguiendo la escalera del [Paso 3 de S2](S2-evals.md) y vuelve a correr:

```
/eval
```

La evidencia es la comparación v0 → v1 sobre los mismos seis casos, con el porqué escrito al lado. Si el número no sube, también es evidencia: escribe qué aprendiste y no cambies dos cosas a la vez.

```bash
git add proyectos/
git commit -m "sesion 3: v1 - <aciertos>/6"
git push
```

---
