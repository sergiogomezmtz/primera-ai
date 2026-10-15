# Patrón 04 — RAG sobre documentos internos

**Responder preguntas usando documentos propios: políticas, manuales, contratos, base de conocimiento.**

## Antes de construirlo: ¿de verdad necesitas RAG?

Pregunta incómoda. Los modelos actuales tienen **contexto de 1M tokens sin sobreprecio** (Fable 5.1, Opus 5.5, Sonnet 5.5 y toda la línea 4.6+). La excepción es Haiku 5.5: arriba de 100k tokens de prompt cobra 5× más, así que para meter un corpus entero usa Sonnet 5.5.

Si tu corpus completo cabe en el contexto —un manual de 200 páginas son unos 150k tokens— **métele el documento entero y cachéalo**. Cache hit = 10% del precio del input, y no cuenta para el rate limit.

Eso te evita: vector DB, embeddings, chunking, retriever, y la clase entera de bugs donde el chunk correcto no se recupera.

**RAG solo cuando el corpus no cabe.** Miles de documentos, o un corpus que crece.

Esta es la recomendación menos popular y la más correcta.

## Si sí necesitas RAG

```
INGESTA (una vez, y cada que cambie el corpus)
Documentos → Text Splitter → Embeddings → Vector Store

CONSULTA
Pregunta
   ↓
Retriever (top-k)              ← recupera los chunks relevantes
   ↓
Reranker                       ← opcional pero cambia mucho la calidad
   ↓
LLM con los chunks + la pregunta
   ↓
Respuesta CON CITAS            ← obligatorio
```

## Lo que decide si funciona

**El chunking.** Es donde se gana o se pierde, y es lo que menos atención recibe. Un chunk que corta una tabla a la mitad, o que separa una cláusula de su encabezado, envenena el retriever. Empieza con Recursive Character Text Splitter, chunks de ~500-1000 tokens con solapamiento. Y **mira los chunks resultantes con tus ojos** antes de indexar nada.

**Citas obligatorias.** El modelo debe decir de qué documento y sección sacó cada afirmación. Sin citas, no puedes verificar y no puedes confiar. Pide un campo `fuentes` en el JSON de salida.

**"No sé" como respuesta válida.** Si el retriever no trajo nada relevante, el modelo **debe** decir que no encontró la información. Escríbelo en el prompt, explícito, y prueba ese caso. Sin esto, RAG alucina con las fuentes puestas — que es peor que alucinar sin ellas, porque parece confiable.

## Vector stores

Prototipo: **Simple Vector Store** de n8n (en memoria — se borra al reiniciar, no lo lleves a producción).

Producción: **PGVector** si ya tienen Postgres (la respuesta correcta la mayoría de las veces), **Qdrant** o **Supabase** si no.

## Evals para RAG

Además de los evals normales: para cada pregunta de prueba, anota **cuál es el chunk que debería recuperarse**. Mide el retrieval por separado de la generación.

Si la respuesta está mal, necesitas saber si fue porque no se recuperó lo correcto o porque el modelo lo usó mal. Son problemas distintos con arreglos distintos.
