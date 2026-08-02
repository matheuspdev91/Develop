from pathlib import Path

from foundation.media.document import Document
from foundation.parser.filenameparser import FilenameParser

parser = FilenameParser()

cases = [
    "Variacao-1965.gif",
    "Alongamento Ombro.gif",
    "Rosca_Direta.gif",
    "Flexão.gif",
    "Agachamento (Lado).gif",
]

for filename in cases:
    document = Document(
        name=filename,
        category="",
        group="",
        extension=Path(filename).suffix,
        relative_path=Path(filename),
        absolute_path=Path(filename),
        sha256="",
    )

    parser.parse(document)

    print(filename)
    print(f"-> {document.normalized_name}\n")
