from tkinter import *
import tkinter as tk
from tkinter import ttk, Scrollbar, font, messagebox
from tkinter.font import nametofont
import datetime
import pyperclip as pc
import time

root = tk.Tk()


class funcoes:

    def __init__(self):
        self.info_window = None
        self.hora_label = None
        self.pop_menu_mnu = None
        self.dados = None
        self.hora = None
        self.data = None
        self.root = root
        self.root.bind("<Button-1>", lambda event: self.unselect(event))
        self.hora = StringVar()

    def cap_dados(self):
        dados = [
            self.e_placa.get(), self.e_nome.get(),
            self.e_nota.get(), self.e_forn.get(), self.e_merc.get()
        ]
        try:
            for item in dados:
                if item == '':
                    messagebox.showinfo("Erro", "Algum Campo Vazio!\n\nPreencha o campo com \"ESPAÇO\" se não houver")
                    self.limpar()
                    return False
                else:
                    pass
        except IndexError:
            pass
            return False

        self.tree.insert(
            "", END, values=(self.data.get(), self.e_placa.get().upper(),
                             self.e_nome.get().upper(), self.e_rg.get().upper(),
                             self.e_forn.get().upper(), self.e_merc.get().upper(),
                             self.e_nota.get().upper(), self.hora.get()))
        ttk.Style().configure("Treeview", font=('Roboto', 11), rowheight=30, background='#d9dbdc', foreground='#000000')

        self.limpar()

    def delete_(self):
        try:
            item_selection = self.tree.selection()[0]
            self.tree.delete(item_selection)
        except IndexError:
            messagebox.showerror("Erro", "Selecione um item para deletar")

    def limpar(self):
        self.e_placa.delete(0, END)
        self.e_nome.delete(0, END)
        self.e_rg.delete(0, END)
        self.e_nota.delete(0, END)
        self.e_forn.delete(0, END)
        self.e_merc.delete(0, END)
        self.e_placa.focus()

    def data_(self):
        while True:
            self.data = datetime.datetime.now()
            self.data = self.data.strftime("%d/%m")
            self.data = StringVar(value=self.data)
            self.root.after(86400000, self.data_)  # 86400000 = 24 horas
            break

    def hora_(self):
        while True:
            self.hora = datetime.datetime.now()
            self.hora = self.hora.strftime("%H:%M")
            self.hora = StringVar(value=self.hora)
            self.root.after(60000, self.hora_)  # 60000 = 1 minuto
            break

    # MENU POPUP
    def pop_menu(self):
        self.pop_menu_mnu = tk.Menu(self.root, tearoff=0)
        self.pop_menu_mnu.add_command(label='Copiar', command=self.copy_paste)  # copia o item selecionado
        self.pop_menu_mnu.add_command(label="Autorizado/Agendado", command=self.autorizado)
        self.pop_menu_mnu.add_command(label='Liberado Pelo Conferente', command=self.liberado)
        self.pop_menu_mnu.add_command(label='Cancelar/Reprovado', command=self.cancelado)
        self.pop_menu_mnu.add_command(label='Deletar', command=self.delete_)
        self.pop_menu_mnu.add_command(label='Linkar', command=self.copy_paste)
        self.pop_menu_mnu.add_command(label='Informações', command=self.mostrar_informacoes)

    def popup_menu_method(self, event):
        try:
            self.pop_menu_mnu.tk_popup(event.x_root, event.y_root)
        finally:
            self.pop_menu_mnu.grab_release()

    def autorizado(self):
        item_selection = self.tree.selection()
        self.tree.tag_configure('azul', background='#9bb0ff')
        self.tree.item(item_selection, tags=('azul',))

    def mostrar_informacoes(self):
        # Get the selected item
        selecionado = self.tree.selection()
        if not selecionado:
            # No item selected, do nothing
            return

        # Get the information about the selected item
        informacoes = self.tree.item(selecionado)['values']


        # Create a window to display the information
        self.info_window = tk.Toplevel(self.root)
        self.info_window.title("Informações")
        self.info_window.geometry("300x200")  # Set window size
        self.info_window.geometry("+{}+{}".format(self.root.winfo_screenwidth() // 2 - 150,
                                                  self.root.winfo_screenheight() // 2 - 100))  # Center window on screen

        # Create a series of labels with the information
        data_label = tk.Label(self.info_window, text="Data: {}".format(informacoes[0]))
        placa_label = tk.Label(self.info_window, text="Placa: {}".format(informacoes[1]))
        nome_label = tk.Label(self.info_window, text="Nome: {}".format(informacoes[2]))
        rg_cpf_label = tk.Label(self.info_window, text="RG/CPF: {}".format(informacoes[3]))
        fornecedor_label = tk.Label(self.info_window, text="Fornecedor: {}".format(informacoes[4]))
        mercadoria_label = tk.Label(self.info_window, text="Mercadoria: {}".format(informacoes[5]))
        nota_label = tk.Label(self.info_window, text="Nota: {}".format(informacoes[6]))
        hora_label = tk.Label(self.info_window, text="Hora Chegada: {}".format(informacoes[7]))

        # Display the labels in the toplevel window
        data_label.pack()
        placa_label.pack()
        nome_label.pack()
        rg_cpf_label.pack()
        fornecedor_label.pack()
        mercadoria_label.pack()
        nota_label.pack()
        hora_label.pack()

    def copy_paste(self):
        try:
            # convertendo o ‘item’ selecionado em string
            item_selection = self.tree.selection()[0]
            item_selection = self.tree.item(item_selection, 'values')
            item_selection = str(item_selection)
            item_selection = item_selection.replace("'", "")
            item_selection = item_selection.replace("(", "")
            item_selection = item_selection.replace(")", "")
            item = item_selection
            pc.copy(item)
        except IndexError:
            messagebox.showerror("Erro", "Selecione um item para copiar")

    def unselect(self, event):
        try:
            if self.tree.identify_row(event.y) == "":
                self.tree.selection_remove(self.tree.selection()[0])
            else:
                pass
        except IndexError:
            pass

    def liberado(self):
        self.tree.item(self.tree.selection()[0], tags=('verde',))
        self.tree.tag_configure('verde', background='#98dd84')

    def cancelado(self):
        self.tree.item(self.tree.selection()[0], tags=('cinza',))
        self.tree.tag_configure('cinza', background='#656565', foreground='#ffffff')


class Principal(funcoes):
    scroll: Scrollbar

    def __init__(self):
        super().__init__()

        self.m_1 = None
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
        self.root.title("Controle de Acesso - V1.0")
        self.root.configure(background='#d9dbdc')
        self.root.geometry('1300x650')

        # ----- menu popup -----
        self.pop_menu()
        self.root.bind('<Button-3>', self.popup_menu_method)  # Criar uma def. para binds

    def entrys(self):
        self.e_placa = Entry(self.root, width=25, font=('Roboto', 23))  # PLACA
        self.e_placa.place(relx=0.1, rely=0.1, relwidth=0.15, relheight=0.05)

        self.e_nome = Entry(self.root, width=25, font=('Roboto', 23))  # NOME
        self.e_nome.place(relx=0.29, rely=0.1, relwidth=0.26, relheight=0.05)

        self.e_rg = Entry(self.root, width=25, font=('Roboto', 23))  # RG CPF
        self.e_rg.place(relx=0.59, rely=0.1, relwidth=0.22, relheight=0.05)

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
        column_names = ('Data', 'Placa', 'Nome', 'Fornecedor', 'Mercadoria', 'Nota', 'Hora_chegada', 'Hr_subida', 'Hr_descida')
        self.tree = ttk.Treeview(self.root, columns=column_names, show='headings')

        '''style = ttk.Style()
        style.configure("Treeview.Heading", font=('Roboto', 11))'''
        nametofont("TkHeadingFont").configure(size=10, weight='bold')
        self.tree.heading("#0", text="")
        self.tree.heading("#1", text="Data")
        self.tree.heading("#2", text="Placa")
        self.tree.heading("#3", text="Nome")
        # self.tree.heading("#4", text="RG/CPF")
        self.tree.heading("#4", text="Fornecedor")
        self.tree.heading("#5", text="Mercadoria")
        self.tree.heading("#6", text="Nota")
        self.tree.heading("#7", text="Hora")
        self.tree.heading("#8", text="Hr_subida")
        self.tree.heading("#9", text="Hr_descida")

        self.tree.column("#0", width=0, anchor='center')
        self.tree.column("#1", width=20, anchor='center')  # data
        self.tree.column("#2", width=30, anchor='center')  # placa
        self.tree.column("#3", width=100, anchor='center')  # nome
        # self.tree.column("#4", width=100, anchor='center')  # rg_cpf
        self.tree.column("#4", width=150, anchor='center')  # fornecedor
        self.tree.column("#5", width=100, anchor='center')  # mercadoria
        self.tree.column("#6", width=100, anchor='center')  # nota
        self.tree.column("#7", width=40, anchor='center')  # hora
        self.tree.column("#8", width=40, anchor='center')  # hora subida
        self.tree.column("#9", width=40, anchor='center')  # hora descida

        self.tree.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.6)

        self.scroll = Scrollbar(self.tree, orient=VERTICAL)
        self.tree.configure(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.tree.yview)
        self.scroll.place(relx=0.979, rely=0.002, relwidth=0.02, relheight=0.995)


Principal()
