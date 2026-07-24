from dataclasses import dataclass


@dataclass(slots=True)
class LLMError(Exception):
    provider: str
    message: str
    status_code: int | None = None

    def __str__(self) -> str:
        if self.status_code is None:
            return f"[{self.provider}] {self.message}"

        return (
            f"[{self.provider}] "
            f"HTTP {self.status_code}: "
            f"{self.message}"
        )