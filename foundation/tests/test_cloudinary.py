from pathlib import Path
from foundation.config import CLOUDINARY
from foundation.clients.cloudinary_client import CloudinaryClient
from foundation.enricher.cloudinary_enricher import CloudinaryEnricher
from foundation.media.document import Document
from pprint import pprint

client = CloudinaryClient(CLOUDINARY)


enricher = CloudinaryEnricher(client)


document = Document(
    name="variacao-1965.gif",
    category="exercicios",
    group="gif",
    extension=".gif",
    relative_path=Path("exercicios/gif/variacao-1965.gif"),
    absolute_path=Path("/tmp/variacao-1965.gif"),
    sha256="teste",
)

# Temporário, até o Parser preencher automaticamente
document.normalized_name = "variacao-1965"

enricher.enrich(document)

print(f"Public ID : {document.public_id}")
print(f"URL       : {document.url}")
print("=" * 50)
print("Document.normalized_name:", document.normalized_name)
print("=" * 50)


client = CloudinaryClient(CLOUDINARY)
assets = client.list_assets()

print(f"Total de assets: {len(assets)}")

pprint(assets[0])

print("-" * 80)



for asset in assets[:10]:
    print(asset["public_id"])
