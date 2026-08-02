import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from foundation.exports.json_exporter import JsonExporter
from foundation.matcher.matcher_result import MatchResult
from foundation.media.document import Document


class TestJsonExporter(unittest.TestCase):
    def test_export_serializes_match_and_non_match(self):
        matched_document = Document(
            name="Supino Reto",
            category="Peitoral",
            group="Peitoral",
            extension="gif",
            relative_path=Path("Peitoral/Supino Reto.gif"),
            absolute_path=Path("/tmp/Peitoral/Supino Reto.gif"),
            sha256="",
            normalized_name="supino-reto",
        )
        unmatched_document = Document(
            name="Desenvolvimento",
            category="Ombros",
            group="Ombros",
            extension="gif",
            relative_path=Path("Ombros/Desenvolvimento.gif"),
            absolute_path=Path("/tmp/Ombros/Desenvolvimento.gif"),
            sha256="",
            normalized_name="desenvolvimento",
        )
        results = [
            MatchResult(matched_document, True, 0.98, "Supino Reto"),
            MatchResult(unmatched_document, False, 0.22, "Valor indevido"),
        ]

        with TemporaryDirectory() as temporary_directory:
            output_path = Path(temporary_directory) / "cloudinary_sync.json"

            JsonExporter(output_path).export(results)

            with output_path.open(encoding="utf-8") as output_file:
                data = json.load(output_file)

        self.assertEqual(
            data,
            [
                {
                    "match": True,
                    "score": 0.98,
                    "document": {
                        "path": "Peitoral/Supino Reto.gif",
                        "normalized_name": "supino-reto",
                        "group": "Peitoral"
                    },
                    "candidate": "Supino Reto",
                },
                {
                    "match": False,
                    "score": 0.22,
                    "document": {
                        "path": "Ombros/Desenvolvimento.gif",
                        "normalized_name": "desenvolvimento",
                        "group": "Ombros"
                    },
                    "candidate": None,
                },
            ],
        )


if __name__ == "__main__":
    unittest.main()
