# Runbook · extracción de facturas · Despacho ACME (FICTICIO)

## Definición de terminado
El archivo `salida/AAAA-MM-DD.csv` tiene una fila por factura recibida ese día, con `rfc`, `total`, `fecha`, y el checker (`checker.py`) reporta 0 discrepancias contra `padron.csv`.

## Pasos clasificados
| Paso | Tipo | Razón |
|---|---|---|
| Trigger de carpeta | herramienta | Watcher de Drive |
| ¿El PDF tiene texto? | if | Longitud del texto > 50 caracteres |
| Extraer rfc/total/fecha | IA | 40 formatos distintos de proveedor |
| Validar RFC contra padrón | if | Lista cerrada |
| Total > 50,000 | humano | Umbral de riesgo acordado con el cliente |

## Diagnóstico cuando inventa un dato (de abajo hacia arriba)
1. Harness: ¿se cayó a media corrida? → log de ejecuciones de n8n.
2. Framework: ¿un PDF escaneado pasó el IF de texto? → ver el valor del campo en la ejecución.
3. Contexto: ¿el texto llegó vacío o truncado? → campo `texto` en el nodo extractor.
4. Modelo: solo si lo anterior está limpio.

## Paradas del reintento
- Éxito: el JSON pasa el checker.
- Presupuesto: máximo 2 vueltas o 0.10 USD por documento.
- No-progreso: el validador reporta el mismo error dos veces.
- Escalamiento: total > 50,000 → el contador aprueba por correo.

## Operación
Lo corre el contador del despacho. Si falla, manda el log por correo al consultor.
