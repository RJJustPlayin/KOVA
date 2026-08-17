from dataclasses import dataclass
import os

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    openai_api_key: str
    model: str
    memory_file: str


def load_settings() -> Settings:
    key = os.getenv("OPENAI_API_KEY", "").strip()
    if not key:
        raise RuntimeError(
            "OPENAI_API_KEY is missing. Copy .env.example to .env and add your key."
        )

    return Settings(
        openai_api_key=key,
        model=os.getenv("KOVA_MODEL", "gpt-5.6"),
        memory_file=os.getenv("KOVA_MEMORY_FILE", "data/memory.json"),
    )
