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

document = documents[0]

response = reviewer.review(document)


print("=" * 40)
print(f"Provider : {response.provider}")
print(f"Model    : {response.model}")
print(f"Prompt   : {response.prompt_tokens}")
print(f"Output   : {response.completion_tokens}")
print(f"Total    : {response.total_tokens}")
print(f"Finish   : {response.finish_reason}")
print("=" * 40)

print(response.content)