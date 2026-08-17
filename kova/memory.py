import json
from pathlib import Path
from typing import Any


class MemoryStore:
    """Small local JSON memory store for the first KOVA prototype."""

    def __init__(self, path: str):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.data: dict[str, Any] = self._load()

    def _load(self) -> dict[str, Any]:
        if not self.path.exists():
            return {"facts": [], "messages": []}
        try:
            return json.loads(self.path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return {"facts": [], "messages": []}

    def add_message(self, role: str, content: str) -> None:
        self.data.setdefault("messages", []).append({"role": role, "content": content})
        # Keep the first prototype lightweight.
        self.data["messages"] = self.data["messages"][-40:]
        self.save()

    def add_fact(self, fact: str) -> None:
        fact = fact.strip()
        if fact and fact not in self.data.setdefault("facts", []):
            self.data["facts"].append(fact)
            self.save()

    def recent_messages(self, limit: int = 20) -> list[dict[str, str]]:
        return self.data.get("messages", [])[-limit:]

    def facts(self) -> list[str]:
        return list(self.data.get("facts", []))

    def save(self) -> None:
        self.path.write_text(json.dumps(self.data, indent=2), encoding="utf-8")
