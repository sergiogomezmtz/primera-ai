#!/usr/bin/env python3
"""Pruebas del camino dorado: sin red, sin credenciales y sin dependencias externas.

Uso desde la raíz del repo (en Windows, cambia python3 por py):
  python3 ejemplo/test_camino_dorado.py

Qué fijan:
  - las tasas que documentan las guías: v0 4/6 y 7/10; v1 6/6 y 10/10;
  - la salida esperada de E1 a E10 y el reparto del núcleo (4/1/1) y la extendida (5/3/2);
  - cada etapa: if determinista, IA solo si ninguna regla aplica, validación y humano;
  - la ruta otro: el modelo puede proponerla, la salida final nunca la lleva;
  - el modo live con respuestas falsas de la API: JSON roto, ruta fuera del contrato,
    campo extra, confianza baja, falla de red y ausencia de clave.

Ninguna prueba sale a internet: urlopen se sustituye para todo el módulo y una
prueba que intente usar la red falla. La clave de las pruebas live es un texto
de relleno que nunca se envía a ningún lado.
"""

from __future__ import annotations

import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock
from urllib.error import URLError

sys.dont_write_bytecode = True  # no deja __pycache__ dentro del repo
sys.path.insert(0, str(Path(__file__).resolve().parent))

import camino_dorado as cd  # noqa: E402

CLAVE_DE_RELLENO = "clave-de-relleno-no-es-una-credencial"

# La verdad de los casos. Si alguien edita casos.json, esta prueba lo detecta.
SALIDA_ESPERADA = {
    "E1": ("facturacion", False),
    "E2": ("ventas", False),
    "E3": ("soporte", False),
    "E4": ("ventas", False),
    "E5": ("escalar_humano", True),
    "E6": ("escalar_humano", True),
    "E7": ("escalar_humano", True),
    "E8": ("facturacion", False),
    "E9": ("escalar_humano", True),
    "E10": ("ventas", False),
}


# ---------------------------------------------------------------------------
# Herramientas de prueba
# ---------------------------------------------------------------------------

def _red_prohibida(*args, **kwargs):
    raise AssertionError("una prueba intentó usar la red")


_guardia_de_red = mock.patch.object(cd, "urlopen", side_effect=_red_prohibida)


def setUpModule():
    _guardia_de_red.start()


def tearDownModule():
    _guardia_de_red.stop()


def correr_main(*argumentos: str) -> tuple[int, str, str]:
    """Corre el script como lo haría una persona y captura lo que imprime."""
    salida, errores = io.StringIO(), io.StringIO()
    with mock.patch.object(sys, "argv", ["camino_dorado.py", *argumentos]):
        with contextlib.redirect_stdout(salida), contextlib.redirect_stderr(errores):
            codigo = cd.main()
    return codigo, salida.getvalue(), errores.getvalue()


def casos_por_id() -> dict[str, dict]:
    return {caso["id"]: caso for caso in cd.load_cases("extendida")}


def ids_que_fallan(version: str, suite: str) -> list[str]:
    fallan = []
    for caso in cd.load_cases(suite):
        final, _errores, _traza = cd.run_case(caso, "offline", version, "sin-modelo")
        esperado = caso["salida_esperada"]
        if (final["ruta"], final["escalar"]) != (esperado["ruta"], esperado["escalar"]):
            fallan.append(caso["id"])
    return fallan


class _RespuestaFalsa:
    def __init__(self, cuerpo: bytes):
        self._cuerpo = cuerpo

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def read(self) -> bytes:
        return self._cuerpo


def api_falsa(texto_del_modelo: str, solicitudes: list, tiempos: list | None = None):
    """Ocupa el lugar de urlopen: guarda la solicitud y devuelve lo que diría la API."""
    cuerpo = json.dumps({"content": [{"type": "text", "text": texto_del_modelo}]}).encode("utf-8")

    def responder(request, timeout=None):
        solicitudes.append(request)
        if tiempos is not None:
            tiempos.append(timeout)
        return _RespuestaFalsa(cuerpo)

    return responder


def salida(ruta="soporte", confianza="alta", razon="Prueba.", fuente="ia", escalar=False, **extra) -> dict:
    return dict(ruta=ruta, confianza=confianza, razon=razon, fuente=fuente, escalar=escalar, **extra)


