---
type: especificacion
title: Open Knowledge Format (OKF)
description: Spec abierto de Google Cloud para representar conocimiento organizacional como markdown + YAML frontmatter, legible por humanos y agentes. Cubre v0.1 y el cambio a v0.2.
resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf
tags: [okf, conocimiento, contexto, interoperabilidad, google]
timestamp: 2026-10-09T00:00:00Z
---

# Open Knowledge Format — hechos verificados

> **Verificado: 9 octubre 2026** contra https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md (v0.2). La sección histórica de v0.1 se verificó el 13 de julio de 2026 contra el blog de Google Cloud.

## Qué es

**OKF.** Especificación abierta de Google Cloud (equipo de Data Cloud) que formaliza el patrón **"LLM wiki"** de Andrej Karpathy en un formato portable e interoperable.

Vendor-neutral. Legible por humanos y por agentes. **Es un formato, no una plataforma** — no requiere cuenta, SDK ni runtime.

Publicado el 12 de junio de 2026 como **v0.1**, explícitamente un punto de partida. **Al 9 de octubre de 2026 el spec va en v0.2** (ver abajo).

## v0.2 — qué cambió (verificado 9 oct 2026)

El SPEC.md oficial declara: *"This document specifies OKF version 0.2."* El cambio importa porque toca el frontmatter que ya escribiste.

**Sigue igual:** `type` es el **único campo obligatorio**. Un concepto con solo `type` es conformante. `title`, `description`, `resource` y `tags` pasan a "recomendados".

**Cambios que rompen (breaking):**
- `timestamp` **desaparece**; lo reemplaza **`generated.at`** (ISO 8601, "último cambio significativo del contenido"). Los consumidores pueden caer a `timestamp` cuando falte `generated`, así que un bundle v0.1 no se vuelve ilegible, pero ya no es la forma canónica.
- La lista `# Citations` en el cuerpo se reemplaza por **`sources`** en el frontmatter.

**Campos nuevos (opcionales):**
- **`generated`**: cómo se produjo el contenido. Si está el objeto, `by` (actor) es obligatorio; `at` es la fecha.
- **`sources`**: lista de materiales de los que deriva el concepto; cada entrada exige `resource`.
- **`verified`**: eventos de verificación, cada uno con `by` y `at`. Es exactamente lo que este repo hacía a mano con "Verificado: 13 julio 2026".
- **`status`**: `draft` | `stable` | `deprecated`. Ausente ⇒ `stable`.
- **`stale_after`**: instante absoluto ISO 8601 a partir del cual el contenido se considera viejo. Es el "re-verificar cada 2 meses" de este repo, pero legible por máquina.

También aparecen un tipo de concepto nuevo (`Attested Computation`) y el encabezado `# Computation`; no aplican a este bundle.

Ejemplo de frontmatter v0.2 para un concepto de este repo:

```yaml
---
type: referencia-api
title: Claude API
description: Precios, rate limits, caching, batch.
resource: https://platform.claude.com/docs/en/about-claude/pricing
tags: [claude, api, costos]
generated:
  by: humano
  at: 2026-10-09T00:00:00Z
sources:
  - resource: https://platform.claude.com/docs/en/about-claude/pricing
verified:
  - by: humano
    at: 2026-10-09T00:00:00Z
status: stable
stale_after: 2026-12-09T00:00:00Z
---
```

**Estado de este bundle:** `referencias/` sigue en frontmatter v0.1 (`timestamp`). La migración a `generated.at` + `verified` + `stale_after` **queda pendiente** y está anotada en `log.md`. No se migró el 9 de octubre porque el cambio toca todos los archivos a la vez y conviene hacerlo en un commit aparte, con el visualizador de referencia a la mano para confirmar que lee ambas versiones.

## El spec completo, en serio (v0.1, la forma que todavía usa este bundle)

Un **bundle** OKF es un directorio de archivos markdown. Cada archivo es un **concepto**: una tabla, un dataset, una métrica, un runbook, una API, lo que sea. **La ruta del archivo es la identidad del concepto.**

Cada concepto lleva YAML frontmatter y cuerpo en markdown:

