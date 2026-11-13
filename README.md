# todo-cli_68

一个使用 Python 编写的命令行待办事项（To-Do List）小工具，支持事项的添加、查看、完成标记与删除，数据保存在本地 JSON 文件中。本项目为《开源文化运动》课程实践作业，按开源项目方式进行版本管理、文档维护与协作。

- **项目名称**：todo-cli_68（68 为学号后两位）
- **开发者**：LiuYuHang195
- **开发语言**：Python 3.10+（仅使用标准库，无第三方依赖）
- **许可证**：MIT License

## 功能特性

- `add`：添加一条待办事项，自动记录创建时间与编号；
- `list`：查看全部事项（含已完成与未完成）；
- `pending`：只查看尚未完成的事项；
- `done`：按编号把事项标记为已完成，记录完成时间；
- `delete`：按编号删除事项；
- 数据以 JSON 格式本地持久化，退出后不丢失。

## 环境要求

- Python 3.10 及以上版本；
- 无需安装第三方依赖，`requirements.txt` 已注明。

## 快速开始

在项目根目录下运行：

```bash
# 添加事项
python main.py add "完成开源报告初稿"
python main.py add "复习应用密码学"

# 查看全部 / 未完成事项
python main.py list
python main.py pending

# 标记完成、删除事项
python main.py done 1
python main.py delete 2
```

## 运行测试

```bash
python -m unittest discover -s tests -v
```

## 项目结构

```
todo-cli_68/
├── main.py              # 程序入口
├── requirements.txt     # 依赖说明（无第三方依赖）
├── README.md            # 项目说明文档
├── LICENSE              # MIT 许可证
├── .gitignore           # Git 忽略规则
├── todo/
│   ├── __init__.py
│   ├── models.py        # 待办事项数据模型
│   ├── storage.py       # JSON 本地存储
│   └── cli.py           # 命令行参数与交互逻辑
├── docs/
│   └── CONTRIBUTING.md   # 贡献指南与分支协作规范
└── tests/
    └── test_todo.py     # 单元测试
```

## 分支管理

项目采用 `main` 主干 + 功能分支的开发方式：

- `main`：稳定主干，随时可运行；
- `feature/*`：功能开发分支，开发完成后合并回 `main`；
- 多人或多分支协作时，若同一文件产生修改冲突，在合并阶段手动解决冲突后再提交。

具体协作规范见 [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)。

## 开源协作与互动

- 欢迎在 Issues 中提出功能建议、问题反馈与讨论；
- 如果本项目对你有帮助，欢迎 Star、Watch 关注更新；
- 贡献代码请先阅读贡献指南，再提交 Pull Request。

## 许可证

本项目基于 [MIT License](LICENSE) 开源，可自由使用、修改与再发布，请在衍生品中保留原始版权声明。

## 作者

- LiuYuHang195（成都信息工程大学，区块链工程专业）
