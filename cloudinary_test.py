from foundation.clients.cloudinary_client import CloudinaryClient
from foundation.media.cloudinaryscanner import CloudinaryMediaScanner

client = CloudinaryClient(
   cloud_name="dkdpsbvri",
   api_key="663385686221129",
   api_secret="Ccj4kJw9QD947LvjpEd2AGLF7iI",
)

scanner = CloudinaryMediaScanner(client)

documents = scanner.scan()

print(f"Total de mídias: {len(documents)}")

for document in documents[:10]:
    print(document)