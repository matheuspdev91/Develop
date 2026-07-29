from pathlib import Path
from foundation.config import CLOUDINARY
from foundation.clients.cloudinary_client import CloudinaryClient
from foundation.enricher.cloudinary_enricher import CloudinaryEnricher
from foundation.media.document import Document

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


