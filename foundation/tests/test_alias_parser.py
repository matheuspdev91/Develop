import unittest
from pathlib import Path

from foundation.media.document import Document
from foundation.parser.alias_parser import AliasParser


class TestAliasParser(unittest.TestCase):

    def test_alias_parser(self):

        aliases = {
            "bench press": "supino reto barra"
        }

        document = Document(
            name="Bench Press",
            category="Peitoral",
            group="Peitoral",
            extension=".gif",
            relative_path=Path("Peitoral/Bench Press.gif"),
            absolute_path=Path("/tmp/Peitoral/Bench Press.gif"),
            sha256="",
            normalized_name="bench press",
        )

        parser = AliasParser(aliases)

        parser.parse(document)

        self.assertEqual(
            document.normalized_name,
            "supino reto barra"
        )


if __name__ == "__main__":
    unittest.main()