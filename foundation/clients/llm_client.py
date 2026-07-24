from abc import ABC, abstractmethod

from foundation.domain.chat_response import ChatResponse
from foundation.prompt_context import PromptContext


class LLMClient(ABC):
    """
    Contrato que todo cliente de IA deve implementar.
    """

    @abstractmethod
    def generate(
        self,
        context: PromptContext,
    ) -> ChatResponse:
        """
        Envia um PromptContext para um modelo de linguagem
        e retorna uma resposta padronizada.
        """
        ...