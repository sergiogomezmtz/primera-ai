<h1 align="center">Agentic AI &amp; Automation Mentor Agent 2026</h1>

<p align="center"><strong>Curso avanzado para convertir automatizaciones en sistemas medibles, gobernables y operables por otra persona.</strong></p>

<p align="center">
  <img src="docs/visuales/repo-header.png" alt="Ilustración de Raúl Sisniega: zorro y gato frente a un sintetizador" width="100%">
</p>

<p align="center"><sub>Ilustración: <a href="https://www.behance.net/biosisniega">Raúl Sisniega</a> ©</sub></p>

<p align="center">
  <a href="LICENSE"><img alt="Licencia MIT" src="https://img.shields.io/badge/License-MIT-0F766E.svg"></a>
  <a href="https://github.com/nabolom/agentic-ai-automation-mentor-agent-2026/actions/workflows/validate.yml"><img alt="Validación" src="https://github.com/nabolom/agentic-ai-automation-mentor-agent-2026/actions/workflows/validate.yml/badge.svg?branch=main"></a>
  <a href="https://www.python.org/"><img alt="Python 3.11+" src="https://img.shields.io/badge/Python-3.11%2B-3776AB.svg?logo=python&amp;logoColor=white"></a>
  <a href="https://code.claude.com/docs/en/overview"><img alt="Workflow compatible con Claude Code" src="https://img.shields.io/badge/Workflow-Claude%20Code-5B5BD6.svg"></a>
  <a href="ALUMNO-EMPIEZA-AQUI.md"><img alt="Ruta compatible con Cowork" src="https://img.shields.io/badge/Ruta-Cowork-0EA5A4.svg"></a>
  <a href="docs/competencias.md"><img alt="Nivel avanzado" src="https://img.shields.io/badge/Nivel-Avanzado-E77B52.svg"></a>
  <a href="ejemplo/README.md"><img alt="Núcleo de seis casos" src="https://img.shields.io/badge/Núcleo-6%20casos-172033.svg"></a>
</p>

## 🚦 Sesión de trabajo — Panorama de Agent Engineering Q4-2026

**Primera sesión técnica de la cohorte · 150 minutos.** La reunión anterior fue de bienvenida y contexto. Aquí empieza el trabajo con el repositorio y el Agente Mentor.

➡️ Empieza por [`Sesión 2 — Panorama y primera medición`](curso/S2-panorama-y-evals.md).

### Elige una ruta, en este orden

| Ruta | Si llegas con… | Haz primero |
|---|---|---|
| **1 — Ya tengo algo construido** | Automatización, prototipo o sistema existente | Trae una falla, cuello de botella o decisión difícil |
| **2 — Quiero descubrir qué agentizar** | Proceso o idea real, pero sin diseño | Acota proceso, usuario, decisión y resultado |
| **3 — Camino dorado opcional** | Ningún proceso claro o bloqueo técnico | Calibra el contrato en `ejemplo/` y vuelve a Ruta 2 |

La [guía completa de rutas](docs/rutas-de-entrada.md) explica el recorrido. **Ruta 2 es la ruta común; Ruta 3 es un andamio, no la entrada universal.**

El mínimo de la sesión es: **ruta elegida · proceso/caso · una decisión · tres casos ancla · salidas esperadas · siguiente paso**. La suite de seis casos, `/eval` y la línea base pertenecen a la continuidad posterior.

## Objetivo

Este repositorio te acompaña para:

1. decidir qué automatizar y qué no, con evidencia;
2. separar lo que debe ser `if`, IA, herramienta o humano;
3. medir un sistema con casos reales y salida esperada;
4. diagnosticar si la falla está en el modelo, el contexto, el harness o la herramienta;
5. gobernar permisos, costos, aprobaciones y recuperación;
6. dejar un sistema que otra persona pueda operar sin ti.

La pregunta que guía todo el curso es:

> **Si mañana no estás, ¿alguien más puede correr el sistema, saber si funcionó y saber qué hacer si no?**

## Autoría y herramientas

**La dirección pedagógica, el diseño del curso, la doctrina y las decisiones finales de este repositorio son de León Ruiz.**

Claude Code y Cowork son **herramientas y asistentes de ejecución bajo su dirección**. No son coautores del repositorio. El criterio final, el alcance y la responsabilidad del material pertenecen a su autor y facilitador.

## Para quién es

