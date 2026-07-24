from foundation.domain.chat_response import ChatResponse


class Formatter:

    @staticmethod
    def console(response: ChatResponse) -> None:
        print("=" * 40)
        print()
        print(response.content)
        print(f"Provider : {response.provider}")
        print(f"Model    : {response.model}")
        print(f"Prompt   : {response.prompt_tokens}")
        print(f"Output   : {response.completion_tokens}")
        print(f"Total    : {response.total_tokens}")
        print(f"Finish   : {response.finish_reason}")
