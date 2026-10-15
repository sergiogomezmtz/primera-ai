# Apéndice técnico: `/rumbo` para la primera medición

> **Apéndice técnico:** la puerta de entrada del grupo es [`Sesión 2 — Panorama y primera medición`](../curso/S2-panorama-y-evals.md). Este archivo conserva los pasos técnicos del assessment `/rumbo`; la continuidad de los seis casos está en la [`Ruta de continuidad de la Sesión 2`](ruta-continuidad-s2.md).

> **No es otra puerta de entrada.** Empieza por la sesión S2. Usa este apéndice solo cuando necesites los pasos técnicos para actualizar o correr `/rumbo`.

El assessment mínimo toma aproximadamente **35 minutos**: fija qué vas a construir, mide con evidencia dónde estás y decide tu ruta. La continuidad completa después de la sesión toma **60–90 minutos** porque añade camino dorado, decisión, seis casos y fallback.

**Caso 1 · Vas a empezar tu repo hoy:**

1. Entra a https://github.com/nabolom/agentic-ai-automation-mentor-agent-2026 y usa "Use this template" → "Create a new repository", márcalo como Private y créalo.
2. Clónalo en tu computadora, entra a la carpeta y abre Claude Code con `claude`.
3. Abre [`ALUMNO-EMPIEZA-AQUI.md`](../ALUMNO-EMPIEZA-AQUI.md), elige Ruta 1, Ruta 2 o Ruta 3 y produce el checkpoint mínimo. Usa `/rumbo` solo después de elegir ruta, si necesitas fijar formalmente el foco.

**Caso 2 · Ya tienes tu repo del curso (creado desde ai-automation-expert):**

1. En la terminal, parado en tu repo, trae el assessment y la capa de acompañamiento:

   ```bash
   mkdir -p .claude/skills/rumbo
   curl -o .claude/skills/rumbo/SKILL.md https://raw.githubusercontent.com/nabolom/agentic-ai-automation-mentor-agent-2026/main/.claude/skills/rumbo/SKILL.md
   curl -o ACOMPANAMIENTO.md https://raw.githubusercontent.com/nabolom/agentic-ai-automation-mentor-agent-2026/main/ACOMPANAMIENTO.md
   echo "@ACOMPANAMIENTO.md" >> CLAUDE.md
   ```

2. Cierra y vuelve a abrir Claude Code. Elige primero la ruta correspondiente; después escribe `/rumbo` solo si necesitas fijar formalmente el foco con evidencia.

**En ambos casos:**

1. Haz commit de tu `rumbo.md` y entrega su frontmatter a León cuando cierres el assessment y antes de la primera medición.
2. Si estás preparando S2, lleva lo que dice la sección "Qué llevo a S2" de tu `rumbo.md`: decisión y tres casos ancla como mínimo; los seis casos pertenecen a la continuidad posterior.
