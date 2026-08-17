from kova.brain import KovaBrain
from kova.config import load_settings
from kova.memory import MemoryStore


def main() -> None:
    settings = load_settings()
    memory = MemoryStore(settings.memory_file)
    brain = KovaBrain(settings.openai_api_key, settings.model, memory)

    print("KOVA online.")
    print("Type 'exit' to shut down.")

    while True:
        try:
            user_text = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nKOVA: Shutting down.")
            break

        if not user_text:
            continue
        if user_text.lower() in {"exit", "quit", "shutdown"}:
            print("KOVA: Shutting down.")
            break

        try:
            print(f"KOVA: {brain.respond(user_text)}")
        except Exception as exc:
            print(f"KOVA: I hit an error: {exc}")


if __name__ == "__main__":
    main()
