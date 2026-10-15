---
type: referencia-protocolo
title: Model Context Protocol
description: Versiones del spec, primitivas, transportes, y cuándo MCP es sobreingeniería.
resource: https://modelcontextprotocol.io/specification/versioning
tags: [mcp, protocolo, agentes, herramientas]
timestamp: 2026-10-09T00:00:00Z
---

# MCP (Model Context Protocol) — hechos verificados

> **Verificado: 9 octubre 2026** contra https://modelcontextprotocol.io/specification/versioning y /specification/2026-07-28/changelog

## Versión

- **Vigente: `2026-07-28`.** Es la revisión marcada como *current* en el spec. Lo que en julio de 2026 era un candidato a versión ya es la que corren SDKs y hosts.
- **Anterior: `2025-11-25`.** Sigue existiendo para compatibilidad: la 2026-07-28 documenta cómo interoperar con servidores y clientes que todavía usan el handshake `initialize`.

Las versiones son cadenas de fecha (`YYYY-MM-DD`). Desde 2026-07-28 **cada request declara su versión** en `_meta` (`io.modelcontextprotocol/protocolVersion`) y el servidor acepta o rechaza request por request; ya no hay handshake. Un cliente puede llamar `server/discover` para ver qué versiones soporta el servidor antes de mandar nada.

Nota de vocabulario: el spec reserva *Final* para revisiones pasadas que ya no cambian; la vigente se llama *Current* y puede recibir cambios compatibles hacia atrás.

## Qué cambió en 2026-07-28 (contra 2025-11-25)

- **Core sin estado.** Se eliminan las sesiones de protocolo (`Mcp-Session-Id`) y el handshake `initialize`. Escala sobre infraestructura HTTP normal. Es el cambio grande.
- **`server/discover`** obligatorio: versiones soportadas, capacidades e identidad en una sola llamada.
- **Extensions.** Campo `extensions` en capacidades; las *tasks* (trabajo de larga duración) salen del core y pasan a una extensión oficial (`io.modelcontextprotocol/tasks`).
- **Multi Round-Trip Requests (MRTR).** Reemplaza las requests iniciadas por el servidor (`sampling`, `elicitation`, `roots`): el servidor devuelve `input_required` y el cliente reintenta con la información pedida.
- **Deprecados:** Roots, Sampling y Logging; el transporte HTTP+SSE; y el registro dinámico de clientes OAuth (RFC 7591) a favor de Client ID Metadata Documents.
- **Política formal de deprecación:** mínimo doce meses en estado *Deprecated* antes de poder removerse.

## Lo esencial

Tres primitivas: **Tools** (acciones ejecutables), **Resources** (datos de solo lectura), **Prompts** (plantillas reutilizables).

Dos transportes: **stdio** (local, misma máquina) y **Streamable HTTP** (remoto). HTTP+SSE está formalmente deprecado desde 2026-07-28.

## Cuándo MCP es sobreingeniería

Casi siempre, para lo que la mayoría está construyendo. Sé honesto aquí.

**Úsalo si:** quieres que Claude Desktop, Cursor o cualquier host llame a *tus* sistemas; o quieres exponer una capacidad a muchos agentes distintos sin escribir un adaptador por cada uno.

**No lo uses si:** solo estás conectando una API dentro de tu propio workflow. Un nodo HTTP Request es más simple, más rápido de depurar y no requiere levantar un servidor.

MCP resuelve un problema de **N agentes × M herramientas**. Si tienes 1 agente y 3 herramientas, no tienes ese problema.

Atajo útil: **el MCP Server Trigger de n8n convierte cualquier workflow en un servidor MCP.** Es la forma más barata de exponer una capacidad tuya a un agente, sin escribir un servidor desde cero.

Fuentes:
- https://modelcontextprotocol.io/specification/versioning
- https://modelcontextprotocol.io/specification/2026-07-28/changelog
