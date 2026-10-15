---
type: referencia-framework
title: LangChain / LangGraph
description: Versiones, lo deprecado (AgentExecutor), y cuándo usar cada uno frente a n8n.
resource: https://docs.langchain.com
tags: [langchain, langgraph, agentes, orquestacion]
timestamp: 2026-07-13T00:00:00Z
---

# LangChain / LangGraph — hechos verificados

> **Verificado: 13 julio 2026** contra langchain.com/blog y github.com/langchain-ai

## Versiones

- **LangChain 1.x** (1.0 salió en octubre 2025). Compromiso público de no romper hasta 2.0.
- **LangGraph 1.2.8** (6 julio 2026).

## Lo que está deprecado — y la gente sigue copiando de tutoriales viejos

**`AgentExecutor` e `initialize_agent()` están deprecados.** En modo mantenimiento hasta diciembre de 2026.

Si ves esto en código o en un tutorial, es de 2024:
```python
from langchain.agents import initialize_agent, AgentExecutor  # NO
```

Hoy: `langchain.agents` (para el patrón prebuilt) o `StateGraph` de LangGraph para orquestación custom. `langgraph.prebuilt` también se movió a `langchain.agents`.

El patrón viejo usaba scratchpads ocultos; el nuevo usa esquemas de estado explícitos (TypedDict). El nuevo es depurable. El viejo no.

## Cuándo cuál

- **LangChain** — construir el agente rápido. Loop de agente estándar, tool calling, middleware. Agnóstico de proveedor.
- **LangGraph** — orquestación de bajo nivel. Grafos cíclicos, estado durable, checkpointers, human-in-the-loop de primera clase, time-travel debugging.
- **n8n** — si el flujo se puede dibujar visualmente y el equipo no es de ingenieros. **Es la opción correcta para la mayoría de las automatizaciones de negocio.**

## La opinión

Si tu automatización cabe en n8n, **hazla en n8n**. LangGraph es para cuando necesitas control fino sobre el ciclo del agente: loops, reintentos condicionales, estado que sobrevive días, workflows de aprobación multi-etapa.

Meter LangGraph a un problema que era un workflow visual es la forma más cara de sentirse ingeniero.

Y lo contrario: **los agentes en memoria son juguetes.** Producción requiere estado durable (Postgres/Redis). Si el servidor se reinicia a media conversación y pierdes todo, no tienes un sistema, tienes una demo.

Fuente: https://www.langchain.com/blog/langchain-langgraph-1dot0
