---
type: referencia-plataforma
title: n8n
description: Nodos, versiones, trampas y los nodos de IA que casi nadie usa (Guardrails, Evaluation, MCP Server Trigger).
resource: https://docs.n8n.io
tags: [n8n, workflows, nodos, automatizacion]
timestamp: 2026-10-09T00:00:00Z
---

# n8n — hechos verificados

> **Verificado: 9 octubre 2026** contra https://registry.npmjs.org/n8n (versión) y https://docs.n8n.io (nodos)
> Re-verificar con `/verificar`.

## Versión

Línea **2.x** (estable **2.42.x** al 9 de octubre de 2026: `latest` = 2.42.6; el canal `next` ya va en 2.43.x). n8n 2.0 fue un cambio mayor con breaking changes: si alguien viene de 1.x, mándalo a la guía de migración antes de nada.

## Los nodos que importan (y que casi nadie usa)

Los nodos de IA viven bajo el paquete `n8n-nodes-langchain.*`. Los de siempre bajo `n8n-nodes-base.*`.

### Decisión con IA — antes de sacar el AI Agent

Casi nunca necesitas el nodo AI Agent. Estos son más baratos, más rápidos y más predecibles:

- **Text Classifier** (`n8n-nodes-langchain.text-classifier`) — clasifica en categorías y **rutea la salida por rama**. Si tu "agente" solo clasifica y enruta, es esto. Punto.
- **Information Extractor** (`n8n-nodes-langchain.information-extractor`) — documento/texto → JSON con esquema. Es el patrón de extracción, ya hecho.
- **Sentiment Analysis** (`n8n-nodes-langchain.sentimentanalysis`)
- **Basic LLM Chain** (`n8n-nodes-langchain.chainllm`) — prompt entra, texto sale. Una sola pasada.
- **AI Agent** (`n8n-nodes-langchain.agent`) — solo cuando el modelo debe **elegir herramientas y orden**. Variantes: Tools Agent (el default correcto), ReAct, Plan-and-Execute, SQL Agent, Conversational.

### Confiabilidad — los tres que cambian todo

- **Guardrails** (`n8n-nodes-langchain.guardrails`) — nodo nativo de validación de entradas/salidas del LLM. Dos operaciones: *Check Text for Violations* (keywords, jailbreak, NSFW, PII, llaves secretas, alineación de tema, regex; lo que viola va a la rama Fail) y *Sanitize Text* (reemplaza URLs, PII y llaves por placeholders). Existe. Úsalo. Doc: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.guardrails
- **Evaluation** y **Evaluation Trigger** (`n8n-nodes-base.evaluation`, `.evaluationtrigger`) — **evals nativos dentro de n8n**. El trigger lee un dataset (Data Table o Google Sheets) y manda los casos uno por uno; el nodo Evaluation fija salidas, métricas y detecta si estás en modo evaluación. Corres tu workflow contra casos con salida esperada y mides. Esto es lo que separa "creo que funciona" de "funciona el 92%". Docs: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.evaluation/ y /n8n-nodes-base.evaluationtrigger/
- **Structured Output Parser** (`n8n-nodes-langchain.outputparserstructured`) y **Auto-fixing Output Parser** (`.outputparserautofixing`) — el auto-fixing reintenta con el error cuando el modelo se sale del esquema. Es tu red de seguridad.

### Human-in-the-loop (nativo desde 2.5/2.6)

- **Chat node** (`n8n-nodes-langchain.chat`) — acción *Send a message and wait for response*. El agente puede pedir aclaración a media ejecución.
- HIL en **tool calls**: el agente propone una acción y espera aprobación humana antes de ejecutarla. Esto es lo que necesitas para cualquier acción irreversible (mandar el correo, cobrar, borrar).

### Modelos y memoria

- **Anthropic Chat Model**: `n8n-nodes-langchain.lmchatanthropic`. También hay OpenAI, Gemini, Bedrock, Groq, OpenRouter, Ollama, DeepSeek, Mistral, xAI.
- **Model Selector** (`n8n-nodes-langchain.modelselector`) — rutea a distintos modelos según condición. Así mandas lo fácil a Haiku 5.5 y lo difícil a Sonnet 5.5 u Opus 5.5 dentro del mismo flujo.
- Memoria: **Simple Memory** (en n8n, se pierde al reiniciar) o Postgres / Redis / MongoDB / Zep para memoria que sobrevive.

### MCP dentro de n8n

- **MCP Client** (`n8n-nodes-langchain.mcpClient`) y **MCP Client Tool** (`.toolmcp`) — n8n consume herramientas de servidores MCP.
- **MCP Server Trigger** (`n8n-nodes-langchain.mcptrigger`) — **tu workflow de n8n se expone como servidor MCP** por SSE o Streamable HTTP. Cualquier agente (Claude, Cursor, lo que sea) puede llamarlo como herramienta. Esto es una puerta trasera enorme y poca gente la usa. Doc: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger/

### Vector stores (para RAG)

Qdrant, Pinecone, PGVector, Supabase, Milvus, Weaviate, Chroma, MongoDB Atlas, Redis, Azure AI Search, y **Simple Vector Store** (en memoria — solo para prototipar; se borra al reiniciar).

### Otros útiles

- **Data Table** (`n8n-nodes-base.datatable`) — tabla persistente dentro de n8n. Para estado sin montar una base de datos.
- **Time Saved** (desde 2.1.0) — mide horas ahorradas por el workflow. Tu reporte de impacto, gratis.
- **Error Trigger** (`n8n-nodes-base.errortrigger`) — workflow que se dispara cuando otro falla. **Tu observabilidad mínima.** Si no tienes uno, tus fallas son invisibles.

## Trampas conocidas

- **Simple Memory y Simple Vector Store viven en RAM.** Se borran al reiniciar. Prototipo sí, producción no.
- **Item linking.** n8n encadena items entre nodos. Si transformas datos en un Code node sin preservar el linking, `$('NodoAnterior').item` se rompe. Es la fuente #1 de errores raros.
- **Orden de ejecución en ramas múltiples.** No es el que crees. Revisa la doc de execution order antes de asumir.
- **Credenciales de n8n Cloud vs self-hosted** no son intercambiables. Los IPs de salida de Cloud están documentados si necesitas allowlist.
- Los nodos de IA requieren n8n ≥1.19.4. Cualquier cosa 2.x los tiene.

Fuente: https://docs.n8n.io
