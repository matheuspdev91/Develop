from pathlib import Path


PROMPTS_DIR = Path(__file__).parent

class PromptLoader:
    def load(self, specialist: str) -> str:
        prompt_path = PROMPTS_DIR / f"{specialist}.md"
        return prompt_path.read_text(encoding="utf-8")
        
