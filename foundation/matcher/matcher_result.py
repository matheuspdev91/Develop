from dataclasses import dataclass
from foundation.media.document import Document

@dataclass
class MatchResult:

    document: Document
    matched: bool
    score: float
    candidate: str | None

