import unittest
from unittest.mock import patch

from foundation.clients.cloudinary_client import CloudinaryClient
from foundation.config import CloudinaryConfig


class TestCloudinaryDiagnostico(unittest.TestCase):
    @patch("foundation.clients.cloudinary_client.cloudinary.config")
    def test_client_uses_cloudinary_config(self, configure_cloudinary):
        config = CloudinaryConfig(
            cloud_name="test-cloud",
            api_key="test-key",
            api_secret="test-secret",
        )

        client = CloudinaryClient(config)

        self.assertIs(client.config, config)
        configure_cloudinary.assert_called_once_with(
            cloud_name="test-cloud",
            api_key="test-key",
            api_secret="test-secret",
            secure=True,
        )


if __name__ == "__main__":
    unittest.main()
