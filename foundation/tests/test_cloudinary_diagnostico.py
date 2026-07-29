from foundation import enricher
from foundation.clients.cloudinary_client import CloudinaryClient
import cloudinary
from foundation.media.document import Document
from foundation.config import (
    CLOUDINARY_CLOUD_NAME,
    CLOUDINARY_API_KEY,
    CLOUDINARY_API_SECRET,
)

cloudinary.config(
    cloud_name=CLOUDINARY_CLOUD_NAME,
    api_key=CLOUDINARY_API_KEY,
    api_secret=CLOUDINARY_API_SECRET,
)

cfg = cloudinary.config()

print("Cloud Name:", cfg.cloud_name)
print("API Key:", cfg.api_key[-4:] if cfg.api_key else None)
print("Secure:", cfg.secure)
print("Upload Prefix:", cfg.upload_prefix)

print("\nTestando resources()...")

try:
    result = cloudinary.api.resources(max_results=1)
    print(result)
except Exception as e:
    print(type(e).__name__)
    print(e)


document = Document(
    ...
)

document.normalized_name = "variacao-1965"

enricher.enrich(document)

print(document.public_id)
print(document.url)