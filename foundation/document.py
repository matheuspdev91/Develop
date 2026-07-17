from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class Document:
    """
    Representa um arquivo de código-fonte.
    """

    path: Path
    content: str

    @property
    def name(self) -> str:
        return self.path.name

    @property
    def extension(self) -> str:
        return self.path.suffix

    @property
    def parent(self) -> Path:
        return self.path.parent