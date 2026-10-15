---
name: integracion-apis
description: Conectar y depurar APIs. Úsala cuando haya que autenticar contra un servicio, manejar rate limits, entender un payload, o cuando una integración falle. También cuando se elija entre llamar una API directo o usar un nodo/conector.
---

# Integración de APIs

## Auth primero, siempre

**La autenticación es donde se quema el 70% del tiempo de integración.** Resuélvela antes de escribir un gramo de lógica.

Por cada servicio, deja registrado: tipo de auth (API key / OAuth2 / service account / JWT), dónde vive la credencial, qué scopes, cuándo expira, cómo se renueva.

**Nunca credenciales en el repo ni en un nodo Code.** Variables de entorno o el gestor de credenciales de la plataforma. Si ves una llave hardcodeada, detente y arréglalo antes de continuar.

## Prueba cada API sola antes de encadenarla

Un `curl`, un nodo suelto, lo que sea. Confirma que responde lo que crees que responde.

**Las APIs mienten en su documentación** con más frecuencia de la que a nadie le gustaría. Campos que no existen, tipos distintos, paginación no documentada.

**Guarda un payload real de ejemplo.** Lo vas a necesitar para los evals y para depurar sin volver a llamar al servicio. A `proyectos/<nombre>/payloads/`.

## Los límites, antes de necesitarlos

Rate limits, costo por llamada, tamaño máximo de payload, timeouts, paginación. Lo que hoy no duele, en producción tumba el sistema.

Anótalo aunque hoy no lo uses.

## Reintentos que no empeoran las cosas

- Backoff exponencial, tope de 3 intentos.
- Si la API te da un `retry-after` (la de Claude lo hace en 429), **úsalo**. No inventes.
- **No reintentes errores 4xx.** Un 400 o un 401 no se arregla insistiendo; se arregla arreglándolo. Reintentar un 4xx en loop es cómo se generan facturas absurdas.
- Reintenta 429 y 5xx.

## Valida la respuesta, no el status code

Un 200 con basura adentro es la falla más traicionera. Valida la estructura de lo que llegó antes de pasárselo al siguiente paso.

## ¿Nodo, MCP o HTTP crudo?

- **¿Hay nodo nativo?** Úsalo. Ya resolvió auth, paginación y reintentos.
- **¿Vas a conectar una API dentro de tu propio workflow?** HTTP Request. Simple, depurable.
- **¿Quieres que un agente externo (Claude Desktop, Cursor) llame a tus sistemas?** Ahí sí MCP.

Montar un servidor MCP para conectar una API dentro de tu propio flujo es sobreingeniería. Ver `referencias/mcp.md`.
