from pathlib import Path


PROMPTS_DIR = Path(__file__).parent

class PromptLoader:
    def load(self, specialist: str) -> str:
        base = (PROMPTS_DIR / "base.md").read_text(encoding="utf-8")

        specialist = (
            PROMPTS_DIR / f"{specialist}.md"
        ).read_text(encoding="utf-8")
        return f"{base}\n\n{specialist}"
       
        
