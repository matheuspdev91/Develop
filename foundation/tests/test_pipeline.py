import unittest
from unittest.mock import Mock

from foundation.pipeline.pipeline_runner import PipelineRunner


class TestPipelineRunner(unittest.TestCase):
    def test_run_orchestrates_current_pipeline_components(self):
        documents = [object(), object()]
        parsed_documents = [object(), object()]
        results = [object(), object()]
        scanner = Mock()
        scanner.scan.return_value = documents
        parser_pipeline = Mock()
        parser_pipeline.run.return_value = parsed_documents
        enricher = Mock()
        matcher = Mock()
        matcher.match.side_effect = results
        exporter = Mock()

        runner = PipelineRunner(scanner, parser_pipeline,
                                enricher, matcher, exporter)

        self.assertEqual(runner.run(), results)
        scanner.scan.assert_called_once_with()
        parser_pipeline.run.assert_called_once_with(documents)
        self.assertEqual(
            enricher.enrich.call_args_list[0].args, (parsed_documents[0],))
        self.assertEqual(
            enricher.enrich.call_args_list[1].args, (parsed_documents[1],))
        self.assertEqual(
            matcher.match.call_args_list[0].args, (parsed_documents[0],))
        self.assertEqual(
            matcher.match.call_args_list[1].args, (parsed_documents[1],))
        exporter.export.assert_called_once_with(results)


if __name__ == "__main__":
    unittest.main()
