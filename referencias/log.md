---
type: log
title: Historial de verificación
description: Registro cronológico de cambios en el bundle de referencias.
tags: [log, historial, verificacion]
timestamp: 2026-10-09T00:00:00Z
---

# Log

## 2026-10-09 — Verificación Q4 (rama q4-rumbo)

Re-verificados contra fuente oficial: `claude-api.md`, `mcp.md`, `n8n.md`, `okf.md`, `agent-engineering.md` (sección METR y lista de no verificados), `multiagente.md` (reescrito con frontmatter OKF y sumado a `index.md`). También las skills `claude-api`, `costos`, `prompts-de-agente`, `mcp`, `okf`, los patrones 01, 02 y 06, `/verificar` y `docs/competencias.md`.

**Hallazgos:**

- **Generación vigente: Fable 5.1 ($10/$50), Opus 5.5 ($4/$20), Sonnet 5.5 ($2/$10), Haiku 5.5 ($0.10/$0.50 hasta 100k tokens de prompt; $0.50/$2.50 arriba).** Haiku 4.5 sigue activo con retiro no antes del 15 de octubre de 2026: dejó de recomendarse en skills y patrones. Sonnet 4.5 deprecado, retiro 30 nov 2026.
- **La subida de Sonnet 5 a $3/$15 no ocurrió.** La página de precios lo dice en su nota 3: el $2/$10 quedó como estándar. Se borró la advertencia de `claude-api.md`, `.claude/skills/costos`, `/verificar` y este log (la entrada de julio se conserva como histórico).
- **"Diferencia de 5×" recalculada:** Haiku 5.5 → Sonnet 5.5 es 20×; Sonnet 5.5 → Opus 5.5 es 2×. El salto caro cambió de lugar.
- **Rate limits re-verificados** para Start/Build/Scale; cache reads siguen sin contar para ITPM; el 429 por tope de gasto no trae `retry-after`.
- **Structured Outputs es GA:** `output_config.format` + `json_schema` y `strict: true` en tools, con decodificación restringida. Excepciones: refusal, max_tokens, capitalización de enums. Pasa a ser el primer camino de salida estructurada en `.claude/skills/claude-api` y `.claude/skills/prompts-de-agente`; la validación propia se mueve de sintaxis a contenido.
- **Campo `confianza`:** la confianza verbalizada tiende a sobreestimarse (Xiong et al., ICLR 2024) pero es señal utilizable (Tian et al., EMNLP 2023). Nota agregada en `prompts-de-agente` y patrones 01, 02, 06: calibrar con la suite antes de enrutar.
- **MCP:** `2026-07-28` ya es la versión vigente (*current*); `2025-11-25` es la anterior. Se reescribió la sección "qué trae" con el changelog oficial (sin estado, `server/discover`, MRTR, tasks como extensión, deprecación de Roots/Sampling/Logging y HTTP+SSE).
- **n8n:** estable 2.42.x (2.42.6 publicado el 9 de octubre de 2026). Guardrails, Evaluation, Evaluation Trigger y MCP Server Trigger siguen existiendo; se agregaron las URLs de doc.
- **OKF va en v0.2:** `type` sigue siendo el único obligatorio; `timestamp` → `generated.at`; aparecen `sources`, `verified`, `status`, `stale_after`. Documentado en `okf.md` y `.claude/skills/okf`. **Pendiente: migrar el frontmatter de este bundle a v0.2.** Se deja a propósito para un commit aparte.
- **METR:** Opus 4.6 = 718.8 min al 50% (IC 95% 316.7–3,633.8) y 69.9 min al 80%; duplicación desde 2023 = 128.7 días (antes decía 130.8). Se conserva la advertencia de >16 h.
- **Multiagente:** UIUC = Gao et al. 2025 (4–220× en tokens de *entrada*, no de costo); Azure SRE Agent consolidó 50+ subagentes en pocos generalistas, no "revirtió"; el 90.2% de Anthropic es mejora relativa sobre Opus 4 en eval interna, y sale de la lista de no verificados de `agent-engineering.md` (ahí queda solo la versión mal citada "90.2% vs 80.9% de precisión"). Las cifras sin link primario ($47,000 vs $22,700; "Stanford; Tran & Kiela; OneFlow") quedan marcadas "no verificado".

**Higiene del harness (mismo día, rama q4-rumbo):** las skills se movieron de `skills/` a `.claude/skills/` para que Claude Code las cargue de verdad; `/loop` pasó a llamarse `/cuatro-paradas` porque chocaba con el `/loop` integrado de Claude Code.

**Pendiente de verificar:** nada de lo tocado quedó sin fuente. La migración del frontmatter a OKF v0.2 es trabajo pendiente, no verificación pendiente.

**Nota metodológica:** el spec de MCP llama *current* a la revisión vigente y reserva *final* para las pasadas; por eso el archivo dice "vigente" y no "final".

## 2026-07-13 — Verificación inicial

Bundle creado. Todas las referencias verificadas contra fuente oficial.

**Hallazgos:**

- **Sonnet 5 está en precio introductorio** ($2/$10 por MTok) **hasta el 31 de agosto de 2026.** Sube a $3/$15 el 1 de septiembre. Cualquier modelo de costos anual hecho con el precio de hoy queda 50% abajo.
- **Tokenizador nuevo** en Opus 4.7+, Sonnet 5 y Fable 5: ~30% más tokens para el mismo texto. Las estimaciones hechas con la intuición de modelos anteriores se quedan cortas por un tercio.
- **Los tokens leídos de cache no cuentan para el rate limit ITPM.** El caching no es solo descuento: es multiplicador de throughput.
- **n8n tiene nodos nativos de Guardrails y Evaluation**, y human-in-the-loop en tool calls. Casi ningún tutorial los menciona.
- **MCP:** estable `2025-11-25`; hay RC `2026-07-28` que aún puede cambiar. No construir contra el RC.
- **LangChain:** `AgentExecutor` deprecado (mantenimiento hasta dic 2026). Los tutoriales que lo usan son de 2024.

**Nota metodológica:** tres de los blogs mejor rankeados de "Claude API pricing 2026" tenían datos viejos o incorrectos —incluyendo el primer resultado de Google— presentando modelos retirados como actuales. **Siempre fuente oficial.**

Bundle convertido a **OKF v0.1** el mismo día.
