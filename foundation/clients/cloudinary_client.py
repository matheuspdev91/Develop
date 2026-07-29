import cloudinary
from cloudinary.api import resources
from foundation.config import CloudinaryConfig

class CloudinaryClient:

    def __init__(self, config: CloudinaryConfig):
        self.config = config

        cloudinary.config(
            cloud_name=config.cloud_name,
            api_key=config.api_key,
            api_secret=config.api_secret,
            secure=config.secure,
        )
   
        
    def list_assets(self) -> list[dict]:


        response = resources(
            type="upload",
            resource_type="image",
            max_results=500,
        )

        return response["resources"]

        