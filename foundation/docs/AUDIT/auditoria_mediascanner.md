# AUDITORIA TÉCNICA — MediaScanner

> **Data:** 2026-08-05
>
> **Escopo:** `foundation/media/media_scanner.py`, `foundation/media/localmidiascanner.py`, `foundation/media/cloudinaryscanner.py`, `foundation/media/document.py`
>
> **Contexto:** P0, P1 e P2 concluídos. Auditoria do Scanner para verificar inconsistência envolvendo classes Document.

---

## 1. Qual classe Document é utilizada pelo MediaScanner (ABC)?

```python
# foundation/media/media_scanner.py — Linha 4
from foundation.document import Document
```

O MediaScanner importa `foundation.document.Document` — o **Document raiz**, que representa arquivos de **código-fonte**.

---

## 2. Qual classe Document é utilizada pelos scanners concretos?

### LocalMediaScanner

```python
# foundation/media/localmidiascanner.py — Linha 3
from foundation.media.document import Document
```

Utiliza `foundation.media.document.Document` — o Document de **mídia**.

### CloudinaryMediaScanner

```python
# foundation/media/cloudinaryscanner.py — Linha 3
from foundation.media.document import Document
```

Utiliza `foundation.media.document.Document` — o Document de **mídia**.

---

## 3. Todos utilizam exatamente a mesma classe Document?

**Não.**

| Componente | Import | Classe real |
|---|---|---|
| `MediaScanner` (ABC) | `from foundation.document import Document` | `foundation.document.Document` |
| `LocalMediaScanner` | `from foundation.media.document import Document` | `foundation.media.document.Document` |
| `CloudinaryMediaScanner` | `from foundation.media.document import Document` | `foundation.media.document.Document` |

**O contrato abstrato (`MediaScanner`) referencia uma classe Document diferente da que as implementações concretas utilizam.**

---

## 4. Existe duplicidade entre os dois Documents?

**Sim.** São duas classes completamente distintas com o mesmo nome.

### `foundation.document.Document`

```python
# foundation/document.py
@dataclass(frozen=True, slots=True)
class Document:
    path: Path
    content: str
```

| Aspecto | Valor |
|---|---|
| Propósito | Representar arquivos de **código-fonte** |
| Campos | `path`, `content` |
| Mutabilidade | **Imutável** (`frozen=True, slots=True`) |
| Properties | `name`, `extension`, `parent` |
| Usado por | `source_scanner.py`, `reviewer.py`, `retriever/`, `promptbuilder.py`, **`media_scanner.py`** |

### `foundation.media.document.Document`

```python
# foundation/media/document.py
@dataclass
class Document:
    name: str
    category: str
    group: str
    extension: str
    relative_path: Path
    absolute_path: Path
    sha256: str
    public_id: str | None = None
    url: str | None = None
    normalized_name: str | None = None
```

| Aspecto | Valor |
|---|---|
| Propósito | Representar arquivos de **mídia** (vídeos, imagens) |
| Campos | `name`, `category`, `group`, `extension`, `relative_path`, `absolute_path`, `sha256`, `public_id`, `url`, `normalized_name` |
| Mutabilidade | **Mutável** (parsers e enrichers mutam campos in-place) |
| Usado por | Todos os scanners concretos, parsers, enrichers, matchers, exporter, testes |

### Resumo

São duas entidades de domínio distintas — não é duplicidade acidental. Porém, compartilham o mesmo nome `Document`, o que causa confusão e, como demonstrado, levou a um import errado no `MediaScanner`.

---

## 5. Existe incompatibilidade de contrato?

**🟠 Problema**

O `MediaScanner` (ABC) define seu contrato assim:

```python
# media_scanner.py — Linha 10
def scan(self) -> list[Document]:   # ← foundation.document.Document
```

Mas as implementações concretas retornam:

```python
# localmidiascanner.py — Linha 12
def scan(self) -> list[Document]:   # ← foundation.media.document.Document

# cloudinaryscanner.py — Linha 12
def scan(self) -> list[Document]:   # ← foundation.media.document.Document
```

