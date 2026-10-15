import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent
COMPARADOR = ROOT / ".claude" / "skills" / "rumbo" / "fixtures" / "comparar.py"
SALIDA_COMPLETA = ROOT / ".claude" / "skills" / "rumbo" / "fixtures" / "salidas" / "F01.md"

spec = importlib.util.spec_from_file_location("comparar_rumbo", COMPARADOR)
comparar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(comparar)


class ComparadorRumboTests(unittest.TestCase):
    def test_salida_completa_pasa_estructura_minima(self):
        texto = SALIDA_COMPLETA.read_text(encoding="utf-8")
        ok, detalle = comparar.check_structure(texto, comparar.frontmatter(texto))
        self.assertTrue(ok, detalle)

    def test_salida_casi_vacia_no_pasa(self):
        texto = "---\nruta: construir\n---\n# Mi rumbo\nUna frase.\n"
        ok, detalle = comparar.check_structure(texto, comparar.frontmatter(texto))
        self.assertFalse(ok)
        self.assertIn("frontmatter incompleto", detalle)
        self.assertIn("falta encabezado", detalle)
        self.assertIn("tabla del mapa", detalle)


if __name__ == "__main__":
    unittest.main()
