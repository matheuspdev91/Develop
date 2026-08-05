# AUDITORIA TÉCNICA — Parsers

> **Data:** 2026-08-05
>
> **Escopo:** `foundation/parser/` e contratos consumidos pelo `ParserPipeline`
>
> **Contexto:** P0, P1 e P2 concluídos. Início do item "Alinhar assinatura dos Parsers" (Prioridade P2 do ROADMAP).

---

## Inventário

| Arquivo | Classe | Tipo |
|---|---|---|
| [base.py](file:///c:/Users/Matheus/Desktop/LLM/foundation/parser/base.py) | `Parser` | Contrato abstrato (ABC) |
| [filenameparser.py](file:///c:/Users/Matheus/Desktop/LLM/foundation/parser/filenameparser.py) | `FilenameParser` | Parser concreto |
| [folder_parser.py](file:///c:/Users/Matheus/Desktop/LLM/foundation/parser/folder_parser.py) | `FolderParser` | Parser concreto |
| [alias_parser.py](file:///c:/Users/Matheus/Desktop/LLM/foundation/parser/alias_parser.py) | `AliasParser` | Parser concreto |
| [pipeline.py](file:///c:/Users/Matheus/Desktop/LLM/foundation/parser/pipeline.py) | `ParserPipeline` | Orquestrador |

---

## 1. Todos os Parsers seguem exatamente o mesmo contrato público?

**Não.**

### Contrato oficial (ABC)

```python
# foundation/parser/base.py — Linha 10

@abstractmethod
def parse(self, document: Document) -> None:
```

**Assinatura esperada:** `parse(self, document: Document) -> None`

### Assinatura de cada Parser

| Parser | Assinatura | Conforme o contrato? |
|---|---|---|
| `FilenameParser` | `parse(self, document: Document) -> None` | ✅ Sim |
| `FolderParser` | `parse(self, document: Document) -> Document` | ❌ Não |
| `AliasParser` | `parse(self, document: Document) -> Document` | ❌ Não |

---

## 2. Existe divergência de parâmetros, retorno ou comportamento?

**Sim.** A divergência é exclusivamente no **tipo de retorno**.

### Detalhamento

#### FilenameParser — 🟢 Saudável

- Assinatura: `parse(self, document: Document) -> None`
- Comportamento: Muta `document.normalized_name` in-place.
- Retorno: `None` (implícito — não há `return`).
- **Conforme o contrato.**

#### FolderParser — 🟠 Problema

- Assinatura: `parse(self, document: Document) -> Document`
- Comportamento: Muta `document.category` e `document.group` in-place.
- Retorno declarado: `-> Document`
- Retorno real: **`None`** (não há `return` no corpo do método).
- **Divergência:** O type hint declara `-> Document`, contradizendo o contrato `-> None` da ABC. Porém, em tempo de execução, o método retorna `None` implicitamente (não há instrução `return`). A divergência é apenas na **anotação de tipo**, não no comportamento real.

#### AliasParser — 🟠 Problema

- Assinatura: `parse(self, document: Document) -> Document`
- Comportamento: Muta `document.normalized_name` in-place (quando há alias correspondente).
- Retorno declarado: `-> Document`
- Retorno real: **`None`** (não há `return` no corpo do método).
- **Divergência:** Idêntica ao FolderParser. O type hint declara `-> Document`, mas o método não retorna nada.

### Resumo da divergência

| Aspecto | Contrato (ABC) | FilenameParser | FolderParser | AliasParser |
|---|---|---|---|---|
| Parâmetro | `document: Document` | ✅ | ✅ | ✅ |
| Retorno declarado | `-> None` | `-> None` ✅ | `-> Document` ❌ | `-> Document` ❌ |
| Retorno real | `None` | `None` ✅ | `None` ✅ | `None` ✅ |
| Mutação in-place | Esperado | ✅ | ✅ | ✅ |

---

## 3. O ParserPipeline consegue consumir todos os Parsers sem adaptações?

**Sim, em tempo de execução. Mas a inconsistência de tipo é um problema de contrato.**

O [ParserPipeline](file:///c:/Users/Matheus/Desktop/LLM/foundation/parser/pipeline.py#L20-L26) consome os parsers da seguinte forma:

```python
def run(self, documents: list[Document]) -> list[Document]:
    for document in documents:
        for parser in self._parsers:
            parser.parse(document)    # Retorno é ignorado
    return documents
```

O pipeline **ignora o retorno** de `parser.parse(document)`. Como todos os parsers mutam o Document in-place e todos retornam `None` na prática, o pipeline funciona corretamente **hoje**.

Porém, a inconsistência de tipo cria dois riscos:

1. **Confusão de contrato:** Um futuro desenvolvedor pode ler `-> Document` no `FolderParser` e concluir que o parser retorna um Document transformado, levando a implementações que dependem do retorno em vez da mutação.

2. **Type checkers (mypy/pyright):** Ferramentas de análise estática emitirão warnings por violar o contrato da ABC (`-> None` vs `-> Document`).

---

## 4. Existe risco arquitetural?

**🟡 Atenção**

### Justificativa

| Risco | Classificação | Explicação |
|---|---|---|
| Divergência de type hints | 🟠 Problema | `FolderParser` e `AliasParser` declaram `-> Document` contra `-> None` do contrato |
| Impacto em runtime | 🟢 Saudável | Todos funcionam corretamente porque o pipeline ignora o retorno |
| Impacto para evolução | 🟡 Atenção | Pode confundir desenvolvedores e quebrar análise estática |
| Falta de `__init__.py` | 🟡 Atenção | O pacote `parser/` não possui `__init__.py`. Funciona em Python 3 (namespace packages), mas é inconsistente com outros pacotes do projeto que possuem `__init__.py` |

A classificação geral é **🟡 Atenção** porque:
- Não há quebra em runtime.
- Mas existe uma violação formal do contrato abstrato que precisa ser alinhada para manter a integridade da arquitetura.

---

## CONCLUSÃO

**☑ Existe pequena inconsistência.**

Dois dos três parsers concretos (`FolderParser` e `AliasParser`) declaram `-> Document` no type hint do método `parse()`, enquanto o contrato abstrato define `-> None`.

O comportamento em runtime é idêntico em todos (mutação in-place, retorno `None` implícito). A inconsistência é apenas na **anotação de tipo**, não no comportamento real.

O `ParserPipeline` consome todos sem problemas porque ignora o retorno.

A correção é simples: alinhar o type hint de retorno dos dois parsers divergentes para `-> None`, conforme o contrato da ABC.
