import cloudinary
from cloudinary.api import resources

class CloudinaryClient:

    def __init__(
        self,
        cloud_name: str,
        api_key: str,
        api_secret: str,
    ):

        cloudinary.config(
            cloud_name=cloud_name,
            api_key=api_key,
            api_secret=api_secret,
            secure=True,
        )

    def list_assets(self) -> list[dict]:


        response = resources(
            type="upload",
            resource_type="image",
            max_results=500,
        )

        return response["resources"]

        