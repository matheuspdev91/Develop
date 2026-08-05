# AUDITORIA TÉCNICA — main.py

> **Data:** 2026-08-05
>
> **Escopo:** Exclusivamente `main.py` (raiz do projeto)
>
> **Contexto:** P0 (ADR001) e P1 (ADR002) concluídos. Início da Prioridade P2 do ROADMAP.
>
> **Localização do arquivo:** `LLM/main.py` (fora do pacote `foundation/`)

---

## 1. O main.py ainda representa o ponto de entrada oficial da Foundation?

**Não.**

Justificativa:

- O `main.py` está localizado na **raiz do projeto** (`LLM/main.py`), **fora** do pacote `foundation/`.
- Ele **não é referenciado** por nenhum outro módulo do projeto.
- Existe um arquivo `foundation/cli.py` que está **vazio** (0 bytes), indicando que a Foundation previa um ponto de entrada via CLI que nunca foi implementado.
- O `main.py` não utiliza nenhum dos componentes oficiais da arquitetura atual (`PipelineRunner`, `ParserPipeline`, `EnricherPipeline`, `Matcher`, `Exporter`).
- O fluxo interno do `main.py` opera com componentes de um domínio completamente diferente: **LLM review / chat** (`Reviewer`, `PromptBuilder`, `Retriever`, `Formatter`).
- O `PipelineRunner` (que é o orquestrador oficial da Foundation) **não é instanciado nem invocado** pelo `main.py`.

**Conclusão:** O `main.py` é um **script de prototipação** que nunca evoluiu para ponto de entrada oficial. Ele pertence a um fluxo anterior ao pipeline atual.

---

## 2. O fluxo utilizado pelo main.py está compatível com a arquitetura atual?

**Não. Existe divergência total.**

### Arquitetura oficial (Pipeline)

```
Scanner → ParserPipeline → EnricherPipeline → Matcher → Exporter
```

### Fluxo real do main.py

```
Scanner.load() → Retriever.retrieve() → Reviewer.review() → Formatter.console()
CloudinaryMediaScanner.scan() → Retriever.retrieve() → Reviewer.review() → Formatter.console()
```

### Divergências identificadas

| Aspecto | Arquitetura Oficial | main.py |
|---|---|---|
| Orquestrador | `PipelineRunner` | Nenhum (script linear) |
| Parser | `ParserPipeline` | Não utilizado |
| Enricher | `EnricherPipeline` | Não utilizado |
| Matcher | `Matcher` | Não utilizado |
| Exporter | `Exporter` | Não utilizado |
| Scanner | `scanner.scan()` → retorna `MediaDocument` | `Scanner.load()` → retorna `Document` (código-fonte) |
| Fluxo LLM | Não faz parte da Foundation | `Reviewer`, `PromptBuilder`, `Retriever`, `Formatter` |

O `main.py` executa um fluxo de **review de código via LLM** (scan de `.py` → seleção por palavras-chave → envio ao LLM → exibição formatada). Este fluxo **não tem nenhuma intersecção** com o pipeline oficial da Foundation (que processa mídias: scan → parse → enrich → match → export).

---

## 3. Existem imports inexistentes, obsoletos ou incompatíveis?

| # | Import | Arquivo de destino | Status |
|---|---|---|---|
| 1 | `from foundation.media.cloudinaryscanner import CloudinaryMediaScanner` | `foundation/media/cloudinaryscanner.py` | 🟢 Saudável — arquivo existe |
| 2 | `from foundation.clients.cloudinary_client import CloudinaryClient` | `foundation/clients/cloudinary_client.py` | 🟢 Saudável — arquivo existe |
| 3 | `from foundation.config import OPENAI_BASE_URL` | `foundation/config.py` | 🟡 Atenção — existe no config, mas **não é utilizado** em nenhuma linha do main.py |
| 4 | `from foundation.config import DEFAULT_OPENAI_MODEL` | `foundation/config.py` | 🟡 Atenção — existe no config, mas **não é utilizado** em nenhuma linha do main.py |
| 5 | `from foundation.clients.openai import OpenAIClient` | `foundation/clients/openai.py` | 🟡 Atenção — arquivo existe, mas `OpenAIClient` **não é utilizado** em nenhuma linha do main.py |
| 6 | `from foundation.config import OPENAI_API_KEY` | `foundation/config.py` | 🟡 Atenção — existe no config, mas **não é utilizado** em nenhuma linha do main.py |
| 7 | `from foundation.retriever.retriever import Retriever` | `foundation/retriever/retriever.py` | 🟢 Saudável — existe e é utilizado |
| 8 | `from pathlib import Path` | stdlib | 🟡 Atenção — importado mas **não utilizado** no main.py |
| 9 | `from foundation.document import Document` | `foundation/document.py` | 🟡 Atenção — importado mas **não utilizado diretamente** (Scanner.load já retorna `list[Document]`) |
| 10 | `from foundation.formatter import Formatter` | `foundation/formatter.py` | 🟢 Saudável — existe e é utilizado |
| 11 | `from foundation.clients.openrouter_client import OpenRouterClient` | `foundation/clients/openrouter_client.py` | 🟡 Atenção — existe, é instanciado (L39-43) mas **nunca utilizado** após instanciação |
| 12 | `from foundation.scanner import Scanner` | **Não existe** | 🟠 Problema — o arquivo real é `foundation/source_scanner.py`. **Não existe** `foundation/scanner.py`. Este import falhará em runtime a menos que haja um mecanismo de re-export não detectado. |
| 13 | `from foundation.clients.ollama_client import OllamaClient` | `foundation/clients/ollama_client.py` | 🟢 Saudável — existe e é utilizado |
| 14 | `from foundation.promptbuilder import PromptBuilder` | `foundation/promptbuilder.py` | 🟢 Saudável — existe e é utilizado |
| 15 | `from foundation.reviewer import Reviewer` | `foundation/reviewer.py` | 🟢 Saudável — existe e é utilizado |
| 16 | `from foundation.config import DEFAULT_MODEL, OLLAMA_HOST, OPENROUTER_API_KEY, OPENROUTER_BASE_URL, OPENROUTER_MODEL` | `foundation/config.py` | 🟢 Saudável — todos existem no config |
| 17 | `from foundation.media.localmidiascanner import LocalMediaScanner` | `foundation/media/localmidiascanner.py` | 🟡 Atenção — arquivo existe, mas `LocalMediaScanner` **não é utilizado** em nenhuma linha do main.py |
| 18 | `from dotenv import load_dotenv` | pacote externo | 🟢 Saudável — biblioteca disponível |

