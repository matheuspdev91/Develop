from abc import ABC
from abc import abstractmethod

from foundation.media.document import Document
from foundation.matcher.matcher_result import MatchResult

class Matcher(ABC):

    @abstractmethod
    def match(self, document: Document) -> MatchResult:
        pass