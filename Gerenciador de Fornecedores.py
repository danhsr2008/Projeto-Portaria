from tkinter import *
import tkinter as tk
from tkinter import ttk, Scrollbar, font
from tkinter.font import nametofont

root = tk.Tk()

dados = [[]]


class funcoes:
    # def __init__(self):
    def cap_dados(self):
        self.tree.insert(
            "", END, values=(self.e_1.get(),
                               self.e_2.get(), self.e_3.get(),
                               self.e_5.get(), self.e_6.get(), self.e_4.get()))
        ttk.Style().configure("Treeview", font=('Roboto', 10), rowheight=30, background='#d9dbdc', foreground='#000000', fieldbackground='#d9dbdc', bordercolor='#d9dbdc', highlightthickness=0, borderwidth=0, relief='flat')



class Principal(funcoes):
    scroll: Scrollbar

    def __init__(self):
        self.e_6 = None
        self.e_5 = None
        self.e_4 = None
        self.b_1 = None
        self.root = root
        self.e_1 = None
        self.e_2 = None
        self.e_3 = None
        self.t_1 = None
        self.tree = None
        self.screen()
        self.entrys()
        self.botoes()
        self.tagg()
        self.treeview()
        root.mainloop()

    def screen(self):
        self.root.title("Gerenciador de Fornecedores v_1.0")
        self.root.configure(background='#d9dbdc')
        self.root.geometry('1300x650')


    def entrys(self):
        self.e_1 = Entry(self.root, width=25, font=('Roboto', 23))  # PLACA
        self.e_1.place(relx=0.1, rely=0.1, relwidth=0.15, relheight=0.05)

        self.e_2 = Entry(self.root, width=25, font=('Roboto', 23))  # NOME
        self.e_2.place(relx=0.29, rely=0.1, relwidth=0.26, relheight=0.05)

        self.e_3 = Entry(self.root, width=25, font=('Roboto', 23))  # RG CPF
        self.e_3.place(relx=0.59, rely=0.1, relwidth=0.24, relheight=0.05)
        #######################################################################################################
        self.e_4 = Entry(self.root, width=25, font=('Roboto', 23))  # NOTA
        self.e_4.place(relx=0.1, rely=0.2, relwidth=0.15, relheight=0.05)

        self.e_5 = Entry(self.root, width=25, font=('Roboto', 23))  # FORNECEDOR
        self.e_5.place(relx=0.29, rely=0.2, relwidth=0.26, relheight=0.05)

        self.e_6 = Entry(self.root, width=25, font=('Roboto', 23))  # MERCADORIA
        self.e_6.place(relx=0.59, rely=0.2, relwidth=0.24, relheight=0.05)

    def botoes(self):
        self.b_1 = Button(self.root, text="Registrar", font=('Roboto', 10), background='#d9dbdc',
                          command=self.cap_dados)
        self.b_1.place(relx=0.85, rely=0.15, relwidth=0.06, relheight=0.05)

    def tagg(self):
        self.t_1 = Label(self.root, text="Placa", font=('Roboto', 10), background='#d9dbdc')  # placa
        self.t_1.place(relx=0.068, rely=0.069, relwidth=0.1, relheight=0.03)

        self.t_1 = Label(self.root, text="Nome", font=('Roboto', 10), background='#d9dbdc')  # nome
        self.t_1.place(relx=0.26, rely=0.069, relwidth=0.1, relheight=0.03)

        self.t_1 = Label(self.root, text="RG/CPF", font=('Roboto', 8), background='#d9dbdc')  # Rg cpf
        self.t_1.place(relx=0.56, rely=0.07, relwidth=0.1, relheight=0.03)

        self.t_1 = Label(self.root, text="Nota", font=('Roboto', 10), background='#d9dbdc')  # nota
        self.t_1.place(relx=0.065, rely=0.17, relwidth=0.1, relheight=0.03)

        self.t_1 = Label(self.root, text="Fornecedor", font=('Roboto', 10), background='#d9dbdc')  # fornecedor
        self.t_1.place(relx=0.27, rely=0.17, relwidth=0.1, relheight=0.03)

        self.t_1 = Label(self.root, text="Mercadoria", font=('Roboto', 10), background='#d9dbdc')  # mercadoria
        self.t_1.place(relx=0.57, rely=0.17, relwidth=0.1, relheight=0.03)

    def treeview(self):
        self.tree = ttk.Treeview(self.root, columns=('Placa', 'Nome', 'RG_CPF', 'Fornecedor', 'Mercadoria', 'Nota'),
                                 show='headings')
        '''style = ttk.Style()
        style.configure("Treeview.Heading", font=('Roboto', 11))'''
        nametofont("TkHeadingFont").configure(size=10, weight='bold')
        self.tree.heading("#0", text="")
        self.tree.heading("#1", text="Placa")
        self.tree.heading("#2", text="Nome")
        self.tree.heading("#3", text="RG/CPF")
        self.tree.heading("#4", text="Fornecedor")
        self.tree.heading("#5", text="Mercadoria")
        self.tree.heading("#6", text="Nota")

        self.tree.column("#0", width=1)
        self.tree.column("#1", width=100)
        self.tree.column("#2", width=200)
        self.tree.column("#3", width=100)
        self.tree.column("#4", width=200)
        self.tree.column("#5", width=200)
        self.tree.column("#6", width=100)

        self.tree.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.6)

        self.scroll = Scrollbar(self.tree, orient=VERTICAL)
        self.tree.configure(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.tree.yview)
        self.scroll.place(relx=0.979, rely=0.002, relwidth=0.02, relheight=0.995)


Principal()
