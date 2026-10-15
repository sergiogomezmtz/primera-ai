---
type: referencia-patron
title: Harness y loop engineering
description: Hallazgos verificados de Anthropic sobre agentes de larga duración: modos de falla, lista de features en JSON, verificación externa.
resource: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
tags: [harness, loops, agentes, contexto, verificacion]
timestamp: 2026-07-13T00:00:00Z
---

# Harness / loop engineering — fuentes verificadas

> **Verificado: 13 julio 2026**

## Fuentes canónicas

| Tema | Fuente | Fecha |
|---|---|---|
| Harnesses para agentes de larga duración | https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents | 26 nov 2025 |
| Context engineering | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | 2025 |
| Multi-context window workflows | Guía de prompting de Claude 4, sección multi-context | — |
| Código de referencia | https://github.com/anthropics/claude-quickstarts/tree/main/autonomous-coding | — |

## Hallazgos verificados (Anthropic, nov 2025)

Experimento: Claude Agent SDK + modelo frontera + compactación + loop + prompt "construye un clon de claude.ai". **No alcanza para producir una app de calidad de producción.** El problema no era el modelo.

**Dos modos de falla observados:**
1. El agente intenta hacerlo todo de un jalón → se queda sin contexto a media implementación → la siguiente sesión hereda una feature a medias y sin documentar, y gasta su tiempo reparando.
2. Un agente posterior ve que hay progreso y **declara el proyecto terminado** antes de tiempo.

**La compactación de contexto no es suficiente.** No siempre pasa instrucciones claras al siguiente agente.

**Solución de dos partes** (mismo harness, distinto primer prompt — no son dos sistemas):
- **Agente inicializador:** crea `init.sh`, `claude-progress.txt`, lista de features en JSON, y el primer commit de git.
- **Agente de trabajo:** progreso incremental, una feature a la vez, deja el entorno limpio.

**Detalle no obvio:** la lista de features va en **JSON, no en Markdown**. El modelo es menos propenso a sobreescribir o editar inapropiadamente un archivo JSON. Verificado experimentalmente por Anthropic.

**Instrucción que funciona:** lenguaje fuerte — *"es inaceptable borrar o editar tests, porque puede llevar a funcionalidad faltante o rota"*. El agente solo puede modificar el campo `passes`.

**Verificación:** sin prompting explícito, Claude marca features como completas sin probarlas end-to-end. Hace unit tests y `curl`, pero no detecta que la feature no sirve. **Darle herramientas de verificación real** (automatización de navegador vía Puppeteer MCP) y pedirle que pruebe *como lo haría un humano* mejoró el resultado de forma dramática.

**Límite conocido:** la automatización de navegador no ve modales nativos del navegador (alerts). Features que dependen de ellos salían con más bugs.

## Tabla de fallas y soluciones (Anthropic)

| Problema | Inicializador | Agente de trabajo |
|---|---|---|
| Declara victoria antes de tiempo | Crea lista de features JSON | Lee la lista al empezar; escoge UNA feature |
| Deja el entorno con bugs o sin documentar | Crea repo git + archivo de progreso | Lee progreso y git log al empezar; corre prueba de humo; commit + progreso al terminar |
| Marca features como listas sin probarlas | Crea lista de features | Auto-verifica; solo marca `passes` tras probar de verdad |
| Pierde tiempo descubriendo cómo correr la app | Escribe `init.sh` | Lee `init.sh` al empezar |

## Pregunta abierta (según Anthropic)

No está resuelto si conviene **un agente general** o una **arquitectura multi-agente** con especialistas (agente de testing, de QA, de limpieza). La solución publicada usa el primero: mismo harness, distintos prompts.

Sé honesto sobre esto: cualquiera que te venda multi-agente como respuesta obvia está adelantándose a la evidencia. El multi-agente introduce coordinación, handoffs y resolución de conflictos — costos reales.

## Context engineering

El contexto es un **recurso finito y curado**, no una cubeta. Incluye system prompt, herramientas, MCP e historial de mensajes — todo compite por el mismo espacio.

**"Altitud" del prompt de sistema:** zona Goldilocks entre lógica if-else frágil hardcodeada, y guía tan vaga que no da señales concretas. Específico para guiar; flexible para que el modelo aplique criterio.
