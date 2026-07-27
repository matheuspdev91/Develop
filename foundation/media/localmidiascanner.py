from pathlib import Path

from foundation.media.document import Document
from foundation.media.scanner import MediaScanner


class LocalMediaScanner(MediaScanner):

    def __init__(self, root: Path):
        self.root = root

    def scan(self) -> list[Document]:

        documents = []

        for file in self.root.rglob("*"):

            if not file.is_file():
                continue

            documents.append(
                Document(
                    name=file.stem,
                    category="",
                    group="",
                    extension=file.suffix.lstrip("."),
                    relative_path=file.relative_to(self.root),
                    absolute_path=file,
                    sha256="",
                )
            )

        return documents