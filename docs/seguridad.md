# Seguridad y límites operativos

Nunca subas credenciales ni datos sensibles. `.gitignore` bloquea `.env`, claves y archivos de credenciales; `.claude/settings.json` añade denegaciones para ubicaciones comunes. Eso ayuda, pero **no es una frontera completa**: un comando de terminal podría leer una ruta que el patrón de archivos no cubre.

## Antes de abrir una ruta live

1. Trabaja con datos sintéticos o anonimizados.
2. Activa el sandbox documentado por Claude Code antes de permitir comandos de terminal.
3. Revisa qué directorios puede escribir el agente.
4. Revisa egress y conexiones de red; no amplíes allowlists sin entender el blast radius.
5. No guardes API keys en el repositorio ni las pegues en el chat.
6. Confirma el modelo, el número máximo de casos, el timeout y el presupuesto antes de ejecutar.
7. Si el entorno no puede cumplir esos límites, usa la ruta offline/preflight.

## Qué sí protege el repo

- `.gitignore` reduce el riesgo de subir secretos por accidente.
- `settings.json` bloquea lecturas de patrones comunes de `.env`, `secrets/` y `credentials.json`.
- El camino dorado offline no necesita red ni credenciales.
- El runner debe marcar errores de API y salidas inválidas como `BLOQUEADO`, no como aciertos.

## Qué no promete

- No promete que Bash, PowerShell o un proceso externo no puedan leer secretos.
- No sustituye sandbox, aislamiento de egress, permisos mínimos ni un gestor de secretos.
- No convierte el modo live en producción.
- No permite enviar datos reales a una API sin revisión de la persona responsable.

Si el proceso toca datos sensibles, lee `.claude/skills/seguridad-datos/SKILL.md` antes de conectar nada.
