---
type: runbook
title: Cómo mantener vivas las referencias
description: Procedimiento para re-verificar hechos duros contra fuente oficial. Ningún hecho sin fecha y sin fuente.
tags: [runbook, mantenimiento, verificacion]
timestamp: 2026-07-13T00:00:00Z
---

# Cómo mantener vivas estas referencias

Estos archivos son la única razón por la que este repo vale más que un asistente de IA a secas.

Un asistente de IA alucina precios, rate limits y nombres de nodos **con total confianza**. Estos archivos están verificados contra fuente oficial y fechados. Ese es todo el truco.

## La regla

**Ningún hecho duro sin fecha y sin fuente.** Si no puedes verificarlo, no lo escribas.

## Cuándo re-verificar

- Cualquier archivo con más de **2 meses** desde su fecha de verificación.
- Antes de cualquier decisión de costos o arquitectura que importe.
- Cuando el asistente y la referencia se contradigan. **Gana la referencia** — hasta que vayas a la fuente y la actualices.

Corre `/verificar` y el acompañador va a las fuentes oficiales, compara y actualiza.

## Advertencia sobre blogs

Al armar estos archivos, **tres de los blogs mejor rankeados de "Claude API pricing 2026" tenían datos viejos o mal**: modelos retirados presentados como actuales, precios de generaciones anteriores. Uno de ellos era la primera posición de Google.

**Siempre la fuente oficial.** Los agregadores están optimizados para SEO, no para estar correctos.

## Fuentes canónicas

| Tema | Fuente |
|---|---|
| Claude API | https://platform.claude.com/docs/en/about-claude/pricing |
| Rate limits | https://platform.claude.com/docs/en/api/rate-limits |
| n8n | https://docs.n8n.io |
| MCP | https://blog.modelcontextprotocol.io |
| LangChain/LangGraph | https://docs.langchain.com |
