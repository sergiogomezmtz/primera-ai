---
type: referencia-campo
title: Sistemas multiagente
description: Cuándo un sistema multiagente paga sus tokens y cuándo no. Solo cifras con fuente primaria; lo demás marcado como no verificado.
resource: https://www.anthropic.com/engineering/multi-agent-research-system
tags: [multiagente, agentes, costos, arquitectura, verificado]
timestamp: 2026-10-09T00:00:00Z
---

# Sistemas multiagente — hechos verificados

> Hechos para citar **de aquí, no de memoria**. Fechados contra fuente. **Verificado: 9 octubre 2026.** Lo que no tiene link primario está marcado "no verificado" y no se presenta en clase.

## El debate fundacional (dos voces, misma semana, jun 2025)

- **Anthropic — "How we built our multi-agent research system"** · https://www.anthropic.com/engineering/multi-agent-research-system · jun 2025.
  - Un sistema multiagente (lead **Claude Opus 4** + subagentes **Claude Sonnet 4**) superó al agente único Opus 4 por **90.2%** en su eval interna de investigación. **Es mejora relativa sobre el agente único en una eval interna, no una precisión.** La versión "90.2% vs 80.9% de precisión" que circula está mal citada.
  - Funciona **principalmente porque gasta suficientes tokens** para resolver el problema. En su análisis de BrowseComp, tres factores explicaron el **95%** de la varianza de desempeño; **el uso de tokens por sí solo explica el 80%**. Los otros dos: número de tool calls y elección de modelo.
  - Costo: los agentes usan ~4× los tokens de un chat; los sistemas multiagente, **~15×**.
  - Brilla en tareas **breadth-first**: direcciones múltiples e independientes en paralelo. Mal ajuste cuando los agentes deben compartir contexto o hay muchas dependencias entre ellos.
- **Cognition — "Don't Build Multi-Agents"** (Walden Yan) · https://cognition.com/blog/dont-build-multi-agents · 12 jun 2025.
  - Subagentes en paralelo toman decisiones independientes → salidas en conflicto (ejemplo: clon de Flappy Bird donde un subagente hace un fondo estilo Super Mario y el otro un pájaro que no cuadra con el juego).
  - Regla textual: **"Share context, and share full agent traces, not just individual messages."** Acuñó el uso de "context engineering" para este problema.
- Reconciliación: no es ideología, es **fit a la forma de la tarea**. Anthropic = investigación breadth-first (subtareas independientes). Cognition = escribir código (cada decisión condiciona la siguiente).

## La economía

- **UIUC — Gao et al. 2025, "Single-agent or Multi-agent Systems? Why Not Both?"** · https://arxiv.org/abs/2505.18286 · University of Illinois Urbana-Champaign.
  - Sección 3.2: en su comparación, el sistema multiagente consume **4–220× más tokens de ENTRADA (prefill)** que su equivalente de un solo agente; en tokens de salida (decode), 2–12×. El 220× es el extremo (AIME). Ojo: es prefill, no costo total ni latencia.
  - Hallazgo central: la ventaja del multiagente **se achica conforme mejora el modelo base**. Proponen escalar en cascada: un agente primero, multiagente solo para lo que falla.
- Multiplicadores de costo con fuente: **~15×** en tokens (Anthropic, arriba); **4–220×** en prefill (UIUC, arriba).
- **No verificado** (sin link primario; no citar en clase): "a presupuesto de tokens igual, un solo agente iguala o supera al multiagente (Stanford; Tran & Kiela; OneFlow)"; "2–5× típico"; el caso de "$47,000/mes multiagente al 94.3% vs $22,700/mes agente único al 92.2%".
- **Microsoft — Azure SRE Agent** · https://techcommunity.microsoft.com/blog/appsonazureblog/context-engineering-lessons-from-building-azure-sre-agent/4481200 · 26 dic 2025. Empezaron con **100+ herramientas y 50+ subagentes especializados** con handoffs; arriba de cuatro handoffs la tarea casi siempre fallaba (descubrimiento, prompts frágiles, loops infinitos, visión de túnel). **No "revirtieron a un agente": consolidaron docenas de especialistas en un puñado de generalistas** con 5 herramientas núcleo y conocimiento de dominio en archivos cargados bajo demanda. Textual: *"The fix was to collapse dozens of specialists into a small set of generalists."* La confiabilidad subió al dejar de depender de la "ruleta de handoffs".

## La aritmética del error compuesto, a nivel de agente

- 1 agente → 95% · 3 → 86% · 5 → **77%** · 8 → 66% (asumiendo 95% por agente). Cada subagente es otro `× 0.95`. No es una cita: es `0.95^n`.

## Modos de falla nuevos (taxonomía de Microsoft, v2, 4 jun 2026)

Fuente: https://www.microsoft.com/en-us/security/blog/2026/06/04/updating-taxonomy-failure-modes-agentic-ai-systems-year-red-teaming-taught-us

- **Inter-Agent Trust Escalation:** en cadenas de delegación, un agente comprometido afirma una identidad falsa o permisos inflados ante un orquestador que no los verifica (el "confused deputy", inducido por lenguaje natural).
- **Computer Use Agent (CUA) Visual Attack:** instrucciones adversarias escondidas en contenido visual que a una persona le parece inofensivo (texto diminuto, fuera de pantalla, imágenes con prompts embebidos).

## Observabilidad (el juez)

- **No verificado** (texto de producto sin link primario): la descripción de LangSmith sobre LangGraph (traza = grafo de ejecución, diffs de estado, replay, costo unificado, P50/P99). La idea sigue siendo correcta como requisito: **el veredicto costo-beneficio sale de la traza, no de la vibra.** Si vas a citar la capacidad concreta, verifica en https://docs.langchain.com primero.

## Cuándo SÍ / cuándo NO

- **SÍ:** subtareas independientes · paralelizables · multi-dominio · no caben en un contexto.
- **NO:** secuencial · dependiente · comparte contexto · cabe en un solo agente bien contextualizado.
