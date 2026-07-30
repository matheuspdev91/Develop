from pathlib import Path
from foundation.document import Document


class Scanner:
    """
    Responsável por localizar e ler arquivos Python.
    """

    IGNORE_DIRS = {
        ".git",
        "venv",
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
    }

    def scan(self, root: str | Path) -> list[Path]:
        """
        Retorna todos os arquivos .py encontrados.
        """
        root_path = Path(root)

        files = []

        for file in root_path.rglob("*.py"):
            if any(part in self.IGNORE_DIRS for part in file.parts):
                continue

            files.append(file)

        return files

    def read(self, file: Path) -> str:
        """
        Lê o conteúdo de um arquivo Python.
        """
        return file.read_text(encoding="utf-8")
        
    def load(self, root: str | Path) -> list[Document]:

        """
        Carrega todos os arquivos Python encontrados.
        """
        documents = []

        for file in self.scan(root):
            documents.append(
                Document(
                    path=file,
                    content=self.read(file),
                )
            )

        return documents

    