from foundation.media.document import Document
from foundation.parser.parser import Parser


class FolderParser(Parser):


    def parse(self, document: Document) -> Document:

        parts = document.relative_path.parts

        if len(parts) > 1:

            document.category = parts[0]
            document.group = parts[0]
            
        return document

