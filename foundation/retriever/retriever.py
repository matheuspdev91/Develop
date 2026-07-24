from foundation.document import Document

class Retriever:

    MATCH_SCORE = 10

    DATABASE_KEYWORDS = (
    "model",
    "models",
    "migration",
    "migrations",
    "database",
    "repository",
)

    def retrieve(
        self,
        documents: list[Document],
        query: str,
    ) -> list[Document]:
        
        ranked_documents = sorted(
            documents,
            key=lambda document: self._score_document(
                document,
                query,
            ),
            reverse=True,
        )

        return [
            documents
            for documents in ranked_documents
            if self._score_document(documents, query) > 0
        ]

    def _score_document(
        self,
        document: Document,
        query: str,
    ) -> int:

        score = 0

        name = document.name.lower()
        query = query.lower()

        for keyword in self.DATABASE_KEYWORDS:
            if keyword in query and keyword in name:
                
                MATCH_SCORE = 10
                score += self.MATCH_SCORE

        return score

       