### Resumo

- 🟢 Saudável: **8** imports
- 🟡 Atenção: **9** imports (importados mas não utilizados)
- 🟠 Problema: **1** import (`from foundation.scanner import Scanner` — módulo inexistente)

---

## 4. O main.py aparenta ser:

**☑ Código legado**

Justificativa:

1. **Caminho hardcoded:** Linha 33 contém `r"C:\Users\Matheus\Desktop\fitflix"`, um path absoluto para um projeto externo.
2. **Duplicação de instanciação:** `CloudinaryClient` é instanciado **duas vezes** de forma idêntica (L25-29 e L81-85).
3. **Código comentado:** Linhas 71-78 contêm código morto comentado.
4. **Fluxo linear sem estrutura:** Não há `if __name__ == "__main__"`, não há funções, não há classes. É um script de execução direta.
5. **Import quebrado:** `from foundation.scanner import Scanner` aponta para módulo inexistente (`scanner.py`), indicando que o arquivo real (`source_scanner.py`) foi renomeado após a criação do main.py sem que o main.py fosse atualizado.
6. **Nenhum componente da arquitetura atual é utilizado:** O `PipelineRunner`, `ParserPipeline`, `EnricherPipeline`, `Matcher` e `Exporter` — todos definidos como pipeline oficial — estão completamente ausentes.
7. **Mistura de domínios:** O script combina scan de código-fonte Python (Retriever/Reviewer) com scan de mídias Cloudinary, sem separação clara de responsabilidades.
8. **Instanciação de `openrouter` sem uso:** O client OpenRouter é instanciado na L39-43 mas nunca é passado para nenhum componente.
9. **O próprio ROADMAP já indica:** Na seção P2, linha 158: *"Provavelmente trata-se de código legado."*

---

## 5. Existe risco arquitetural?

**🟡 Atenção**

Explicação:

- **Risco baixo para a Foundation em si:** O `main.py` não é importado por nenhum módulo da Foundation. Não há acoplamento reverso. Removê-lo ou ignorá-lo não quebraria nenhum componente existente.
- **Risco de confusão:** Um novo desenvolvedor pode assumir que `main.py` é o ponto de entrada oficial, usar seu fluxo como referência, e implementar integrações **fora** do pipeline oficial (`PipelineRunner`).
- **Risco de import fantasma:** O import `from foundation.scanner import Scanner` aponta para um módulo inexistente. Se alguém tentar executar o `main.py` hoje, ele falhará imediatamente com `ModuleNotFoundError`.
- **Risco de exposição de credenciais:** O `config.py` contém API keys hardcoded (OpenAI, OpenRouter). O `main.py` importa essas credenciais. Embora este não seja um risco do `main.py` especificamente, o script perpetua o padrão inseguro.

---

## CONCLUSÃO

**☑ O main.py é legado e pode ser removido futuramente.**

Justificativa:

1. Não representa o ponto de entrada da Foundation.
2. Não utiliza nenhum componente da arquitetura oficial.
3. Contém import quebrado (`foundation.scanner`).
4. Possui 9 imports não utilizados.
5. Contém paths hardcoded e código duplicado.
6. O `cli.py` (vazio) é o candidato natural para ponto de entrada futuro.
7. O próprio ROADMAP já classificava este arquivo como "provavelmente legado".
8. O `PipelineRunner` já existe e é o orquestrador oficial da Foundation.

O `main.py` cumpriu seu papel como script de experimentação durante as fases iniciais do projeto. Com a arquitetura formalizada (Scanner → ParserPipeline → EnricherPipeline → Matcher → Exporter) e o PipelineRunner implementado, este arquivo não tem função no fluxo atual.
