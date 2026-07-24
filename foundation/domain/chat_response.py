from dataclasses import dataclass


@dataclass(slots=True)
class ChatResponse:
    """
    Representa a resposta de um modelo de linguagem.

    Essa classe abstrai os diferentes formatos de resposta
    dos provedores (Ollama, OpenAI, OpenRouter, Claude etc.)
    em uma estrutura única utilizada pelo Foundation.
    """

    content: str
    model: str
    provider: str

    prompt_tokens: int
    completion_tokens: int
    total_tokens: int

    finish_reason: str