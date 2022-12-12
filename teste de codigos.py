"""barra de menu no topo da janela


def menu_click(self):
    self.m_1 = Menu(self.root, tearoff=0)
    self.m_1.add_command(label="Sair", command=self.root.destroy)

    self.root.config(menu=self.m_1)
    self.root.bind("<Button-3>", self.menu_click)"""

import tkinter as tk
from tkinter import ttk


class TreeviewEdit(ttk.Treeview):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)











if __name__ == '__main__':
    root = tk.Tk()
    root.title("teste")
    root.geometry("800x600")



    column_names = ("vehicle_name", "year", "colour")

    treeview_vehicles = TreeviewEdit(root, columns=column_names)

    treeview_vehicles.pack(fill=tk.BOTH, expand=True)

    treeview_vehicles.heading("#0", text="Vehicle Type")
    treeview_vehicles.heading("vehicle_name", text='Vehicle Name')
    treeview_vehicles.heading("year", text="year")




    root.mainloop()





