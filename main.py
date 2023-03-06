import calendar
import tkinter as tk
from tkinter import ttk

# Windows

class App(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent, padding=(20))
        self.parent = parent #guardamos una referencia a la ventana principal
        parent.title = "Calendar"
        parent.geometry("650x450")
        parent.config(bg="#242424") # background 
        parent.resizable(False, False)

        ttk.Label(self, text="Testing ").grid() 


root = tk.Tk()
App(root).grid()
root.mainloop()