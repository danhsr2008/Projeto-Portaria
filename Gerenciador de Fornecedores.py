import datetime
import tkinter as tk
from tkinter import *
from tkinter import ttk, Scrollbar, messagebox, StringVar
from tkinter.font import nametofont
import pyperclip as pc
import threading
import time

root = tk.Tk()


class Funcoes:

    def __init__(self):
        self.save = None
        self.obs = None
        self.e_rg = None
        self.e_nota = None
        self.e_placa = None
        self.e_merc = None
        self.e_forn = None
        self.e_nome = None
        self.info_window = None
        self.hora_label = None
        self.pop_menu_mnu = None
        self.dados = None
        self.hora = None
        self.data_tempo = None
        self.root = root
        self.tree = None
        self.root.bind("<Button-1>", lambda event: self.unselect(event))
        self.hora = StringVar()
        self.hora_subida = StringVar()
        self.hora_liberado = StringVar()

    def cap_dados(self):
        dados = [
            self.e_placa.get(), self.e_nome.get(), self.e_nota.get(), self.e_forn.get(), self.e_merc.get()
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
            "", END, values=(self.data_tempo.get(), self.e_placa.get().upper(), self.e_nome.get().upper(), self.e_rg.get().upper(),
                             self.e_forn.get().upper(), self.e_merc.get().upper(), self.e_nota.get().upper(), self.hora.get()))
        ttk.Style().configure("Treeview", font=('Roboto', 11), rowheight=30, background='#d9dbdc', foreground='#000000')
        self.limpar()

    def delete_(self):
        try:
            item_selection = self.tree.selection()[0]
            self.tree.delete(item_selection)
        except IndexError:
            messagebox.showerror("Erro", "Selecione um item para deletar")

    def data_(self):
        while True:
            self.data_tempo = datetime.datetime.now().strftime("%d/%m")
            self.data_tempo = StringVar(value=self.data_tempo)
            self.root.after(86400000, self.data_)  # 86400000 = 24 horas
            break

    def hora_(self):
        while True:
            self.hora = datetime.datetime.now().strftime("%H:%M")
            self.hora = StringVar(value=self.hora)
            self.root.after(60000, self.hora_)  # 60000 = 1 minuto
            break

    def copy_paste(self):
        pass

    # MENU POPUP
    def pop_menu(self):
        self.pop_menu_mnu = tk.Menu(self.root, tearoff=0)
        self.pop_menu_mnu.add_command(label='Copiar', command=self.copy_paste)  # copia o item selecionado
        self.pop_menu_mnu.add_command(label='Editar', command=self.copy_paste)  # copia o item selecionado
        self.pop_menu_mnu.add_command(label='Aguardar', command=self.aguardar)
        self.pop_menu_mnu.add_command(label="Autorizado/Agendado", command=self.autorizado)
        self.pop_menu_mnu.add_command(label='Liberado', command=self.liberado)
        self.pop_menu_mnu.add_command(label='Cancelar/Reprovado', command=self.cancelado)
        self.pop_menu_mnu.add_command(label='Deletar', command=self.delete_)
        self.pop_menu_mnu.add_separator()
        self.pop_menu_mnu.add_command(label='Informações', command=self.mostrar_informacoes)

    def popup_menu_method(self, event):
        try:
            self.pop_menu_mnu.tk_popup(event.x_root, event.y_root)
        finally:
            self.pop_menu_mnu.grab_release()

    def autorizado(self):
        print('captura hora: ok')
        item_selection = self.tree.selection()[0]
        self.tree.tag_configure('azul', background='#9bb0ff')
        self.tree.item(item_selection, tags=('azul',))
        try:
            self.hora_subida = datetime.datetime.now().strftime("%H:%M")
            self.hora_subida = StringVar(value=self.hora_subida)

            # atualizar o item selecionado com a hora de subida
            self.tree.item(self.tree.selection()[0],
                           values=(
                               self.tree.item(self.tree.selection()[0])['values'][0], self.tree.item(self.tree.selection()[0])['values'][1], self.tree.item(self.tree.selection()[0])['values'][2],
                               self.tree.item(self.tree.selection()[0])['values'][3], self.tree.item(self.tree.selection()[0])['values'][4], self.tree.item(self.tree.selection()[0])['values'][5],
                               self.tree.item(self.tree.selection()[0])['values'][6], self.tree.item(self.tree.selection()[0])['values'][7], self.hora_subida.get()
                           ))
        except IndexError:
            messagebox.showerror("Erro", "Selecione um item para autorizar/agendar")

    def liberado(self):
        print('captura hora: ok')
        item_selection = self.tree.selection()[0]
        self.tree.tag_configure('verde', background='#9bff9b')
        self.tree.item(item_selection, tags=('verde',))
        try:
            self.hora_liberado = datetime.datetime.now().strftime("%H:%M")
            self.hora_liberado = StringVar(value=self.hora_liberado)

            # atualizar o item selecionado com a hora de subida
            self.tree.item(self.tree.selection()[0],
                           values=(
                               self.tree.item(self.tree.selection()[0])['values'][0], self.tree.item(self.tree.selection()[0])['values'][1], self.tree.item(self.tree.selection()[0])['values'][2],
                               self.tree.item(self.tree.selection()[0])['values'][3], self.tree.item(self.tree.selection()[0])['values'][4], self.tree.item(self.tree.selection()[0])['values'][5],
                               self.tree.item(self.tree.selection()[0])['values'][6], self.tree.item(self.tree.selection()[0])['values'][7], self.tree.item(self.tree.selection()[0])['values'][8],
                               self.hora_liberado.get()
                           ))
        except IndexError:
            messagebox.showerror("Erro", "Autorizar primeiro")

    def aguardar(self):
        item_selection: object = self.tree.selection()[0]
        self.tree.tag_configure('laranja', background='#FF9D49')
        self.tree.item(item_selection, tags=('laranja',))

    def limpar(self):  # testar if True
        self.e_placa.delete(0, END)
        self.e_nome.delete(0, END)
        self.e_rg.delete(0, END)
        self.e_nota.delete(0, END)
        self.e_forn.delete(0, END)
        self.e_merc.delete(0, END)
        self.e_placa.focus()

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
        self.info_window.geometry("390x440")  # Set window size
        self.info_window.resizable(False, False)
        self.info_window.geometry("+{}+{}".format(self.root.winfo_screenwidth() // 2 - 150,
                                                  self.root.winfo_screenheight() // 2 - 100))  # Center window on screen

        self.entry_info_window()
        self.button_sv_obs()

        # Create a series of labels with the information
        data_label = tk.Label(self.info_window, text="Data: ")
        dt_label = tk.Label(self.info_window, text="{}".format(informacoes[0]))

        placa_label = tk.Label(self.info_window, text="Placa: ")
        plc_label = tk.Label(self.info_window, text="{}".format(informacoes[1]))

        nome_label = tk.Label(self.info_window, text="Nome: ")
        nm_label = tk.Label(self.info_window, text="{}".format(informacoes[2]))

        rg_cpf_label = tk.Label(self.info_window, text="RG/CPF: ")
        rgcpf_label = tk.Label(self.info_window, text="{}".format(informacoes[3]))

        fornecedor_label = tk.Label(self.info_window, text="Fornecedor: ")
        forn_label = tk.Label(self.info_window, text="{}".format(informacoes[4]))

        mercadoria_label = tk.Label(self.info_window, text="Mercadoria: ")
        merc_label = tk.Label(self.info_window, text="{}".format(informacoes[5]))

        nota_label = tk.Label(self.info_window, text="Nota: ")
        nt_label = tk.Label(self.info_window, text="{}".format(informacoes[6]))

        hora_chegada_label = tk.Label(self.info_window, text="Hora Chegada: ")
        hr_cheg_var = tk.Label(self.info_window, text="{}".format(informacoes[7]))

        try:
            hora_subida_label = tk.Label(self.info_window, text="Hora Subida: ")
            hora_subida_label.grid(column=0, row=2, sticky=W, padx=15, pady=2)
            hr_sub_var = tk.Label(self.info_window, text='{}'.format(informacoes[8]))
            hr_sub_var.grid(column=0, row=2, sticky=E, padx=20)

            hora_liberado_label = tk.Label(self.info_window, text="Hora Liberado: ")
            hora_liberado_label.grid(column=0, row=3, sticky=W, padx=15, pady=2)
            hr_lib_var = tk.Label(self.info_window, text='{}'.format(informacoes[9]))
            hr_lib_var.grid(column=0, row=3, sticky=E, padx=20)

        except IndexError:
            pass

        # Display the labels in the toplevel window
        hora_chegada_label.grid(column=0, row=1, sticky=W, padx=15, pady=2)
        hr_cheg_var.grid(column=0, row=1, sticky=E, padx=20)

        data_label.grid(column=0, row=4, sticky=W, padx=15, pady=2)
        dt_label.grid(column=0, row=4, sticky=E, padx=20)

        placa_label.grid(column=0, row=5, sticky=W, padx=15, pady=2)
        plc_label.grid(column=0, row=5, sticky=E, padx=20)

        nome_label.grid(column=0, row=6, sticky=W, padx=15, pady=2)
        nm_label.grid(column=0, row=6, sticky=E, padx=20)

        rg_cpf_label.grid(column=0, row=7, sticky=W, padx=15, pady=2)
        rgcpf_label.grid(column=0, row=7, sticky=E, padx=20)

        fornecedor_label.grid(column=0, row=8, sticky=W, padx=15, pady=2)
        forn_label.grid(column=0, row=8, sticky=E, padx=20)

        mercadoria_label.grid(column=0, row=9, sticky=W, padx=15, pady=2)
        merc_label.grid(column=0, row=9, sticky=E, padx=20)

        nota_label.grid(column=0, row=10, sticky=W, padx=15, pady=2)
        nt_label.grid(column=0, row=10, sticky=E, padx=20)

    def entry_info_window(self):
        obs_label = tk.Label(self.info_window, text="OBSERVAÇÕES")
        obs_label.grid(column=0, row=11, pady=10, sticky=S)
        self.obs = Text(self.info_window, font=('Roboto', 13), width=35, height=6, bg='#FFFFF0')  # Observaçoes
        self.obs.grid(column=0, row=12, padx=20)

    def button_sv_obs(self):
        self.save = Button(self.info_window, text="Save", font=('Roboto', 10), background='#d9dbdc', command=self.function_button_save)
        self.save.grid(column=0, row=11, sticky=E, padx=20)

    def function_button_save(self):
        # Recupera o texto da caixa de texto
        text = self.obs.get("1.0", "end-1c")

        # Adiciona uma quebra de linha a cada 35 caracteres
        formatted_text = ""
        for i in range(0, len(text), 29):
            formatted_text += text[i:i + 29] + "\n"

        # Atualiza a variável de texto com o texto formatado
        info_text = tk.StringVar()
        info_text.set(formatted_text)

        # Cria a label de texto com o texto da variável
        label_txt = Label(self.info_window, textvariable=info_text, font=('Roboto', 11), bd=4, bg='#FFFFF0', width=44, height=6, anchor='center')
        label_txt.grid(column=0, row=12, padx=15)

        self.obs.destroy()
        self.save.destroy()

    def unselect(self, event):
        try:
            if self.tree.identify_row(event.y) == "":
                self.tree.selection_remove(self.tree.selection()[0])
            else:
                pass
        except IndexError:
            pass

    def cancelado(self):
        self.tree.item(self.tree.selection()[0], tags=('cinza',))
        self.tree.tag_configure('cinza', background='#656565', foreground='#ffffff')


class Principal(Funcoes):
    scroll: Scrollbar

    def __init__(self):
        super().__init__()
        self.edits = {}
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
        self.b_1 = Button(self.root, text="Registrar", font=('Roboto', 10), background='#d9dbdc', command=self.cap_dados)
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
        column_names = (
            'Data', 'Placa', 'Nome', 'rg_cpf', 'Fornecedor', 'Mercadoria', 'Nota', 'Hora_chegada', 'Hora_Subida', 'Hora_Liberado', '')
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
        self.tree.heading("#8", text="Hr. Cheg.")
        self.tree.heading("#9", text="Hr. Sub.")
        self.tree.heading("#10", text="Hr. Lib.")
        self.tree.heading("#11", text='')

        self.tree.column("#0", width=0, stretch=NO)
        self.tree.column("#1", width=40, anchor='center')  # data
        self.tree.column("#2", width=60, anchor='center')  # placa
        self.tree.column("#3", width=140, anchor='center')  # nome
        self.tree.column("#4", width=100, anchor='center')  # rg_cpf
        self.tree.column("#5", width=170, anchor='center')  # fornecedor
        self.tree.column("#6", width=140, anchor='center')  # mercadoria
        self.tree.column("#7", width=100, anchor='center')  # nota
        self.tree.column("#8", width=70, anchor='center')  # hora_chegada
        self.tree.column("#9", width=70, anchor='center')  # hora_subida
        self.tree.column("#10", width=70, anchor='center')  # hora liberado
        self.tree.column("#11", width=0, anchor='center')  # vazio (espaço para scroll)

        self.tree.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.6)

        self.scroll = Scrollbar(self.tree, orient=VERTICAL)
        self.tree.configure(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.tree.yview)
        self.scroll.place(relx=0.979, rely=0.003, relwidth=0.02, relheight=0.995)

        # Associe o evento <Double-Button-1> à função select_cell
        self.tree.bind('<Double-Button-1>', self.on_double_click)

    def on_double_click(self, event):
        # indetify the region that was double_clicked
        region_clicked = self.tree.identify_region(event.x, event.y)
        # area interessada > cell
        if region_clicked not in "cell":
            return

        # item desejado a ser clicado?
        column = self.tree.identify_column(event.x)
        selected_iid = self.tree.focus()
        selected_values = self.tree.item(selected_iid)
        column_index = int(column[1:]) - 1
        selected_text = ''
        try:
            if column == "#1":
                selected_text = selected_values.get("values")[0]  # pegar valor do indice 1
            elif column == "#2":
                selected_text = selected_values.get("values")[1]
            elif column == "#3":
                selected_text = selected_values.get("values")[2]
            elif column == "#4":
                selected_text = selected_values.get("values")[3]
            elif column == "#5":
                selected_text = selected_values.get("values")[4]
            elif column == "#6":
                selected_text = selected_values.get("values")[5]
            elif column == "#7":
                selected_text = selected_values.get("values")[6]
            elif column == "#8":
                selected_text = selected_values.get("values")[7]
            elif column == "#9":
                selected_text = selected_values.get("values")[8]
            elif column == "#10":
                selected_text = selected_values.get("values")[9]
            else:
                selected_text = selected_values.get('values')[column_index]
        except IndexError:
            messagebox.showerror("Erro", "Item vazio!\ndefina a hora de subida ou de liberação\nantes de clicar novamente")
        except UnboundLocalError:
            pass

        column_box = self.tree.bbox(selected_iid, column)
        print(column_box)
        entry_edit = Entry(self.tree, width=column_box[2], font=('Roboto', 13))

        # record the column index and item iid
        entry_edit.editing_column_index = column_index
        entry_edit.editing_item_iid = selected_iid

        entry_edit.insert(0, selected_text)
        entry_edit.select_range(0, END)

        entry_edit.focus()

        entry_edit.bind('<FocusOut>', self.on_focus_out)
        entry_edit.bind('<Return>', self.on_focus_out)
        entry_edit.bind('<Return>', self.on_enter_pressed)

        entry_edit.place(x=column_box[0], y=column_box[1], w=column_box[2], h=column_box[3])

    @staticmethod
    def on_focus_out(event):
        if event.widget:
            event.widget.destroy()
        else:
            pass

    def on_enter_pressed(self, event):
        new_text = event.widget.get()
        new_text = new_text.upper()
        selected_iid = event.widget.editing_item_iid
        column_index = event.widget.editing_column_index
        try:
            if column_index == -1:
                self.item(selected_iid, text=new_text)
            else:
                current_values = self.tree.item(selected_iid).get('values')
                current_values[column_index] = new_text
                self.tree.item(selected_iid, values=current_values)

            event.widget.destroy()
            print("Item updated:", self.tree.item(selected_iid))
        except IndexError:
            messagebox.showerror("Erro", "Botão Direito do mouse sobre o item\n\nClique em Autorizado/Agendado\n\npara definir a hora de subida ou de liberação")


Principal()
