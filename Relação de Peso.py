from tkinter import *
import tkinter as tk
from tkinter import IntVar, Entry, Label
from time import sleep

root = tk.Tk()

# LOCAL RESERVADO PAR AVARIAVEIS GLOBAIS
var_especial = tk.StringVar()  # usar classe com self
pesa = "PESA"
nao_pesa = "NÃO PESA"
erro = 'Entrada Inválida'
limpa = ''
vazio= ''

# estrutura principal
lista_main = ["laranja", "manga", "batata", "batata doce",
              "cebola", "melancia", "coco seco", "abacate",
              "abobora", "alho", "beterraba", "cenoura",
              "inhame", "limao", "mamao", "maracuja",
              "melao", "mexerica", "bergamota", "repolho"]


# classes para botoes, labels e entradas

class funcoes:
    def __init__(self):
        self.label_1 = None

    def limpa_tela(self):
        self.entrada_1.delete(0, END)
        self.entrada_2.delete(0, END)
        var_especial.set(limpa)
        self.entrada_2.config(state='disabled')

    def disable_entry(self):
        self.entrada_2.config(state="normal")

    def changeOnHover(self, colorOnHover, colorOnLeave):
        self.bind("<Enter>", func=lambda e: self.config(
            background=colorOnHover
        ))
        self.bind("<Leave>", func=lambda e: self.config(
            background=colorOnLeave
        ))

        return colorOnHover

    def bot_batido(self):
        botao_batido = self.entrada_1.get().lower()
        if botao_batido in lista_main:
            return var_especial.set(pesa)
        else:
            return var_especial.set(nao_pesa)

    def cons(self):
        while True:
            try:
                e_1 = self.entrada_1.get().lower()
                e_2 = int(self.entrada_2.get())  # pega a entrada do usuario, e converte em inteiro
                if e_1 in lista_main:
                    if e_2 >= 6:
                        return var_especial.set(pesa)
                    elif e_1 == None:
                        return var_especial.set(vazio)
                    else:
                        return var_especial.set(nao_pesa)
                else:
                    return var_especial.set(nao_pesa)
            except ValueError:
                return var_especial.set(erro)


class Application(funcoes):
    def __init__(self):
        super().__init__()
        self.bt_consultar = None
        self.bt_batido = None
        self.bt_limpar = None
        self.texto_2 = None
        self.texto_1 = None
        self.bt_palet = None
        self.entrada_2 = None
        self.entrada_1 = None
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.bot_limpar()
        self.label_txt()
        self.entradas()
        root.mainloop()

    def tela(self):
        self.root.title("Relação de Peso. v_1.1: Remastered 23_11_22")
        self.root.configure(background='#d9dbdc')
        self.root.geometry('940x500')
        self.root.resizable(False, False)

    def frames_da_tela(self):
        self.label_1 = Label(self.root, bd=4, bg='#CDFFD4', highlightbackground='#015B00', highlightthickness=3,
                             textvariable=var_especial, font=("Roboto", 32))
        self.label_1.place(relx=0.02, rely=0.57, relwidth=0.96, relheight=0.4)

    def bot_limpar(self):
        # botao limpar
        self.bt_limpar = Button(self.root, text='Limpar', command=self.limpa_tela, bg='#ffffff')
        self.bt_limpar.place(relx=0.02, rely=0.5, relwidth=0.1, relheight=0.06)
        # botao paletizado
        self.bt_palet = Button(self.root, text='Paletizado', command=self.disable_entry)
        self.bt_palet.place(relx=0.245, rely=0.3, relwidth=0.1, relheight=0.06)
        # botao Batido
        self.bt_batido = Button(self.root, text='Batido', command=self.bot_batido)
        self.bt_batido.place(relx=0.655, rely=0.3, relwidth=0.1, relheight=0.06)
        # botao consultar
        self.bt_consultar = Button(self.root, text='Consultar', command=self.cons)
        self.bt_consultar.place(relx=0.45, rely=0.43, relwidth=0.1, relheight=0.07)

    def label_txt(self):
        self.texto_1 = Label(self.root, text="Mercadoria", font=("Roboto", 32), background='#d9dbdc')
        self.texto_1.place(relx=0.35, rely=0.05, relwidth=0.3, relheight=0.09)
        self.texto_2 = Label(self.root, text='Qt. Paletes', font=('Roboto', 10), background='#d9dbdc')
        self.texto_2.place(relx=0.46, rely=0.235, relwidth=0.08, relheight=0.09)

    def entradas(self):
        # Entrada maior
        self.entrada_1 = Entry(self.root, width=25, font=('Roboto', 25))
        self.entrada_1.place(relx=0.245, rely=0.17)
        # Entrada menor
        self.entrada_2 = Entry(self.root, width=25, font=('Roboto', 25))
        self.entrada_2.configure(disabledbackground='#d9dbdc', state='disabled')
        self.entrada_2.place(relx=0.45, rely=0.3, relwidth=0.1, relheight=0.06)


# finaliza janela


Application()