# ---------------------------------------------------------------------------
# 1. Las tasas que documentan README y guías
# ---------------------------------------------------------------------------

class TasasDocumentadas(unittest.TestCase):
    def test_v0_nucleo_4_de_6_sale_con_1(self):
        codigo, out, _ = correr_main("--modo", "offline", "--version", "v0")
        self.assertEqual(codigo, 1)
        self.assertIn("TASA: 4/6", out)
        self.assertIn("núcleo válido", out)

    def test_v0_extendida_7_de_10_sale_con_1(self):
        codigo, out, _ = correr_main("--modo", "offline", "--version", "v0", "--suite", "extendida")
        self.assertEqual(codigo, 1)
        self.assertIn("TASA: 7/10", out)
        self.assertIn("suite extendida válida", out)

    def test_v1_nucleo_6_de_6_sale_con_0(self):
        codigo, out, _ = correr_main("--modo", "offline", "--version", "v1")
        self.assertEqual(codigo, 0)
        self.assertIn("TASA: 6/6", out)

    def test_v1_extendida_10_de_10_sale_con_0(self):
        codigo, out, _ = correr_main("--modo", "offline", "--version", "v1", "--suite", "extendida")
        self.assertEqual(codigo, 0)
        self.assertIn("TASA: 10/10", out)

    def test_alias_core_y_all(self):
        self.assertIn("TASA: 6/6", correr_main("--suite", "core")[1])
        self.assertIn("TASA: 10/10", correr_main("--suite", "all")[1])

    def test_v0_falla_solo_en_limite_y_adversariales(self):
        self.assertEqual(ids_que_fallan("v0", "nucleo"), ["E5", "E6"])
        self.assertEqual(ids_que_fallan("v0", "extendida"), ["E5", "E6", "E7"])
        self.assertEqual(ids_que_fallan("v1", "extendida"), [])

    def test_la_verificacion_no_le_pregunta_al_modelo(self):
        _, out, _ = correr_main()
        self.assertIn("sin preguntarle al modelo", out)
        self.assertIn("secuencia: entrada -> if determinista", out)


# ---------------------------------------------------------------------------
# 2. Los casos: la verdad se revisa antes de medir
# ---------------------------------------------------------------------------

