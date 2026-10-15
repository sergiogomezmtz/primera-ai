---
type: index
title: Referencias verificadas
description: Bundle OKF con los hechos duros del stack. Verificados contra fuente oficial y fechados. Ninguno se cita de memoria.
tags: [index, referencias, hechos-verificados]
timestamp: 2026-10-09T00:00:00Z
---

# Referencias

Bundle conforme a **Open Knowledge Format v0.1** (el spec ya va en v0.2; la migración del frontmatter está pendiente, ver [okf.md](okf.md) y [log.md](log.md)). Cada archivo es un concepto; el frontmatter es consultable; los links cruzados forman el grafo.

Esto es lo que hace que este repo valga más que un asistente a secas: **hechos verificados contra fuente oficial, con fecha.** Un LLM alucina precios y rate limits con total confianza. Estos archivos no.

**Regla: ningún hecho duro se cita de memoria. Se lee de aquí.**

## Conceptos

| Concepto | Tipo | Qué contiene |
|---|---|---|
| [Claude API](claude-api.md) | referencia-api | Precios, rate limits, caching, batch, costos ocultos |
| [n8n](n8n.md) | referencia-plataforma | Nodos, versiones, trampas, los nodos de IA infrautilizados |
| [MCP](mcp.md) | referencia-protocolo | Versiones del spec, primitivas, cuándo es sobreingeniería |
| [LangChain / LangGraph](langchain.md) | referencia-framework | Versiones, lo deprecado, cuándo usar cuál |
| [Harness](harness.md) | referencia-patron | Agentes de larga duración: fallas y soluciones verificadas |
| [Gobernanza](gobernanza.md) | referencia-patron | Contención, permisos mínimos, egress, fatiga de aprobación, blast radius |
| [Agent Engineering](agent-engineering.md) | referencia-campo | Estado del campo: adopción, horizonte autónomo, error compuesto, las 7 capas |
| [Multiagente](multiagente.md) | referencia-campo | Cuándo un multiagente paga sus tokens: Anthropic vs Cognition, UIUC, Azure SRE, modos de falla |
| [OKF](okf.md) | especificacion | El formato de este bundle (v0.1 en uso; v0.2 documentada) |
| [Cómo actualizar](COMO-ACTUALIZAR.md) | runbook | Procedimiento de re-verificación |

## Estado

**Última verificación: 9 de octubre de 2026** (Claude API, MCP, n8n, OKF, METR, multiagente). LangChain y harness siguen con fecha 13 de julio de 2026; gobernanza fue verificada el 3 de agosto de 2026.

Se pudren. Corre `/verificar` cada dos meses, o antes de cualquier decisión de costos que importe.

Ver [log.md](log.md) para el historial.
