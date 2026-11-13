"""待办事项数据模型。"""

from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class TodoItem:
    """单条待办事项。"""

    id: int
    title: str
    done: bool = False
    created_at: str = ""
    finished_at: str = ""

    def mark_done(self) -> None:
        """标记为已完成，并记录完成时间。"""
        self.done = True
        self.finished_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "TodoItem":
        return cls(**data)
