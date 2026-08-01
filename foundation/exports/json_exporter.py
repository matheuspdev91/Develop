import json
from pathlib import Path

from foundation.matcher.matcher_result import MatchResult


class JsonExporter:
    """Exporta resultados de match para um arquivo JSON."""

    def __init__(self, output_path: Path | str = "cloudinary_sync.json"):
        self.output_path = Path(output_path)

    def export(self, results: list[MatchResult]) -> None:
        data = []

        for result in results:
            item = {
                "match": result.matched,
                "score": result.score,
                "document": {
                    "path": result.document.relative_path.as_posix(),
                    "normalized_name": result.document.normalized_name,
                },
                "candidate": result.candidate if result.matched else None,
            }
            data.append(item)

        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        with self.output_path.open("w", encoding="utf-8") as output_file:
            json.dump(data, output_file, ensure_ascii=False, indent=4)
