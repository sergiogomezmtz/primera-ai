# Antes de clase — primera sesión técnica: Sesión 2

## Un día antes

- [ ] Compartí la copia correcta del repositorio o la plantilla de GitHub.
- [ ] Compartí [`ALUMNO-EMPIEZA-AQUI.md`](../ALUMNO-EMPIEZA-AQUI.md) y la guía de [`S2`](../curso/S2-panorama-y-evals.md).
- [ ] Aclaré que esta es la primera sesión técnica; la reunión anterior fue de bienvenida y contexto.
- [ ] Pedí que traigan lo que tengan: idea/proceso, prototipo, automatización que falla o sistema que ya corre para otras personas.
- [ ] No presenté instalación masiva como requisito. Node/NPM son condicionales.
- [ ] Recordé que no se pegan API keys ni datos sensibles en el repo o el chat.
- [ ] Preparé el camino dorado offline y `ejemplo/casos.json` como fallback.
- [ ] Preparé una pantalla con el diagrama `if → IA → salida estructurada → validación → humano`.

## Antes de abrir la sesión

- [ ] El repositorio público abre desde la rama `main`.
- [ ] `python3 ejemplo/camino_dorado.py --modo offline --version v1` funciona; en Windows está lista la alternativa `py`.
- [ ] La terminal y Claude Code están visibles para la demo.
- [ ] Tienes a mano el prompt de inspección del repositorio.
- [ ] Preparaste una tabla o formulario para clasificar a cada persona en descubrir, construir, endurecer o productificar/escalar.
- [ ] Tienes una pareja de ejemplo con un caso típico, uno límite y uno adversarial.
- [ ] Tienes un plan B si falla Claude Code, Git, Python, la herramienta visual o la autenticación.

## Qué debe estar visible

1. **Panorama Q4-2026:** el modelo genera; el sistema organiza, verifica y limita.
2. **Contrato común:**

   ```text
   if → IA → salida estructurada → validación → humano
   ```

3. **Núcleo de casos:**

   ```text
   6 casos = 4 típicos + 1 límite + 1 adversarial
   ```

4. **Mínimo de hoy:** una decisión, tres casos ancla y un siguiente paso.

## Durante la sesión

- [ ] La plenaria dura 30 minutos y no se convierte en soporte técnico.
- [ ] La teoría dura 30–45 minutos y desemboca en el camino dorado.
- [ ] Hay un break de 10 minutos.
- [ ] El laboratorio ocurre dentro de Claude Code o con fallback equivalente.
- [ ] Nadie trabaja dos procesos a la vez.
- [ ] Las salidas esperadas las fija la persona que conoce la operación.
- [ ] Quien ya trae automatización trabaja en escalar, replantear/endurecer o productificar; no vuelve a empezar.
- [ ] Quien no tiene proceso propio usa el camino dorado sin vergüenza ni penalización.
- [ ] Quien va rápido recibe una extensión, pero no cambia el ritmo del grupo.

## Si el grupo se retrasa

1. Vuelve al diagrama del camino dorado.
2. Reduce el foco a una sola decisión.
3. Pide solo tres casos ancla.
4. Cambia live por offline o papel.
5. Deja los seis casos completos para la entrega inmediata.

## Si el grupo termina antes

Ofrece una sola extensión, en este orden:

1. Completar los tres casos restantes hasta llegar a 4/1/1.
2. Correr `/eval` y guardar la línea base.
3. Nombrar la falla que más preocupa.
4. Para perfiles avanzados: costo, confianza, handoff o justificación de no usar loop.

No abras MCP, multiagente o loops solo para llenar tiempo.
