from tkinter import *
import tkinter as tk
from tkinter import ttk, Scrollbar, font, messagebox
from tkinter.font import nametofont
import datetime
import pyperclip as pc

root = tk.Tk()


class funcoes:

    def __init__(self):
        self.pop_menu_mnu = None
        self.dados = None
        self.hora = None
        self.data = None

    def cap_dados(self):
        dados = [
            self.e_placa.get(), self.e_nome.get(), self.e_rg.get(),
            self.e_nota.get(), self.e_forn.get(), self.e_merc.get()
        ]
        try:
            for item in dados:
                match item:
                    case '':
                        messagebox.showinfo("Erro",
                                            "Algum Campo Vazio!\n\nPreencha o campo com \"ESPAÇO\" se não houver")
                        self.limpar()
                        return False
                    case _:
                        pass
        except SyntaxError or KeyError:
            for item in dados:
                if item == '':
                    messagebox.showinfo("Erro", "Algum Campo Vazio!\n\nPreencha o campo com \"ESPAÇO\" se não houver")
                    self.limpar()
                    return False
                else:
                    pass

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
            self.root.after(1440000, self.data_)  # 1440000 = 24 horas # erro de 1 dia
            break

    def hora_(self):
        while True:
            self.hora = datetime.datetime.now()
            self.hora = self.hora.strftime("%H:%M")
            self.hora = StringVar(value=self.hora)
            self.root.after(1000, self.hora_)  # 1000 = 1 minuto
            break

    # MENU POPUP
    def pop_menu(self):
        self.pop_menu_mnu = tk.Menu(self.root, tearoff=0)
        self.pop_menu_mnu.add_command(label='Copiar', command=self.copy_paste)  # copia o item selecionado
        self.pop_menu_mnu.add_command(label='Autorizado', command=self.copy_paste)  # Marcar com autorizado (amarelo)
        self.pop_menu_mnu.add_command(label='Liberado', command=self.copy_paste)  # Marcar como liberado (verde)
        self.pop_menu_mnu.add_command(label='Cancelar', command=self.copy_paste)  # Marcar como cancelado (vermelho)
        self.pop_menu_mnu.add_command(label='Deletar', command=self.delete_)  # deletar item
        self.pop_menu_mnu.add_command(label='Linkar',
                                      command=self.copy_paste)  # inicia um focus para o registro linkado
        self.pop_menu_mnu.add_command(label='Informações',
                                      command=self.copy_paste)  # mostra uma label com todas informações do item selecionado

    def popup_menu_method(self, event):
        try:
            self.pop_menu_mnu.tk_popup(event.x_root, event.y_root)
        finally:
            self.pop_menu_mnu.grab_release()

    def copy_paste(self):
        try:
            # convertendo o item selecionado em string
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
            
            
            
"""def unselect(event):
    # Obtém o widget que foi clicado
    widget = event.widget

    # Obtém o item selecionado
    selection = widget.selection()

    # Se houver um item selecionado
    if selection:
        # Deseleciona o item
        widget.selection_remove(selection)
"""

"""treeview.bind('<Button-1>', unselect)
"""
            
            


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
        # self.time_live()
        root.mainloop()

    def screen(self):
        self.root.title("Controle de Acesso - V1.0")
        self.root.configure(background='#d9dbdc')
        self.root.geometry('1300x650')

        # ----- menu popup -----
        self.pop_menu()
        self.root.bind('<Button-3>', self.popup_menu_method)  # criar uma def para binds

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
        column_names = ('Data', 'Placa', 'Nome', 'RG_CPF', 'Fornecedor', 'Mercadoria', 'Nota', 'Hora')
        self.tree = ttk.Treeview(self.root, columns=column_names, show='headings')

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
