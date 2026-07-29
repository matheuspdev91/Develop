from abc import ABC
from abc import abstractmethod

from foundation.media.document import Document


class Enricher(ABC):

    @abstractmethod
    def enrich(self, document: Document) -> None:
        """
        Enriquece um document com informações externas
        """
       