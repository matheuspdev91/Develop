from foundation.document import Document
from foundation.prompt_context import PromptContext
from foundation.prompts.loader import PromptLoader


class PromptBuilder:

    def __init__(self):
        self.loader = PromptLoader()

    def build(
        self,
        specialist: str,
        documents: list[Document],
        question: str,
    ) -> PromptContext:

        system_prompt = self.loader.load(specialist)

        

        parts = []

        # ==========================
        # Projeto
        # ==========================

        parts.append(
            f"""
####################################
PROJETO
####################################

Linguagem: Python
Framework: Django

Quantidade de documentos: {len(documents)}

####################################
PERGUNTA
####################################

{question}
"""
        )

        # ==========================
        # Documentos
        # ==========================

        for document in documents:

            parts.append(
                f"""
####################################
DOCUMENTO
####################################

Arquivo:
{document.path}

Conteúdo:

{document.content}

####################################
FIM DO DOCUMENTO
####################################
"""
            )

        user_prompt = "\n".join(parts)

        return PromptContext(
            system=system_prompt,
            user=user_prompt,
        )