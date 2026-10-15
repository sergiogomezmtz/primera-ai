# Patrón 05 — Watcher

**Vigilar algo. Actuar cuando cambia.** Precios, competidores, menciones, un estado en un CRM, un archivo en Drive, una métrica que cruza un umbral.

## Estructura

```
Schedule Trigger               ← cada X minutos/horas
   ↓
Leer el estado actual          ← API, scrape, query
   ↓
Comparar contra el estado anterior   ← ← ← AQUÍ ESTÁ TODO
   ↓
¿Cambió de forma relevante?
   ├─ No  → terminar en silencio
   └─ Sí  → ¿el cambio requiere juicio?
              ├─ No  → acción directa (`if`)
              └─ Sí  → LLM evalúa → acción
   ↓
Guardar el nuevo estado
   ↓
Notificar
```

## El estado es el patrón

Todo lo demás es plomería. **Sin memoria del estado anterior, no tienes un watcher: tienes un notificador que te spamea cada 5 minutos.**

Dónde guardarlo: **Data Table** de n8n (sin montar nada), Postgres, o hasta una hoja de Google. No importa. Que persista y que se escriba **después** de la acción, no antes — si la acción falla, quieres reintentar, no perder el evento.

## "Cambio relevante" no es "cambio"

El error más común: notificar cualquier diferencia. Un precio que se mueve $0.01, un timestamp que cambió, un campo que se reordenó.

Define **umbral de relevancia** antes de escribir el código:
- ¿Cuánto tiene que moverse para importar?
- ¿Qué campos ignoro por completo?
- ¿Cuál es la frecuencia máxima de notificación aceptable? (nadie quiere 40 alertas al día)

Si el humano empieza a ignorar las notificaciones, el sistema está muerto aunque siga corriendo. Es la forma más común en que estos mueren: no fallan, se vuelven ruido.

## Frecuencia

Más seguido ≠ mejor. Cada corrida cuesta: llamadas a API, rate limits, tokens.

Pregunta: **¿cuánto tiempo puede pasar antes de que enterarse tarde sea un problema?** Esa es tu frecuencia. Normalmente es mucho menos frecuente de lo que la gente asume.

## Fallas típicas

- **La fuente cambia de formato** y el watcher lee basura sin darse cuenta. Valida la estructura en cada corrida.
- **La fuente cae** y el watcher interpreta "sin datos" como "cambió a nada" y dispara alertas falsas. Distingue error de cambio. Son cosas distintas.
- **Ejecuciones solapadas** si una corrida tarda más que el intervalo. Pon un lock o sube el intervalo.
