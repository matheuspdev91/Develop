from foundation.config import CLOUDINARY
from foundation.clients.cloudinary_client import CloudinaryClient

client = CloudinaryClient(CLOUDINARY)

assets = client.list_assets()

print(f"{len(assets)} assets encontrados")