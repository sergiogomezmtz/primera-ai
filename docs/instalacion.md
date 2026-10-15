## Arranque

> Para decidir qué necesitas según tu sistema y ruta, empieza por [`Dependencias y preflight`](dependencias-y-preflight.md). Esta página contiene los pasos detallados de instalación.

### Paso 1 — Instala Claude Code

El método principal es el **instalador nativo**. No necesita Node ni npm.

**macOS, Linux y WSL:**

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows (PowerShell):**

```powershell
irm https://claude.ai/install.ps1 | iex
```

Cierra y vuelve a abrir la terminal, y verifica:

```bash
claude --version
```

Debe devolver un número de versión. Si dice `command not found`, el directorio de instalación no está en tu PATH todavía: sigue la guía oficial en https://code.claude.com/docs/en/setup (sección *Fix your PATH*).

**Alternativa con npm** (solo si ya vives en Node; requiere Node 22 o superior):

```bash
npm install -g @anthropic-ai/claude-code
```

Necesitas también **Git** (`git --version`). En macOS viene con las Command Line Tools (`xcode-select --install`); en Windows, desde [git-scm.com](https://git-scm.com/download/win).

Claude Code requiere una cuenta Pro, Max, Team, Enterprise o de Console. Al correr `claude` por primera vez te pide iniciar sesión en el navegador.

### Preflight antes de clase

Haz estas comprobaciones antes de la sesión:

```bash
claude --version
git --version
```

Después entra con `claude` y, dentro de la sesión, usa `/doctor` si necesitas un diagnóstico de configuración. La [guía oficial de Claude Code](https://code.claude.com/docs/en/quickstart) también ofrece `/help` y `/exit` para orientarte. Si algún paso falla, conserva el mensaje o una captura y lleva el problema a office hours; no necesitas resolverlo para participar en la actividad.

El preflight de Python, Node.js y NPM es condicional a la ruta del proyecto. No instales Node/NPM solo para hacer funcionar Claude Code: el instalador nativo no los necesita.

Si no llegas con Claude Code listo, usa el camino dorado sin credenciales desde la raíz del repositorio:

```bash
python3 ejemplo/camino_dorado.py --modo offline --version v1
```

En Windows, cambia `python3` por `py`. Si tampoco tienes Python, abre `ejemplo/casos.json` y recorre los seis casos del núcleo en papel con el diagrama de [`ejemplo/README.md`](../ejemplo/README.md).

El fallback permite practicar entradas, salidas esperadas, validación y escalamiento. La autenticación real se agrega después, cuando el contrato ya está claro.

### Paso 2 — Crea tu copia del repo

**No hagas fork ni clones directo.** Usa el botón de template para tener tu propio repo con permisos de escritura:

1. Ve a [github.com/nabolom/agentic-ai-automation-mentor-agent-2026](https://github.com/nabolom/agentic-ai-automation-mentor-agent-2026)
2. Click en el botón verde **“Use this template”** → **“Create a new repository”**
3. Pon el nombre que quieras (ej. `mi-automatizacion`)
4. Márcalo como **Private** — tus procesos de negocio no tienen por qué ser públicos
5. Click en **“Create repository”**

Ahora clona **tu** repo (el que acabas de crear, no el mío). `git clone` crea la carpeta **donde estés parado en la terminal**; corre `pwd` si no sabes dónde estás.

```bash
mkdir ~/proyectos-ia && cd ~/proyectos-ia
git clone https://github.com/TU-USUARIO/TU-REPO.git
cd TU-REPO
claude
```

Al entrar al directorio y correr `claude`, el agente lee automáticamente `CLAUDE.md` y carga la doctrina, el mapa del repo, las skills y la capa de acompañamiento. No necesitas configurar nada más.

Los repos creados desde template **no reciben actualizaciones automáticas**: son una foto del día que los creaste. Cada sesión del curso trae su propio paso para traer lo nuevo con `curl`.

### Paso 3 — Elige tu ruta antes de usar un comando

No escribas `/arrancar` automáticamente. Primero abre [`ALUMNO-EMPIEZA-AQUI.md`](../ALUMNO-EMPIEZA-AQUI.md) y elige:

- **Ruta 1:** ya tienes algo construido; lleva una falla, cuello de botella o decisión difícil.
- **Ruta 2:** tienes un proceso o idea; acótalo y elige una decisión candidata.
- **Ruta 3:** no tienes proceso claro o estás bloqueado; recorre el camino dorado offline y vuelve a Ruta 2.

Usa `/rumbo` solo después de elegir la ruta, cuando necesites fijar formalmente el foco con evidencia. Usa `/arrancar` únicamente en Ruta 2 o cuando el Mentor confirme que necesitas convertir un proceso acotado en diseño de automatización. En todos los casos, empieza con una pregunta de solo lectura y no inventes tu proceso.
