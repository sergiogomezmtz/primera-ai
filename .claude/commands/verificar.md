---
description: Re-verifica los hechos de referencias/ contra las fuentes oficiales
---

Los archivos de `referencias/` son la razón por la que este repo vale más que un asistente a secas. Se pudren. Este comando los revive.

## Qué hacer

1. Lee cada archivo de `referencias/` y anota su fecha de verificación.
2. Para los que tengan **más de 2 meses** (o todos, si te lo piden):
   - Busca en web la **fuente oficial** de la tabla de fuentes canónicas en `referencias/COMO-ACTUALIZAR.md`.
   - Compara contra lo que dice el archivo.
   - Actualiza lo que cambió. Actualiza la fecha de verificación.
3. Reporta los cambios: qué se movió, qué es nuevo, qué se deprecó.

## Reglas

**Fuente oficial, siempre.** Los blogs y agregadores de "pricing 2026" están optimizados para SEO, no para estar correctos — al armar estos archivos, tres de los mejor rankeados tenían datos viejos o mal, incluyendo el primer resultado de Google.

**Ningún hecho sin fecha y sin fuente.** Si no puedes verificarlo, no lo escribas. Dilo.

**Presta atención especial a:**
- Precios con fecha de vencimiento o escalones por longitud de prompt (ej. Haiku 5.5 arriba de 100k tokens). Y precios "introductorios" que luego se quedan: el de Sonnet 5 iba a subir en septiembre de 2026 y no subió
- Modelos deprecados o retirados
- Nombres de nodos que cambiaron
- Versiones de spec (MCP se mueve rápido)
- APIs que cambiaron parámetros

Al terminar, di en una línea qué tan desactualizado estaba el repo.
