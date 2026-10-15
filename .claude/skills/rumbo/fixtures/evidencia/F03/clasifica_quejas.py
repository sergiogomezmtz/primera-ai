# FICTICIO. Script que clasifica quejas con Claude. Se corre a mano cada mañana.
import csv, os, json
import anthropic

PROMPT = """Clasificas quejas de clientes en UNA categoría: entrega, producto, cobro, atencion, otro.
Devuelve JSON: {"categoria": "...", "confianza": "alta|media|baja", "razonamiento": "una frase"}"""

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

def clasificar(texto):
    r = client.messages.create(model="claude-haiku-5-5", max_tokens=200,
        messages=[{"role": "user", "content": PROMPT + "\n\nQUEJA:\n" + texto}])
    return json.loads(r.content[0].text)

if __name__ == "__main__":
    vistos = set()
    for fila in csv.DictReader(open("quejas_hoy.csv")):
        if fila["folio"] in vistos: continue
        vistos.add(fila["folio"])
        out = clasificar(fila["texto"])
        destino = "revision.csv" if out["confianza"] == "baja" else "clasificadas.csv"
        with open(destino, "a") as f: f.write(f'{fila["folio"]},{out["categoria"]},{out["confianza"]}\n')
