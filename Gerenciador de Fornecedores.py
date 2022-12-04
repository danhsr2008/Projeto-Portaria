from tkinter import *
import tkinter as tk


root = tk.Tk()


class Principal:
    def __init__(self):
        self.root = root
        self.screen()
        self.entrys()
        self.tagg()
        root.mainloop()

    def screen(self):
        self.root.title("Gerenciador de Fornecedores v_1.0")
        self.root.configure(background = '#d9dbdc')
        self.root.geometry('940x500')

    def entrys(self):
        self.e_1 = Entry(self.root, width = 25, font = ('Roboto', 23)) # PLACA
        self.e_1.place(relx= 0.1, rely= 0.1, relwidth=0.15, relheight=0.05)

        self.e_2 = Entry(self.root, width = 25, font = ('Roboto', 23)) # NOME
        self.e_2.place(relx= 0.29, rely= 0.1, relwidth= 0.26, relheight= 0.05)

        self.e_3 = Entry(self.root, width= 25, font= ('Roboto', 23)) # RG CPF
        self.e_3.place(relx= 0.59, rely= 0.1, relwidth= 0.24, relheight= 0.05)
#######################################################################################################
        self.e_1 = Entry(self.root, width=25, font=('Roboto', 23)) # NOTA
        self.e_1.place(relx=0.1, rely=0.2, relwidth=0.15, relheight=0.05)

        self.e_2 = Entry(self.root, width=25, font=('Roboto', 23)) # FORNECEDOR
        self.e_2.place(relx=0.29, rely=0.2, relwidth=0.26, relheight=0.05)

        self.e_3 = Entry(self.root, width=25, font=('Roboto', 23)) # MERCADORIA
        self.e_3.place(relx=0.59, rely=0.2, relwidth=0.24, relheight=0.05)

    def tagg(self):
        self.t_1 = Label(self.root, text= "Placa", font= ('Roboto', 10), background= '#d9dbdc') # placa
        self.t_1.place(relx= 0.068, rely= 0.069, relwidth= 0.1, relheight= 0.03)

        self.t_1 = Label(self.root, text="Nome", font=('Roboto', 10), background='#d9dbdc')  # nome
        self.t_1.place(relx=0.263, rely=0.069, relwidth=0.1, relheight=0.03)

        self.t_1 = Label(self.root, text="RG/CPF", font=('Roboto', 8), background='#d9dbdc')  # Rg cpf
        self.t_1.place(relx=0.565, rely=0.07, relwidth=0.1, relheight=0.03)

        self.t_1 = Label(self.root, text="Nota", font=('Roboto', 10), background='#d9dbdc')  # nota
        self.t_1.place(relx=0.068, rely=0.17, relwidth=0.1, relheight=0.03)

        self.t_1 = Label(self.root, text="Fornecedor", font=('Roboto', 10), background='#d9dbdc')  # fornecedor
        self.t_1.place(relx=0.275, rely=0.17, relwidth=0.1, relheight=0.03)

        self.t_1 = Label(self.root, text="Mercadoria", font=('Roboto', 10), background='#d9dbdc')  # mercadoria
        self.t_1.place(relx=0.574, rely=0.17, relwidth=0.1, relheight=0.03)

Principal()