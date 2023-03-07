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
        parent.resizable(True, True)

class Logo(ttk.Frame):
    def __init__(self, parent, filename, size=None):
        self.parent = parent
        self.image = tk.PhotoImage(file=filename)
        self.image = self.image.subsample(2, 2)
        if size is not None:
            self.image = self.image.zoom(size[0], size[0])
        self.label = tk.Label(self.parent, image=self.image)
        self.label.grid()


class FechaFrame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)

        d = time.strftime('%H:%M:%S', time.localtime())

        fecha = ttk.Label(
            self,
            text=datetime.date.today(), 
            background="yellow", 
            font=("Century Gothic", 17))
        fecha.grid(column=1, row=1, sticky=tk.N, padx=275)

        hora = ttk.Label(
            self, 
            text=d, 
            background="green",
            font=("Century Gothic", 15)
            )
        hora.grid(column=1, row=0, sticky=tk.N)





root = tk.Tk()
logo = Logo(root, "Mirai.png" , size=(1,0))
App(root).grid()
FechaFrame(root).grid(pady=0)
root.mainloop()