**As implementações retornam `foundation.media.document.Document`, mas o contrato abstrato promete `foundation.document.Document`.**

Essas são classes **incompatíveis**:

| Aspecto | `foundation.document.Document` | `foundation.media.document.Document` |
|---|---|---|
| `name` | Property (derivada de `path`) | Campo direto (`str`) |
| `content` | ✅ Presente | ❌ Ausente |
| `category` | ❌ Ausente | ✅ Presente |
| `group` | ❌ Ausente | ✅ Presente |
| `normalized_name` | ❌ Ausente | ✅ Presente |
| `relative_path` | ❌ Ausente | ✅ Presente |
| `sha256` | ❌ Ausente | ✅ Presente |
| `public_id` | ❌ Ausente | ✅ Presente |
| `url` | ❌ Ausente | ✅ Presente |
| Mutabilidade | Imutável | Mutável |

Não há herança entre elas. Não há interface comum. São tipos completamente distintos.

Em runtime o Python não impede isso (duck typing), mas o contrato formal está incorreto — o `MediaScanner` declara retornar um tipo que nenhuma das suas implementações realmente retorna.

---

## 6. O contrato do MediaScanner está alinhado com o restante da Foundation?

**Não.**

Toda a Foundation (parsers, enrichers, matchers, exporter, testes) opera sobre `foundation.media.document.Document`.

Mapeamento completo dos imports de `foundation.media.document.Document`:

| Módulo | Import |
|---|---|
| `parser/base.py` | `from foundation.media.document import Document` |
| `parser/pipeline.py` | `from foundation.media.document import Document` |
| `parser/filenameparser.py` | `from foundation.media.document import Document` |
| `parser/folder_parser.py` | `from foundation.media.document import Document` |
| `parser/alias_parser.py` | `from foundation.media.document import Document` |
| `enricher/enricher.py` | `from foundation.media.document import Document` |
| `enricher/pipeline.py` | `from foundation.media.document import Document` |
| `enricher/cloudinary_enricher.py` | `from foundation.media.document import Document` |
| `matcher/matcher.py` | `from foundation.media.document import Document` |
| `matcher/exact_matcher.py` | `from foundation.media.document import Document` |
| `matcher/matcher_result.py` | `from foundation.media.document import Document` |
| `media/localmidiascanner.py` | `from foundation.media.document import Document` |
| `media/cloudinaryscanner.py` | `from foundation.media.document import Document` |
| `media/mediarepository.py` | `from foundation.media.document import Document` |

O **único** componente da arquitetura oficial que importa o Document errado é o `media_scanner.py`:

| Módulo | Import | Correto? |
|---|---|---|
| `media/media_scanner.py` | `from foundation.document import Document` | ❌ |

Os demais consumidores de `foundation.document.Document` são componentes do **fluxo legado** (LLM review):

| Módulo | Observação |
|---|---|
| `source_scanner.py` | Scanner de código-fonte (fluxo legado) |
| `reviewer.py` | Reviewer LLM (fluxo legado) |
| `retriever/retriever.py` | Retriever LLM (fluxo legado) |
| `promptbuilder.py` | Prompt builder LLM (fluxo legado) |

---

## CONCLUSÃO

**☑ Existe inconsistência arquitetural.**

O `MediaScanner` (ABC) importa `foundation.document.Document` (Document de código-fonte, imutável), enquanto toda a Foundation — incluindo as duas implementações concretas do próprio `MediaScanner` — opera sobre `foundation.media.document.Document` (Document de mídia, mutável).

São classes com campos, propósitos e comportamentos completamente diferentes. O contrato abstrato está referenciando o tipo errado.

A correção é pontual (um único import), mas a inconsistência é **arquitetural** porque o contrato da ABC — que é a interface formal do estágio Scanner na arquitetura `Scanner → Parser → Enricher → Matcher → Exporter` — está declarando o tipo errado.
