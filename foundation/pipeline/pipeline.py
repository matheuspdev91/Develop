from foundation.parser.folder_parser import FolderParser
from foundation.media.localmidiascanner import LocalMediaScanner
from foundation.parser.filenameparser import FilenameParser
from foundation.media.document import Document
from foundation.parser.parser import Parser


class Pipeline:
    def __init__(self, *parsers: Parser):
        self.parsers = parsers

    def run(self, documents: list[Document]) -> list[Document]:
        for document in documents:

            for parser in self.parsers:
                parser.parse(document)

        return documents


