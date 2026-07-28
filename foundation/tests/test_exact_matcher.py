import unittest
from pathlib import Path

from foundation.media.document import Document
from foundation.matcher.exact_matcher import ExactMatcher


class TestExactMatcher(unittest.TestCase):

    def test_exact_matcher(self):

        matcher = ExactMatcher(
            {
                "supino reto barra",
                "agachamento",
                "crucifixo",
            }
        )

        document = Document(
            name="Supino",
            category="Peitoral",
            group="Peitoral",
            extension=".gif",
            relative_path=Path("Peitoral/Supino.gif"),
            absolute_path=Path("/tmp/Peitoral/Supino.gif"),
            sha256="",
            normalized_name="supino reto barra",
        )

        result = matcher.match(document)

        self.assertTrue(result.matched)
        self.assertEqual(result.score, 1.0)
        self.assertEqual(result.candidate, "supino reto barra")
        self.assertEqual(result.document, document)





    def test_exact_matcher_not_found(self):

        matcher = ExactMatcher(
            {
                "supino reto barra",
                "crucifixo",
            }
        )

        document = Document(
            name="Desenvolvimento Militar",
            category="Ombros",
            group="Ombros",
            extension=".gif",
            relative_path=Path("Ombros/Desenvolvimento Militar.gif"),
            absolute_path=Path("/tmp/Ombros/Desenvolvimento Militar.gif"),
            sha256="",
            normalized_name="desenvolvimento militar",
        )

        result = matcher.match(document)

        self.assertFalse(result.matched)
        self.assertEqual(result.score, 0.0)
        self.assertIsNone(result.candidate)
        self.assertEqual(result.document, document)


    def test_exact_matcher_null_normalized_name(self):

        matcher = ExactMatcher(
            {
                "supino reto barra",
                "crucifixo",
            }
        )

        document = Document(
            name="Desenvolvimento Militar",
            category="Ombros",
            group="Ombros",
            extension=".gif",
            relative_path=Path("Ombros/Desenvolvimento Militar.gif"),
            absolute_path=Path("/tmp/Ombros/Desenvolvimento Militar.gif"),
            sha256="",
            normalized_name=None,
        )

        result = matcher.match(document)

        self.assertFalse(result.matched)
        self.assertEqual(result.score, 0.0)
        self.assertIsNone(result.candidate)
        self.assertEqual(result.document, document)

        
if __name__ == "__main__":
    unittest.main()
