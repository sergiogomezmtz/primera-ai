---
type: dependencias-y-preflight
title: Dependencias y preflight por ruta
description: Qué instalar para la primera medición en macOS, Windows y Linux sin convertir el onboarding en soporte técnico.
tags: [instalacion, preflight, onboarding, dependencias, rutas-1-2-3]
timestamp: 2026-10-13T00:00:00Z
---

# Dependencias y preflight por ruta

**Propósito:** saber qué necesitas para participar sin instalar herramientas que todavía no vas a usar. Esta guía es referencia secundaria: primero elige Ruta 1, 2 o 3 en [`Rutas de entrada`](rutas-de-entrada.md).

> **No instales todo.** Elige una ruta, verifica sus dependencias y conserva un fallback. Node/NPM no son requisitos generales del curso.

## 1. Matriz rápida

| Elemento | Ruta estándar de código | Ruta visual/Cowork | ¿Es requisito para la primera medición? |
|---|---|---|---|
| Cuenta de GitHub y acceso al repo | Sí | Sí | Sí |
| Git | Sí, para clonar y guardar evidencia | Recomendado; puede esperar si trabajarás en Cowork o ZIP | Sí para la ruta estándar |
| Claude Code | Sí | No, si trabajarás solo en Cowork | Una de las dos: Claude Code o Cowork |
| Cowork | No, si usas Claude Code | Sí | Una de las dos: Claude Code o Cowork |
| Python 3.11+ | Sí, para el camino dorado y scripts | No si usarás la ruta visual; útil para el fallback | Condicional |
| Node.js + NPM | Solo para proyectos JS/TS, n8n local o MCP | Solo si esa herramienta lo requiere | **No** |
| n8n/Make | Solo si tu proceso vive ahí | Solo si tu proceso vive ahí | **No** |
| API keys, bases de datos, Docker | Después del contrato y los evals | Después del contrato y los evals | **No** |

### Decisión en 30 segundos

- **Voy por código/API:** Git + Claude Code + Python son la combinación recomendada.
- **Voy por Cowork/visual:** Cowork + acceso al repo bastan para comenzar; Git y Python pueden esperar.
- **Mi proyecto es JavaScript/TypeScript, n8n local o MCP:** añade Node.js y NPM solo cuando el proyecto lo pida.
- **No sé todavía:** usa Claude Code o Cowork, corre el camino dorado y no instales Node/NPM por anticipado.

## 2. Preflight mínimo

### Todos

Confirma que tienes:

- cuenta de GitHub y acceso para crear o abrir tu copia privada;
- una carpeta de trabajo o workspace en Cowork;
- una ruta elegida: Claude Code o Cowork;
- conexión a internet para el primer acceso, sin necesidad de usar una API real.

### Claude Code + código

```bash
claude --version
git --version
```

Después entra con `claude` y, dentro de la sesión, usa `/doctor` si necesitas un diagnóstico de configuración.

Para Python:

```bash
# macOS/Linux
python3 --version

# Windows PowerShell
py --version
```

### Node.js + NPM, solo si tu proyecto lo necesita

```bash
node --version
npm --version
```

Si no tienes Node/NPM y tu proyecto no es JS/TS, no te detengas: no son requisitos del núcleo.

## 3. Instalación por sistema operativo

### Claude Code

El instalador nativo es la ruta recomendada y **no necesita Node ni NPM**:

**macOS, Linux y WSL:**

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows PowerShell:**

```powershell
irm https://claude.ai/install.ps1 | iex
```

