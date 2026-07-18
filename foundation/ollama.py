import json
import requests

from foundation.config import (
    DEFAULT_MODEL,
    OLLAMA_HOST,
)


class OllamaClient:
    """
    Cliente responsável por conversar com o Ollama.
    """
    def __init__(
        self,
        model: str = DEFAULT_MODEL,
        host: str = OLLAMA_HOST
    ):
        
        self.model = model
        self.host = host


    def _build_payload(
        self,
        system: str,
        user: str,
    ):
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": system,
                },

                {
                    "role": "user",
                    "content": user,
                },
            ],

            "stream": False,
        }

        return payload


    def chat(
    
        self,
        system: str,
        user: str,
    ):
        payload = self._build_payload(system, user)

        response = requests.post(
            url=f"{self.host}/api/chat",
            json=payload,
        )

        response.raise_for_status()
        return response.json()

       
