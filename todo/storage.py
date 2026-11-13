"""基于 JSON 文件的本地存储。"""

import json
import os

from todo.models import TodoItem


class Storage:
    """把待办事项读写到本地 JSON 文件。"""

    def __init__(self, path: str = "todos.json") -> None:
        self.path = path

    def load(self) -> list[TodoItem]:
        if not os.path.exists(self.path):
            return []
        with open(self.path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [TodoItem.from_dict(item) for item in data]

    def save(self, items: list[TodoItem]) -> None:
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump([item.to_dict() for item in items], f, ensure_ascii=False, indent=2)
