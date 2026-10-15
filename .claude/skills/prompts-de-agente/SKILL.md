---
name: prompts-de-agente
description: Escribir y depurar prompts para sistemas autónomos. Úsala cuando haya que redactar el prompt de un agente o un clasificador, cuando la IA responda fuera de formato o alucine, cuando haya que decidir el esquema de salida, o cuando alguien pida "mejorar el prompt".
---

# Prompts para sistemas autónomos

Un prompt de agente no es un prompt de chat. **No hay humano al otro lado corrigiendo.** Lo que salga, se ejecuta.

## Anatomía

```
ROL Y OBJETIVO
Una frase. "Clasificas solicitudes entrantes y decides la ruta."

CONTEXTO DEL NEGOCIO
Lo mínimo para decidir bien. No la historia de la empresa.

REGLAS DE DECISIÓN
Literales. Numeradas. Sacadas de la tabla de diseño.
Incluye SIEMPRE: qué hacer cuando ninguna regla aplica.

FORMATO DE SALIDA
JSON con esquema explícito. Nada antes, nada después.
Campos obligatorios: resultado, confianza, razonamiento.

AMBIGÜEDAD
"Si no puedes decidir con confianza alta, devuelve accion: 'escalar'
 y explica qué te faltó. NO adivines."

EJEMPLOS
2-3. Uno típico, uno límite, uno que debe escalar.
```

## Los dos campos que salvan el sistema

**`confianza`** — pídele al modelo que declare qué tan seguro está. Luego enruta: confianza baja → humano. Es la forma más barata de manejar el 5% raro sin construir lógica para cada caso.

> **Sobre `confianza`:** la confianza que un modelo verbaliza tiende a sobreestimarse (Xiong et al., ICLR 2024, https://arxiv.org/abs/2306.13063), aunque es una señal utilizable y suele estar mejor calibrada que las probabilidades internas (Tian et al., EMNLP 2023, https://aclanthology.org/2023.emnlp-main.330/).
> **Regla:** antes de enrutar con ella, calíbrala con tu suite: tasa de acierto por etiqueta (`alta`, `media`, `baja`). Si "alta" acierta el 70%, no es alta.

**`razonamiento`** — cuando el agente decida mal, vas a querer saber *por qué*. Sin este campo estás depurando a ciegas.

## Salida estructurada, siempre

Si el modelo devuelve prosa, el siguiente nodo no puede confiar en ella.

- JSON con esquema.
- **Primer camino: Structured Outputs** (GA en la API de Claude, verificado 9 oct 2026). `output_config.format` con `type: "json_schema"`, o `strict: true` en la herramienta. La API restringe la decodificación: la sintaxis sale bien por construcción. Detalle y límites en la skill `claude-api`.
- **Tu validación pasa de sintaxis a contenido.** Escribe un checker: ¿el `rfc` existe en el padrón? ¿el `total` cuadra con la OC? ¿la `categoria` es coherente con el texto? ¿`confianza: alta` viene con `razonamiento` vacío? Eso la gramática no lo garantiza. Si el checker falla, reintenta una vez metiéndole el error al prompt; si vuelve a fallar, escala.
- Sigue revisando `stop_reason`: `refusal` y `max_tokens` devuelven salida que puede no cumplir el esquema.
- Nunca dejes pasar una salida que no pasó por el checker.

En n8n: **Structured Output Parser** y **Auto-fixing Output Parser** (el segundo hace el reintento por ti). Si el nodo que usas no expone Structured Outputs, el camino viejo (pedir JSON y validar el esquema tú) sigue funcionando; es el segundo camino, no el primero.

## Descomponer

Si el agente hace cinco cosas, son **cinco prompts encadenados**, no uno. Un prompt monolítico es imposible de depurar: falla y no sabes cuál de las cinco cosas se rompió.

Y cada paso encadenado puede ir a un modelo distinto. Clasificar → Haiku 5.5. Redactar → Sonnet 5.5.

## Errores frecuentes

**Prompt vago.** "Clasifica bien los correos." ¿Bien según quién? Si tú no puedes escribir la regla, el modelo no la va a inferir.

**Sin caso default.** El modelo encuentra algo que no encaja en ninguna categoría e inventa una. Siempre define qué pasa entonces.

**Demasiado contexto.** Meterle 5,000 palabras de política interna degrada la decisión y multiplica el costo. Solo lo que necesita para decidir.

**Ejemplos solo del camino feliz.** Incluye siempre un ejemplo que debe escalar. Si no, el modelo aprende que siempre hay que decidir algo.

## Cuando la precisión es mala

En este orden, no en otro:

1. **¿La regla está escrita de forma ambigua?** — Es lo más común. El humano no sabía qué quería y le pasó la ambigüedad al modelo.
2. ¿Faltan ejemplos, sobre todo del caso límite?
3. ¿Le estás pidiendo al modelo algo que era un `if`?
4. ¿El modelo es el adecuado?

Casi nunca es el modelo.

## Versiónalos

Los prompts son código. Van a `proyectos/<nombre>/prompts.md`, con versión. Cuando cambies uno, **corre los evals otra vez** (ver skill `errores-y-evals`).
