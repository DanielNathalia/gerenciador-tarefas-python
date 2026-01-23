import tkinter as tk
from app.services.task_service import TaskService
from tkinter import messagebox


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gerenciador de Tarefas")
        self.root.geometry("420x520")
        self.root.configure(bg="#f4f6f8")

        self.service = TaskService()

        self.create_frames()
        self.create_widgets()
        self.load_tasks()

        self.root.bind("<Return>", lambda event: self.add_task())
        self.listbox.bind("<Double-Button-1>", self.toggle_task)

    # ---------------- FRAMES ----------------
    def create_frames(self):
        self.top_frame = tk.Frame(self.root, bg="#f4f6f8")
        self.top_frame.pack(pady=15)

        self.middle_frame = tk.Frame(self.root, bg="#f4f6f8")
        self.middle_frame.pack(pady=10)

        self.bottom_frame = tk.Frame(self.root, bg="#f4f6f8")
        self.bottom_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

    # ---------------- WIDGETS ----------------
    def create_widgets(self):
        # Título
        self.title_label = tk.Label(
            self.top_frame,
            text="📝 Minhas Tarefas",
            font=("Segoe UI", 14, "bold"),
            bg="#f4f6f8",
            fg="#111827",
        )
        self.title_label.pack()

        # Entry
        self.entry = tk.Entry(
            self.middle_frame,
            width=30,
            font=("Segoe UI", 10),
        )
        self.entry.pack(side=tk.LEFT, padx=5)

        # Botão adicionar
        self.add_button = tk.Button(
            self.middle_frame,
            text="Adicionar",
            command=self.add_task,
            bg="#4f46e5",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            relief=tk.FLAT,
            padx=10,
            pady=5,
        )
        self.add_button.pack(side=tk.LEFT)

        # Botão Excluir
        self.delete_button = tk.Button(
            self.middle_frame,
            text="Excluir",
            command=self.delete_task,
            bg="#ef4444",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            relief=tk.FLAT,
            padx=10,
            pady=5,
        )
        self.delete_button.pack(side=tk.LEFT, padx=5)

        # Listbox + Scrollbar
        self.scrollbar = tk.Scrollbar(self.bottom_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(
            self.bottom_frame,
            font=("Segoe UI", 10),
            yscrollcommand=self.scrollbar.set,
            selectbackground="#c7d2fe",
            activestyle="none",
        )
        self.listbox.pack(fill=tk.BOTH, expand=True)

        self.scrollbar.config(command=self.listbox.yview)

    # ---------------- AÇÕES ----------------
    def add_task(self):
        title = self.entry.get().strip()

        if title:
            self.service.add_task(title)
            self.entry.delete(0, tk.END)
            self.load_tasks()

    def load_tasks(self):
        self.listbox.delete(0, tk.END)

        for index, task in enumerate(self.service.get_tasks()):
            title = task.title

            if task.completed:
                title = f"✔ {title}"

            self.listbox.insert(tk.END, title)

            if task.completed:
                self.listbox.itemconfig(index, fg="#9ca3af")  # cinza

    def delete_task(self):
        selected = self.listbox.curselection()
        if not selected:
            return

        index = selected[0]

        confirm = messagebox.askyesno(
            "Excluir tarefa", "Tem certeza que deseja excluir esta tarefa?"
        )

        if confirm:
            self.service.remove_task(index)
            self.load_tasks()

    def toggle_task(self, event):
        selected = self.listbox.curselection()
        if not selected:
            return

        index = selected[0]
        self.service.toggle_task(index)
        self.load_tasks()

    def run(self):
        self.root.mainloop()
