# Patrón 02 — Extraer documento → JSON

**Llega un documento (factura, CV, contrato, correo, PDF). Hay que sacarle campos estructurados.**

## Estructura

```
Trigger (Drive / Email / Webhook)
   ↓
Extract From File            ← PDF/docx → texto
   ↓
Validación                   ← ¿hay texto? ¿es el tipo de documento esperado?
   ↓                            Un PDF escaneado sin OCR llega VACÍO. Detéctalo.
Information Extractor        ← texto → JSON con esquema
   ↓
Validación de esquema        ← Auto-fixing Output Parser
   ↓
├─ Válido + confianza alta → escribir (Sheets / CRM / DB)
└─ Inválido o confianza baja → revisión humana
```

## Lo que rompe este patrón

**PDFs escaneados.** Extract From File devuelve vacío o basura. El sistema no truena — sigue adelante con nada y escribe registros en blanco. Valida que haya texto antes de continuar.

**El campo que a veces no está.** Una factura sin RFC, un CV sin fecha. Tu esquema **debe** permitir `null`. Si obligas al modelo a llenar un campo que no existe en el documento, lo inventa. Siempre.

**Números y fechas.** El modelo te va a devolver "1,234.56" o "$1,234.56" o "1234.56" según le parezca. Especifica el formato en el esquema y **valida el tipo** después.

## El esquema

Sé explícito con lo opcional. Esto es lo que evita la alucinación:

```json
{
  "rfc": "string | null — null si no aparece en el documento",
  "total": "number — solo el número, sin símbolo de moneda ni separadores",
  "fecha": "string ISO 8601 (YYYY-MM-DD) | null",
  "conceptos": [{"descripcion": "string", "monto": "number"}],
  "confianza": "alta|media|baja",
  "campos_no_encontrados": ["lista de campos que no aparecen en el documento"]
}
```

Ese último campo, `campos_no_encontrados`, es la diferencia entre un extractor que te avisa y uno que te inventa datos. **Pídeselo explícitamente.**

> **Sobre `confianza`:** la confianza que un modelo verbaliza tiende a sobreestimarse (Xiong et al., ICLR 2024, https://arxiv.org/abs/2306.13063), aunque es una señal utilizable y suele estar mejor calibrada que las probabilidades internas (Tian et al., EMNLP 2023, https://aclanthology.org/2023.emnlp-main.330/).
> **Regla:** antes de enrutar con ella, calíbrala con tu suite: tasa de acierto por etiqueta (`alta`, `media`, `baja`). Si "alta" acierta el 70%, no es alta.

## Costo

Haiku 5.5 para documentos simples y estructurados (ojo: arriba de 100k tokens de prompt se encarece 5×; un PDF largo puede cruzar ese umbral). Sonnet 5.5 si el formato varía mucho.

**Si procesas documentos en lote y no es urgente: Batch API, 50% menos.** Este patrón es el caso de uso canónico de batch, y casi nadie lo aprovecha.
