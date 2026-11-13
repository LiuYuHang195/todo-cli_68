"""命令行交互入口。"""

import argparse
from datetime import datetime

from todo.models import TodoItem
from todo.storage import Storage


def next_id(items: list[TodoItem]) -> int:
    return (max(item.id for item in items) + 1) if items else 1


def add(storage: Storage, title: str) -> None:
    items = storage.load()
    item = TodoItem(
        id=next_id(items),
        title=title,
        created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )
    items.append(item)
    storage.save(items)
    print(f"已添加：[{item.id}] {item.title}")


def list_items(storage: Storage, show_all: bool = True) -> None:
    items = storage.load()
    if not show_all:
        items = [item for item in items if not item.done]
    if not items:
        print("暂无待办事项。")
        return
    for item in items:
        status = "✓" if item.done else " "
        suffix = f"（完成于 {item.finished_at}）" if item.done else ""
        print(f"[{status}] #{item.id} {item.title}{suffix}")


def done(storage: Storage, item_id: int) -> None:
    items = storage.load()
    for item in items:
        if item.id == item_id:
            item.mark_done()
            storage.save(items)
            print(f"已完成：[{item.id}] {item.title}")
            return
    print(f"未找到编号 {item_id} 的事项。")


def delete(storage: Storage, item_id: int) -> None:
    items = storage.load()
    remaining = [item for item in items if item.id != item_id]
    if len(remaining) == len(items):
        print(f"未找到编号 {item_id} 的事项。")
        return
    storage.save(remaining)
    print(f"已删除：[{item_id}]")


def main() -> None:
    parser = argparse.ArgumentParser(description="todo-cli 命令行待办清单")
    sub = parser.add_subparsers(dest="command")

    p_add = sub.add_parser("add", help="添加待办事项")
    p_add.add_argument("title", help="事项内容")

    sub.add_parser("list", help="查看全部事项")
    sub.add_parser("pending", help="查看未完成事项")

    p_done = sub.add_parser("done", help="标记事项完成")
    p_done.add_argument("id", type=int)

    p_del = sub.add_parser("delete", help="删除事项")
    p_del.add_argument("id", type=int)

    args = parser.parse_args()
    storage = Storage()

    if args.command == "add":
        add(storage, args.title)
    elif args.command == "list":
        list_items(storage)
    elif args.command == "pending":
        list_items(storage, show_all=False)
    elif args.command == "done":
        done(storage, args.id)
    elif args.command == "delete":
        delete(storage, args.id)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
