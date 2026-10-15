# Ejercicio final S5 — Comparar antes de coordinar

> **El objetivo no es usar más agentes. Es elegir la menor arquitectura que permite que la información circule como el caso lo necesita. El veredicto queda abierto hasta comparar evidencia.**

## 1. Primero descarga el ejercicio

Abre tu **Terminal** y copia estas tres líneas, una sola vez y en este orden:

```bash
git clone https://github.com/nabolom/nest-a-juicio.git
cd nest-a-juicio
bash scripts/empezar.sh
```

`git clone` descarga el ejercicio; `cd` entra a la carpeta; `bash scripts/empezar.sh` valida que Claude Code esté listo. Este último comando **no ejecuta agentes todavía**.

Si aparece `OK`, continúa. Si pide autenticación, ejecuta `claude auth login` y vuelve a correr `bash scripts/empezar.sh`.

---

## 2. Después lee el caso en el README

Abre el archivo **README.md** que está en tu carpeta `nest-a-juicio` o léelo directamente en GitHub: https://github.com/nabolom/nest-a-juicio

Ahí encontrarás el caso completo de **Cobranza Pro**: Producto está listo, Ventas prometió acceso a 40 clientes, Riesgo bloquea activación automática para 12 clientes regulados y Operaciones solo alcanza 15 inscripciones manuales en una semana.

No necesitas escribir `cat` ni abrir archivos desde la Terminal para entender el caso. El README lo presenta en lenguaje normal antes de pedirte ejecutar nada.

---

## 3. Entiende los dos patrones y haz una predicción

| Arquitectura | Qué hace |
|---|---|
| **Agente único** | Un agente resuelve el caso sin coordinación entre especialistas. Es el baseline. |
| **Nest** | Cuatro especialistas reportan a un líder. El líder integra y decide. |
| **Swarm** | Los agentes comparten tareas y pueden enviarse mensajes directos entre sí. |

Después de leer el caso, responde:

> “Para Cobranza Pro predigo que la menor arquitectura suficiente será [agente único / Nest / Swarm] porque [razón]. Si no puedo correr una alternativa, marcaré la comparación como incompleta en vez de inventar un veredicto.”

---

## 4. Ejecuta el Nest — todos los Aprendedores(as)

En la Terminal, dentro de la carpeta `nest-a-juicio`, ejecuta:

```bash
bash scripts/correr-nest.sh
```

Verás cuatro delegaciones: Producto, Ventas, Riesgo y Operaciones. El líder recibirá esos reportes, decidirá si lanzar, hacer un piloto o posponer y producirá un plan de 72 horas.

La corrida es válida cuando aparece:

```text
ARCHIVO GUARDADO: resultados/conclusion-nest.md
NEST COMPLETADO: 4/4 reportes recibidos.
```

El primer mensaje confirma que el Nest guardó la decisión de negocio, la evidencia, las tensiones y el plan de 72 horas en `resultados/conclusion-nest.md`. Guarda una captura del transcript y escribe `/exit`. No necesitas usar `/usage` ni calcular costos.

---

## 5. Ejecuta el Swarm — Aprendedores(as) y facilitador

Ahora ejecuta el mismo caso como un Agent Team:

```bash
bash scripts/correr-swarm.sh
```

El líder conserva Producto y el script crea tres teammates: Ventas, Riesgo y Operaciones. Verás cuatro tareas compartidas y solo dos mensajes directos obligatorios: Riesgo → Ventas y la respuesta de Ventas. Es una demostración breve de coordinación, no una investigación larga.

La corrida cuenta como Swarm cuando aparecen:

```text
SALIDA GUARDADA: resultados/reporte-swarm.md
SWARM COMPLETADO: teammates, tareas compartidas y dos mensajes entre pares observados.
```

El archivo `resultados/reporte-swarm.md` deja la decisión, evidencia por rol, comunicación observada y qué cambió —o no— frente al Nest. Agent Teams es experimental. Si en 90 segundos no aparecen teammates, escribe `/exit`; no intentes depurarlo durante el taller. El debrief de Claude puede explicar el contraste incluso sin una corrida válida.

---

## 6. Compara con una rúbrica común y deja abierto el veredicto

No necesitas terminar una entrevista larga durante el taller. Abre Claude Code dentro del repo:

```bash
claude
```

Luego pide un debrief que compare las corridas disponibles:

```text
Compara el baseline de agente único, Nest y Swarm solo cuando exista evidencia.
Usa la misma tarea y registra calidad, tiempo, costo/tokens, fallas y complejidad operativa.
No presupongas que Nest o Swarm ganan.
Si falta una corrida, marca la comparación como incompleta y no inventes datos.
Escribe resultados/debrief-swarm.md con predicción, evidencia, limitaciones y veredicto abierto.
```

El veredicto válido puede ser: agente único suficiente, Nest justificado, Swarm justificado o comparación incompleta. La menor arquitectura suficiente gana; a veces esa arquitectura será no usar multiagente.

`/decidir-arquitectura` queda como actividad opcional para quien quiera defender una decisión propia en más detalle.

## 7. Crea una entrega descargable

Una vez que tengas la conclusión del Nest y el debrief automático, abre Claude Code dentro del repo:

```bash
claude
```

Luego escribe:

```text
/cerrar-s5
```

Se creará `resultados/entrega-s5.md`, un archivo único con la conclusión del caso, el debrief de Claude y la evidencia disponible. Adjunta ese archivo desde la carpeta `resultados` en Finder, Explorador de archivos o la plataforma donde entregarás tu trabajo.

## 8. Configura tu propio sistema

Después del caso guiado, crea una copia privada de la [plantilla para configurar Nest o Swarm](https://github.com/nabolom/plantilla-nest-swarm). Ese repo entrevista tu propio proceso y genera el esqueleto del patrón que justifiques.

Para el recorrido completo, los diagramas, el caso, la decisión guiada y la guía de facilitación, consulta el [README de `nest-a-juicio`](https://github.com/nabolom/nest-a-juicio).

## Referencias

[1]: https://code.claude.com/docs/en/agent-teams "Claude Code Docs — Agent teams"
