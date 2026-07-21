from foundation.prompts import PromptBuilder
from foundation.ollama import OllamaClient

class Reviewer:
    def __init__(self, client, prompt_builder):

        self.client = client
        self.prompt_builder = prompt_builder

    def review_file(self, document):
        code = document.content
        prompt = self.prompt_builder.build_review_prompt(code)+
     