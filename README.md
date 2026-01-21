# 📝 Gerenciador de Tarefas em Python (Tkinter)

Aplicação desktop desenvolvida em Python utilizando **Tkinter**, com foco em organização de tarefas, persistência de dados e arquitetura em camadas.

Este projeto foi criado com fins de estudo e portfólio, aplicando boas práticas de organização de código, orientação a objetos e versionamento com Git.

---

## 🚀 Funcionalidades

- ✅ Adicionar tarefas
- 🗑️ Excluir tarefas
- ✔️ Marcar tarefas como concluídas (duplo clique)
- 💾 Persistência de dados em arquivo JSON
- 📜 Lista de tarefas com scrollbar
- ⌨️ Atalho com tecla **Enter** para adicionar tarefas

---

## 🧱 Arquitetura do Projeto

O projeto segue uma arquitetura em camadas, separando responsabilidades de forma clara:

gerenciador-tarefas-python/
│
├── app/
│ ├── models/ # Modelos de dados
│ ├── services/ # Regras de negócio e persistência
│ ├── ui/ # Interface gráfica (Tkinter)
│ └── main.py # Ponto de entrada da aplicação
│
├── data/
│ └── tasks.json # Armazenamento das tarefas
│
├── tests/ # Testes automatizados
│
└── README.md


---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Tkinter
- JSON
- Git e GitHub
- unittest (testes automatizados)

---

## ▶️ Como Executar o Projeto

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/DanielNathalia/gerenciador-tarefas-python.git
cd gerenciador-tarefas-python
