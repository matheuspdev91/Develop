import unittest
from pathlib import Path

from foundation.media.document import Document
from foundation.parser.folder_parser import FolderParser


class TestFolderParser(unittest.TestCase):
    def test_folder_parser_sets_group_from_current_document_structure(self):
        document = Document(
            name="Supino Reto Barra",
            category=None,
            group=None,
            extension="gif",
            relative_path=Path("exercicios/Peitoral/Supino Reto Barra.gif"),
            absolute_path=Path("/tmp/exercicios/Peitoral/Supino Reto Barra.gif"),
            sha256="",
        )

        FolderParser().parse(document)

        self.assertEqual(document.group, "Peitoral")


if __name__ == "__main__":
    unittest.main()
