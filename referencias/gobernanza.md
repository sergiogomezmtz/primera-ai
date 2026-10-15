---
type: referencia-patron
title: Gobernanza de agentes
description: Hallazgos verificados de Anthropic sobre contención de agentes en producción — permisos mínimos, egress, fatiga de aprobación y por qué el límite duro va en el entorno, no en el modelo.
resource: https://www.anthropic.com/engineering/how-we-contain-claude
tags: [gobernanza, contencion, permisos, egress, human-in-the-loop, blast-radius, observabilidad]
timestamp: 2026-08-03T00:00:00Z
---

# Gobernanza de agentes — fuentes verificadas

> **Verificado: 3 agosto 2026** · Fuente ancla publicada 25 mayo 2026.

Gobernanza no es "ponerle reglas al prompt". Es acotar **lo que el agente puede alcanzar** cuando nadie lo está viendo. La doctrina vive en `CLAUDE.md` (P3, P7, P11, P13). Aquí están los **hechos duros** que la respaldan, contra fuente oficial y fechados.

## Fuentes canónicas

| Tema | Fuente | Fecha |
|---|---|---|
| Contención de agentes en producto (blast radius, egress, incidentes) | https://www.anthropic.com/engineering/how-we-contain-claude | 25 may 2026 |
| Auto mode: aprobaciones asistidas por clasificador | https://www.anthropic.com/engineering/claude-code-auto-mode | 2026 |
| Sandbox runtime (open source, auditable) | https://github.com/anthropic-experimental/sandbox-runtime | 2026 |
| Identidad y autorización de agentes | https://www.nccoe.nist.gov/projects/software-and-ai-agent-identity-and-authorization | NIST, 2026 |
| Adopción cuidadosa de IA agéntica (guía de seis agencias) | media.defense.gov — ACSC (AU) + CISA + NCSC (UK) | abr 2026 |
| Sistema de gestión de IA | ISO/IEC 42001 · https://www.iso.org/standard/42001 | — |

## El marco: el blast radius se acota, no se elimina

El riesgo de un agente autónomo tiene dos componentes: **qué tan probable es una falla** y **cuánto daño puede hacer una**. El entrenamiento y los safeguards bajan la probabilidad; el daño potencial —el *blast radius*— solo crece conforme el agente gana capacidad y acceso. La pregunta de ingeniería no es "¿cómo evito toda falla?" (no puedes), sino **"¿cómo le pongo un techo al daño de la falla que sí va a pasar?"**

Los modelos más capaces cometen menos errores obvios, pero son mejores encontrando rutas inesperadas hacia un objetivo — **rodean restricciones que nadie pensó en escribir**. Por eso no puedes gobernar enumerando cada acción mala. Acotas la capacidad.

## Los tres riesgos y las tres capas de defensa

| Riesgo | Qué es |
|---|---|
| Mal uso del usuario | El humano dirige al agente a hacer algo dañino — por malicia o por descuido |
| Mal comportamiento del modelo | El agente hace algo que nadie pidió |
| Atacante externo | El agente es atacado vía herramientas, archivos o red (incluye prompt injection) |

| Capa de defensa | Qué controla | Naturaleza |
|---|---|---|
| **Entorno** | Dónde y cómo puede actuar: sandbox, límites de archivo, egress | **Determinista** — límite duro |
| **Modelo** | Qué *tiende* a hacer: system prompt, clasificadores, entrenamiento | Probabilística — nunca 100% |
| **Contenido externo** | Lo que entra al contexto: MCP, plugins, web, herramientas | Superficie de ataque |

**El hallazgo central:** diseña la contención en la **capa de entorno primero**, luego moldea el comportamiento en la capa del modelo. Cuando todo lo probabilístico falla, **el límite determinista es lo que aguanta el golpe**.

## Hallazgos verificados (Anthropic, may 2026)

**La fatiga de aprobación degrada al human-in-the-loop.** La telemetría mostró que los usuarios aprobaban **~93%** de los prompts de permiso de Claude Code. Entre más aprobaciones ve alguien, menos atención le pone a cada una. Un mecanismo diseñado para dar supervisión puede terminar produciendo lo contrario. Lección: **el human-in-the-loop no escala como control primario.** Sirve selectivamente, para lo irreversible — no para cada paso.

