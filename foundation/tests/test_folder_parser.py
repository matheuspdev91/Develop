import unittest
from pathlib import Path

from foundation.media.document import Document
from foundation.parser.folder_parser import FolderParser


class TestFolderParser(unittest.TestCase):

    def test_folder_parser(self):

        document = Document(
            name="Supino Reto Barra",
            category=None,
            group=None,
            extension=".gif",
            relative_path=Path("Peitoral/Supino Reto Barra.gif"),
            absolute_path=Path("/tmp/Peitoral/Supino Reto Barra.gif"),
            sha256="",
            normalized_name=None,
        )

        parser = FolderParser()
        parser.parse(document)

        self.assertEqual(document.category, "Peitoral")
        self.assertEqual(document.group, "Peitoral")


if __name__ == "__main__":
    unittest.main()