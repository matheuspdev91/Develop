from pathlib import Path

import cloudinary
import cloudinary.uploader
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
           "resource_type": "image",
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

    def upload(
        self,
        local_path: Path,
        public_id: str,
    ):

        if not local_path.exists():
            raise FileNotFoundError(local_path)

        return cloudinary.uploader.upload(
                str(local_path),
                public_id=public_id,
                resource_type="image",
            )




        

    
    