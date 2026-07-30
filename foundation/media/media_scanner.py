from abc import ABC
from abc import abstractmethod

from foundation.document import Document


class MediaScanner(ABC):

    @abstractmethod
    def scan(self) -> list[Document]:
        ...