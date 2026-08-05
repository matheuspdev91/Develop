# FOUNDATION ROADMAP

> Status atual da Foundation.
>
> Este documento centraliza:
>
> - backlog técnico;
> - decisões arquiteturais;
> - auditorias;
> - progresso da implementação.
>
> Nenhuma alteração arquitetural deve ser feita sem atualizar este documento.

---

# STATUS GERAL

**Versão:** Foundation V1

**Estado atual:**

🟡 Em desenvolvimento

Última atualização:

2026-08-04

---

# AUDITORIA

## Resultado

✅ Auditoria concluída.

Classificação:

🟡 Foundation pronta com pequenos ajustes.

Principais conclusões:

- Fluxos principais funcionam.
- Não há bloqueadores arquiteturais dentro da Foundation.
- Existem riscos para evolução futura.
- O `main.py` aparenta ser um script legado/desatualizado.

---

# BACKLOG

## 🔴 Prioridade P0

### [ ] Definir contrato do PipelineRunner

Status:

⬜ Não iniciado

Origem:

Auditoria Geral

Descrição:

O PipelineRunner espera um `Enricher` singular (`.enrich()`), enquanto a Foundation possui um `EnricherPipeline` (`.run()`).

Objetivo:

Definir oficialmente qual contrato será utilizado pela composição da aplicação.

Critério para concluir:

- [X] Decisão arquitetural tomada.
- [X] Implementação realizada.
- [X] Testes passando.


Decisão:

✅ Aprovada

O PipelineRunner deve consumir pipelines através do contrato:

run(documents)

Componentes unitários mantêm seus contratos próprios:

- Parser.parse(document)
- Enricher.enrich(document)
- Matcher.match(document)

Justificativa:

O PipelineRunner é um orquestrador de estágios, não de documentos.
---

## 🟠 Prioridade P1

### [ ] Unificar normalização de nomes

Status:

⬜ Não iniciado

Origem:

Auditoria Geral

Descrição:

Hoje existem três estratégias independentes:

- FilenameParser
- CloudinaryEnricher
- CloudinarySync

Objetivo:

Definir uma única estratégia oficial.

Critérios para conclusão:

- [X] Decisão arquitetural tomada.
- [x] ADR002 criado.
- [x] Implementação concluída.
- [x] Testes pós-implementação passando.
- [x] Componentes alinhados.

------

## 🟡 Prioridade P2

### [ ] Revisar `main.py`

Status:

⬜ Não iniciado

Observação:

Provavelmente trata-se de código legado.

---

### [ ] Alinhar assinatura dos Parsers

Status:

⬜ Não iniciado

---

### [ ] Revisar fixtures dos testes

Status:

⬜ Não iniciado

---

### [ ] Integrar CloudinarySync ao pipeline

Status:

⬜ Não iniciado

---

# DECISÕES ARQUITETURAIS

## ADR-001

### Semântica de `matched`

Status:

✅ Definida

Decisão:

```text
matched == True

↓

Existe um correspondente.
```

Motivo:

Padronizar Matcher, Exporter e CloudinarySync.

---

# HISTÓRICO

## 2026-08-04

- Acceptance Test funcionando.
- Auditoria geral concluída.
- Backlog inicial criado.

---

# MÉTRICAS

Auditoria

- [x] Concluída

Pipeline

- [ ] Scanner
- [x] Parser
- [x] Enricher
- [ ] Matcher
- [ ] Exporter
- [ ] PipelineRunner
- [ ] CloudinarySync

Integração

- [ ] Completa

Foundation

🟡 Em desenvolvimento

Fitflix

⬜ Ainda não iniciado