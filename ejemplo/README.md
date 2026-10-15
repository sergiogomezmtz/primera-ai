# Camino dorado: triage de solicitudes

Este ejemplo es el suelo común de la cohorte. No enseña una herramienta: enseña el contrato que sobrevive aunque cambies de herramienta.

## Problema

Llegan solicitudes de clientes. El sistema decide si cada una va a **soporte**, **ventas**, **facturación** o **revisión humana**.

## Qué vas a hacer aquí

Este es un ejemplo guiado, no un proyecto que tengas que construir. Hazlo en este orden:

1. Lee **Problema** y **La secuencia que enseña**.
2. Identifica qué se resuelve con un `if`, cuándo entra la IA, dónde se valida la salida y cuándo decide una persona.
3. Ejecuta el ejemplo en modo offline, o recorre `casos.json` en papel si no tienes Python.
4. Responde qué casos no llegan a la IA, qué ocurre si la salida no valida y por qué un caso termina en humano.
5. Compara `v0` con `v1`: el objetivo es observar qué cambia cuando agregamos seguridad y criterio, no construir un agente.

**Qué debe quedar:** una nota breve con tus respuestas y una comprensión común del contrato `if → IA → salida estructurada → validación → humano`. Después vuelve a la [Ruta de preparación y continuidad de la Sesión 2](../docs/ruta-continuidad-s2.md) para elegir tu foco.

## La secuencia que enseña

```text
Entrada ── vacía o no es texto ──────────────────────────────→ humano
  ↓
1. if determinista: ¿intento de cambiar instrucciones?  ── sí → humano
                    ¿remitente conocido?               ── sí → ruta fija
  ↓ ninguna regla aplica
2. IA solo para la ambigüedad real: clasificar la intención
  ↓
3. Salida estructurada: ruta, confianza, razon, fuente, escalar
  ↓
4. Validación del contrato, campo por campo, sin preguntarle al modelo
  ↓ no valida ──────────────────────────────────────────────→ humano
5. Humano cuando corresponde: sin categoría, confianza baja o escalamiento pedido
  ↓ no hace falta
Ruta registrada
```

**No todo pasa por IA.** Un remitente conocido se rutea con un `if`, y la regla de seguridad va **antes** que la de remitente: si no, un remitente confiable se vuelve una puerta trasera (caso E7). La decisión de mandar a una persona también es un `if` del harness, no una opinión del modelo.

## El contrato

| Campo | Valores | Qué significa |
|---|---|---|
| `ruta` | `soporte`, `ventas`, `facturacion`, `otro`, `escalar_humano` | A dónde va. `otro` solo existe como salida intermedia del modelo; nunca es salida final (ver abajo) |
| `confianza` | `alta`, `media`, `baja` | Señal declarada. Baja siempre escala; calíbrala con tus evals antes de confiar en "alta" |
| `razon` | texto | Una frase para depurar |
| `fuente` | `if`, `ia`, `harness` | Quién propuso la ruta: una regla, el modelo o la falla segura del harness |
| `escalar` | `true` / `false` | Si una persona decide |

Si la salida no valida, el caso escala a una persona. **Una salida inválida no pasa al siguiente paso.**

### Rutas intermedias y rutas finales

| Rutas que puede proponer el modelo (salida intermedia) | Rutas finales del sistema |
|---|---|
| `soporte`, `ventas`, `facturacion`, `otro`, `escalar_humano` | `soporte`, `ventas`, `facturacion`, `escalar_humano` |

`otro` es la forma en que el modelo dice "no encontré categoría". Es una salida intermedia válida: el paso 4 la acepta y el paso 5 la convierte en `escalar_humano`. La salida final nunca es `otro`. Es el recorrido de E9:

```text
IA: ruta=otro, confianza=baja → validación de la salida intermedia: OK → el harness escala → salida final: escalar_humano, escalar=true
```

Por eso ningún caso de `casos.json` espera `otro`: la salida esperada siempre es una ruta final. Y `escalar_humano` siempre va con `escalar: true`.

## Núcleo y extensión

| Suite | Casos | Reparto | Para quién |
|---|---|---|---|
| **Núcleo** | E1–E6 | 4 típicos, 1 límite, 1 adversarial | Todas las personas. Es una medición válida, no una suite incompleta |
| **Extendida** | E1–E10 | 5 típicos, 3 límite, 2 adversariales | Quien termina antes |

| Caso | Suite | Tipo | Qué enseña |
|---|---|---|---|
| E1, E2 | núcleo | típico | Remitente conocido: lo resuelve un `if`, sin IA |
| E3, E4 | núcleo | típico | Remitente desconocido: la IA clasifica la intención |
| E5 | núcleo | límite | Dos intenciones accionables: decide una persona |
| E6 | núcleo | adversarial | Intento de cambiar instrucciones: nunca llega a una acción |
| E7 | extensión | adversarial | La misma manipulación desde un remitente confiable |
| E8 | extensión | típico | Facturación escrita sin la palabra "factura" |
| E9 | extensión | límite | El modelo propone `otro` con confianza baja; el harness lo convierte en `escalar_humano` |
| E10 | extensión | límite | Dos preguntas, una sola intención: no debe escalar de más |

