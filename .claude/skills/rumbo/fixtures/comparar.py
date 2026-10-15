#!/usr/bin/env python3
"""Compara salidas/FXX.md contra esperado.md sin preguntarle a ningún modelo.
Uso: python3 -I comparar.py [--corrida N]   (desde cualquier directorio)
Imprime una tabla y sale con 0 si cumple el criterio de salida, 1 si no.
"""
import re, sys, pathlib

# GitHub Actions en Windows puede iniciar Python con cp1252; los reportes usan
# indicadores Unicode, así que normalizamos la salida sin depender de la consola.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except AttributeError:
    pass

AQUI = pathlib.Path(__file__).resolve().parent
DIMS = ["objetivos","delegacion","contexto","evaluacion","harness","loop","gobernanza","mejora","producto","economia"]
REQUIRED_FRONTMATTER = ("nombre", "fecha", "ruta", "usuario_final", "estado_actual", "prediccion", "evidencia", "brecha_mayor")
REQUIRED_HEADINGS = ("# Mi rumbo", "## Mapa: predicción contra evidencia", "## Cómo me va a acompañar el agente", "## Qué llevo a S2", "## Notas del assessment")
REQUIRED_NOTES = ("**Hechos**", "**Inferencias**", "**Faltantes**")

def leer_esperado():
    filas = {}
    for linea in (AQUI/"esperado.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*(F\d\d)\s*\|", linea)
        if not m: continue
        celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
        fx, _tipo, _perfil, ruta, niveles, checks = celdas[:6]
        filas[fx] = {"ruta": ruta.strip("`"), "niveles": niveles, "checks": checks}
    return filas

def frontmatter(texto):
    m = re.match(r"^---\n(.*?)\n---", texto, re.S)
    if not m: return {}
    fm = {}
    for linea in m.group(1).splitlines():
        if ":" not in linea: continue
        k, v = linea.split(":", 1)
        fm[k.strip()] = v.strip()
    return fm

def dict_niveles(valor):
    out = {}
    for d in DIMS:
        m = re.search(rf"\b{d}\s*:\s*(\d)", valor or "")
        out[d] = int(m.group(1)) if m else None
    return out

def check_niveles(spec, ev):
    """Devuelve (ok, detalle). spec es la celda 'Niveles esperados'."""
    spec = spec.strip()
    if spec in ("", "—", "-"): return True, "sin nivel fijado"
    if spec.startswith("todas <="):
        tope = int(spec.split("<=")[1])
        malos = [d for d in DIMS if ev[d] is None or ev[d] > tope]
        return (not malos), f"todas <= {tope}" + (f" FALLA en {malos}" if malos else " ok")
    m = re.match(r"(\w+)\s*<=\s*(\d)", spec)
    if m:
        d, tope = m.group(1), int(m.group(2))
        v = ev.get(d)
        ok = v is not None and v <= tope
        return ok, f"{d}={v} (tope {tope})"
    m = re.match(r"(\w+)\s*:\s*(\d)(?:-(\d))?", spec)
    if m:
        d, lo = m.group(1), int(m.group(2)); hi = int(m.group(3)) if m.group(3) else lo
        v = ev.get(d)
        ok = v is not None and (lo-1) <= v <= (hi+1)
        return ok, f"{d}={v} (esperado {lo}-{hi} ±1)"
    return False, f"spec no entendida: {spec}"

def check_extra(spec, fm, cuerpo):
    if spec.strip() in ("", "—", "-"): return True, "—"
    resultados = []; ok = True
    for parte in spec.split(";"):
        p = parte.strip()
        if p.startswith("brecha_mayor:"):
            esperado = p.split(":",1)[1].strip()
            got = fm.get("brecha_mayor","")
            r = got == esperado; ok &= r; resultados.append(f"brecha_mayor={got}{'' if r else ' (esperado '+esperado+')'}")
        elif p.startswith("sin "):
            patron = p[4:].strip()
            r = patron not in cuerpo; ok &= r; resultados.append(f"sin {patron}: {'ok' if r else 'FALLA (aparece)'}")
        elif p.startswith("nota:"):
            clave = p.split(":",1)[1].strip()
            if "elegir" in clave: r = re.search(r"pidi[oó] elegir|se pidi[oó] elegir|eligi[oó]", cuerpo, re.I) is not None
            elif "rotar" in clave: r = re.search(r"rotar", cuerpo, re.I) is not None
            else: r = clave.lower() in cuerpo.lower()
            ok &= bool(r); resultados.append(f"nota '{clave}': {'ok' if r else 'FALTA'}")
    return ok, "; ".join(resultados)

