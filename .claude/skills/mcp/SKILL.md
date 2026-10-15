---
name: mcp
description: Model Context Protocol. Úsala cuando se hable de MCP, servidores MCP, conectar Claude Desktop o Cursor a sistemas propios, o cuando alguien proponga MCP como solución. También para decidir si MCP es lo correcto o es sobreingeniería.
---

# MCP

**Lee `referencias/mcp.md` para versiones. La vigente es `2026-07-28` (sin estado, sin handshake: cada request declara su versión); `2025-11-25` es la anterior y sigue soportada por compatibilidad.**

## Empieza por aquí: probablemente no lo necesitas

Sé honesto. MCP resuelve un problema de **N agentes × M herramientas**: escribir un adaptador por cada combinación no escala, así que se estandariza el protocolo.

**Si tienes 1 agente y 3 herramientas, no tienes ese problema.**

- ¿Conectar una API dentro de tu propio workflow? → **HTTP Request.** Más simple, más rápido de depurar, no requiere levantar un servidor.
- ¿Que Claude Desktop, Cursor o un agente externo llame a *tus* sistemas? → **ahí sí, MCP.**
- ¿Exponer una capacidad tuya a muchos agentes distintos sin escribir un adaptador por cada uno? → MCP.

Montar un servidor MCP para conectar una API dentro de tu propio flujo es la forma más elegante de complicarse la vida.

## El atajo que casi nadie usa

**El nodo MCP Server Trigger de n8n convierte cualquier workflow en un servidor MCP.**

Construyes el flujo visualmente, le pones ese trigger, y ya tienes una herramienta que Claude Desktop puede llamar. Sin escribir un servidor, sin manejar el transporte, sin OAuth.

Si alguien quiere "que Claude pueda consultar nuestro inventario", esto es la respuesta correcta en el 90% de los casos, no escribir un servidor MCP desde cero.

Al revés también: n8n consume servidores MCP con **MCP Client** y **MCP Client Tool**.

## Lo esencial del protocolo

Tres primitivas:
- **Tools** — acciones ejecutables. Lo que casi siempre quieres.
- **Resources** — datos de solo lectura que el host decide cuándo cargar.
- **Prompts** — plantillas reutilizables.

Dos transportes: **stdio** (local) y **Streamable HTTP** (remoto). HTTP+SSE está formalmente deprecado desde 2026-07-28; no construyas nada nuevo sobre él.

## Seguridad

Un servidor MCP le da a un agente la capacidad de **ejecutar acciones en tus sistemas**.

- Scope mínimo. Si solo necesita leer, no expongas escritura.
- Cualquier herramienta que haga algo irreversible → confirmación humana.
- El contenido que devuelve una herramienta puede contener inyección de prompt. Ver skill `seguridad-datos`.
