from foundation.media.document import Document
from foundation.enricher.enricher import Enricher
from foundation.clients.cloudinary_client import CloudinaryClient


class CloudinaryEnricher(Enricher):

    def __init__(self, client: CloudinaryClient):
        self.client = client
        self.cloudinary_assets = self._load_assets()


    def enrich(self, document: Document) -> None:
        asset = self.cloudinary_assets.get(document.normalized_name)

        if asset:
            document.public_id = asset["public_id"]
            document.url = asset["secure_url"]


    def _load_assets(self) -> dict [str, dict]:

        assets = self.client.list_assets()

        print(f"Total de assets: {len(assets)}")

        index: dict[str, dict] = {}

        for asset in assets:
            public_id = asset['public_id']

            print(public_id)

            normalized  = public_id.rsplit("/", 1)[-1]

            if normalized in index:
                raise ValueError(
                    f"Dois assets possuem o mesmo nome normalizado: {normalized}"
                )
            index[normalized] = asset

        print(f"Índice criado com {len(index)} assets.")

        return index
            








