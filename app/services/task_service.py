import json
import os
from app.models.task import Task


class TaskService:
    def __init__(self):
        self.tasks = []

        root_dir = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )

        self.file_path = os.path.join(root_dir, "data", "tasks.json")

        # 🔥 CRIA A PASTA data SE NÃO EXISTIR
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        self.load_tasks()

    def add_task(self, title):
        self.tasks.append(Task(title))
        self.save_tasks()

    def get_tasks(self):
        return self.tasks

    def save_tasks(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(
                [task.to_dict() for task in self.tasks],
                file,
                ensure_ascii=False,
                indent=4,
            )

    def load_tasks(self):
        if not os.path.exists(self.file_path):
            return

        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            self.tasks = [Task.from_dict(item) for item in data]

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()
