from foundation.document import Document
from foundation.retriever.keywords import(
    DATABASE_QUERY,
    DATABASE_FILES
)

class Retriever:

    MATCH_SCORE = 10

    def retrieve(
        self,
        documents: list[Document],
        query: str,
    ) -> list[Document]:
        
        domain = self._detect_domain(query)

        ranked_documents = sorted(
            documents,
            key=lambda document: self._score_document(
                document,
                domain,
            ),
            reverse=True,
        )

        return [
            document
            for document in ranked_documents
            if self._score_document(document, domain) > 0
        ]

    def _score_document(
        self,
        document: Document,
        domain: str | None,
    ) -> int:

        score = 0
        if domain == "database":
            
            name = document.name.lower()

            for keyword in DATABASE_FILES:

                if keyword in name:
                    score += self.MATCH_SCORE

        print(f"[DEBUG] {document.name} -> {score}")

        return score
       

    def _detect_domain(
        self,
        query: str,
    ) -> str | None:

        query = query.lower()

        if any(keyword in query for keyword in DATABASE_QUERY):
            return "database"

        return None


     


