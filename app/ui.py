import tkinter as tk

def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa:
        lista_tarefas.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)

# Janela principal
root = tk.Tk()
root.title("Gerenciador de Tarefas")

# Campo de entrada
entrada_tarefa = tk.Entry(root, width=40)
entrada_tarefa.pack(pady=10)

# Botão para adicionar tarefa
btn_adicionar = tk.Button(root, text="Adicionar Tarefa", command=adicionar_tarefa)
btn_adicionar.pack(pady=5)

# Lista de tarefas
lista_tarefas = tk.Listbox(root, width=50, height=10)
lista_tarefas.pack(pady=10)

# Iniciar o loop da interface
root.mainloop()