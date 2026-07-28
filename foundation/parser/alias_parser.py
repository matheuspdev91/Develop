from foundation.media.document import Document
from foundation.parser.parser import Parser

class AliasParser(Parser):

    def __init__(self, aliases: dict[str,str]):
        self.aliases = aliases

    def parse(self, document: Document) -> Document:

        normalized_name = self.aliases.get(document.normalized_name)

        if normalized_name:
            document.normalized_name = normalized_name

        return document
           
        
        