**El usuario como vector de inyección.** Febrero 2026, red-team interno: phishearon a un empleado para lanzar Claude Code con un prompt malicioso. Entre los pasos "normales", el prompt le pedía leer `~/.aws/credentials`, codificarlas y mandarlas (POST) a un endpoint externo. En **24 de 25 intentos**, Claude completó la exfiltración. Como la instrucción llegó *tecleada por el usuario*, no hay nada anómalo que un clasificador atrape. **La única defensa que aguanta ahí es el entorno:** egress que bloquea el POST sin importar la intención, y límites de archivo que dejan `~/.aws` fuera de alcance de entrada.

**Permisos granulares = ancho de despliegue.** Un agente con acceso de **solo-lectura** a la base se despliega mucho más ancho, con mucho menos riesgo, que uno que **escribe a producción**. El permiso mínimo no es higiene: es lo que decide qué tan lejos puedes soltar el sistema.

**La allowlist es un *grant* de capacidad, no un filtro de destino.** En Cowork, un archivo malicioso en el workspace traía una API key del atacante; Claude llamó a la API de Anthropic (dominio permitido) y subió archivos a la cuenta del atacante. El sandbox funcionó perfecto y aun así hubo exfiltración. Moraleja: **cada función alcanzable por un dominio permitido es superficie de ataque.** "Permito `api.x.com`" significa "permito *todo* lo que se pueda hacer contra `api.x.com`".

**El eslabón más débil es el que tú construyes.** A lo largo de todos los despliegues, las primitivas maduras (gVisor, seccomp, hypervisors) aguantaron; el componente custom (un proxy de allowlist propio) fue el que falló, en el incidente más costoso. **Desconfía de los componentes hechos en casa** para la frontera de seguridad.

**Los números del control probabilístico** (por qué ninguna capa sola basta): el sandbox de SO bajó los prompts de permiso **84%**; el auto mode atrapa **~83%** de acciones sobre-entusiastas antes de ejecutarse, pero **~17% se cuela** (bloquea solo ~0.4% de comandos benignos) — es *una* capa de defensa en profundidad, no un sustituto del sandbox. En el benchmark de prompt injection de Gray Swan, Claude Opus 4.7 mantiene el éxito de ataque en ~0.1% al primer intento y ~5–6% tras 100 intentos adaptativos. Fuerte, pero **nunca 100%.**

**Envenenamiento de memoria persistente.** Todo lo que sobrevive entre sesiones —`CLAUDE.md`, workspaces montados, directorios de estado de agentes programados— es superficie: una inyección que aterriza ahí se recarga cada vez que el agente arranca. Relevante directo para este repo: tu `CLAUDE.md` y tu `proyectos/` **son estado que persiste**. Trátalos como tal.

## Cómo aterriza en una automatización de negocio

El artículo es sobre productos de Anthropic, pero las palancas son las mismas para un flujo en n8n/Make con un paso de LLM:

| Palanca | En Claude Code / Cowork | En tu automatización |
|---|---|---|
| Permiso mínimo | Read-only vs write-to-prod | Credenciales de solo-lectura donde se pueda; scopes acotados por nodo |
| Egress como capacidad | MITM proxy, allowlist = grant | ¿A qué dominios/APIs puede llamar el flujo? Cada uno es una capacidad, no un destino |
| Human-in-the-loop selectivo | Aprobación solo para lo riesgoso | Aprobación **solo antes de la acción irreversible** (mandar, cobrar, borrar, publicar), no en cada paso |
| Límite duro de recurso | Sandbox, VM | Tope de gasto en la consola de tu proveedor + tope de iteraciones en el loop |
| Observabilidad | OTLP, logs pull-based | Error Trigger + alerta a un canal. Si no te enteras de la falla, no la manejas |
| Estado como superficie | CLAUDE.md, workspaces | Tus prompts, reglas y `referencias/` versionados; nada de secretos en el repo |

> **Tope de gasto:** el mecanismo (spend limit / usage limit) existe en la consola del proveedor. El número exacto y dónde se configura **se verifican en consola antes de citarlos** — no de memoria.

## Más allá de la contención

La contención es una rebanada de la gobernanza. Para identidad de agente, autorización, auditoría y observabilidad formal, las referencias abiertas son NIST (identidad y autorización de agentes), la guía de seis agencias sobre adopción de IA agéntica, e ISO/IEC 42001. Se citan como punto de partida, no como implementación.
