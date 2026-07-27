from foundation.media.cloudinaryscanner import CloudinaryMediaScanner
from foundation.clients.cloudinary_client import CloudinaryClient
from foundation.config import OPENAI_BASE_URL
from foundation.config import DEFAULT_OPENAI_MODEL
from foundation.clients.openai import OpenAIClient
from foundation.config import OPENAI_API_KEY
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
from foundation.media.localmidiascanner import LocalMediaScanner
from dotenv import load_dotenv

load_dotenv()

import os


client = CloudinaryClient(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
)

scanner = Scanner()

documents = scanner.load(r"C:\Users\Matheus\Desktop\fitflix")

print(f"Documentos encontrados: {len(documents)}")



openrouter = OpenRouterClient(
    api_key=OPENROUTER_API_KEY,
    model=OPENROUTER_MODEL,
    base_url=OPENROUTER_BASE_URL,
)


ollama= OllamaClient(
    model=DEFAULT_MODEL,
    host=OLLAMA_HOST
)
builder = PromptBuilder()

reviewer = Reviewer(
    client=ollama,
    prompt_builder=builder,
)

retriever = Retriever()

selected = retriever.retrieve(
    documents,
"Resuma o arquivo models.py em cinco linhas."
)

response = reviewer.review(
    documents=selected,
    question="Resuma o arquivo models.py em cinco linhas."
)

Formatter.console(response)

#response = reviewer.review(document)

#Formatter.console(response)

#print("=" * 40)
#print()

#print(response.content)


client = CloudinaryClient(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
)

scanner = CloudinaryMediaScanner(client)

documents = scanner.scan()

question = "Liste exercícios que contenham a palavra supino"

selected = retriever.retrieve(
    documents,
    question,
)

response = reviewer.review(
    documents=selected,
    question=question,
)

Formatter.console(response)


