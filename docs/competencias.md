---
type: mapa-de-competencias
title: Competencias de Agentic AI al terminar el curso
description: Mapa de salida del núcleo S2-S4 y extensiones avanzadas de Agentic AI.
tags: [competencias, autodiagnostico, agentic-ai, agent-engineering]
timestamp: 2026-10-13T00:00:00Z
---

# Competencias de Agentic AI al terminar el curso

Las herramientas cambian cada seis meses. El criterio para diseñar sistemas confiables cambia mucho menos.

Este mapa convierte las ocho competencias originales del repositorio en **seis competencias núcleo** más una **extensión avanzada**. No se pierde contenido: se agrupa para que la salida sea recordable, observable y evaluable.

> **Promesa de salida:** al terminar el núcleo, cada Aprendedor(a) puede convertir una automatización o proceso en un sistema medible, diagnosticable, gobernable y operable por otra persona.

## Núcleo común — S2 a S4

| ID | Competencia | Al terminar, el Aprendedor(a) puede… | Evidencia observable |
|---|---|---|---|
| C1 | **Especificación y framing** | Convertir un deseo o proceso difuso en una decisión acotada, un alcance y un criterio de terminado verificable. | `proyecto.md`, `alcance.md` y una frase de “terminado” que un tercero pueda revisar. |
| C2 | **Juicio de delegación y arquitectura** | Decidir qué debe ser `if`, IA, herramienta o humano; distinguir workflow de agente sin usar autonomía como objetivo. | Mapa de flujo con la asignación de cada paso y una justificación de por qué la IA sí o no entra. |
| C3 | **Contexto, contrato y harness** | Diseñar qué información recibe el sistema, qué salida debe producir, cómo se valida y qué ocurre cuando no puede responder con seguridad. | Contrato de entrada/salida, salida estructurada, validación, permisos y ruta de escalamiento. |
| C4 | **Evaluación y medición** | Escribir casos antes de construir, fijar salidas esperadas y reportar una tasa en vez de una opinión. | Seis casos núcleo: 4 típicos, 1 límite y 1 adversarial; línea base y salida cruda. |
| C5 | **Diagnóstico, iteración y mejora** | Distinguir falla de modelo, contexto, herramienta o harness; decidir si necesita un loop y cambiar una sola cosa a la vez. | Diagnóstico de una falla, evidencia que descarte capas y comparación v0 → v1 sobre los mismos casos. |
| C6 | **Gobernanza y operabilidad** | Diseñar permisos mínimos, límites de costo, aprobaciones, observabilidad, recuperación y un handoff usable por otra persona. | Matriz de gobernanza, una falla provocada, registro de cómo se detectó y una pareja ejecutando una prueba sin ayuda. |

## Cómo se reagrupan las ocho competencias originales

| Competencia anterior | Dónde vive ahora |
|---|---|
| Especificación de objetivos | C1 |
| Juicio de delegación | C2 |
| Context Engineering | C3 |
| Evaluación | C4 |
| Harness literacy | C3 y C5 |
| Loop Engineering | C5, como decisión basada en evidencia |
| Gobernanza | C6 |
| Mejora continua | C5 |

## Extensión avanzada

Estas competencias agregan profundidad sin convertirse en requisito común para S2–S4:

| ID | Extensión | Evidencia sugerida |
|---|---|---|
| A1 | **Loops y harnesses durables** | Cuatro paradas con éxito verificable, presupuesto, no-progreso y escalamiento. |
| A2 | **Integración de APIs, herramientas y costos** | Auth, rate limits, manejo de errores, costo por corrida y proyección mensual. |
| A3 | **MCP, conocimiento durable y contexto a escala** | Selección de herramientas/contexto con permisos y una razón explícita para no agregar más. |
| A4 | **Multiagente y productización** | Comparación agente único vs Nest/Swarm; decisión basada en calidad, velocidad y costo. |

La extensión es para quien termina antes o ya trae experiencia. No debe frenar al grupo ni convertirse en una carrera de complejidad.

## Niveles de dominio

| Nivel | Descripción | Qué demuestra |
|---:|---|---|
| 0 | **Reconoce** | Puede explicar el vocabulario, pero todavía no produce evidencia propia. |
| 1 | **Aplica con andamio** | Completa el camino dorado y puede seguir una plantilla con acompañamiento. |
| 2 | **Transfiere con evidencia** | Lleva el criterio a un proceso propio o caso acotado y defiende sus decisiones con números, archivos o criterios. |
| 3 | **Opera y enseña** | Otra persona puede correr una prueba, reconocer una falla y actuar dentro de límites claros. |

## Criterio de salida del núcleo

El núcleo se considera logrado cuando el Aprendedor(a):

- llega al menos a **nivel 2 en C1–C5**;
- llega al menos a **nivel 2 en C6** al cerrar S4;
- puede mostrar un paquete mínimo: una decisión, seis casos, una medición, un diagnóstico y un handoff;
- puede responder las cinco preguntas de defensa del curso sin recurrir a “el modelo dijo que sí”.

No es requisito memorizar una API, conectar datos reales, construir un loop o usar multiagente.

## Autodiagnóstico rápido

Marca honestamente:

- [ ] Puedo escribir qué significa “terminado” sin preguntarle al modelo.
- [ ] Puedo clasificar un paso como `if`, IA, herramienta o humano.
- [ ] Puedo decir qué contexto entra y qué contexto dejo fuera.
- [ ] Puedo escribir seis casos antes de confiar en un prompt.
- [ ] Puedo nombrar la capa rota cuando algo falla.
- [ ] Puedo definir permisos, costo, aprobación y handoff.

La primera sesión técnica está en la [`Sesión 2 — Panorama y primera medición`](../curso/S2-panorama-y-evals.md). La continuidad técnica de los seis casos está en la [`Ruta de continuidad de la Sesión 2`](ruta-continuidad-s2.md).

## La frase que las ordena

> **La productividad no viene de pedirle más al modelo. Viene de diseñar el entorno donde el modelo puede trabajar:** contexto correcto, herramientas adecuadas, memoria durable, criterios de éxito claros y límites seguros.

La evidencia manda: el asistente propone borradores; la persona que conoce la operación fija las salidas esperadas, umbrales y límites.
