from foundation.config import CLOUDINARY
from pathlib import Path

from foundation.media.localmidiascanner import LocalMediaScanner

from foundation.enricher.cloudinary_enricher import CloudinaryEnricher
from foundation.parser.pipeline import ParserPipeline
from foundation.parser.filenameparser import FilenameParser
from foundation.parser.folder_parser import FolderParser
from foundation.parser.alias_parser import AliasParser
from foundation.enricher.pipeline import EnricherPipeline
from foundation.clients.cloudinary_client import CloudinaryClient

"""
Acceptance Test

Objetivo:
Validar a execução ponta a ponta da Foundation utilizando
a biblioteca real do Fitflix.

Fluxo esperado:

LocalMediaScanner
    ↓
ParserPipeline
    ↓
MetadataEnricher
    ↓
Matcher
    ↓
JsonExporter
    ↓
Manifest.json
"""



FITFLIX_MEDIA_PATH = (
    r"C:\Users\Matheus\Desktop\fitflix\media\exercicios"
)

scanner = LocalMediaScanner(
    Path(FITFLIX_MEDIA_PATH)
)

parser_pipeline = ParserPipeline([
    FilenameParser(),
    FolderParser(),
    AliasParser({}),
])


client = CloudinaryClient(CLOUDINARY)


enricher_pipeline = EnricherPipeline([
    CloudinaryEnricher(client),
])


documents = scanner.scan()

documents = parser_pipeline.run(documents)

documents = enricher_pipeline.run(documents)