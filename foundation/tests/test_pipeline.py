from foundation import document
import unittest
from pathlib import Path
from foundation.media.document import Document
from foundation.parser.folder_parser import FolderParser
from foundation.parser.alias_parser import AliasParser
from foundation.pipeline.pipeline import Pipeline


class TestPipeline(unittest.TestCase):

    def test_pipeline(self):
        document = Document(
            name="supino reto",
            category="",
            group="",
            extension=".gif",
            relative_path=Path("peitoral/supino reto.gif"),
            absolute_path=Path("/tmp/peitoral/supino reto.gif"),
            sha256="123"
)
    document.normalized_name = "supino reto"

    aliases = {
    "supino reto": "supino"
}
    alias_parser = AliasParser(aliases)


    pipeline = Pipeline(
    FolderParser(),
    alias_parser
)
