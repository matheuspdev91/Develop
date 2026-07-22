from foundation.promptbuilder import PromptBuilder
from foundation.document import Document


class Reviewer:

    def __init__(
        self,
        client,
        prompt_builder: PromptBuilder,
    ):
        self.client = client
        self.prompt_builder = prompt_builder


    def review(
        self,
        document: Document,
    ):
        print("1 - montando contexto")

        context = self.prompt_builder.build(
            specialist="review",
            document=document,
        )

        print("2 - chamando o Ollama")

        response = self.client.generate(context)

        print("3 - resposta recebida")

        return response

        