```markdown
---
type: BigQuery Table          ← ÚNICO CAMPO OBLIGATORIO
title: Orders
description: Una fila por pedido completado.
resource: https://console.cloud.google.com/bigquery?p=acme&d=sales&t=orders
tags: [sales, revenue]
timestamp: 2026-05-28T14:30:00Z   ← en v0.2 esto es generated.at
---

# Schema
| Columna | Tipo | Descripción |
|---|---|---|
| `order_id` | STRING | Identificador único del pedido. |
| `customer_id` | STRING | FK a [customers](/tables/customers.md). |

# Joins
Se une con [customers](/tables/customers.md) por `customer_id`.
```

**Los conceptos se enlazan con links normales de markdown.** Eso convierte el directorio en un **grafo** de relaciones, más rico que la jerarquía de carpetas.

Dos archivos reservados, opcionales:
- **`index.md`** — divulgación progresiva. El agente navega la jerarquía sin cargarlo todo.
- **`log.md`** — historial cronológico de cambios.

Estructura típica:
```
sales/
├── index.md
├── datasets/
│   ├── index.md
│   └── orders_db.md
├── tables/
│   ├── index.md
│   ├── orders.md
│   └── customers.md
└── metrics/
    ├── index.md
    └── weekly_active_users.md
```

## Los tres principios de diseño

1. **Mínimamente opinionado.** Solo exige `type`. Qué tipos existen, qué otros campos, qué secciones tiene el cuerpo — todo eso lo decide el productor. **El spec define la superficie de interoperabilidad, no el modelo de contenido.**
2. **Independencia productor/consumidor.** Un bundle escrito a mano por un humano lo puede consumir un agente. Uno generado por un pipeline lo puede navegar un visualizador. Uno sintetizado por un LLM lo puede consultar otro. **El formato es el contrato; las herramientas de cada extremo son intercambiables.**
3. **Formato, no plataforma.** No atado a ninguna nube, base de datos, proveedor de modelo ni framework de agentes.

## Qué se envió con el spec

Implementaciones de referencia (pruebas de concepto, no productos):
- **Agente de enriquecimiento** que recorre un dataset de BigQuery y redacta un concepto OKF por cada tabla y vista; luego una segunda pasada de LLM lo enriquece con citas, esquemas y join paths.
- **Visualizador HTML estático** — convierte cualquier bundle en un grafo interactivo, un solo archivo autocontenido, sin backend, sin que los datos salgan de la página.
- **Tres bundles de ejemplo** navegables: GA4 e-commerce, Stack Overflow, y datasets públicos de Bitcoin.

Google Cloud Knowledge Catalog (antes Dataplex) ya ingiere OKF nativamente.

Repo: https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf

## El problema que resuelve

En la mayoría de las organizaciones el contexto que un modelo necesita **es conocimiento interno**: el esquema de una tabla, el significado de negocio de una métrica, el runbook de un incidente, los join paths, el aviso de deprecación de una API vieja.

Ese conocimiento vive fragmentado: catálogos de metadatos con su propia API, wikis, drives compartidos, comentarios en el código, y **la cabeza de dos ingenieros senior**.

Cada constructor de agentes resuelve el mismo problema de ensamblado de contexto desde cero. Cada vendor reinventa el mismo modelo de datos. Y el conocimiento queda encerrado en la superficie que lo creó.

## La honestidad sobre OKF

**Va en v0.2 y el ecosistema es, hoy, Google.** Knowledge Catalog y las implementaciones de referencia. Nadie más lo consume todavía de forma seria.

**Pero adoptar la convención es prácticamente gratis** — es YAML frontmatter en archivos markdown que de todos modos ibas a escribir. No hay lock-in, no hay SDK, no hay dependencia.

Entonces: **adopta el formato, no apuestes la arquitectura.** Si OKF prende, ya estás. Si no prende, tienes markdown con frontmatter, que es exactamente lo que tenías antes.

Es una de las pocas apuestas tecnológicas con costo cercano a cero y opción positiva.

## OKF es la capa de conocimiento, no la de capacidad

No confundas:
- **OKF** = cómo se representa el **conocimiento** (hechos, esquemas, definiciones, runbooks)
- **Skills** = cómo se representa una **capacidad** (qué sabe hacer el agente)
- **Harness** = cómo se representa el **loop** (cuándo para, quién verifica, qué entra al contexto)

Son tres capas distintas. La gente las revuelve. OKF no compite con skills ni con MCP — MCP mueve datos en tiempo de ejecución; **OKF los representa en reposo**, en disco, versionados junto al código que describen.

Fuentes:
- https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md (v0.2)
- https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing
- Gist de Karpathy sobre LLM wikis: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
