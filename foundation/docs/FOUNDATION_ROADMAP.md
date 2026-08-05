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

2026-08-05

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
- O `main.py` foi classificado como código legado.

---

# BACKLOG

## 🔴 Prioridade P0

### [x] Definir contrato do PipelineRunner

Status:

✅ Concluído

Origem:

Auditoria Geral

Descrição:

O PipelineRunner esperava um `Enricher` singular (`.enrich()`), enquanto a Foundation possuía um `EnricherPipeline` (`.run()`).

Objetivo:

Definir oficialmente qual contrato será utilizado pela composição da aplicação.

Critérios para conclusão:

- [x] Decisão arquitetural tomada.
- [x] Implementação realizada.
- [x] Testes passando.

Decisão:

✅ Aprovada

O PipelineRunner deve consumir pipelines através do contrato:

```text
run(documents)
```

Componentes unitários mantêm seus contratos próprios:

- Parser.parse(document)
- Enricher.enrich(document)
- Matcher.match(document)

Justificativa:

O PipelineRunner é um orquestrador de estágios, não de documentos.

---

## 🟠 Prioridade P1

### [x] Unificar normalização de nomes

Status:

✅ Concluído

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

- [x] Decisão arquitetural tomada.
- [x] ADR002 criado.
- [x] Implementação concluída.
- [x] Testes pós-implementação passando.
- [x] Componentes alinhados.

Decisão:

✅ Aprovada

O FilenameParser é a única autoridade autorizada a produzir
`normalized_name`.

CloudinaryEnricher, Matcher, JsonExporter e CloudinarySync
devem consumir esse valor sem recalcular sua normalização.

Justificativa:

`normalized_name` é um dado derivado do nome do arquivo.

Sua responsabilidade pertence ao estágio de parsing.

Consumidores podem adaptar formatos externos quando necessário,
mas não podem recalcular informações internas.

---

## 🟡 Prioridade P2

### [x] Revisar `main.py`

Status:

✅ Implementado

Data:

2026-08-05

Observação:

Trata-se de código legado.

Decisão:

✅ Aprovada

O `main.py` deixa de ser considerado o ponto de entrada oficial da Foundation.

O arquivo é classificado como código legado.

Sua remoção dependerá da criação de um novo entrypoint alinhado à arquitetura oficial.

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

## ADR001

**Status**

✅ Implementado

**Resumo**

O PipelineRunner consome composições através do contrato:

```text
run(documents)
```

Componentes unitários preservam seus contratos individuais.

---

## ADR002

**Status**

✅ Implementado

**Resumo**

O FilenameParser é a única autoridade sobre
`normalized_name`.

Todos os demais componentes apenas consomem esse valor.

---

## ADR003

**Status**

✅ Implementado

**Resumo**

O `main.py` deixa de ser considerado o ponto de entrada oficial da Foundation e passa a ser classificado como código legado.

Sua remoção dependerá da criação de um novo entrypoint oficial.

---

# HISTÓRICO

## 2026-08-04

- Acceptance Test funcionando.
- Auditoria geral concluída.
- Backlog inicial criado.

## 2026-08-05

- ADR001 implementado.
- ADR002 implementado.
- ADR003 implementado.
- PipelineRunner alinhado ao contrato de composição.
- Normalização de nomes centralizada no FilenameParser.
- `main.py` classificado como código legado.

---

# MÉTRICAS

Auditoria

- [x] Concluída

Pipeline

- [X] Scanner
- [x] Parser
- [x] Enricher
- [x] Matcher
- [ ] Exporter
- [x] PipelineRunner
- [x] CloudinarySync

Integração

- [ ] Completa

Foundation

🟡 Em desenvolvimento

Fitflix

⬜ Ainda não iniciado