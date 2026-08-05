"""Orquestra a execução sequencial de parsers."""

from collections.abc import Iterable

from foundation.media.document import Document
from foundation.parser.base import Parser


class ParserPipeline:
    """
    Orquestra a execução sequencial dos parsers sobre cada documento.
    Cada documento percorre toda a cadeia de parsers antes que o próximo
    documento seja processado."""
    

    def __init__(self, parsers: Iterable[Parser]) -> None:
        """Inicializa o pipeline com os parsers que serão executados."""
        self._parsers = list(parsers)

    def run(self, documents: list[Document]) -> list[Document]:
        """Executa todos os parsers em sequência e retorna os documentos."""
        for document in documents:
            for parser in self._parsers:
                parser.parse(document)

        return documents
