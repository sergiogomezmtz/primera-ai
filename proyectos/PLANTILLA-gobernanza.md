# Gobernanza — <nombre del proyecto>

> Se llena después de correr `/auditar`. Cada renglón cierra un hueco que la auditoría encontró.
> Regla: el límite duro va en el **entorno**, no en el prompt. El modelo nunca es la última línea.

## 1. Permisos mínimos

El agente recibe **el mínimo que le permite hacer su trabajo, ni uno más**. Solo-lectura donde se pueda.

| Recurso / credencial | Acceso concedido | ¿Solo-lectura? | Por qué es el mínimo |
|---|---|---|---|
| | | | |
| | | | |

**Regla de la allowlist:** cada dominio/API que permites es un *grant de capacidad*, no un destino. Anota qué puede hacer el agente con cada uno.

| Dominio / API que puede llamar | Qué capacidad concede (todo lo alcanzable ahí) |
|---|---|
| | |

## 2. Tope de gasto

Un loop con API de pago es una factura sin techo hasta que le pones un número.

| Límite | Número | Dónde se enforce | Qué pasa al tocarlo |
|---|---|---|---|
| Gasto ($ / mes) | | consola del proveedor | |
| Tokens / corrida | | | |
| Iteraciones / corrida | | loop.md (parada de presupuesto) | |

> Verifica el número real y dónde se configura **en la consola**, no de memoria.

## 3. Human-in-the-loop — solo lo irreversible

La aprobación en cada paso no escala (fatiga: ~93% se aprueba sin mirar). Reserva el humano para lo que no se puede deshacer. *(Extiende la tabla de escalamiento de `loop.md`.)*

| Acción irreversible | ¿Requiere aprobación? | Quién aprueba | Por qué canal | Qué ve antes de aprobar |
|---|---|---|---|---|
| Mandar correo / mensaje | | | | |
| Cobrar / mover dinero | | | | |
| Borrar / sobreescribir | | | | |
| Publicar / hacer público | | | | |

## 4. Error Trigger + observabilidad

Si no te enteras de que falló, la falla es invisible. Toda automatización autónoma necesita un disparador de error que avise.

| Qué falla | Cómo me entero | Canal | Umbral de alerta |
|---|---|---|---|
| La API cae / da timeout | | | |
| El LLM se sale del esquema | | | |
| Presupuesto tocado | | | |
| No-progreso (N intentos sin cambio) | | | |

## 5. Trazabilidad — qué se registra por corrida

| Campo | Se registra | Dónde queda |
|---|---|---|
| Entrada / caso | | |
| Decisión del modelo + confianza | | |
| Acción tomada (o escalada) | | |
| Costo (tokens / $) | | |
| Resultado verificado | | |

## Hueco → cierre (de la auditoría)

| Hallazgo de `/auditar` | Sección que lo cierra | Estado |
|---|---|---|
| | | |
| | | |
