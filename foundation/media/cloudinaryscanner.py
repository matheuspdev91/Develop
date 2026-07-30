from pathlib import Path, PurePosixPath

from foundation.media.document import Document
from foundation.media.media_scanner import MediaScanner


class CloudinaryMediaScanner(MediaScanner):

    def __init__(self, client):
        self.client = client

    def scan(self) -> list[Document]:

        documents = []

        for asset in self.client.list_assets():

            public_id = asset["public_id"]
            path = PurePosixPath(public_id)

            documents.append(
                Document(
                    name=path.stem,
                    category="",
                    group="",
                    extension=path.suffix.lstrip("."),
                    relative_path=Path(path),
                    absolute_path=Path(),
                    sha256="",
                    public_id=public_id,
                    url=asset["secure_url"],
                )
            )

        return documents