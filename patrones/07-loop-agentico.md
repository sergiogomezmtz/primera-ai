# Patrón 07 — Loop agéntico de larga duración

**La tarea no cabe en una sola pasada ni en una sola ventana de contexto.** El agente tiene que trabajar en sesiones, cada una empezando sin memoria de la anterior.

Es el patrón más difícil y el que más se construye mal. Si puedes evitarlo, evítalo — descompón en workflows. Cuando no puedas, esto es lo que funciona.

## La metáfora que lo explica

Un proyecto atendido por ingenieros **en turnos**, donde cada uno llega sin memoria del turno anterior.

¿Qué necesita un ingeniero así para ser útil en su turno? Exactamente lo que necesita tu agente:
- Saber qué se hizo (**bitácora**)
- Saber qué falta (**lista de tareas**)
- Saber cómo correr el sistema (**script de arranque**)
- Poder revertir si rompe algo (**control de versiones**)
- Y **probar** que lo suyo funciona antes de irse

## Estructura

```
SESIÓN 1 — Inicializador (corre una sola vez)
   ├─ Expande el objetivo en una lista de tareas EXHAUSTIVA (JSON)
   ├─ Crea el archivo de progreso
   ├─ init.sh — levanta el entorno con un comando
   └─ Commit inicial

SESIÓN N — Trabajador (todas las demás)
   ├─ ORIENTARSE
   │    pwd → leer progreso → leer git log → leer lista de tareas
   │    correr init.sh → PRUEBA DE HUMO end-to-end
   ├─ Escoger UNA tarea (la de mayor prioridad no hecha)
   ├─ Ejecutarla
   ├─ VERIFICAR con herramienta externa   ← no preguntarle al modelo
   ├─ Marcar `passes: true` SOLO si pasó de verdad
   └─ Commit + actualizar progreso
```

Nota: no son dos agentes distintos. Es **el mismo harness con distinto primer prompt**.

## Las cuatro reglas que lo sostienen

**1. Una tarea por sesión. Una.** La tendencia natural del modelo es intentar todo de un jalón, quedarse sin contexto a media implementación, y dejarle a la siguiente sesión un desastre sin documentar. Acótalo explícitamente.

**2. La lista de tareas en JSON, no en Markdown.** Verificado: el modelo respeta menos un Markdown — lo "mejora", lo reescribe, borra cosas. Con JSON se contiene. Y solo puede tocar el campo `passes`. Díselo con lenguaje fuerte: *"es inaceptable borrar o editar tareas"*.

**3. Prueba de humo antes de construir nada.** Si la sesión pasada dejó algo roto, lo descubres **antes** de apilar encima. Sin esto, un error se propaga por cinco sesiones y luego nadie sabe dónde empezó.

**4. Verificación externa.** El modelo va a marcar tareas como hechas sin probarlas. Corre el test. Abre el navegador. Consulta la base. **No le preguntes si funcionó.**

## Presupuestos y parada

- Tope de iteraciones
- Tope de gasto (en la consola, no en el código)
- **Detector de no-progreso:** si repite el mismo tool call con el mismo error N veces, rompe el loop y escala. Este es el que casi nadie pone, y es el que evita las facturas absurdas.

## Cuándo NO usar este patrón

Si puedes dibujar el diagrama completo de la tarea, **no es un loop agéntico: es un workflow**. Constrúyelo en n8n, encadena los pasos, y duerme tranquilo.

Este patrón es caro, no determinista y difícil de depurar. Se justifica cuando el camino no se puede predecir de antemano — no cuando simplemente da flojera dibujar el diagrama.

Fuente: `referencias/harness.md`