class Casos(unittest.TestCase):
    def test_salida_esperada_de_e1_a_e10_no_cambia(self):
        with cd.CASES_PATH.open(encoding="utf-8") as archivo:
            casos = json.load(archivo)
        reales = {c["id"]: (c["salida_esperada"]["ruta"], c["salida_esperada"]["escalar"]) for c in casos}
        self.assertEqual(reales, SALIDA_ESPERADA)

    def test_casos_json_pasa_su_propia_revision(self):
        with cd.CASES_PATH.open(encoding="utf-8") as archivo:
            self.assertEqual(cd.check_dataset(json.load(archivo)), [])

    def test_nucleo_son_seis_casos_4_1_1_y_es_valido(self):
        nucleo = cd.load_cases("nucleo")
        self.assertEqual([c["id"] for c in nucleo], ["E1", "E2", "E3", "E4", "E5", "E6"])
        self.assertEqual(
            cd.describe_reparto(nucleo),
            "núcleo válido (4 típicos, 1 límite, 1 adversarial)",
        )

    def test_extendida_son_diez_casos_5_3_2(self):
        self.assertEqual(
            cd.describe_reparto(cd.load_cases("extendida")),
            "suite extendida válida (5 típicos, 3 límite, 2 adversariales)",
        )

    def test_reparto_incompleto_se_marca_parcial(self):
        sin_adversarial = cd.load_cases("nucleo")[:5]
        reparto = cd.describe_reparto(sin_adversarial)
        self.assertTrue(reparto.startswith("parcial (4 típicos, 1 límite, 0 adversariales)"))
        self.assertIn("el núcleo pide 4 típicos, 1 límite y 1 adversarial", reparto)

    def test_revision_detecta_casos_mal_escritos(self):
        base = {"suite": "nucleo", "tipo": "tipico", "texto": "Hola."}
        malos = [
            dict(base, id="X1", salida_esperada={"ruta": "ventas", "escalar": False}),
            dict(base, id="X1", salida_esperada={"ruta": "ventas", "escalar": False}),
            dict(base, id="X2", tipo="raro", salida_esperada={"ruta": "ventas", "escalar": False}),
            dict(base, id="X3", salida_esperada={"ruta": "otro", "escalar": True}),
            dict(base, id="X4", salida_esperada={"ruta": "escalar_humano", "escalar": False}),
            dict(base, id="X5"),
            dict(base, id="X6", tipo=[], salida_esperada={"ruta": "ventas", "escalar": False}),
            dict(base, id="X7", suite=[], salida_esperada={"ruta": "ventas", "escalar": False}),
            dict(base, id="X8", salida_esperada={"ruta": [], "escalar": False}),
        ]
        problemas = " | ".join(cd.check_dataset(malos))
        self.assertIn("X1: id repetido", problemas)
        self.assertIn("X2: tipo debe ser", problemas)
        self.assertIn("X3: la ruta esperada es la salida final del sistema", problemas)
        self.assertIn("'otro' solo es una ruta intermedia que puede proponer el modelo", problemas)
        self.assertIn("X4: escalar_humano y escalar=true van juntos", problemas)
        self.assertIn("X5: falta salida_esperada", problemas)
        self.assertIn("X6: tipo debe ser", problemas)
        self.assertIn("X7: suite debe ser", problemas)
        self.assertIn("X8: la ruta esperada es la salida final del sistema", problemas)

    def test_casos_invalidos_no_producen_una_tasa(self):
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "casos.json"
            ruta.write_text(json.dumps([{"id": "X1", "tipo": "raro"}]), encoding="utf-8")
            with mock.patch.object(cd, "CASES_PATH", ruta):
                codigo, out, err = correr_main()
        self.assertEqual(codigo, 2)
        self.assertNotIn("TASA", out)
        self.assertIn("casos.json no es válido", err)


# ---------------------------------------------------------------------------
# 3. Las cinco etapas
# ---------------------------------------------------------------------------

class Etapas(unittest.TestCase):
    def test_remitente_conocido_lo_resuelve_un_if_sin_ia(self):
        with mock.patch.object(cd, "offline_llm", side_effect=AssertionError("no debía llamar a la IA")):
            final, errores, traza = cd.run_case(casos_por_id()["E1"], "offline", "v1", "sin-modelo")
        self.assertEqual((final["ruta"], final["fuente"], final["escalar"]), ("facturacion", "if", False))
        self.assertEqual(errores, [])
        self.assertIn("if: remitente conocido -> facturacion", traza)

    def test_regla_de_seguridad_va_antes_que_el_remitente(self):
        e7 = casos_por_id()["E7"]
        final, _, traza = cd.run_case(e7, "offline", "v1", "sin-modelo")
        self.assertEqual((final["ruta"], final["fuente"], final["escalar"]), ("escalar_humano", "if", True))
        self.assertIn("if: regla de seguridad -> escalar_humano", traza)
        # v0 no tiene la regla: el remitente confiable se vuelve puerta trasera.
        final_v0, _, _ = cd.run_case(e7, "offline", "v0", "sin-modelo")
        self.assertEqual(final_v0["ruta"], "facturacion")

    def test_la_ia_solo_entra_si_ninguna_regla_aplica(self):
        final, _, traza = cd.run_case(casos_por_id()["E3"], "offline", "v1", "sin-modelo")
        self.assertEqual((final["ruta"], final["fuente"]), ("soporte", "ia"))
        self.assertEqual(traza[1], "if: ninguna regla aplica")
        self.assertTrue(traza[2].startswith("IA (simulada): soporte"))
        self.assertEqual(traza[3], "validación del contrato: OK")
        self.assertEqual(traza[4], "humano: no hace falta")

    def test_entrada_vacia_escala_sin_llamar_a_la_ia(self):
        with mock.patch.object(cd, "offline_llm", side_effect=AssertionError("no debía llamar a la IA")):
            final, _, traza = cd.run_case({"id": "V", "texto": "   "}, "offline", "v1", "sin-modelo")
        self.assertEqual((final["ruta"], final["fuente"], final["escalar"]), ("escalar_humano", "harness", True))
        self.assertEqual(traza[0], "entrada: vacía o no es texto")

    def test_sin_categoria_y_confianza_baja_decide_una_persona(self):
        # IA: ruta=otro, confianza=baja -> validación de la salida intermedia
        # -> escalamiento del harness -> salida final: escalar_humano
        final, errores, traza = cd.run_case(casos_por_id()["E9"], "offline", "v1", "sin-modelo")
        self.assertEqual(traza[2], "IA (simulada): otro / confianza baja")
        self.assertEqual(errores, [])
        self.assertEqual(traza[3], "validación del contrato: OK")
        self.assertIn("sin categoría", traza[-1])
        self.assertIn("confianza baja", traza[-1])
        self.assertEqual((final["ruta"], final["escalar"]), ("escalar_humano", True))

    def test_ninguna_salida_final_es_otro(self):
        self.assertIn("otro", cd.MODEL_ROUTES)
        self.assertEqual(cd.FINAL_ROUTES, cd.MODEL_ROUTES - {"otro"})
        for version in ("v0", "v1"):
            for caso in cd.load_cases("extendida"):
                with self.subTest(version=version, caso=caso["id"]):
                    final, _, _ = cd.run_case(caso, "offline", version, "sin-modelo")
                    self.assertIn(final["ruta"], cd.FINAL_ROUTES)
                    self.assertEqual(final["ruta"] == "escalar_humano", final["escalar"])

    def test_humano_no_interviene_si_no_hace_falta(self):
        entrada = salida(ruta="ventas")
        final, paso = cd.stage_human(entrada)
        self.assertEqual(final, entrada)
        self.assertEqual(paso, "humano: no hace falta")


