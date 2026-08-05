from foundation.media.document import Document
from foundation.parser.base import Parser


class FolderParser(Parser):


    def parse(self, document: Document) -> Document:

        parts = document.relative_path.parts

        if len(parts) >= 3:

            document.category = parts[0]
            document.group = parts[1]
            
      

