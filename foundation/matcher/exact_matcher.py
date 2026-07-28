from foundation.matcher.matcher import Matcher
from foundation.matcher.matcher_result import MatchResult
from foundation.media.document import Document

class ExactMatcher(Matcher):

    def __init__(self, candidates: set[str]):
        self.candidates = candidates 


    def match(self, document: Document) -> MatchResult:

        matched = (
            document.normalized_name is not None 
            and document.normalized_name in self.candidates
        )

        candidate=document.normalized_name if matched else None
        score = 1.0 if matched else 0.0


        return MatchResult(
            document=document,
            matched=matched,
            score=score,
            candidate=candidate,
        )