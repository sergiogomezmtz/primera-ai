# Patrón 01 — Clasificar y rutear

**Llega algo (correo, ticket, lead, formulario). Hay que decidir a dónde va.**

Es el patrón más común y el que más se construye mal.

## El error

Sacar el nodo AI Agent. **No.** Un agente sirve cuando el modelo debe elegir herramientas y orden. Aquí solo hay que clasificar. En n8n eso es el nodo **Text Classifier**, que además rutea la salida por rama.

Más barato, más rápido, más predecible, y no puede alucinar un paso que no existe.

## Estructura

```
Trigger (Gmail / Webhook / Form)
   ↓
Validación de entrada        ← ¿está vacío? ¿es del tipo correcto?
   ↓
Filtro con `if`              ← lo que se puede decidir sin IA, se decide sin IA
   ↓                            (remitente conocido, dominio interno, palabra clave exacta)
Text Classifier              ← SOLO la ambigüedad real
   ↓
├─ Categoría A → acción
├─ Categoría B → acción
├─ Categoría C → acción
└─ Sin categoría / baja confianza → HUMANO
   ↓
Error Trigger (workflow aparte, observabilidad)
```

## Las tres cosas que casi nadie hace

**1. El filtro `if` antes del clasificador.** Si el 40% de los correos vienen de un dominio conocido y siempre van a la misma rama, eso es un `if`. No pagues tokens por ello. Reduces costo y aumentas precisión al mismo tiempo, porque el clasificador solo ve los casos difíciles.

**2. La rama de "no sé".** El clasificador *va* a encontrar cosas que no encajan. Si no le das una salida, va a inventar una categoría. Rama explícita: baja confianza o ninguna categoría → humano.

**3. Medir.** 6 casos de eval (4 típicos, 1 límite, 1 adversarial) con la categoría correcta anotada a mano; 10 en la suite extendida. Sin eso, "funciona bien" es una opinión. El ejemplo completo corre en [`ejemplo/`](../ejemplo/README.md).

## Prompt del clasificador

```
Clasificas [X] entrantes en exactamente una categoría.

CATEGORÍAS
- soporte_tecnico: el usuario reporta que algo no funciona
- ventas: pregunta por precio, demo o contratación
- facturacion: cobros, facturas, pagos
- otro: no encaja claramente en ninguna anterior

REGLAS
- Una sola categoría. La más específica que aplique.
- Si el mensaje toca dos temas, gana el que motiva la acción.
- Si dudas, usa "otro". NO fuerces una categoría.

SALIDA (JSON, nada más)
{
  "categoria": "soporte_tecnico|ventas|facturacion|otro",
  "confianza": "alta|media|baja",
  "razonamiento": "una frase"
}
```

Enruta `confianza: baja` a humano. Es tu red.

> **Sobre `confianza`:** la confianza que un modelo verbaliza tiende a sobreestimarse (Xiong et al., ICLR 2024, https://arxiv.org/abs/2306.13063), aunque es una señal utilizable y suele estar mejor calibrada que las probabilidades internas (Tian et al., EMNLP 2023, https://aclanthology.org/2023.emnlp-main.330/).
> **Regla:** antes de enrutar con ella, calíbrala con tu suite: tasa de acierto por etiqueta (`alta`, `media`, `baja`). Si "alta" acierta el 70%, no es alta.

## Costo

Haiku 5.5 (`claude-haiku-5-5`). Nunca Opus para esto; con los precios vigentes Sonnet 5.5 cuesta 20× más que Haiku 5.5 en esta tarea. Si el volumen es alto y no es urgente, considera Batch API (50% menos). Ver `referencias/claude-api.md`.