Cierra y vuelve a abrir la terminal y verifica `claude --version`. Si falla el PATH, sigue la [guía oficial de setup](https://code.claude.com/docs/en/setup).

### Git

**macOS:**

```bash
xcode-select --install
```

Si ya tienes Git, `git --version` lo confirma. También puedes usar el instalador oficial de [Git para macOS](https://git-scm.com/download/mac).

**Windows:**

Instala [Git for Windows](https://git-scm.com/download/win) y vuelve a abrir PowerShell o Git Bash. Comprueba con `git --version`.

**Ubuntu/Debian:**

```bash
sudo apt update && sudo apt install git
```

**Fedora:**

```bash
sudo dnf install git
```

### Python

**macOS/Windows:** usa el instalador oficial de [python.org](https://www.python.org/downloads/). En Windows, activa la opción para añadir Python al PATH o usa el lanzador `py`.

**Ubuntu/Debian:**

```bash
sudo apt update && sudo apt install python3 python3-venv
```

**Fedora:**

```bash
sudo dnf install python3
```

Después verifica `python3 --version` en macOS/Linux o `py --version` en Windows.

### Node.js + NPM, condicional

Instálalos solo si tu proyecto usa JavaScript/TypeScript, n8n local o un servidor MCP que los requiera. Usa la versión LTS desde [nodejs.org](https://nodejs.org/en/download/) y verifica:

```bash
node --version
npm --version
```

No instales Node/NPM para “hacer funcionar Claude Code”: la ruta nativa de Claude Code no los necesita.

## 4. ¿Estoy listo para offline o live?

| Estado | Significa | Qué hago |
|---|---|---|
| **Verde** | Tengo Claude Code o Cowork, acceso al repo y puedo seguir una ruta. | Continúo con Ruta 1 o Ruta 2. |
| **Amarillo** | Me falta Git o Python, pero tengo Cowork, el repo o `casos.json`. | Uso el fallback; llevo la falla documentada a office hours. |
| **Azul** | Me falta Node/NPM, pero mi proyecto no usa JS/TS, n8n local ni MCP. | No hago nada todavía. No es bloqueo. |
| **Rojo** | No tengo acceso al repo ni una ruta de trabajo. | Pido acceso o uso Ruta 3 como andamio compartido. |

## 5. Fallbacks sin detener el aprendizaje

| Falla | Fallback inmediato | Qué se conserva |
|---|---|---|
| Claude Code no instala | Cowork o camino dorado offline | Contrato, casos y criterio |
| Git no está listo | Cowork, ZIP o trabajo en papel; instala Git después | Decisión y evidencia, aunque el commit quede pendiente |
| Python no está listo | Abrir `ejemplo/casos.json` y recorrer casos manualmente | Salidas esperadas y escalamiento |
| Node/NPM no está listo | Continuar si el proyecto no los necesita | Todo el núcleo del curso |
| API/auth no funciona | No pegar claves; trabajar offline | Contrato y punto de integración |
| La herramienta visual no responde | Usar formato local y el caso común | Evals y criterio de diseño |

## 6. Diferencia entre preflight offline y live

El preflight offline comprueba herramientas y archivos locales; no comprueba calidad de modelo, seguridad de producción ni readiness live.

El preflight offline comprueba herramientas y archivos locales; no comprueba calidad de modelo, seguridad de producción ni readiness live.

El preflight offline comprueba herramientas y archivos locales; no comprueba calidad de modelo, seguridad de producción ni readiness live.

El preflight offline comprueba herramientas y archivos locales; no comprueba calidad de modelo, seguridad de producción ni readiness live.

Para la primera medición todavía no necesitas:

- Node.js/NPM si tu ruta no los usa;
- Docker;
- n8n local;
- una base de datos;
- una API key;
- servidores MCP;
- diez casos;
- un loop o sistema multiagente.

Primero: proceso, decisión, contrato, seis casos y salida esperada.

## Referencias

- [Rutas de continuidad de la Sesión 2](ruta-continuidad-s2.md)
- [Rutas de entrada](rutas-de-entrada.md)
- [Instalación y arranque](instalacion.md)
- [Empieza aquí como Aprendedor(a)](../ALUMNO-EMPIEZA-AQUI.md)
- [Setup oficial de Claude Code](https://code.claude.com/docs/en/setup)
