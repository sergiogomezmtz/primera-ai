---
name: okf
description: Open Knowledge Format. Úsala cuando haya que representar conocimiento organizacional para agentes — esquemas de tablas, definiciones de métricas, runbooks, APIs, contexto de negocio. También cuando se hable de LLM wikis, bases de conocimiento para agentes, catálogos de datos, o cuando alguien pregunte dónde vive el contexto que el agente necesita.
---

# OKF — Open Knowledge Format

**Lee `referencias/okf.md` para el spec verificado.**

## El problema real

Los modelos ya son buenos. Lo que los limita es **el contexto**, y ese contexto es **conocimiento interno**: el esquema de una tabla, qué significa "usuario activo" *en esta empresa*, el runbook del incidente, los join paths, la API que está deprecada.

Ese conocimiento vive fragmentado: catálogos con su propia API, wikis, drives, comentarios en el código, y la cabeza de dos personas.

Cada agente nuevo resuelve el mismo problema de ensamblado de contexto desde cero.

**La respuesta no es otro servicio de conocimiento. Es un formato.**

## El spec, completo

Un **bundle** es un directorio de markdown. Cada archivo es un **concepto**. La ruta es la identidad. YAML frontmatter arriba, markdown abajo.

**El único campo obligatorio es `type`.** Los demás (`title`, `description`, `resource`, `tags`) son la superficie consultable.

**v0.2 (verificado 9 oct 2026):** `timestamp` desaparece y lo reemplaza `generated.at`; aparecen `sources` (de dónde deriva el concepto), `verified` (quién lo verificó y cuándo), `status` (`draft`/`stable`/`deprecated`) y `stale_after` (a partir de cuándo se considera viejo). `type` sigue siendo lo único obligatorio. Detalle y ejemplo en `referencias/okf.md`. El ejemplo de abajo está en v0.1, que es lo que todavía usa este bundle.

```markdown
---
type: metrica
title: Usuarios activos semanales
description: Usuarios únicos con al menos un evento de sesión en 7 días.
resource: https://console.cloud.google.com/...
tags: [producto, engagement]
timestamp: 2026-07-13T00:00:00Z
---

# Definición
Un usuario cuenta como activo si dispara `session_start` al menos una vez
en la ventana de 7 días. Se calcula sobre [events](/tables/events.md).

# Trampas
NO incluye usuarios que solo abren notificaciones push. Esa fue una decisión
de producto en marzo 2026 y sigue siendo la fuente #1 de discrepancias
con el equipo de growth.
```

Los conceptos se enlazan con **links normales de markdown** — eso convierte el directorio en un **grafo**, más rico que la jerarquía de carpetas.

Dos archivos reservados: **`index.md`** (divulgación progresiva — el agente navega sin cargar todo) y **`log.md`** (historial).

Eso es todo. El spec entero cabe en una página.

## Por qué importa que sea *aburrido*

La reacción típica es "esto es demasiado simple para funcionar". **Ese es exactamente el punto.**

La complejidad de los sistemas de conocimiento está en la **integración**, no en la representación. Al fijar la representación en el mínimo común denominador —archivos, markdown, frontmatter— la integración se vuelve trivial: cualquiera puede producirlo sin SDK, cualquiera puede consumirlo sin integración, y sobrevive al moverse entre sistemas.

Separa quién **escribe** el conocimiento de quién lo **consume**. El formato es el contrato; las herramientas de cada extremo son intercambiables.

## Dónde encaja — no lo confundas

Tres capas distintas que la gente revuelve constantemente:

| Capa | Qué representa | Formato |
|---|---|---|
| **Conocimiento** | Hechos, esquemas, definiciones, runbooks | **OKF** |
| **Capacidad** | Qué sabe hacer el agente | Skills |
| **Loop** | Cuándo para, quién verifica, qué entra al contexto | Harness |

**OKF no compite con MCP.** MCP mueve datos **en tiempo de ejecución**; OKF los representa **en reposo**, en disco, versionados junto al código que describen. Son complementarios: un servidor MCP puede servir un bundle OKF.

## La recomendación honesta

**Va en v0.2 y hoy el ecosistema es básicamente Google.** Nadie más lo consume en serio todavía.

Pero adoptar la convención cuesta **casi cero**: es frontmatter en archivos markdown que de todos modos ibas a escribir. Sin SDK, sin cuenta, sin lock-in.

**Adopta el formato. No apuestes la arquitectura.** Si OKF prende, ya estás. Si no prende, tienes markdown con frontmatter — exactamente lo que tenías. Es una apuesta con costo cercano a cero y opción positiva. Hay pocas así.

## Cómo aplicarlo a una automatización

El agente necesita saber cosas que **no están en su entrenamiento y no están en la base de datos**:

- Qué significa cada estatus del CRM *en esta empresa*
- Cuáles clientes son cuenta clave y por qué
- Qué política aplica a devoluciones después de 30 días
- Por qué el campo `legacy_id` sigue existiendo y cuándo NO usarlo

Eso es un bundle OKF. Un concepto por cosa. El agente lo lee cuando lo necesita, y —esto es lo bueno— **lo puede actualizar él mismo** cuando aprende algo nuevo.

Es la idea de Karpathy: los LLMs no se aburren, no se les olvida actualizar una referencia cruzada, y pueden tocar 15 archivos de un jalón. La contabilidad que hace que los humanos abandonen sus wikis es justamente en lo que un LLM es bueno.

## Este repo es un bundle OKF

`referencias/` es conforme a OKF v0.1: frontmatter, un concepto por archivo, `index.md`, `log.md`, links cruzados. La migración del frontmatter a v0.2 (`generated.at`, `verified`, `stale_after`) está pendiente; `verified` y `stale_after` son exactamente la disciplina de "fecha de verificación + re-verificar cada 2 meses" que este repo ya practica a mano.

Si alguien pregunta cómo se ve OKF en la práctica, **enséñale este directorio.**