# ---------------------------------------------------------------------------
# 4. El contrato: salida estructurada validada sin preguntarle al modelo
# ---------------------------------------------------------------------------

class Contrato(unittest.TestCase):
    def test_salida_valida_no_tiene_errores(self):
        self.assertEqual(cd.validate_output(salida()), [])

    def test_cada_defecto_se_detecta(self):
        sin_ruta = salida()
        del sin_ruta["ruta"]
        defectos = {
            "faltan campos": sin_ruta,
            "campos no previstos": salida(monto=100),
            "ruta inválida": salida(ruta="legal"),
            "confianza inválida": salida(confianza="0.9"),
            "razon vacía": salida(razon="  "),
            "fuente inválida": salida(fuente="humano"),
            "escalar debe ser booleano": salida(escalar="no"),
            "escalar debe ser true cuando la ruta es escalar_humano": salida(ruta="escalar_humano", escalar=False),
            "la salida no es un objeto JSON": ["soporte"],
        }
        for esperado, candidata in defectos.items():
            with self.subTest(defecto=esperado):
                self.assertTrue(
                    any(esperado in error for error in cd.validate_output(candidata)),
                    f"no se detectó: {esperado}",
                )
        for candidata, esperado in (
            (salida(ruta=[]), "ruta inválida"),
            (salida(confianza=[]), "confianza inválida"),
            (salida(fuente=[]), "fuente inválida"),
        ):
            with self.subTest(tipo_invalido=esperado):
                self.assertTrue(any(esperado in error for error in cd.validate_output(candidata)))

    def test_salida_invalida_no_pasa_al_siguiente_paso(self):
        with mock.patch.object(cd, "offline_llm", return_value=salida(ruta="legal")):
            final, errores, traza = cd.run_case(casos_por_id()["E3"], "offline", "v1", "sin-modelo")
        self.assertEqual((final["ruta"], final["fuente"], final["escalar"]), ("escalar_humano", "harness", True))
        self.assertIn("ruta inválida", errores)
        self.assertTrue(any(paso.startswith("validación del contrato: FALLA") for paso in traza))


# ---------------------------------------------------------------------------
# 5. Modo live sin red: la API se sustituye por respuestas falsas
# ---------------------------------------------------------------------------

