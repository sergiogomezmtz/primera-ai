# Rescates y extensiones

## Principio

Cuando algo se rompe, rescata el **objetivo de aprendizaje**, no necesariamente la herramienta que el Aprendedor(a) eligió.

## Matriz de rescate

| Situación | Rescate inmediato | Evidencia que conserva |
|---|---|---|
| Claude Code no instala | Camino dorado offline o en papel | Contrato, casos y recorrido |
| No hay Python | Leer `casos.json` y completar tabla manual | Salida esperada y decisión por etapa |
| No hay autenticación | No pedir ni pegar una llave; usar offline | Contrato y punto de integración documentado |
| Herramienta visual no responde | Trabajar con formato local y comparar después | Evals y criterio de escalamiento |
| No hay proyecto propio | Usar el camino dorado y nombrar la transferencia | Decisión acotada y seis casos |
| El Aprendedor(a) trae dos proyectos | Elegir uno; dejar el otro fuera de alcance | Alcance explícito |
| El loop no arranca | Especificar cuatro paradas o tomar ruta no-loop | Harness y checker |
| Agent Teams no arranca | No depurarlo durante el taller | Juicio arquitectónico documentado |

## Cómo acompañar por nivel

| Nivel observable | Tu postura | Siguiente pregunta |
|---|---|---|
| 0–1 | Enseñar con ejemplo corto | “¿Qué parte de este ejemplo se parece a tu proceso?” |
| 2 | Retar y pedir evidencia | “¿Qué archivo, número o criterio falta?” |
| 3 | Revisar como par | “¿Qué riesgo o contradicción estás aceptando?” |

## Extensiones ordenadas

Ofrece una sola extensión a la vez:

1. Completar de 6 a 10 casos.
2. Medir costo por corrida y confianza.
3. Correr end-to-end y comparar con escritorio.
4. Diseñar un loop con cuatro paradas, solo si el proceso itera.
5. Preparar un handoff operable por otra persona.
6. Comparar agente único con multiagente en S5.

## Qué no usar como extensión de emergencia

- más conceptos teóricos;
- más herramientas;
- más agentes;
- una integración live sin contrato;
- datos reales sensibles;
- una tarea que no tiene criterio de éxito verificable.
