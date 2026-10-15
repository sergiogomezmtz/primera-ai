# Empieza aquí — Aprendedor(a)

Esta página te ayuda a elegir **una ruta**, no a leer todo el repositorio. La primera decisión no es “¿qué herramienta instalo?”, sino “¿qué evidencia puedo producir hoy?”.

## Paso 0 — Elige una ruta

| Ruta | Si llegas con… | Empieza por… |
|---|---|---|
| **1. Ya tengo algo construido** | Automatización, prototipo o sistema existente | Tu falla, cuello de botella o decisión difícil |
| **2. Quiero descubrir qué agentizar** | Proceso o idea real, pero todavía sin diseño | Definir el proceso y la decisión candidata |
| **3. Camino dorado opcional** | Ningún proceso claro, bloqueo técnico o necesidad de ver un ejemplo | [`ejemplo/README.md`](ejemplo/README.md) |

La **Ruta 2 es la ruta común principal**. La Ruta 3 sirve para calibrar y luego regresar a la Ruta 2.

Para ver la decisión completa, abre [`docs/rutas-de-entrada.md`](docs/rutas-de-entrada.md).

## Paso 1 — Abre tu entorno

### EN TERMINAL

Si ya tienes una copia del repositorio, abre la terminal en esa carpeta. Si trabajas en Cowork, abre la carpeta desde allí.

```bash
claude --version
```

### EN TERMINAL

```bash
claude
```

Si algo falla, guarda el mensaje o una captura. No conviertas la primera sesión en soporte técnico: sigue con Cowork, ZIP, papel o la Ruta 3 offline.

## Paso 2 — Habla con el Mentor

### DENTRO DE CLAUDE CODE O COWORK

```text
Lee CLAUDE.md, ACOMPANAMIENTO.md y docs/rutas-de-entrada.md.
Hazme una pregunta a la vez.
Primero ayúdame a elegir entre Ruta 1, Ruta 2 y Ruta 3.
No edites archivos todavía.
No inventes mi proceso, mis casos ni mis salidas esperadas.
```

## Paso 3 — Trabaja según tu ruta

### Ruta 1 — Ya tengo algo construido

Responde:

- ¿Qué parte ya funciona?
- ¿Qué falla, cuesta demasiado o depende de ti?
- ¿Qué decisión es la más difícil de medir?
- ¿Qué evidencia tienes hoy?

No vuelvas a construir desde cero. Tu salida es una decisión difícil, tres casos ancla y una hipótesis de mejora.

### Ruta 2 — Quiero descubrir qué agentizar

Dile al Mentor:

```text
Quiero descubrir qué parte de este proceso vale la pena agentizar.
Hazme preguntas sobre usuario, entrada, pasos, decisión, riesgo y resultado.
Ayúdame a elegir una sola decisión candidata.
Clasifica cada paso como if, IA, herramienta o humano.
No avances hasta que la salida esperada sea verificable.
```

Tu salida es: proceso acotado, decisión candidata, qué queda fuera y tres casos ancla.

### Ruta 3 — Camino dorado opcional

Abre [`ejemplo/README.md`](ejemplo/README.md) y lee solamente:

1. Problema.
2. Qué vas a hacer aquí.
3. La secuencia que enseña.

Después identifica:

```text
if → IA → salida estructurada → validación → humano
```

Si tienes Python:

### EN TERMINAL — macOS/Linux

```bash
python3 ejemplo/camino_dorado.py --modo offline --version v1 --suite nucleo
```

### EN TERMINAL — Windows PowerShell

```powershell
py ejemplo/camino_dorado.py --modo offline --version v1 --suite nucleo
```

Si no tienes Python, abre `ejemplo/casos.json` y recorre los seis casos en una tabla. Luego vuelve a la Ruta 2: elige un proceso propio o declara que continuarás con el caso común.

## Paso 4 — Usa `/rumbo` solo cuando aplique

`/rumbo` no es la puerta universal.

- Ruta 1: úsalo para fijar foco si ya tienes evidencia.
- Ruta 2: úsalo después de acotar el proceso y la decisión.
- Ruta 3: úsalo después de comprender el camino dorado y volver a la Ruta 2.

### DENTRO DE CLAUDE CODE

```text
Ahora que ya elegimos la ruta y una decisión candidata,
corre /rumbo sin inventar evidencia.
Hazme una pregunta a la vez y guarda solo lo que realmente decidamos.
```

## Entregable mínimo

Guarda en una nota, `rumbo.md` o el archivo que el Mentor indique:

- ruta elegida;
- proceso o caso en una frase;
- una sola decisión;
- qué queda fuera;
- tres casos ancla: típico, límite y adversarial;
- salida esperada de cada caso;
- siguiente paso y fallback.

Los seis casos y la línea base son continuidad posterior. Los diez casos y S5 son extensión.

## Qué no necesitas hacer hoy

- No necesitas construir un agente completo.
- No necesitas conectar una API real.
- No necesitas instalar Node/NPM si tu ruta no los usa.
- No necesitas convertir una automatización existente en agente.
- No necesitas completar diez casos.
- No necesitas pegar datos sensibles en el repo o en el chat.

## Cómo sabrás que avanzaste

Puedes responder:

1. ¿Qué parte es un `if`?
2. ¿Qué parte necesita IA y por qué?
3. ¿Cuál es la salida esperada?
4. ¿Qué caso podría romper la decisión?
5. ¿Qué acción nunca dejarías automática?
6. ¿Qué medirás después?

## Siguiente paso

- Si elegiste Ruta 1: lleva tu falla o cuello de botella a S3/S4 según corresponda.
- Si elegiste Ruta 2: cierra tres casos ancla en S2 y seis casos en continuidad.
- Si elegiste Ruta 3: vuelve a Ruta 2 o documenta qué aprendiste del caso común.

Si estás bloqueado, consulta [`docs/dependencias-y-preflight.md`](docs/dependencias-y-preflight.md) como referencia secundaria.
