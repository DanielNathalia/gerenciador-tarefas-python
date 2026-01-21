class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def toggle(self):
        self.completed = not self.completed

    def to_dict(self):
        return {
            "title": self.title,
            "completed": self.completed,
        }

    @staticmethod
    def from_dict(data):
        return Task(
            title=data["title"],
            completed=data.get("completed", False),
        )
