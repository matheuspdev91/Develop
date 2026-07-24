from foundation.retriever.retriever import Retriever
from pathlib import Path
from foundation.document import Document
from foundation.formatter import Formatter
from foundation.clients.openrouter_client import OpenRouterClient
from foundation.scanner import Scanner
from foundation.clients.ollama_client import OllamaClient
from foundation.promptbuilder import PromptBuilder
from foundation.reviewer import Reviewer
from foundation.config import DEFAULT_MODEL, OLLAMA_HOST, OPENROUTER_API_KEY, OPENROUTER_BASE_URL, OPENROUTER_MODEL

scanner = Scanner()

documents = scanner.load(r"C:\Users\Matheus\Desktop\fitflix")

print(f"Documentos encontrados: {len(documents)}")



client = OpenRouterClient(
    api_key=OPENROUTER_API_KEY,
    model=OPENROUTER_MODEL,
    base_url=OPENROUTER_BASE_URL,
)

builder = PromptBuilder()

reviewer = Reviewer(
    client=client,
    prompt_builder=builder,
)

retriever = Retriever()

selected = retriever.retrieve(
    documents,
    "Analise meu banco de dados",
)

for document in selected:
    print(document.path)

#response = reviewer.review(document)

#Formatter.console(response)

#print("=" * 40)
#print()

#print(response.content)