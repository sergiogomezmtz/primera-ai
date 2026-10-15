---
type: suite-de-evals
proyecto: [nombre]
decision: [la decisión de IA que estás evaluando]
suite: nucleo   # nucleo = 6 casos (4/1/1) · extendida = 10 casos (5/3/2)
modo: escritorio   # escritorio (S2-S3) · sistema (S4) · importado (ruta visual)
estado: sin-correr
---

# Evals — [tu decisión]

<!--
CÓMO USAR ESTA PLANTILLA
1. Copia este archivo a proyectos/<tu-proyecto>/evals.md
2. Llena las 6 filas del núcleo con TUS casos reales (4 típicos, 1 límite y 1 adversarial).
   Con eso ya puedes medir: el núcleo es una suite válida. Las filas E7-E10 son extensión opcional.
3. Cuando esté lleno, corre /eval. NO llenes resultados a mano: eso lo hace /eval.
   Tu trabajo aquí es el input y la salida esperada. Nada más.
-->

Toma la decisión más difícil de tu `decisiones.md`. Los primeros 6 casos forman el núcleo, que basta para medir y avanzar. Los 10 forman la suite extendida, si te da el tiempo.

**Reglas al llenar (no las negocies):**
- **Núcleo: 4 típicos · 1 límite · 1 adversarial. Extendida (opcional): 5 típicos · 3 límite · 2 adversariales.** Si los casos son del camino feliz, tu número va a mentir hacia arriba.
  - *Típico:* lo que pasa casi siempre.
  - *Límite:* raro pero real, sacado de tu operación (el redondeo, el caso fronterizo, el "a veces son las dos").
  - *Adversarial:* diseñado para romperla — input vacío, en otro idioma, un intento de manipular al agente, un dato que no está.
- **La salida esperada la fijas tú, y tiene que verificarse SIN volver a preguntarle al modelo.** Un campo concreto: una categoría, un sí/no, un valor. Si para saber si acertó tendrías que opinar, el caso está mal escrito.
- **En modo escritorio, un caso que resuelve un `if` no mide tu IA.** Anótalo aparte. En modo sistema (S4) sí entra, porque ahí mides el flujo completo, como en el [camino dorado del repositorio canónico](https://github.com/nabolom/agentic-ai-automation-mentor-agent-2026/blob/main/ejemplo/README.md).

## Casos

| # | Suite | Tipo | Input (tu caso real) | Salida esperada |
|---|---|---|---|---|
| E1 | núcleo | típico |  |  |
| E2 | núcleo | típico |  |  |
| E3 | núcleo | típico |  |  |
| E4 | núcleo | típico |  |  |
| E5 | núcleo | límite |  |  |
| E6 | núcleo | adversarial |  |  |
| E7 | extensión | típico |  |  |
| E8 | extensión | límite |  |  |
| E9 | extensión | límite |  |  |
| E10 | extensión | adversarial |  |  |

<!--
Después de correr /eval, este archivo va a tener columnas de resultados (v0, v1…),
una tasa con su suite y su modo (ej. "v0 · escritorio · núcleo 6 casos: 4/6")
y la salida cruda de al menos un fallo. El diff entre versiones es la historia de tu sistema.
Corre /eval cada vez que toques el prompt.
-->
