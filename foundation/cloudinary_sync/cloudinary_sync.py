from foundation.media.media_scanner import MediaScanner
from foundation.parser.parser import Parser
from foundation.enricher.enricher import Enricher
from foundation.matcher.matcher import Matcher

class CloudinarySync:

    def __init__(
        self,
        scanner: MediaScanner,
        parser: Parser,
        enricher: Enricher,
        matcher: Matcher,
        persister,
    ):

        self.scanner = scanner
        self.parser = parser
        self.enricher = enricher
        self.matcher = matcher
        self.persister = persister


    def run(self):

        documents = self.scanner.scan()

        results = []

        for document in documents:

            self.parser.parse(document)

            self.enricher.enrich(document)

            results.append(
                self.matcher.match(document)
            )

        self.export(results)

        return results

    
