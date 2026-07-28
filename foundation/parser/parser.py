from abc import ABC
from abc import abstractmethod

from foundation.media.document import Document


class Parser(ABC):

    @abstractmethod
    def parse(self, document: Document) -> Document:
        """
        Interpreta um Document e enriquece seus metadados.
        """
        ...