class ModoLiveSinRed(unittest.TestCase):
    CASO = {"id": "L1", "remitente": "cliente@example.test", "texto": "No puedo entrar a mi cuenta."}

    def setUp(self):
        entorno = mock.patch.dict(os.environ, {"ANTHROPIC_API_KEY": CLAVE_DE_RELLENO})
        entorno.start()
        self.addCleanup(entorno.stop)

    def correr_live(self, texto_del_modelo: str):
        solicitudes: list = []
        with mock.patch.object(cd, "urlopen", side_effect=api_falsa(texto_del_modelo, solicitudes)):
            resultado = cd.run_case(self.CASO, "live", "v1", "modelo-de-prueba")
        return resultado, solicitudes

    def test_el_timeout_restante_se_pasa_al_transporte(self):
        solicitudes, tiempos = [], []
        with mock.patch.object(cd, "urlopen", side_effect=api_falsa(json.dumps(salida()), solicitudes, tiempos)):
            final, errores, _ = cd.run_case(self.CASO, "live", "v1", "modelo-de-prueba", request_timeout=2.5)
        self.assertEqual(final["ruta"], "soporte")
        self.assertEqual(errores, [])
        self.assertEqual(tiempos, [2.5])

    def test_ninguna_prueba_sale_a_internet(self):
        with self.assertRaises(AssertionError):
            cd.urlopen("https://api.anthropic.com/v1/messages")

    def test_respuesta_valida_pasa_y_se_pidio_salida_estructurada(self):
        (final, errores, traza), solicitudes = self.correr_live(json.dumps(salida()))
        self.assertEqual((final["ruta"], final["fuente"], final["escalar"]), ("soporte", "ia", False))
        self.assertEqual(errores, [])
        self.assertIn("IA: soporte / confianza alta", traza)
        self.assertEqual(len(solicitudes), 1)
        solicitud = solicitudes[0]
        self.assertEqual(solicitud.full_url, "https://api.anthropic.com/v1/messages")
        cuerpo = json.loads(solicitud.data.decode("utf-8"))
        self.assertEqual(cuerpo["model"], "modelo-de-prueba")
        formato = cuerpo["output_config"]["format"]
        self.assertEqual(formato["type"], "json_schema")
        self.assertFalse(formato["schema"]["additionalProperties"])
        self.assertEqual(set(formato["schema"]["required"]), cd.REQUIRED_FIELDS)
        self.assertEqual(formato["schema"]["properties"]["fuente"]["enum"], ["ia"])
        self.assertIn("DATA\nNo puedo entrar a mi cuenta.\nEND DATA", cuerpo["messages"][0]["content"])

    def test_json_roto_escala_con_fuente_harness(self):
        (final, errores, traza), _ = self.correr_live("esto no es JSON")
        self.assertEqual((final["ruta"], final["fuente"], final["escalar"]), ("escalar_humano", "harness", True))
        self.assertIn("no es JSON parseable", errores[0])
        self.assertIn("validación: sin salida que validar", traza)

    def test_bloque_de_contenido_no_objeto_escala_sin_traceback(self):
        cuerpo = json.dumps({"content": [7]}).encode("utf-8")
        with mock.patch.object(cd, "urlopen", return_value=_RespuestaFalsa(cuerpo)):
            final, errores, _ = cd.run_case(self.CASO, "live", "v1", "modelo-de-prueba")
        self.assertEqual((final["ruta"], final["fuente"], final["escalar"]), ("escalar_humano", "harness", True))
        self.assertIn("no es JSON parseable", errores[0])

    def test_ruta_fuera_del_contrato_escala(self):
        (final, errores, _), _ = self.correr_live(json.dumps(salida(ruta="legal")))
        self.assertEqual((final["ruta"], final["fuente"]), ("escalar_humano", "harness"))
        self.assertIn("ruta inválida", errores)

    def test_campo_extra_escala(self):
        (final, errores, _), _ = self.correr_live(json.dumps(salida(monto=100)))
        self.assertEqual((final["ruta"], final["fuente"]), ("escalar_humano", "harness"))
        self.assertTrue(any("campos no previstos" in error for error in errores))

    def test_confianza_baja_escala_aunque_el_modelo_no_lo_pida(self):
        (final, errores, traza), _ = self.correr_live(json.dumps(salida(ruta="ventas", confianza="baja")))
        self.assertEqual(errores, [])
        self.assertEqual((final["ruta"], final["fuente"], final["escalar"]), ("escalar_humano", "ia", True))
        self.assertIn("confianza baja", traza[-1])

    def test_falla_de_red_escala_con_fuente_harness(self):
        with mock.patch.object(cd, "urlopen", side_effect=URLError("sin conexión")):
            final, errores, _ = cd.run_case(self.CASO, "live", "v1", "modelo-de-prueba")
        self.assertEqual((final["ruta"], final["fuente"], final["escalar"]), ("escalar_humano", "harness", True))
        self.assertIn("falló la llamada a Claude", errores[0])

    def test_sin_clave_no_hay_medicion(self):
        with mock.patch.dict(os.environ):
            os.environ.pop("ANTHROPIC_API_KEY", None)
            with mock.patch.object(cd, "urlopen") as urlopen_espia:
                codigo, out, err = correr_main("--modo", "live")
        self.assertEqual(codigo, 2)
        self.assertNotIn("TASA", out)
        self.assertIn("Una falla de autenticación no es una medición", err)
        urlopen_espia.assert_not_called()


