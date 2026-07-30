from foundation.media.document import Document
from foundation.media.media_scanner import MediaScanner


class MediaRepository:

    def __init__(self, *scanners: MediaScanner):
        self.scanners = scanners

    def load(self) -> list[Document]:

        media: list[Document] = []

        for scanner in self.scanners:
            media.extend(scanner.scan())

        return media