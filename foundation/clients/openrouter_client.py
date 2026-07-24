from foundation.domain import chat_response
from foundation.domain.chat_response import ChatResponse
import requests
from foundation.clients.llm_client import LLMClient


class OpenRouterClient(LLMClient):

    def __init__(
        self,
        api_key: str,
        model: str,
        base_url: str,
    ):
        self.api_key = api_key
        self.model = model
        self.base_url = base_url

    def generate(self, context):
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

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
    "max_tokens": 1024,
}

        response = requests.post(
        f"{self.base_url}/chat/completions",
        headers=headers,
        json=payload,
       )

        #print(response.status_code)

        #print(response.text)

        response.raise_for_status()

        data = response.json()

        message = data["choices"][0]["message"]

        content = message["content"]

        usage = data["usage"]

        finish_reason = data["choices"][0]["finish_reason"]

        

        return ChatResponse(
            content=content,
            model=data['model'],
            provider='openrouter',

            prompt_tokens=usage["prompt_tokens"],
            completion_tokens=usage["completion_tokens"],
            total_tokens=usage["total_tokens"],

            finish_reason=finish_reason,
    )

    