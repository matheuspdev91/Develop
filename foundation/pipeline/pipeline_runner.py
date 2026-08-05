
class PipelineRunner:

    def __init__(
        self,
        scanner,
        parser_pipeline,
        enricher,
        matcher,
        exporter,
    ):
        self.scanner = scanner
        self.parser_pipeline = parser_pipeline
        self.enricher = enricher
        self.matcher = matcher
        self.exporter = exporter

    def run(self):

        documents = self.scanner.scan()

        documents = self.parser_pipeline.run(documents)

        for document in documents:

            self.enricher.enrich(document)

        results = []

        for document in documents:

            result = self.matcher.match(document)
            results.append(result)

        self.exporter.export(results)

        return results
