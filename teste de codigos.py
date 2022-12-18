import tkinter as tk
from tkinter import ttk, messagebox
import datetime


class Application:

    def __init__(self, root):
        self.root = root
        self.popup_menu = None
        self.data = None
        self.hora = None
        self.info_window = None
        self.root.bind("<Button-1>", self.unselect)
        self.create_widgets()
        self.start_time_tracking()

    def create_widgets(self):
        # Cria a árvore de dados e os botões
        self.tree = ttk.Treeview(self.root,
                                 columns=('data', 'placa', 'nome', 'rg', 'fornecedor', 'mercadoria', 'nota', 'hora'))
        self.tree.heading('#0', text='Item')
        self.tree.heading('data', text='Data')
        self.tree.heading('placa', text='Placa')
        self.tree.heading('nome', text='Nome')
        self.tree.heading('rg', text='RG')
        self.tree.heading('fornecedor', text='Fornecedor')
        self.tree.heading('mercadoria', text='Mercadoria')
        self.tree.heading('nota', text='Nota')
        self.tree.heading('hora', text='Hora')
        self.tree.column('#0', width=30, minwidth=30, stretch=tk.NO)
        self.tree.column('data', width=70, minwidth=70, stretch=tk.NO)
        self.tree.column('placa', width=100, minwidth=100, stretch=tk.NO)
        self.tree.column('nome', width=100, minwidth=100, stretch=tk.NO)
        self.tree.column('rg', width=100, minwidth=100, stretch=tk.NO)
        self.tree.column('fornecedor', width=100, minwidth=100, stretch=tk.NO)
        self.tree.column('mercadoria', width=100, minwidth=100, stretch=tk.NO)
        self.tree.column('nota', width=100, minwidth=100, stretch=tk.NO)
        self.tree.column('hora', width=100, minwidth=100, stretch=tk.NO)
        self.tree.pack(side=tk.LEFT, fill=tk.Y)

        # Cria os campos de entrada de dados e os botões
        self.e_placa = tk.Entry(self.root)
        self.e_nome = tk.Entry(self.root)
        self.e_rg = tk.Entry(self.root)
        self.e_nota = tk.Entry(self.root)

        self.e_forn = tk.Entry(self.root)
        self.e_merc = tk.Entry(self.root)
        self.e_placa.pack(side=tk.TOP, fill=tk.X)
        self.e_nome.pack(side=tk.TOP, fill=tk.X)
        self.e_rg.pack(side=tk.TOP, fill=tk.X)
        self.e_nota.pack(side=tk.TOP, fill=tk.X)
        self.e_forn.pack(side=tk.TOP, fill=tk.X)
        self.e_merc.pack(side=tk.TOP, fill=tk.X)

        btn_capture = tk.Button(self.root, text="Capturar Dados", command=self.capture_data)
        btn_capture.pack(side=tk.TOP, fill=tk.X)
        btn_clear = tk.Button(self.root, text="Limpar Campos", command=self.clear_fields)
        btn_clear.pack()

        # Cria a janela de informações
        self.info_window = tk.Label(self.root, text="")
        self.info_window.pack(side=tk.BOTTOM, fill=tk.X)

    def capture_data(self):
        data = [
            self.e_placa.get(), self.e_nome.get(), self.e_rg.get(),
            self.e_nota.get(), self.e_forn.get(), self.e_merc.get()
        ]
        for item in data:
            if item == '':
                messagebox.showinfo("Erro", "Algum Campo Vazio!\n\nPreencha o campo com \"ESPAÇO\" se não houver")
                self.clear_fields()
                return
        self.tree.insert(
            "", "end", values=(self.data.get(), self.e_placa.get().upper(),
                               self.e_nome.get().upper(), self.e_rg.get().upper(),
                               self.e_forn.get().upper(), self.e_merc.get().upper(),
                               self.e_nota.get().upper(), self.hora.get()))
        ttk.Style().configure("Treeview", font=('Roboto', 11), rowheight=30, background='#d9dbdc', foreground='#000000')
        self.clear_fields()

    def delete(self):
        try:
            item_selection = self.tree.selection()[0]
            self.tree.delete(item_selection)
        except IndexError:
            messagebox.showerror("Erro", "Selecione um item para deletar")

    def clear_fields(self):
        self.e_placa.delete(0, "end")
        self.e_nome.delete(0, "end")
        self.e_rg.delete(0, "end")
        self.e_nota.delete(0, "end")
        self.e_forn.delete(0, "end")
        self.e_merc.delete(0, "end")
        self.e_placa.focus()

    def start_time_tracking(self):
        self.update_date()
        self.update_time()

    def update_date(self):
        self.data = datetime.datetime.now()
        self.data = self.data.strftime("%d/%m")
        self.data = tk.StringVar(value=self.data)
        self.root.after(86400000, self.update_date)  # 86400000 = 24 horas

    def update_time(self):
        self.hora = datetime.datetime.now()
        self.hora = self.hora.strftime("%H:%M")
        self.hora = tk.StringVar(value=self.hora)
        self.root.after(60000, self.update_time)  # 60000 = 1 minuto

    def unselect(self, event):
        self.tree.selection_remove(self.tree.focus())

    def right_click_event(self, event):
        self.popup_menu = tk.Menu(self.root, tearoff=0)
        self.popup_menu.add_command(label="Autorizado/Agendado", command=self.color_menu)
        self.popup_menu.add_separator()
        self.popup_menu.add_command(label="Deletar", command=self.delete)
        try:
            self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.popup_menu.grab_release()

    def color_menu(self):
        try:
            item_selection = self.tree.selection()[0]
            self.tree.item(item_selection, tags=('blue'))
            self.tree.tag_configure('blue', background='#0000ff')
            self.tree.update()
        except IndexError:
            messagebox.showerror("Erro", "Selecione um item para alterar a cor")

        # Obtém a hora atual e atualiza a janela de informações com ela
        current_time = datetime.datetime.now().strftime("%H:%M")
        self.info_window.config(text=f"Ação realizada às {current_time}")
        self.info_window.update()



