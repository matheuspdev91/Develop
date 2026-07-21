from foundation.document import Document
from foundation.prompt_context import PromptContext
from foundation.prompts.loader import PromptLoader


class PromptBuilder:

    def __init__(self):
        self.loader = PromptLoader()

    def build(
        self,
        specialist: str,
        document: Document,
    ) -> PromptContext:

        system_prompt = self.loader.load(specialist)
        user_prompt = document.content

        return PromptContext(
          system=system_prompt,
          user=user_prompt,
        )

        