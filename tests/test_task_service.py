import unittest
from app.services.task_service import TaskService


class TestTaskService(unittest.TestCase):

    def setUp(self):
        self.service = TaskService()
        self.service.tasks = []  # evita interferência do JSON

    def test_add_task(self):
        self.service.add_task("Estudar Python")
        self.assertEqual(len(self.service.tasks), 1)
        self.assertEqual(self.service.tasks[0].title, "Estudar Python")

    def test_remove_task(self):
        self.service.add_task("Tarefa 1")
        self.service.remove_task(0)
        self.assertEqual(len(self.service.tasks), 0)

    def test_toggle_task(self):
        self.service.add_task("Tarefa teste")
        self.service.toggle_task(0)
        self.assertTrue(self.service.tasks[0].completed)


if __name__ == "__main__":
    unittest.main()
