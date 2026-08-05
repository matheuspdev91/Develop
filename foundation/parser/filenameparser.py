import re
import unicodedata
from pathlib import Path

from foundation.media.document import Document
from foundation.parser.base import Parser

class FilenameParser(Parser):

    def parse(self, document: Document) -> None:
        stem = Path(document.name).stem

        normalized = unicodedata.normalize("NFKD", stem)
        normalized = normalized.encode("ascii", "ignore").decode("ascii")
        normalized = normalized.lower()

        normalized = normalized.replace("_", "-")
        normalized = re.sub(r"\s+", "-", normalized)
        normalized = re.sub(r"[^a-z0-9-]", "", normalized)
        normalized = re.sub(r"-+", "-", normalized)

        document.normalized_name = normalized.strip("-")