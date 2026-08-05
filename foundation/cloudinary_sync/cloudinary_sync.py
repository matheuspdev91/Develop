from pathlib import Path
import json

class CloudinarySync:

    def __init__(
        self,
        client,
        media_root: Path | str,
        manifest_path: Path | str,

    ):
        self.client = client
        self.media_root = Path(media_root)
        self.manifest_path = Path(manifest_path)

        
    def run(self):
        
        with self.manifest_path.open(
            "r",
            encoding="utf-8",
        )as file:

            manifest = json.load(file)

            for item in manifest:


                if not item["match"]:
                    continue

                local_path = self.media_root / item["document"]["path"]

                group = item["document"]["group"]
                candidate = item["candidate"]

                public_id = self._build_public_id(
                    group,
                    candidate,
                )

                self.client.upload(
                    local_path,
                    public_id,
                )
    
    def _build_public_id(self, group: str, candidate: str) -> str:

        group = group.lower().replace(" ", "_")

        return f"{group}/{candidate}"
                

                
        