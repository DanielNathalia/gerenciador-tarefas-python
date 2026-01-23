class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def toggle(self):
        self.completed = not self.completed

    def to_dict(self):
        return {"title": self.title, "completed": self.completed}

    @classmethod
    def from_dict(cls, data):
        return cls(title=data["title"], completed=data.get("completed", False))
