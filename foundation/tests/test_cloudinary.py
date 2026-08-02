import unittest
from pathlib import Path
from unittest.mock import Mock

from foundation.enricher.cloudinary_enricher import CloudinaryEnricher
from foundation.media.document import Document


class TestCloudinaryEnricher(unittest.TestCase):
    def test_enriches_document_from_matching_normalized_asset(self):
        client = Mock()
        client.list_assets.return_value = [
            {
                "public_id": "exercicios/gif/variacao-1965",
                "secure_url": "https://example.com/variacao-1965.gif",
            }
        ]
        document = Document(
            name="variacao-1965.gif",
            category="exercicios",
            group="gif",
            extension="gif",
            relative_path=Path("exercicios/gif/variacao-1965.gif"),
            absolute_path=Path("/tmp/variacao-1965.gif"),
            sha256="teste",
            normalized_name="variacao-1965",
        )

        CloudinaryEnricher(client).enrich(document)

        self.assertEqual(document.public_id, "exercicios/gif/variacao-1965")
        self.assertEqual(document.url, "https://example.com/variacao-1965.gif")


if __name__ == "__main__":
    unittest.main()
