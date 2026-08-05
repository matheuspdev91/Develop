"""Orquestra a execução sequencial de enrichers."""

from collections.abc import Iterable

from foundation.enricher.enricher import Enricher
from foundation.media.document import Document


class EnricherPipeline:
    """
    Orquestra a execução sequencial dos enrichers sobre cada documento.
    Cada documento percorre toda a cadeia de enrichers antes que o próximo
    documento seja processado.
    """

    def __init__(self, enrichers: Iterable[Enricher]) -> None:
        """Inicializa o pipeline com os enrichers que serão executados."""
        self._enrichers = list(enrichers)

    def run(self, documents: list[Document]) -> list[Document]:
        """Executa todos os enrichers em sequência e retorna os documentos."""
        for document in documents:
            for enricher in self._enrichers:
                enricher.enrich(document)

        return documents
