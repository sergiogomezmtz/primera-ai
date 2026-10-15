# Rúbrica de entrega

La entrega no se califica por la cantidad de comandos ejecutados ni por usar un agente. Se califica por la calidad de las decisiones y la evidencia que las sostiene.

## Niveles

| Dimensión | 0 — ausente | 1 — descrita | 2 — demostrada | 3 — defendible |
|---|---|---|---|---|
| **Problema y alcance** | No hay proceso observable | Hay proceso, pero no está acotado | Tiene dentro, fuera y definición de terminado | Tiene línea base, supuesto riesgoso y criterio que un tercero puede verificar |
| **Delegación** | Todo es “IA” | Distingue algunas piezas | Clasifica `if`, IA, herramienta y humano con razones | Puede defender por qué quitó IA o mantuvo una persona |
| **Evaluación** | “Funciona” | Hay casos, pero falta salida esperada o número | Tiene el núcleo de seis casos (4/1/1) y una tasa reproducible | Además, análisis de error y comparación antes/después sobre los mismos casos |
| **Confiabilidad** | Solo camino feliz | Nombra fallas | Valida entrada/salida y tiene escalamiento | Tiene verificación externa, presupuesto, no-progreso u observabilidad según aplique |
| **Operabilidad** | Solo el autor puede correrlo | Hay notas sueltas | Otra persona puede seguir el README | Hay handoff, permisos mínimos, acción irreversible protegida y runbook de falla |

## Mínimo para aprobar

- **Problema y alcance:** mínimo 2.
- **Delegación:** mínimo 2.
- **Evaluación:** mínimo 2.
- **Confiabilidad:** mínimo 1.
- **Operabilidad:** mínimo 1.

No se exige un loop, la suite extendida de diez casos ni multiagente. Si el Aprendedor(a) justifica que no corresponden, esa decisión cuenta como evidencia de criterio.

## Qué cuenta como evidencia

Un archivo no es evidencia por existir. Cuenta lo que un tercero puede revisar sin preguntarte:

- La tasa como `aciertos/total`, con su suite y su modo (por ejemplo, `v0 · escritorio · núcleo 6 casos: 4/6`).
- La salida cruda de al menos un caso fallido, junto a la salida esperada.
- La comparación antes/después sobre los mismos casos, con el porqué del cambio.
- La traza de una corrida, o la corrida del checker si no hay loop.
- Otra persona ejecutando una prueba con tu handoff, sin tu ayuda.

## Defensa de tres minutos

Cada persona debe poder responder:

1. ¿Qué proceso elegiste y qué dejaste fuera?
2. ¿Dónde usas IA y por qué no un `if`?
3. ¿Cuál es tu tasa y sobre cuántos casos?
4. ¿Qué caso falló o te da más miedo?
5. ¿Cómo sabes que terminó sin preguntarle al modelo?
6. ¿Qué acción irreversible requiere aprobación?
7. Si tú desapareces mañana, ¿quién lo corre?

## Extensiones

Para una evaluación avanzada, agrega una de estas pruebas:

- costo por corrida y proyección mensual;
- calibración de confianza;
- corrida end-to-end;
- comparación single-agent vs Nest/Swarm;
- prueba de recuperación después de un timeout;
- revisión por un compañero que no conozca el sistema.