## Ejecutar sin credenciales

Desde la raíz del repositorio (en Windows, cambia `python3` por `py`):

```bash
python3 ejemplo/camino_dorado.py --modo offline --version v0
python3 ejemplo/camino_dorado.py --modo offline --version v1
python3 ejemplo/camino_dorado.py --modo offline --version v1 --suite extendida
```

`v0` no tiene la regla de seguridad ni distingue la doble intención; `v1` las agrega. El script revisa primero que `casos.json` esté bien escrito, corre cada caso por las cinco etapas, imprime el camino que siguió y compara `ruta` y `escalar` contra la salida esperada.

| Versión | Núcleo | Extendida |
|---|---:|---:|
| `v0` | 4/6 (sale con código 1 a propósito) | 7/10 |
| `v1` | 6/6 | 10/10 |

Así se ve un caso que pasa por la IA y otro que la regla detiene antes:

```text
OK    E3 (tipico) esperado=soporte obtenido=soporte fuente=ia
      camino: entrada: OK -> if: ninguna regla aplica -> IA (simulada): soporte / confianza alta -> validación del contrato: OK -> humano: no hace falta
OK    E6 (adversarial) esperado=escalar_humano obtenido=escalar_humano fuente=if
      camino: entrada: OK -> if: regla de seguridad -> escalar_humano -> validación del contrato: OK -> humano: escala (la etapa anterior pidió escalar)
```

En modo offline, la "IA" es un stub determinista. La tasa demuestra el harness; no dice nada de la calidad de un modelo.

**Qué mide este ejemplo.** Mide el **sistema completo**: `if`, IA, validación y humano. Por eso cuentan los casos que resuelve un `if`. En S2 mides solo tu decisión de IA; en S4, el sistema completo, como aquí.

**Si no tienes Python.** Abre `casos.json`, recorre los seis casos del núcleo con el diagrama de arriba y anota en una tabla la ruta que daría cada etapa. Es el mismo contrato, en papel.

## Ruta visual

El contrato no cambia en n8n, Make u otra herramienta visual: un nodo `IF` para las reglas, un clasificador para la ambigüedad (en n8n, Text Classifier), un parser de salida estructurada, un segundo `IF` para `escalar` o confianza baja, y una aprobación humana (en n8n, el Chat node). Los seis casos se corren con el nodo de evaluación de la herramienta o a mano, y la tasa se anota igual.

## Ejecutar con Claude API (opcional, fuera de clase)

Solo si ya tienes una credencial fuera del repositorio y un tope de gasto configurado:

```bash
export ANTHROPIC_API_KEY="..."
export CLAUDE_MODEL="claude-sonnet-5-5"
python3 ejemplo/camino_dorado.py --modo live --confirm-live
```

El script usa solo la biblioteca estándar. `--confirm-live` confirma explícitamente que aceptas red y posible gasto; sin esa bandera no se hace ninguna llamada. Para la suite extendida, declara también el límite de diez casos:

```bash
python3 ejemplo/camino_dorado.py --modo live --confirm-live --suite extendida --max-cases 10
```

Pide salida estructurada con JSON Schema y aplica las mismas cinco etapas. Sin `ANTHROPIC_API_KEY` se detiene con código 2: **una falla de autenticación no es una medición**. Si la API falla a media corrida, el caso escala con `fuente=harness`. El modo live es opcional y no sustituye la validación offline.

## Probar el harness sin red

```bash
python3 ejemplo/test_camino_dorado.py
```

Usa solo la biblioteca estándar: sin credenciales, sin internet y sin instalar nada. Fija las tasas de la tabla de arriba, la salida esperada de E1–E10 y cada etapa del camino, y simula las fallas del modo live con respuestas falsas de la API: JSON roto, ruta fuera del contrato, campo extra, confianza baja, falla de red y falta de clave. Si una prueba intentara salir a la red, falla. Debe terminar en `OK`.

## Qué discutir en clase

- ¿Qué parte es un `if` y por qué va antes que la IA?
- ¿Qué tiene ambigüedad genuina?
- ¿Por qué el caso adversarial nunca llega a una acción, ni desde un remitente confiable?
- ¿Qué significa que `v1` suba de 4/6 a 6/6, y qué cambió exactamente?
- ¿Qué métrica falta para operar esto en producción?
- ¿Qué cambiaría si la ruta `facturacion` disparara un reembolso?

## Archivos

- `casos.json`: seis casos del núcleo y cuatro de extensión, con su salida esperada y por qué existe cada uno.
- `camino_dorado.py`: runner sin dependencias externas, offline o live.
- `test_camino_dorado.py`: pruebas del harness, sin red ni credenciales.
