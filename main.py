from foundation.scanner import Scanner
from foundation.ollama import OllamaClient
from foundation.promptbuilder import PromptBuilder
from foundation.reviewer import Reviewer

scanner = Scanner()

documents = scanner.load(r"C:\Users\Matheus\Desktop\fitflix")

print(f"Documentos encontrados: {len(documents)}")


client = OllamaClient()
builder = PromptBuilder()

reviewer = Reviewer(
    client=client,
    prompt_builder=builder,
)

document = documents[0]

response = reviewer.review(document)

print(response)