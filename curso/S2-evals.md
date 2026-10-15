# Continuidad técnica de S2 — Evals: mide tu decisión de IA

Esta página **no es una puerta de entrada**. Úsala después del laboratorio de S2, cuando ya tienes una ruta elegida, un proceso/caso y una decisión candidata. Si todavía estás descubriendo qué agentizar, vuelve a [`Rutas de entrada`](../docs/rutas-de-entrada.md) y trabaja la Ruta 2. Si estás bloqueado, usa la Ruta 3 como andamio.

La continuidad responde: **¿cuánto acierta una decisión que ya acotaste?** No exige una S1 técnica ni artefactos previos. Puedes crear los mínimos desde esta sesión: una decisión, una regla, una salida esperada y seis casos. La suite de seis casos es el núcleo; diez casos son extensión.

## En clase y después

| Momento | Qué corresponde | Resultado |
|---|---|---|
| Laboratorio S2 | Ruta 1, 2 o 3; decisión y tres casos ancla | Evidencia mínima observable |
| Continuidad S2 | Completar seis casos y salidas esperadas | Suite núcleo 4/1/1 |
| S3 | Diagnóstico por capas, un cambio y nueva corrida | Comparación v0 → v1 |

La línea base solo se corre si el sistema está listo. Si no, se registra `BLOQUEADO`; nunca se inventa una tasa.

**Ruta visual (n8n, Make u otra herramienta).** Escribe los mismos seis casos en `evals.md`. Córrelos en tu herramienta o a mano y pega la salida real. `/eval` puede trabajar en modo importado: comparar y contar sin volver a ejecutar nada.

**Si falla instalación, autenticación o herramienta.** Corre el camino dorado offline con `python3`/`py`, o escribe los seis casos en papel. Conservas el contrato y la verdad esperada; la medición queda pendiente.

## Parte A — Conceptos

### ¿Qué es un eval?

Un eval es un caso de prueba con dos cosas:

| Parte | Qué es | Ejemplo |
|---|---|---|
| **Input** | Lo que entra a tu sistema | Correo: «su producto llegó roto» |
| **Salida esperada** | Lo que debería salir, escrito antes de ejecutar | `categoría: queja` |

La salida debe verificarse sin preguntarle al modelo si acertó: categoría, sí/no, valor o escalamiento.

### ¿Qué prompt se mide?

Es la instrucción que el sistema usa para tomar **la decisión que acabas de acotar en S2**. Vive en `proyectos/<tu-proyecto>/prompts.md`. Si no existe, crea el mínimo desde la decisión, la regla y la salida esperada de S2. Si ya tienes `flujo.md`, `decisiones.md` o `reglas.md`, se usan; no son prerrequisitos narrativos.

Cada cambio conserva la versión anterior: v0, v1, v2. Los prompts se miden como código.

### Dónde se hace cada cosa

| Lugar | Qué haces ahí |
|---|---|
| **EN TERMINAL** | `git`, `python3`/`py`, `claude`, archivos y commits |
| **DENTRO DE CLAUDE CODE/COWORK** | preguntas al Mentor, `/eval`, `/arrancar` y decisiones |

`/arrancar` es una herramienta condicional para convertir un proceso acotado en diseño; no es la puerta universal. Primero elige Ruta 1, Ruta 2 o Ruta 3 y fija una decisión.

Para salir de Claude Code escribe `/exit` o usa el mecanismo de tu terminal. No pegues comandos de shell dentro de la conversación ni prompts del Mentor en la shell.

### Por qué los casos van antes que el prompt

> La verdad se fija antes de medir.

Si escribes el prompt primero, puedes construir casos que ya resuelve y obtener un número bonito pero mentiroso. Primero fija inputs y salidas esperadas; después crea el prompt mínimo.

## Parte B — Continuidad paso a paso

| Paso | Qué haces | Dónde | Qué queda |
|---|---|---|---|
| **0** | Comprueba si tienes `/eval` y la plantilla; actualiza solo si falta | EN TERMINAL | Comando disponible o fallback documentado |
| **1** | Escribe seis casos: 4 típicos, 1 límite, 1 adversarial | Claude Code/Cowork | `evals.md` |
| **2** | Escribe prompt v0 desde la decisión de S2 y mide si puedes | Claude Code/Cowork | `prompts.md` + número o `BLOQUEADO` |
| **3** | Registra fallos y preguntas; reserva diagnóstico para S3 | Claude Code/Cowork | Observaciones, no arreglo especulativo |
| **4** | En S3 cambia una cosa y compara v0 vs v1 | Claude Code/Cowork | Evidencia de mejora |

### Paso 0 — Comprueba si tienes `/eval`

### EN TERMINAL — macOS/Linux

```bash
ls .claude/commands/
```

### EN TERMINAL — Windows PowerShell

```powershell
Get-ChildItem .claude/commands/
```

Si aparece `eval.md`, salta al Paso 1. Si falta, pide al Mentor que te indique cómo incorporar la plantilla según el estado de tu copia. No descargues archivos remotos a ciegas ni sobrescribas trabajo sin revisar el diff.

### Paso 1 — Escribe seis casos antes de correr

### DENTRO DE CLAUDE CODE/COWORK

```text
Copia proyectos/PLANTILLA-evals.md a proyectos/<tu-proyecto>/evals.md y ayúdame a llenarla.
La decisión que quiero evaluar es la que acotamos en S2.
Hazme preguntas sobre mi operación para construir los casos; no los inventes tú.
Fija la salida esperada antes de hablar del prompt.
```

| Tipo | Núcleo (6) | Extendida (10, opcional) | Qué son |
|---|---:|---:|---|
| Típicos | 4 | 5 | El caso normal de todos los días |
| Límite | 1 | 3 | Raro pero real, fronterizo o ambiguo |
| Adversarial | 1 | 2 | Diseñado para romper la decisión |

### Paso 2 — Prompt v0 y línea base

### DENTRO DE CLAUDE CODE/COWORK

```text
Escribe la versión v0 del prompt para la decisión que acotamos en S2.
Usa la regla y salida esperada que fijamos; si falta un archivo, crea el mínimo.
Que sea mínima: instrucción y reglas, sin adornos ni contexto especulativo.
Guárdala como v0 en proyectos/<tu-proyecto>/prompts.md.
```

Después usa `/eval` solo si los casos y el sistema están listos. El resultado puede ser `4/6`, `5/6` o `BLOQUEADO`; no maquilles la señal.

### Paso 3 — Registra fallos; no adelantes S3

En continuidad S2 registra qué caso falló y qué pregunta deja. El diagnóstico por capas, el arreglo y la nueva corrida pertenecen a S3.

No culpes automáticamente al modelo. Las capas de revisión son:

1. regla ambigua;
2. dato o contexto faltante;
3. `if` disfrazado;
4. herramienta/harness;
5. modelo, como último escalón.

### Paso 4 — S3 compara

En S3 agrega solo el cambio que la evidencia pidió, conserva v0 y vuelve a correr sobre los mismos casos. La mejora v0 → v1 es la evidencia; no basta decir que “se ve mejor”.

## Cierre uniforme

- **Estás aquí:** continuidad S2 y suite de casos.
- **Siguiente:** S3 para diagnóstico por capas y comparación v0 → v1.
- **Si estás bloqueado:** camino dorado offline, Cowork o tabla manual.
- **Si terminaste antes:** suite extendida de diez casos o una extensión justificada.
