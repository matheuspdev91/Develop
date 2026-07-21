from dataclasses import dataclass


@dataclass(frozen=True, slots=True)

class PromptContext:
    system: str
    user: str