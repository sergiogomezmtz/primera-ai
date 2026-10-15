# Prompts · calificador de leads (FICTICIO)

## v0 (2026-09-10)
Califica este lead del 1 al 5 según qué tan probable es que compre. Devuelve JSON {score, razon}.

## v1 (2026-09-24) — agrega ICP
Califica este lead del 1 al 5. Cliente ideal: empresa de 20 a 200 empleados, sector servicios, México, con un responsable de operaciones. 5 = cumple todo; 1 = no cumple nada. Devuelve JSON {score, razon, confianza}.

Fuera del contexto: histórico de leads (no sé cómo usarlo todavía).
