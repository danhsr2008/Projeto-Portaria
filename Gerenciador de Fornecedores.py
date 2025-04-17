import datetime
import tkinter as tk
from tkinter import ttk, messagebox, StringVar
from tkinter.font import nametofont
from PIL import Image
import pyperclip as pc


class Funcoes:
    def __init__(self):
        self.root = tk.Tk()
        self.tree = None
        self.icons = {}
        self.e_rg = None
        self.e_nota = None
        self.e_placa = None
        self.e_mercadoria = None
        self.e_fornecedor = None
        self.e_nome = None
        self.info_window = None
        self.hora_label = None
        self.pop_menu = None
        self.dados = None
        self.hora = StringVar()
        self.hora_subida = StringVar()
        self.hora_liberado = StringVar()

        self.setup_bindings()

    def setup_bindings(self):
        self.root.bind("<Button-1>", self.unselect)

    def capturar_dados(self):
        dados = [
            self.e_placa.get(),
            self.e_nome.get(),
            self.e_nota.get(),
            self.e_fornecedor.get(),
            self.e_mercadoria.get()
        ]
        if any(campo == '' for campo in dados):
            messagebox.showinfo(
                "Erro",
                "Algum campo está vazio!\n\n"
                "Preencha o campo com \"ESPAÇO\" se não houver valor."
            )
            self.limpar_campos()
            return False

        self.tree.insert(
            "",
            0,
            values=(
                self.data_tempo.get(),
                self.e_placa.get().upper(),
                self.e_nome.get().upper(),
                self.e_rg.get().upper(),
                self.e_fornecedor.get().upper(),
                self.e_mercadoria.get().upper(),
                self.e_nota.get().upper(),
                self.hora.get()
            )
        )
        ttk.Style().configure(
            "Treeview",
            font=('Roboto', 11),
            rowheight=24,
            background='#d9dbdc',
            foreground='#000000'
        )
        self.limpar_campos()

    def limpar_campos(self):
        self.e_placa.delete(0, tk.END)
        self.e_nome.delete(0, tk.END)
        self.e_rg.delete(0, tk.END)
        self.e_nota.delete(0, tk.END)
        self.e_fornecedor.delete(0, tk.END)
        self.e_mercadoria.delete(0, tk.END)
        self.e_placa.focus()

    def deletar_item(self):
        try:
            item_selecionado = self.tree.selection()[0]
            self.tree.delete(item_selecionado)
        except IndexError:
            messagebox.showerror("Erro", "Selecione um item para deletar.")

    def atualizar_hora(self):
        self.hora.set(datetime.datetime.now().strftime("%H:%M"))
        self.root.after(60000, self.atualizar_hora)  # Atualiza a cada 1 minuto

    def atualizar_data(self):
        self.data_tempo.set(datetime.datetime.now().strftime("%d/%m"))
        self.root.after(86400000, self.atualizar_data)  # Atualiza a cada 24 horas

    def unselect(self, event):
        try:
            if self.tree.identify_row(event.y) == "":
                self.tree.selection_remove(self.tree.selection()[0])
        except IndexError:
            pass