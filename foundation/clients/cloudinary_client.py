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

       assets = []
       next_cursor = None

       params = {
           "type": "upload",
           "resourse_type": "image",
           "max_results": 500,
       }

       while True:
            request_params = params.copy()

            if next_cursor:
                request_params["next_cursor"] = next_cursor

            response = resources(**request_params)

            assets.extend(response.get('resources', [])) 

            next_cursor = response.get("next_cursor")

            if not next_cursor:
                break

       return assets

    
    