| Perfil | Qué obtiene |
|---|---|
| Ya tienes automatizaciones y quieres productificarlas o escalarlas | Un marco para medir, endurecer, gobernar y entregar tu sistema. |
| Eres autodidacta o intermedio y ya sabes construir cosas | Una ruta que parte de tu experiencia y te pide la evidencia que falta, sin explicarte lo que ya sabes. |
| Eres avanzado | Un núcleo común y extensiones de costos, harness, MCP, loops y multiagente. |
| Todavía no tienes proceso claro | Ruta 3 opcional para calibrar y volver a Ruta 2. |

No es un chatbot de curso ni una lista de tutoriales. Es una infraestructura de trabajo para pasar del proceso al sistema y del sistema al producto.

## Puertas de entrada

| Soy… | Empiezo por… | Resultado inicial |
|---|---|---|
| Aprendedor(a) con sistema | [Ruta 1](docs/rutas-de-entrada.md) | Falla, cuello de botella o decisión difícil |
| Aprendedor(a) con proceso/idea | [Ruta 2](docs/rutas-de-entrada.md) | Proceso acotado y decisión candidata |
| Aprendedor(a) sin claridad o bloqueado | [Ruta 3](docs/rutas-de-entrada.md) | Contrato entendido y transferencia a Ruta 2 |
| Aprendedor(a) avanzado(a) | [Ruta 1 / fast lane](docs/ruta-continuidad-s2.md) | Evidencia existente y una extensión justificada |
| Facilitador | [`facilitador/README.md`](facilitador/README.md) | Agenda, preguntas, rescates y extensiones |

> Consulta [`Dependencias y preflight`](docs/dependencias-y-preflight.md) solo si necesitas resolver una instalación. No instales Node/NPM si tu ruta no los necesita.

## Primeros 15 minutos

1. Abre [`Empieza aquí como Aprendedor(a)`](ALUMNO-EMPIEZA-AQUI.md).
2. Elige Ruta 1, Ruta 2 o Ruta 3.
3. Abre Claude Code/Cowork o activa el fallback de la Ruta 3.
4. Produce el primer checkpoint de tu ruta; no leas todo el repositorio.

No necesitas conectar una API real, usar n8n ni construir un agente autónomo para empezar.

## Ruta del curso

```text
proceso → decisión → evals → diagnóstico → límites → handoff
```

| Sesión | Pregunta central | Evidencia |
|---|---|---|
| Sesión 2 — Panorama Q4-2026 y primera medición | ¿Qué decisión quiero medir y cómo sabré si funciona? | Track, decisión, tres casos ancla y salidas esperadas; seis casos como continuidad |
| S3 — Loops | ¿Qué capa está fallando y necesito iteración real? | Diagnóstico, checker o cuatro paradas, traza y comparación v0 → v1 |
| S4 — Gobernanza | ¿Puede otra persona operar esto con límites claros? | Permisos, costo, aprobación, observabilidad, demo y handoff |
| S5 — Multiagente | ¿La complejidad adicional está justificada? | Extensión opcional para quien terminó el núcleo |

Los **6 casos** son el requisito mínimo válido. Los **10 casos** son una suite extendida para profundizar, no una condición para avanzar.

## Mapa del recorrido

![Mapa del recorrido: Ruta 1 sistema existente, Ruta 2 descubrir qué agentizar, Ruta 3 camino dorado opcional, S2–S4 y S5 opcional](docs/visuales/mapa-del-curso.png)

Fuente editable: [`docs/visuales/mapa-del-curso.mmd`](docs/visuales/mapa-del-curso.mmd).

## Ruta 3 — Camino dorado opcional

El camino dorado no es la entrada por defecto ni un producto que debas construir. Es un andamio para quien no tiene proceso claro o está bloqueado. Después de recorrerlo, vuelve a la Ruta 2 y decide qué quieres agentizar.

```text
entrada → if determinista → IA solo si hay ambigüedad → salida estructurada → validación → humano
```

Puedes correrlo sin credenciales:

```bash
python3 ejemplo/camino_dorado.py --modo offline --version v1
```

| Versión | Núcleo | Extendida |
|---|---:|---:|
| `v0` | 4/6 — línea base intencional | 7/10 |
| `v1` | 6/6 | 10/10 |

Si no tienes Python, abre [`ejemplo/casos.json`](ejemplo/casos.json) y recorre los seis casos en papel. El contrato y las preguntas de diseño son los mismos.

