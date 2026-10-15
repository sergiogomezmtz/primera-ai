---
type: ruta-continuidad
title: Rutas de continuidad de la Sesión 2
description: Cómo pasar de una ruta elegida a una decisión, tres casos ancla y la continuidad de seis casos.
tags: [rutas-1-2-3, onboarding, evals, continuidad]
timestamp: 2026-10-14T00:00:00Z
---

# Rutas de continuidad de la Sesión 2

Esta página no sustituye la elección inicial. La fuente canónica es [`Rutas de entrada`](rutas-de-entrada.md). Aquí se explica qué hacer después de elegir Ruta 1, 2 o 3.

## Resultado común

Todas las rutas llegan a:

- proceso o caso en una frase;
- una sola decisión;
- salida esperada verificable;
- tres casos ancla: típico, límite y adversarial;
- siguiente paso y fallback.

Los seis casos, la línea base y `/eval` son continuidad posterior cuando ya existe suelo operativo.

## Ruta 1 — Fast lane para sistemas existentes · 30–45 min

Úsala si puedes mostrar una automatización, prototipo, falla, traza o cuello de botella.

1. Elige una sola decisión difícil.
2. Reúne evidencia existente: prompt, corrida, error, costo, queja o handoff.
3. Clasifica el flujo en `if`, IA, herramienta y humano.
4. Revisa tres casos ancla usando tus datos; no inventes casos nuevos si ya existen.
5. Ejecuta `/rumbo` solo para fijar foco si hace falta.
6. Elige una extensión: diagnóstico, costo, harness, loop, MCP o multiagente.

**Llegada:** no repites onboarding; produces una hipótesis de mejora medible.

## Ruta 2 — Descubrir qué agentizar · 60–90 min

Úsala si tienes un proceso o idea real, pero todavía no sabes qué decisión delegar.

### Paso 0 — Abre tu espacio

Elige Claude Code, Cowork o un fallback. No instales todo el ecosistema.

**Checkpoint:** puedes abrir la carpeta o tienes una alternativa documentada.

### Paso 1 — Describe el proceso actual

Escribe quién lo ejecuta, qué lo dispara, qué entra, qué pasos ocurren, qué resultado debe salir y qué riesgo no aceptarías automatizar.

**Checkpoint:** proceso en una frase y una lista corta de pasos.

### Paso 2 — Clasifica antes de agentizar

Marca cada paso como `if` o regla determinista, decisión con IA, herramienta/integración o humano/aprobación.

**Checkpoint:** puedes explicar por qué una parte necesita IA y otra no.

### Paso 3 — Elige una sola decisión

```text
Ayúdame a elegir una sola decisión de este proceso que valga la pena medir.
Hazme una pregunta a la vez sobre ambigüedad, riesgo, frecuencia y salida esperada.
No inventes mi operación ni conviertas todo el proceso en un agente.
```

**Checkpoint:** decisión candidata y qué queda explícitamente fuera.

### Paso 4 — Escribe tres casos ancla

Uno típico, uno límite y uno adversarial. Para cada caso fija la salida esperada antes de ejecutar nada.

**Checkpoint final de S2:** puedes enseñar proceso/caso, decisión, casos, salidas y fallback.

## Ruta 3 — Camino dorado opcional · 20–35 min

Úsala solo si falta claridad, no existe proceso propio o hay bloqueo técnico.

1. Lee [`ejemplo/README.md`](../ejemplo/README.md): Problema, Qué vas a hacer aquí y La secuencia que enseña.
2. Identifica `if`, IA, salida estructurada, validación y humano.
3. Corre el ejemplo offline o recorre `casos.json` en papel.
4. Responde qué no llega a la IA, cuándo entra la IA, qué valida el sistema, cuándo escala y qué cambia de v0 a v1.
5. Regresa a Ruta 2 y elige un proceso propio, o declara que continuarás con el caso común.

**Importante:** el runner offline demuestra el contrato y el harness. No mide la capacidad de un modelo real.

## Continuidad de seis casos

Cuando ya tienes una decisión:

1. Completa cuatro casos típicos, uno límite y uno adversarial.
2. Fija las salidas esperadas.
3. Corre la línea base si la herramienta está lista.
4. Si no puedes correrla, registra `BLOQUEADO` y conserva la tabla.
5. Lleva el caso más preocupante a S3.

No conectes una API real para cumplir un número y no uses datos sensibles.

## Stop lines

- **Minuto 20:** si Ruta 3 todavía no se entiende, explica el diagrama en papel.
- **Minuto 45:** si Ruta 2 no tiene una decisión, reduce el proceso a una sola categoría, sí/no, valor o escalamiento.
- **Minuto 60:** si Ruta 1 ya tiene evidencia, no repitas el caso común; pasa a la falla.
- **Fin del bloque:** congela extensiones y guarda el checkpoint mínimo.

## Cierre uniforme

Escribe: **estás aquí** (ruta y decisión) · **siguiente** (una acción concreta) · **si estoy bloqueado** (fallback) · **si terminé antes** (extensión y por qué).
