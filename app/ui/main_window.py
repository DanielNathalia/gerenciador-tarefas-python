import tkinter as tk
from app.services.task_service import TaskService


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gerenciador de Tarefas")
        self.root.geometry("400x500")

        self.service = TaskService()

        # frame superior
        top_frame = tk.Frame(self.root)
        top_frame.pack(fill=tk.X, pady=10, padx=10)

        self.entry = tk.Entry(top_frame)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.add_button = tk.Button(top_frame, text="Adicionar", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)

        # Frame central (lista)
        middle_frame = tk.Frame(self.root)
        middle_frame.pack(fill=tk.BOTH, expand=True, padx=10)

        scrollbar = tk.Scrollbar(middle_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(middle_frame, yscrollcommand=scrollbar.set)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        scrollbar.config(command=self.listbox.yview)

        self.delete_button = tk.Button(
            middle_frame, text="Excluir", command=self.delete_task
        )
        self.delete_button.pack(side=tk.RIGHT)

        self.root.bind("<Return>", lambda event: self.add_task())

        self.load_tasks()

    def add_task(self):
        title = self.entry.get().strip()
        if title:
            self.service.add_task(title)
            self.entry.delete(0, tk.END)
            self.load_tasks()

    def delete_task(self):
        selected_indices = self.listbox.curselection()
        if not selected_indices:
            return
        index = selected_indices[0]
        self.service.remove_task(index)
        self.load_tasks()

    def load_tasks(self):
        self.listbox.delete(0, tk.END)
        for task in self.service.get_tasks():
            self.listbox.insert(tk.END, task.title)

    def run(self):
        self.root.mainloop()