## Comandos

| Comando | Qué hace |
|---|---|
| `/rumbo` | Assessment de entrada: qué quieres construir, qué puedes demostrar y qué ruta te conviene |
| `/arrancar` | Lleva un proceso al diseño de una automatización |
| `/eval` | Corre tus evals contra el sistema y devuelve una tasa |
| `/cuatro-paradas` | Diseña y ejecuta un loop con trabajo, verificación, parada y escalamiento |
| `/auditar` | Revisión crítica: identifica riesgos, contradicciones y teatro |
| `/verificar` | Re-verifica referencias sensibles contra fuentes oficiales |

Fuera de los comandos, habla normal con el asistente de ejecución. Pídele código, discute decisiones y conserva lo importante en disco.

## Qué hay en este repositorio

```text
README.md             esta portada y las puertas de entrada
ALUMNO-EMPIEZA-AQUI.md guía de primeros 15 minutos
docs/competencias.md   mapa de competencias de salida
docs/ruta-continuidad-s2.md preparación accionable para S2
docs/dependencias-y-preflight.md matriz de dependencias por ruta y sistema operativo
CLAUDE.md             instrucciones del asistente bajo tu dirección
ACOMPANAMIENTO.md     cómo cambia el acompañamiento según tu evidencia
facilitador/          checklist, guiones 2–4, rescates y debrief
curso/                ruta de cohorte y guías de sesión
docs/rutas-de-entrada.md fuente canónica de las tres rutas
ejemplo/              camino dorado opcional, dataset y pruebas reproducibles
proyectos/            plantillas, rúbrica, demo y handoff
patrones/             siete patrones de automatización
referencias/          hechos verificados y fechados; gobernanza: 3 agosto 2026; gobernanza: 3 agosto 2026; gobernanza: 3 agosto 2026
docs/                 instalación, doctrina, seguridad y visuales
verificar.py          validación local de pruebas, fixtures, tasas y enlaces
.github/workflows/    validación automática en cada push y pull request
```

## Cómo te acompaña el Agente Mentor

El nivel de evidencia que demuestras en `/rumbo` decide cómo se te acompaña:

| Nivel | Modo | Qué hace |
|---|---|---|
| 0–1 | Enseñar | Explica el mecanismo en corto, con un ejemplo y una sola pregunta |
| 2 | Retar | Pide la evidencia que falta: número, archivo o criterio |
| 3 | Revisar como par | Señala riesgos y contradicciones; tú conduces |

La verdad de las salidas esperadas, umbrales y límites la fija la persona que conoce la operación. El asistente propone borradores; no inventa la verdad.

## Doctrina

- **Si puedes escribirlo como un `if`, que sea un `if`.**
- **Diseña la falla, no el éxito.**
- **Salida estructurada o no hay sistema.**
- **El harness importa más que el modelo.**
- **La condición de parada debe ser verificable sin el modelo.**

La versión completa está en [`docs/doctrina.md`](docs/doctrina.md) y [`CLAUDE.md`](CLAUDE.md).

## Verificación local

Antes de clase o antes de compartir cambios, ejecuta:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verificar.py
```

La verificación cubre pruebas reproducibles, fixtures de `/rumbo`, tasas del camino dorado, enlaces locales y whitespace de Git.

## Hechos y fechas

El framing de la sesión es **Panorama de Agent Engineering Q4-2026**, con corte editorial del repositorio al 14 de octubre de 2026. Los archivos de [`referencias/`](referencias/) conservan la fecha de verificación de cada fuente: 9 de octubre de 2026 para Claude API, MCP, n8n, OKF, METR y multiagente; 13 de julio de 2026 para LangChain y harness; 3 de agosto de 2026 para gobernanza.

El conocimiento se pudre. Corre `/verificar` cada dos meses o antes de tomar una decisión de costos que importe. Para hechos sensibles a fecha, usa siempre la fuente oficial.

## Créditos y licencia

[MIT](LICENSE) © 2026 León Ruiz. Curso Productividad con Claude (IA) AVANZADO, [Collective Academy](https://collectiveacademy.com/). Basado en [ai-automation-expert](https://github.com/nabolom/ai-automation-expert) (Q3 2026).

Ilustración de portada: [Raúl Sisniega](https://www.behance.net/biosisniega) ©. Publicada con autorización del autor.
