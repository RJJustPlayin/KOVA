import tempfile
import unittest
from pathlib import Path

from kova.memory import MemoryStore


class MemoryStoreTests(unittest.TestCase):
    def test_messages_and_facts_persist(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = str(Path(tmp) / "memory.json")
            memory = MemoryStore(path)
            memory.add_message("user", "Hello KOVA")
            memory.add_fact("User likes KOVA")

            loaded = MemoryStore(path)
            self.assertEqual(loaded.recent_messages(), [{"role": "user", "content": "Hello KOVA"}])
            self.assertEqual(loaded.facts(), ["User likes KOVA"])


if __name__ == "__main__":
    unittest.main()
