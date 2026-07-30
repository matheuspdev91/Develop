from abc import ABC
from abc import abstractmethod

from foundation.media.document import Document


class Parser(ABC):

    @abstractmethod
    def parse(self, document: Document) -> None:
        """
        Interpreta um Document e preenche atributos derivados
        a partir dos seus próprios dados.
        """