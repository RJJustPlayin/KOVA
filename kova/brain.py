from openai import OpenAI

from .memory import MemoryStore
from .personality import SYSTEM_PROMPT


class KovaBrain:
    def __init__(self, api_key: str, model: str, memory: MemoryStore):
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.memory = memory

    def _instructions(self) -> str:
        facts = self.memory.facts()
        if not facts:
            return SYSTEM_PROMPT
        memory_block = "\nKnown user facts:\n" + "\n".join(f"- {fact}" for fact in facts)
        return SYSTEM_PROMPT + memory_block

    def respond(self, user_text: str) -> str:
        self.memory.add_message("user", user_text)

        messages = [{"role": "system", "content": self._instructions()}]
        messages.extend(self.memory.recent_messages(limit=20))

        response = self.client.responses.create(
            model=self.model,
            instructions=self._instructions(),
            input=messages[1:],
        )
        answer = response.output_text.strip()
        self.memory.add_message("assistant", answer)
        return answer
