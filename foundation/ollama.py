import requests
from foundation.prompt_context import PromptContext
import json

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
        context: PromptContext,
    ) -> dict:

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": context.system,
                },

                {
                    "role": "user",
                    "content": context.user,
                },
            ],

            "stream": False,

            "options": {
                "num_predict": 200,
            },
        }

        return payload


    def generate(
    
        self,
        context: PromptContext,
    ) -> dict:
      
        payload = self._build_payload(context)
        
        print("=" * 80)
        print(f"Modelo: {self.model}")
        print(f"System: {len(context.system)} caracteres")
        print(f"User: {len(context.user)} caracteres")
        print("=" * 80)


        print("=" * 80)
        print(f"Modelo: {self.model}")
        print(f"Prompt do sistema: {len(context.system)} caracteres")
        print(f"Prompt do usuário: {len(context.user)} caracteres")
        print(f"num_predict: {payload['options']['num_predict']}")
        print("=" * 80)

        response = requests.post(
            url=f"{self.host}/api/chat",
            json=payload,
            timeout = 120,
        )

        response.raise_for_status()
        return response.json()

    
