# S2 — Apoyo técnico posterior: evals

> La agenda canónica está en [`S2-panorama-guion.md`](S2-panorama-guion.md). Esta página no es otra agenda: sirve para cerrar la continuidad de seis casos cuando ya existe una decisión acotada.

## Cuándo usarlo

- Ruta 1: ya existe una falla o sistema medido.
- Ruta 2: ya se definió proceso y decisión.
- Ruta 3: solo después de comprender el camino dorado y regresar a Ruta 2.

No uses esta guía para bloquear la entrada a S2 ni para exigir `/eval` durante el laboratorio.

## Secuencia técnica

1. Confirmar ruta, proceso/caso y decisión.
2. Escribir seis casos: 4 típicos, 1 límite y 1 adversarial.
3. Fijar salidas esperadas antes de correr el sistema.
4. Crear prompt v0 desde la decisión de S2, sin asumir una sesión técnica previa.
5. Ejecutar `/eval` solo si el sistema está listo.
6. Si no corre, registrar `BLOQUEADO`; no inventar una tasa.
7. Llevar el caso fallido y la pregunta de diagnóstico a S3.

## Cierre

**Estás aquí:** continuidad de S2 y casos.

**Siguiente:** S3 para diagnóstico por capas y comparación v0 → v1.

**Si estás bloqueado:** usa el camino dorado offline o una tabla manual.

**Si terminaste antes:** suite extendida de diez casos o una extensión justificada.

La guía detallada está en [`curso/S2-evals.md`](../curso/S2-evals.md).
