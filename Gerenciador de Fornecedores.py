from tkinter import *
import tkinter as tk
from tkinter import ttk, Scrollbar, font, messagebox
from tkinter.font import nametofont
import datetime

root = tk.Tk()


# hora = StringVar()


class funcoes:
    def __init__(self):
        self.hora = None
        self.data = None

    def cap_dados(self):

        if self.e_placa.get() == '' or self.e_placa.get() == ' ': # escrever match para os entrys
            messagebox.showerror(title='ERRO', message='Insira um dado válido')

            self.e_placa.delete(0, END)
            self.e_nome.delete(0, END)
            self.e_rg.delete(0, END)
            self.e_nota.delete(0, END)
            self.e_forn.delete(0, END)
            self.e_merc.delete(0, END)
            self.e_placa.focus()
            return False

        self.tree.insert(
            "", END, values=(self.data.get(), self.e_placa.get(),
                             self.e_nome.get(), self.e_rg.get(),
                             self.e_forn.get(), self.e_merc.get(),
                             self.e_nota.get(), self.hora.get()))
        ttk.Style().configure("Treeview", font=('Roboto', 12), rowheight=30, background='#d9dbdc', foreground='#000000')

        self.e_placa.delete(0, END)
        self.e_nome.delete(0, END)
        self.e_rg.delete(0, END)
        self.e_nota.delete(0, END)
        self.e_forn.delete(0, END)
        self.e_merc.delete(0, END)
        self.e_placa.focus()

    def delete_(self):
        try:
            item_selection = self.tree.selection()[0]
            self.tree.delete(item_selection)
        except IndexError:
            messagebox.showerror("Erro", "Selecione um item para deletar")

    def data_(self):
        while True:
            self.data = datetime.datetime.now()
            self.data = self.data.strftime("%d/%m")
            self.data = StringVar(value=self.data)
            self.root.after(1440000, self.data_)  # 1440000 = 24 horas
            break

    def hora_(self):
        while True:
            self.hora = datetime.datetime.now()
            self.hora = self.hora.strftime("%H:%M")
            self.hora = StringVar(value=self.hora)
            self.root.after(1000, self.hora_)  # 1000 = 1 minuto
            break


class Principal(funcoes):
    scroll: Scrollbar

    def __init__(self):
        super().__init__()
        self.b_2 = None
        self.t_2 = None
        self.t_3 = None
        self.t_4 = None
        self.t_5 = None
        self.t_6 = None
        self.e_merc = None
        self.e_forn = None
        self.e_nota = None
        self.b_1 = None
        self.root = root
        self.e_placa = None
        self.e_nome = None
        self.e_rg = None
        self.t_1 = None
        self.tree = None
        self.screen()
        self.entrys()
        self.botoes()
        self.tagg()
        self.treeview()
        self.data_()
        self.hora_()
        root.mainloop()

    def screen(self):
        self.root.title("Gerenciador de Fornecedores v_1.0")
        self.root.configure(background='#d9dbdc')
        self.root.geometry('1300x650')

    def entrys(self):
        self.e_placa = Entry(self.root, width=25, font=('Roboto', 23))  # PLACA
        self.e_placa.place(relx=0.1, rely=0.1, relwidth=0.15, relheight=0.05)

        self.e_nome = Entry(self.root, width=25, font=('Roboto', 23))  # NOME
        self.e_nome.place(relx=0.29, rely=0.1, relwidth=0.26, relheight=0.05)

        self.e_rg = Entry(self.root, width=25, font=('Roboto', 23))  # RG CPF
        self.e_rg.place(relx=0.59, rely=0.1, relwidth=0.22, relheight=0.05)
        #######################################################################################################
        self.e_nota = Entry(self.root, width=25, font=('Roboto', 23))  # NOTA
        self.e_nota.place(relx=0.1, rely=0.2, relwidth=0.15, relheight=0.05)

        self.e_forn = Entry(self.root, width=25, font=('Roboto', 23))  # FORNECEDOR
        self.e_forn.place(relx=0.29, rely=0.2, relwidth=0.26, relheight=0.05)

        self.e_merc = Entry(self.root, width=25, font=('Roboto', 23))  # MERCADORIA
        self.e_merc.place(relx=0.59, rely=0.2, relwidth=0.22, relheight=0.05)

    def botoes(self):
        self.b_1 = Button(self.root, text="Registrar", font=('Roboto', 10), background='#d9dbdc',
                          command=self.cap_dados)
        self.b_1.place(relx=0.84, rely=0.1, relwidth=0.06, relheight=0.05)

        self.b_2 = Button(self.root, text="Deletar", font=('Roboto', 10), background='#d9dbdc', command=self.delete_)
        self.b_2.place(relx=0.84, rely=0.2, relwidth=0.06, relheight=0.05)

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

        self.t_2 = Label(self.root, text="Nome", font=('Roboto', 10), background='#d9dbdc')  # nome
        self.t_2.place(relx=0.263, rely=0.069, relwidth=0.1, relheight=0.03)

        self.t_3 = Label(self.root, text="RG/CPF", font=('Roboto', 8), background='#d9dbdc')  # Rg cpf
        self.t_3.place(relx=0.565, rely=0.07, relwidth=0.1, relheight=0.03)

        self.t_4 = Label(self.root, text="Nota", font=('Roboto', 10), background='#d9dbdc')  # nota
        self.t_4.place(relx=0.068, rely=0.17, relwidth=0.1, relheight=0.03)

        self.t_5 = Label(self.root, text="Fornecedor", font=('Roboto', 10), background='#d9dbdc')  # fornecedor
        self.t_5.place(relx=0.275, rely=0.17, relwidth=0.1, relheight=0.03)

        self.t_6 = Label(self.root, text="Mercadoria", font=('Roboto', 10), background='#d9dbdc')  # mercadoria
        self.t_6.place(relx=0.574, rely=0.17, relwidth=0.1, relheight=0.03)

    def treeview(self):
        self.tree = ttk.Treeview(self.root, columns=(
            'Data', 'Placa', 'Nome', 'RG_CPF', 'Fornecedor', 'Mercadoria', 'Nota', 'Hora'),
                                 show='headings')
        '''style = ttk.Style()
        style.configure("Treeview.Heading", font=('Roboto', 11))'''
        nametofont("TkHeadingFont").configure(size=10, weight='bold')
        self.tree.heading("#0", text="")
        self.tree.heading("#1", text="Data")
        self.tree.heading("#2", text="Placa")
        self.tree.heading("#3", text="Nome")
        self.tree.heading("#4", text="RG/CPF")
        self.tree.heading("#5", text="Fornecedor")
        self.tree.heading("#6", text="Mercadoria")
        self.tree.heading("#7", text="Nota")
        self.tree.heading("#8", text="Hora")

        self.tree.column("#0", width=0)
        self.tree.column("#1", width=20)  # data
        self.tree.column("#2", width=30)  # placa
        self.tree.column("#3", width=100)  # nome
        self.tree.column("#4", width=100)  # rg_cpf
        self.tree.column("#5", width=150)  # fornecedor
        self.tree.column("#6", width=100)  # mercadoria
        self.tree.column("#7", width=100)  # nota
        self.tree.column("#8", width=40)  # hora

        self.tree.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.6)

        self.scroll = Scrollbar(self.tree, orient=VERTICAL)
        self.tree.configure(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.tree.yview)
        self.scroll.place(relx=0.979, rely=0.002, relwidth=0.02, relheight=0.995)


Principal()
