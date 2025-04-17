import tkinter as tk
from tkinter import ttk


class MinimalistaApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Controle de Acesso - Minimalista")
        self.root.geometry("900x500")
        self.root.configure(bg="#f5f5f5")  # Cor de fundo suave

        self.setup_layout()

    def setup_layout(self):
        # Título
        title_label = tk.Label(
            self.root,
            text="Gerenciador de Fornecedores",
            font=("Helvetica", 20, "bold"),
            fg="#333",
            bg="#f5f5f5"
        )
        title_label.pack(pady=20)

        # Frame principal
        main_frame = tk.Frame(self.root, bg="#ffffff", bd=2, relief="groove")
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Entradas e Rótulos
        entry_frame = tk.Frame(main_frame, bg="#ffffff")
        entry_frame.pack(pady=20)

        labels = ["Placa", "Nome", "RG/CPF", "Nota", "Fornecedor", "Mercadoria"]
        self.entries = []

        for i, label_text in enumerate(labels):
            label = tk.Label(
                entry_frame,
                text=label_text,
                font=("Helvetica", 12),
                bg="#ffffff",
                fg="#555"
            )
            label.grid(row=i, column=0, sticky="w", padx=10, pady=5)

            entry = tk.Entry(
                entry_frame,
                font=("Helvetica", 12),
                bd=1,
                relief="solid",
                width=30
            )
            entry.grid(row=i, column=1, pady=5, padx=10)
            self.entries.append(entry)

        # Botão de registro
        register_button = tk.Button(
            main_frame,
            text="Registrar",
            font=("Helvetica", 12, "bold"),
            bg="#4caf50",
            fg="#fff",
            bd=0,
            relief="flat",
            command=self.on_register_click
        )
        register_button.pack(pady=10)

        # Tabela
        self.tree = ttk.Treeview(
            main_frame,
            columns=("Placa", "Nome", "RG/CPF", "Nota", "Fornecedor", "Mercadoria"),
            show="headings",
            height=8
        )
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Estilo da tabela
        style = ttk.Style()
        style.configure("Treeview", font=("Helvetica", 11), rowheight=25)
        style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor="center")

        # Barra de rolagem
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

    def on_register_click(self):
        # Insere os valores das entradas na tabela
        values = [entry.get() for entry in self.entries]
        if all(values):
            self.tree.insert("", "end", values=values)
            for entry in self.entries:
                entry.delete(0, tk.END)
        else:
            print("Preencha todos os campos!")  # Aqui você pode usar messagebox para um alerta.

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = MinimalistaApp()
    app.run()