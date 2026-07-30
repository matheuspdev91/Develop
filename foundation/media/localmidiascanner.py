from pathlib import Path

from foundation.media.document import Document
from foundation.media.media_scanner import MediaScanner


class LocalMediaScanner(MediaScanner):

    def __init__(self, root: Path):
        self.root = root

    def scan(self) -> list[Document]:

        print(self.root)
        print(self.root.exists())
        print(list(self.root.iterdir()))

        documents = []

        for file in self.root.rglob("*"):
            print(file, file.is_file())

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