import requests
import dataclasses
from foundation.domain import chat_response
from foundation.prompt_context import PromptContext
from foundation.domain.chat_response import ChatResponse
from foundation.clients.llm_client import LLMClient




class OllamaClient(LLMClient):
    """
    Cliente responsável por conversar com o Ollama.
    """
    def __init__(
        self,
        model: str,
        host: str,
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

        data = response.json()

        from pprint import pprint

        pprint(data)


        message = data["message"]

        content = (
            message.get("content")
            or message.get("thinking")
            or ""
        )

        return ChatResponse(
            content=content,
            model=data['model'],
            provider='ollama',
        )
            

    