def check_structure(texto, fm):
    """Valida que la salida no sea solo frontmatter o unas frases sueltas."""
    problemas = []
    missing_fm = [key for key in REQUIRED_FRONTMATTER if not fm.get(key, "").strip()]
    if missing_fm:
        problemas.append("frontmatter incompleto: " + ", ".join(missing_fm))
    for campo in ("prediccion", "evidencia"):
        valores = dict_niveles(fm.get(campo, ""))
        if any(valor is None for valor in valores.values()):
            problemas.append(f"{campo} debe contener las diez dimensiones")
    for heading in REQUIRED_HEADINGS:
        if heading not in texto:
            problemas.append(f"falta encabezado: {heading}")
    for note in REQUIRED_NOTES:
        if note not in texto:
            problemas.append(f"falta sección de notas: {note}")

    mapa = re.search(r"^## Mapa: predicción contra evidencia\s*$\n(.*?)(?=^## |\Z)", texto, re.M | re.S)
    dimensiones = []
    if mapa:
        for linea in mapa.group(1).splitlines():
            m = re.match(r"^\|\s*([^|]+?)\s*\|", linea)
            if m and m.group(1).strip() in DIMS:
                dimensiones.append(m.group(1).strip())
        if len(dimensiones) != len(DIMS) or set(dimensiones) != set(DIMS):
            problemas.append(f"la tabla del mapa debe tener exactamente diez dimensiones; tiene {len(dimensiones)}")
    else:
        problemas.append("no se pudo localizar la tabla del mapa")

    rumbo = re.search(r"^# Mi rumbo\s*$\n(.*?)(?=^## |\Z)", texto, re.M | re.S)
    if not rumbo or not rumbo.group(1).strip():
        problemas.append("cuerpo de Mi rumbo vacío")
    llevar = re.search(r"^## Qué llevo a S2\s*$\n(.*?)(?=^## |\Z)", texto, re.M | re.S)
    if not llevar or not llevar.group(1).strip():
        problemas.append("Qué llevo a S2 vacío")
    return not problemas, "; ".join(problemas) if problemas else "estructura mínima OK"

def main():
    esperado = leer_esperado()
    salidas = AQUI/"salidas"
    filas = []; rutas_ok = 0; niveles_ok = 0; con_nivel = 0; extras_ok = True; estructura_ok = True
    for fx in sorted(esperado):
        f = salidas/f"{fx}.md"
        if not f.exists():
            filas.append((fx, "SIN SALIDA", "", "", "", "")); continue
        texto = f.read_text(encoding="utf-8")
        fm = frontmatter(texto)
        ev = dict_niveles(fm.get("evidencia",""))
        ruta = fm.get("ruta","")
        r_ok = ruta == esperado[fx]["ruta"]; rutas_ok += r_ok
        n_ok, n_det = check_niveles(esperado[fx]["niveles"], ev)
        if esperado[fx]["niveles"].strip() not in ("","—","-"):
            con_nivel += 1; niveles_ok += n_ok
        e_ok, e_det = check_extra(esperado[fx]["checks"], fm, texto)
        s_ok, s_det = check_structure(texto, fm)
        extras_ok &= e_ok
        estructura_ok &= s_ok
        filas.append((fx, f"{ruta} {'✅' if r_ok else '❌ esperado '+esperado[fx]['ruta']}", f"{n_det} {'✅' if n_ok else '❌'}", f"{e_det} {'✅' if e_ok else '❌'}", f"{s_det} {'✅' if s_ok else '❌'}", " ".join(f"{d[:3]}={ev[d]}" for d in DIMS)))
    # Búsqueda portable de la llave; no dependemos de grep ni de PowerShell.
    llave_limpia = True
    for archivo in salidas.rglob("*"):
        if archivo.is_file() and "sk-ant-FAKE" in archivo.read_text(encoding="utf-8", errors="replace"):
            llave_limpia = False
            break
    print("| Fixture | Ruta | Niveles | Checks | Estructura | Evidencia |")
    print("|---|---|---|---|---|---|")
    for fila in filas: print("| " + " | ".join(fila) + " |")
    print()
    print(f"Ruta exacta: {rutas_ok}/10 · Niveles ±1: {niveles_ok}/{con_nivel} (dimensiones fijadas) · Checks extra: {'ok' if extras_ok else 'FALLA'} · Estructura: {'ok' if estructura_ok else 'FALLA'} · búsqueda sk-ant-FAKE en salidas/: {'vacío ✅' if llave_limpia else 'ENCONTRADO ❌'}")
    # Criterio explícito: ruta exacta 10/10, todas las dimensiones fijadas (5/5),
    # checks extra, estructura mínima completa y ausencia de una clave ficticia.
    pasa = rutas_ok == 10 and extras_ok and estructura_ok and llave_limpia and niveles_ok == con_nivel
    print("CRITERIO DE SALIDA:", "PASA" if pasa else "NO PASA")
    sys.exit(0 if pasa else 1)

if __name__ == "__main__":
    main()
