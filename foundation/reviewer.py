from foundation.promptbuilder import PromptBuilder
from foundation.document import Document
from foundation.clients.llm_client import LLMClient


class Reviewer:

    def __init__(
        self,
        prompt_builder: PromptBuilder,
        client: LLMClient,
    ):
        self.client = client
        self.prompt_builder = prompt_builder


    def review(
        self,
        documents: list[Document],
        question: str,
    ):
        print("1 - montando contexto")

        context = self.prompt_builder.build(
            specialist="review",
            question=question,
            documents=documents,
        )

        print("2 - chamando LLM")

        response = self.client.generate(context)

        print("3 - resposta recebida")

        return response

        

