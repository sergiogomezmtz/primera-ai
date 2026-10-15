## La doctrina, en corto

> La doctrina completa vive en CLAUDE.md. Los principios se citan por nombre, no por número.

- **Si puedes escribirlo como un `if`, que sea un `if`.** La IA es cara, lenta y no determinista.
- **¿Puedes dibujar el diagrama completo?** Entonces es un workflow, no un agente.
- **Diseña la falla, no el éxito.** Nadie está viendo a las 3 AM.
- **Salida estructurada o no hay sistema.** JSON con esquema, validado.
- **Los prompts son código.** Versiónalos, corre evals cuando cambien.
- **Un sistema completo a medias > medio sistema completo.**
- **El agente debe saber cuándo no sabe.** Escalamiento explícito.
- **Mide el proceso antes de automatizarlo.** No se recupera después.
- **Lo que no está en disco no existe.**
- **El harness importa más que el modelo.** Antes de subir de modelo, arregla el andamio.
- **La condición de parada debe ser verificable sin el modelo.** Un modelo siempre cree que avanzó.
- **El conocimiento vive en archivos, no en prompts.** Un concepto por archivo, versionado junto al código (OKF).
- **Menos pasos, siempre.** `0.95^20 = 0.358`. Veinte pasos al 95% y el sistema funciona el 36% de las veces.
- **Cuando falle, pregunta qué CAPA está rota.** Casi nunca es el modelo. Ver `referencias/agent-engineering.md`.

¿Sabes hacer las ocho cosas que separan una demo de un sistema? → [`competencias.md`](competencias.md)
