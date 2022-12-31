import datetime
import tkinter as tk
from tkinter import *
from tkinter import ttk, Scrollbar, messagebox, StringVar
from tkinter.font import nametofont
from PIL import Image
import pyperclip as pc

root = tk.Tk()


class Funcoes:

    def __init__(self):
        self.btn_conf = None
        self.root = root
        self.e_conf = None
        self.ajudante_ico = None
        self.sair_ico = None
        self.opcoes_ico = None
        self.informacoes_ico = None
        self.deletar_ico = None
        self.cancelar_ico = None
        self.liberado_ico = None
        self.autorizado_ico = None
        self.aguardar_ico = None
        self.edit_icon = None
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
        self.tree = None
        self.root.bind("<Button-1>", lambda event: self.unselect(event))
        self.hora = StringVar()
        self.hora_subida = StringVar()
        self.hora_liberado = StringVar()
        self.copy_icon = None

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
            "", 0, values=(self.data_tempo.get(), self.e_placa.get().upper(), self.e_nome.get().upper(), self.e_rg.get().upper(),
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

    # MENU POPUP
    def pop_menu(self):
        self.pop_menu_mnu = tk.Menu(self.root, tearoff=0)

        # resize image
        aguardar_resize = Image.open('ico/aguardar.png')
        aguardar_resize = aguardar_resize.resize((16, 16))
        aguardar_resize.save('ico/aguardar_ico_small.png')

        autorizado_resize = Image.open('ico/autorizado.png')
        autorizado_resize = autorizado_resize.resize((13, 13))
        autorizado_resize.save('ico/autorizado_ico_small.png')

        liberado_resize = Image.open('ico/liberado.png')
        liberado_resize = liberado_resize.resize((16, 16))
        liberado_resize.save('ico/liberado_ico_small.png')

        cancelar_resize = Image.open('ico/cancelar.png')
        cancelar_resize = cancelar_resize.resize((14, 14))
        cancelar_resize.save('ico/cancelar_ico_small.png')

        deletar_resize = Image.open('ico/deletar.png')
        deletar_resize = deletar_resize.resize((15, 15))
        deletar_resize.save('ico/deletar_ico_small.png')

        informacoes_resize = Image.open('ico/informacoes.png')
        informacoes_resize = informacoes_resize.resize((16, 16))
        informacoes_resize.save('ico/informacoes_ico_small.png')

        opcoes_resize = Image.open('ico/opcoes.png')
        opcoes_resize = opcoes_resize.resize((14, 14))
        opcoes_resize.save('ico/opcoes_ico_small.png')

        sair_resize = Image.open('ico/sair.png')
        sair_resize = sair_resize.resize((16, 16))
        sair_resize.save('ico/sair_ico_small.png')

        ajudante_resize = Image.open('ico/ajudante.png')
        ajudante_resize = ajudante_resize.resize((16, 16))
        ajudante_resize.save('ico/ajudante_ico_small.png')

        # icones
        self.copy_icon = PhotoImage(file='ico/copy.png')
        self.edit_icon = PhotoImage(file='ico/edit.png')
        self.aguardar_ico = PhotoImage(file='ico/aguardar_ico_small.png')
        self.autorizado_ico = PhotoImage(file='ico/autorizado_ico_small.png')
        self.liberado_ico = PhotoImage(file='ico/liberado_ico_small.png')
        self.cancelar_ico = PhotoImage(file='ico/cancelar_ico_small.png')
        self.deletar_ico = PhotoImage(file='ico/deletar_ico_small.png')
        self.informacoes_ico = PhotoImage(file='ico/informacoes_ico_small.png')
        self.opcoes_ico = PhotoImage(file='ico/opcoes_ico_small.png')
        self.sair_ico = PhotoImage(file='ico/sair_ico_small.png')
        self.ajudante_ico = PhotoImage(file='ico/ajudante_ico_small.png')

        self.pop_menu_mnu.add_command(label=" Opções", image=self.opcoes_ico, compound='left')
        self.pop_menu_mnu.add_separator()
        self.pop_menu_mnu.add_command(label='  Copiar', command=self.copy_paste, image=self.copy_icon, compound='left')
        self.pop_menu_mnu.add_command(label='  Editar', command=self.edit_mnu, image=self.edit_icon, compound='left')
        self.pop_menu_mnu.add_command(label='  Aguardar', command=self.aguardar, image=self.aguardar_ico, compound='left')
        self.pop_menu_mnu.add_command(label="  N/Agend-Autoriz.", command=self.autorizado, image=self.autorizado_ico, compound='left')
        self.pop_menu_mnu.add_command(label='  Entrada/Subida', command=self.liberado, image=self.liberado_ico, compound='left')
        self.pop_menu_mnu.add_command(label='  Saida', command=self.saida, image=self.sair_ico, compound='left')
        self.pop_menu_mnu.add_command(label='  Cancelar/Reprovado', command=self.cancelado, image=self.cancelar_ico, compound='left')
        self.pop_menu_mnu.add_command(label='  Deletar', command=self.delete_, image=self.deletar_ico, compound='left')
        self.pop_menu_mnu.add_command(label='  Ad. Ajudantes', command=self.delete_, image=self.ajudante_ico, compound='left')
        self.pop_menu_mnu.add_separator()
        self.pop_menu_mnu.add_command(label='| Informações', command=self.mostrar_informacoes, image=self.informacoes_ico, compound='left')

    def popup_menu_method(self, event):
        try:
            self.pop_menu_mnu.tk_popup(event.x_root, event.y_root)
        finally:
            self.pop_menu_mnu.grab_release()

    def copy_paste(self):
        try:
            # convertendo o item selecionado em string
            item_selection1 = self.tree.selection()[0]
            item_selection1 = self.tree.item(item_selection1, 'values')
            item_selection1 = str(item_selection1)
            item_selection1 = item_selection1.replace("'", "")
            item_selection1 = item_selection1.replace("(", "")
            item_selection1 = item_selection1.replace(")", "")
            item1 = item_selection1
            pc.copy(item1)
        except IndexError:
            messagebox.showerror("Erro", "Selecione um item para copiar")

    def edit_mnu(self):
        # recuperar o item selecionado no treeview
        selecionados = self.tree.selection()
        if not selecionados:
            # nenhum item selecionado
            return
        indice = selecionados[0]  # pegar o primeiro item da tupla
        item = self.tree.item(indice)  # recuperar as informações do item
        # atualizar as entrys com os valores do item
        self.e_placa.delete(0, "end")
        self.e_placa.insert(0, item["values"][1])
        self.e_nome.delete(0, "end")
        self.e_nome.insert(0, item["values"][2])
        self.e_rg.delete(0, "end")
        self.e_rg.insert(0, item["values"][3])
        self.e_forn.delete(0, "end")
        self.e_forn.insert(0, item["values"][4])
        self.e_merc.delete(0, "end")
        self.e_merc.insert(0, item["values"][5])
        self.e_nota.delete(0, "end")
        self.e_nota.insert(0, item["values"][6])
        item_selection = self.tree.selection()[0]
        self.tree.delete(item_selection)

    def autorizado(self):
        item_selection = self.tree.selection()[0]
        self.tree.tag_configure('azul', background='#9bb0ff')
        self.tree.item(item_selection, tags=('azul',))

    def liberado(self):
        try:
            item_selection = self.tree.selection()[0]
            self.tree.tag_configure('verde', background='#9bff9b')
            self.tree.item(item_selection, tags=('verde',))
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

        self.win_conferente()

    def aguardar(self):
        try:
            item_selection: object = self.tree.selection()[0]
            self.tree.tag_configure('laranja', background='#FF9D49')
            self.tree.item(item_selection, tags=('laranja',))
            self.hora = datetime.datetime.now().strftime("%H:%M")
            self.hora = StringVar(value=self.hora)

            # atualizar o item selecionado com a hora de subida
            self.tree.item(self.tree.selection()[0],
                           values=(
                               self.tree.item(self.tree.selection()[0])['values'][0], self.tree.item(self.tree.selection()[0])['values'][1], self.tree.item(self.tree.selection()[0])['values'][2],
                               self.tree.item(self.tree.selection()[0])['values'][3], self.tree.item(self.tree.selection()[0])['values'][4], self.tree.item(self.tree.selection()[0])['values'][5],
                               self.tree.item(self.tree.selection()[0])['values'][6], self.hora.get()
                           ))
        except IndexError:
            pass

    def saida(self):
        try:
            item_selection = self.tree.selection()[0]
            self.tree.tag_configure('verde', background='#9bff9b')
            self.tree.item(item_selection, tags=('verde',))
            self.hora_liberado = datetime.datetime.now().strftime("%H:%M")
            self.hora_liberado = StringVar(value=self.hora_liberado)

            # atualizar o item selecionado com a hora de decida
            self.tree.item(self.tree.selection()[0],
                           values=(
                               self.tree.item(self.tree.selection()[0])['values'][0], self.tree.item(self.tree.selection()[0])['values'][1], self.tree.item(self.tree.selection()[0])['values'][2],
                               self.tree.item(self.tree.selection()[0])['values'][3], self.tree.item(self.tree.selection()[0])['values'][4], self.tree.item(self.tree.selection()[0])['values'][5],
                               self.tree.item(self.tree.selection()[0])['values'][6], self.tree.item(self.tree.selection()[0])['values'][7], self.tree.item(self.tree.selection()[0])['values'][8],
                               self.hora_liberado.get()
                           ))
        except IndexError:
            messagebox.showerror("Erro", "Liberar primeiro")

    def limpar(self):  # testar if True
        self.e_placa.delete(0, END)
        self.e_nome.delete(0, END)
        self.e_rg.delete(0, END)
        self.e_nota.delete(0, END)
        self.e_forn.delete(0, END)
        self.e_merc.delete(0, END)
        self.e_placa.focus()

    def win_conferente(self):
        win_conferente = Toplevel(self.root)
        win_conferente.title("Conferente")
        win_conferente.geometry("300x50")
        win_conferente.resizable(False, False)
        win_conferente.geometry("+{}+{}".format(self.root.winfo_screenwidth() // 2 - 150,
                                                self.root.winfo_screenheight() // 2 - 100))  # Center window on screen

        self.entry_conf(win_conferente)

    def entry_conf(self, win_conferente):
        self.e_conf = Entry(win_conferente, width=25, font=("Arial", 12))
        self.e_conf.place(x=10, y=10, width=150, height=30)
        self.e_conf.focus()

        self.btn_conf = Button(win_conferente, text="OK", command=lambda: self.conf(win_conferente))
        self.btn_conf.place(x=170, y=10, width=120, height=30)

    def conf(self, win_conferente):
        pass

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
        save_resize = Image.open('ico/salvar.png')
        save_resize = save_resize.resize((27, 27))
        save_resize.save('ico/save_ico_small.png')
        save_img = PhotoImage(file='ico/save_ico_small.png', width=27, height=27)
        self.save = Button(self.info_window, background='#FFFFF0', command=self.function_button_save, width=20, height=20, borderwidth=0)
        self.save.image = save_img
        self.save.config(image=self.save.image, compound=CENTER)
        self.save.grid(column=0, row=11, sticky=E, padx=20)

    def function_button_save(self):
        # Recupera o texto da caixa de texto
        text = self.obs.get("1.0", "end-1c")
        text = text.upper()

        # Adiciona uma quebra de linha a cada 35 caracteres
        formatted_text = ""
        for i in range(0, len(text), 38):
            formatted_text += text[i:i + 38] + "\n"

        # Atualiza a variável de texto com o texto formatado
        info_text = tk.StringVar()
        info_text.set(formatted_text)

        # Cria a label de texto com o texto da variável
        label_txt = Label(self.info_window, textvariable=info_text, font=('Roboto', 11), bd=4, bg='#FFFFF0', wraplength=400, width=44, height=6, anchor='center')
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
        item_selection = self.tree.selection()[0]
        self.tree.tag_configure('cinza', background='#656565', foreground='#ffffff')
        self.tree.item(item_selection, tags=('cinza',))


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
        self.tree.heading("#9", text="Hr. Entr.")
        self.tree.heading("#10", text="Hr. Said.")
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

        root_ = self.tree.winfo_toplevel()  # obtém a janela principal da interface Tkinter
        root_.clipboard_clear()  # limpa a área de transferência
        root_.clipboard_append(selected_text)  # copia o texto para a área de transferência

    @staticmethod
    def on_focus_out(event):
        event.widget.destroy()

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

    def item(self, selected_iid, text):
        pass


Principal()
