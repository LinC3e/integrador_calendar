import calendar
import datetime
import time
import tkinter as tk
from tkinter import ttk

# Windows

class App(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent, padding="20")

        self.parent = parent #guardamos una referencia a la ventana principal
        self.grid(sticky=(tk.N,tk.S, tk.E, tk.W))

        parent.title = "Calendar"
        parent.geometry("650x450")
        parent.config(bg="#242424")
        parent.resizable(False, False)


class FechaFrame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)

        d = time.strftime('%H:%M:%S', time.localtime())

        fecha = ttk.Label(self, text=datetime.date.today(), background="yellow")
        fecha.grid(column=1, row=1, sticky=tk.N, padx=5, pady=5)

        hora = ttk.Label(self, text=d, background="green")
        hora.grid(column=1, row=0, sticky=tk.N)



root = tk.Tk()
App(root).grid()
FechaFrame(root).grid()
root.mainloop()