class MedicionEstrica(unittest.TestCase):
    def test_presupuesto_no_finito_no_hace_medicion(self):
        codigo, out, err = correr_main("--max-seconds", "nan")
        self.assertEqual(codigo, 2)
        self.assertNotIn("TASA:", out)
        self.assertIn("finito y positivo", err)

    def test_caso_que_termina_fuera_de_presupuesto_bloquea_la_tasa(self):
        relojes = [0.0, 0.0, 1.0] + [1.0] * 20
        with mock.patch.object(cd, "run_case", return_value=(salida(), [], [])):
            with mock.patch.object(cd.time, "monotonic", side_effect=relojes):
                codigo, out, err = correr_main("--max-seconds", "0.5")
        self.assertEqual(codigo, 2)
        self.assertNotIn("TASA:", out)
        self.assertIn("MEDICION BLOQUEADA", err)

    def test_error_de_api_bloquea_la_tasa_en_main(self):
        with mock.patch.dict(os.environ, {"ANTHROPIC_API_KEY": CLAVE_DE_RELLENO}):
            with mock.patch.object(cd, "urlopen", side_effect=URLError("API caída")):
                codigo, out, err = correr_main("--modo", "live", "--confirm-live")
        self.assertEqual(codigo, 2)
        self.assertNotIn("TASA:", out)
        self.assertIn("MEDICION BLOQUEADA", err)

    def test_modelo_live_no_permitido_no_hace_llamada(self):
        with mock.patch.dict(os.environ, {"ANTHROPIC_API_KEY": CLAVE_DE_RELLENO}, clear=False):
            with mock.patch.object(cd, "urlopen") as urlopen_espia:
                codigo, out, err = correr_main("--modo", "live", "--confirm-live", "--model", "modelo-no-permitido")
        self.assertEqual(codigo, 2)
        self.assertNotIn("TASA:", out)
        self.assertIn("modelo no permitido", err)
        urlopen_espia.assert_not_called()

    def test_dataset_rechaza_id_y_remitente_invalidos(self):
        caso = {"id": "", "suite": "nucleo", "tipo": "tipico", "remitente": [], "texto": "Hola", "salida_esperada": {"ruta": "ventas", "escalar": False}}
        problemas = " | ".join(cd.check_dataset([caso]))
        self.assertIn("id no vacío", problemas)
        self.assertIn("remitente debe ser", problemas)

    def test_dataset_rechaza_suite_incompleta_al_cargar(self):
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "casos.json"
            casos = [{"id": "X", "suite": "nucleo", "tipo": "tipico", "remitente": "x@example.test", "texto": "Hola", "salida_esperada": {"ruta": "ventas", "escalar": False}}]
            ruta.write_text(json.dumps(casos), encoding="utf-8")
            with mock.patch.object(cd, "CASES_PATH", ruta):
                with self.assertRaises(ValueError) as ctx: cd.load_cases("nucleo")
        self.assertIn("suite nucleo inválida", str(ctx.exception))


if __name__ == "__main__":
    unittest.main(verbosity=2)
