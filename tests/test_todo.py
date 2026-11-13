"""todo-cli 单元测试。"""

import os
import unittest

from todo.models import TodoItem
from todo.storage import Storage


class TestTodo(unittest.TestCase):
    def setUp(self) -> None:
        self.path = "test_todos.json"
        if os.path.exists(self.path):
            os.remove(self.path)
        self.storage = Storage(self.path)

    def tearDown(self) -> None:
        if os.path.exists(self.path):
            os.remove(self.path)

    def test_add_and_load(self) -> None:
        items = self.storage.load()
        items.append(
            TodoItem(id=1, title="写报告", created_at="2026-11-13 10:00:00")
        )
        self.storage.save(items)
        loaded = self.storage.load()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].title, "写报告")

    def test_mark_done(self) -> None:
        item = TodoItem(id=1, title="测试", created_at="2026-11-13 10:00:00")
        item.mark_done()
        self.assertTrue(item.done)
        self.assertTrue(item.finished_at)

    def test_priority_default(self) -> None:
        item = TodoItem(id=1, title="优先级", created_at="2026-11-13 10:00:00")
        self.assertEqual(item.priority, "normal")


if __name__ == "__main__":
    unittest.main()
