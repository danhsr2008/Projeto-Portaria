from tkinter import Tk, StringVar, Entry, Label, Button, END
import tkinter as tk


# Lista principal de mercadorias
MERCADORIAS = [
    "laranja", "manga", "batata", "batata doce", "cebola", "melancia",
    "coco seco", "abacate", "abobora", "alho", "beterraba", "cenoura",
    "inhame", "limao", "mamao", "maracuja", "melao", "mexerica",
    "bergamota", "repolho"
]

# Constantes
PESA = "PESA"
NAO_PESA = "NÃO PESA"
ERRO = "Entrada Inválida"
LIMPA = ""
VAZIO = ""


class Funcoes:
    """Classe com as funções principais da aplicação."""

    def __init__(self):
        self.entrada_1 = None
        self.entrada_2 = None
        self.label_1 = None

    def limpar_tela(self):
        """Limpa os campos de entrada."""
        self.entrada_1.delete(0, END)
        self.entrada_2.delete(0, END)
        var_especial.set(LIMPA)
        self.entrada_2.config(state="disabled")

    def habilitar_entrada(self):
        """Habilita o campo de entrada 2."""
        self.entrada_2.config(state="normal")

    def verificar_batido(self):
        """Verifica se a mercadoria está na lista."""
        mercadoria = self.entrada_1.get().lower()
        if mercadoria in MERCADORIAS:
            var_especial.set(PESA)
        else:
            var_especial.set(NAO_PESA)

    def consultar(self):
        """Verifica se a mercadoria e quantidade atendem aos critérios."""
        try:
            mercadoria = self.entrada_1.get().lower()
            quantidade = int(self.entrada_2.get())

            if mercadoria in MERCADORIAS:
                if quantidade >= 6:
                    var_especial.set(PESA)
                else:
                    var_especial.set(NAO_PESA)
            else:
                var_especial.set(NAO_PESA)
        except ValueError:
            var_especial.set(ERRO)


class Application(Funcoes):
    """Classe principal da aplicação."""

    def __init__(self):
        super().__init__()
        self.root = Tk()
        self.var_especial = StringVar()

        self.configurar_tela()
        self.criar_componentes()
        self.root.mainloop()

    def configurar_tela(self):
        """Configura a janela principal."""
        self.root.title("Relação de Peso - v1.1: Remastered 23_11_22")
        self.root.configure(background="#d9dbdc")
        self.root.geometry("940x500")
        self.root.resizable(False, False)

    def criar_componentes(self):
        """Cria os componentes da interface."""
        self.criar_labels()
        self.criar_entradas()
        self.criar_botoes()

    def criar_labels(self):
        """Cria os labels da interface."""
        Label(
            self.root, text="Mercadoria", font=("Roboto", 32), background="#d9dbdc"
        ).place(relx=0.35, rely=0.05, relwidth=0.3, relheight=0.09)

        Label(
            self.root, text="Qt. Paletes", font=("Roboto", 10), background="#d9dbdc"
        ).place(relx=0.46, rely=0.235, relwidth=0.08, relheight=0.09)

        self.label_1 = Label(
            self.root, bd=4, bg="#CDFFD4", highlightbackground="#015B00",
            highlightthickness=3, textvariable=var_especial,
            font=("Roboto", 32)
        )
        self.label_1.place(relx=0.02, rely=0.57, relwidth=0.96, relheight=0.4)

    def criar_entradas(self):
        """Cria os campos de entrada."""
        self.entrada_1 = Entry(self.root, width=25, font=("Roboto", 25))
        self.entrada_1.place(relx=0.245, rely=0.17)

        self.entrada_2 = Entry(self.root, width=25, font=("Roboto", 25))
        self.entrada_2.configure(disabledbackground="#d9dbdc", state="disabled")
        self.entrada_2.place(relx=0.45, rely=0.3, relwidth=0.1, relheight=0.06)

    def criar_botoes(self):
        """Cria os botões da interface."""
        Button(
            self.root, text="Limpar", command=self.limpar_tela, bg="#ffffff"
        ).place(relx=0.02, rely=0.5, relwidth=0.1, relheight=0.06)

        Button(
            self.root, text="Paletizado", command=self.habilitar_entrada
        ).place(relx=0.245, rely=0.3, relwidth=0.1, relheight=0.06)

        Button(
            self.root, text="Batido", command=self.verificar_batido
        ).place(relx=0.655, rely=0.3, relwidth=0.1, relheight=0.06)

        Button(
            self.root, text="Consultar", command=self.consultar
        ).place(relx=0.45, rely=0.43, relwidth=0.1, relheight=0.07)


# Variável global para a interface
var_especial = StringVar()

# Inicializa a aplicação
if __name__ == "__main__":
    Application()