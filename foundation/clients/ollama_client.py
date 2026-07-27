from foundation.exceptions.llms_erros import LLMError
import requests
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
                "num_predict": 1024,
            },
        }

        return payload


    def generate(
    
        self,
        context: PromptContext,
    ) -> ChatResponse:
      
        payload = self._build_payload(context)
        
    
        print("=" * 80)
        print(f"Modelo: {self.model}")
        print(f"Prompt do sistema: {len(context.system)} caracteres")
        print(f"Prompt do usuário: {len(context.user)} caracteres")
        print(f"num_predict: {payload['options']['num_predict']}")
        print("=" * 80)

        response = requests.post(
            url=f"{self.host}/api/chat",
            json=payload,
            timeout = None,
        )

        try:
            response.raise_for_status()

        except requests.RequestException as exc:
            raise LLMError(
                provider="ollama",
                status_code=response.status_code,
                message=str(exc),
            ) from exc

        data = response.json()

        from pprint import pprint

        pprint(data)


        message = data["message"]

        content = (
            message.get("content", "")
        )

        return ChatResponse(
            content=content,
            model=data['model'],
            provider='ollama',
            
            prompt_tokens=data.get("prompt_eval_count"),
            completion_tokens=data.get("eval_count"),
            total_tokens=(
                data.get("prompt_eval_count", 0)
                + data.get("eval_count", 0)
            ),
            finish_reason=data.get("done_reason"),

            thinking=message.get("thinking"),
        )

    
