from dataclasses import dataclass
from pathlib import Path


@dataclass
class MediaDocument:
    name: str
    category: str
    group: str

    extension: str
    relative_path: Path
    absolute_path: Path

    sha256: str

    public_id: str | None = None
    url: str | None = None