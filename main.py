import tkinter as tk
from tkinter import ttk
import datetime
import time

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=(20))
        self.parent = parent # guardamos una referencia de la ventana ppal
        parent.title("Calendar") 
        parent.geometry("650x450+100+100") 
        parent.config(bg="#242424")
        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        parent.columnconfigure(0, weight=1) 
        parent.rowconfigure(0, weight=1) 
        parent.resizable(False, False)

        self.title = tk.StringVar
        self.date = datetime.date.today()
        self.time = time.strftime('%H:%M:%S', time.localtime())
        self.duration = 1
        self.description = ""
        self.importance = "normal"
        
        ttk.Button(self, text="Abrir ventana", command=self.crear_evento).grid()
        

    def crear_evento(self):
# creamos la ventana secundaria
# como padre indicamos la ventana principal
        toplevel = tk.Toplevel(self.parent)
# agregamos el frame (Secundaria) a la ventana (toplevel)
        CrearEvento(toplevel).grid()
        


class CrearEvento(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=(20))
        parent.title("Crear Evento") 
        parent.geometry("350x100+180+100") 
        self.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        parent.columnconfigure(0, weight=1) 
        parent.rowconfigure(0, weight=1) 
        parent.resizable(True, True) 

        self.title_label = tk.Label(self, text="Title:")
        self.title_label.grid()
        self.title_entry = tk.Entry(self)
        self.title_entry.grid()

        self.date_label = tk.Label(self, text="Date (MM/DD/YYYY):")
        self.date_label.grid()
        self.date_entry = tk.Entry(self)
        self.date_entry.grid()

        self.time_label = tk.Label(self, text="Time (HH:MM AM/PM):")
        self.time_label.grid()
        self.time_entry = tk.Entry(self)
        self.time_entry.grid()

        self.duration_label = tk.Label(self, text="Duration (in hours):")
        self.duration_label.grid()
        self.duration_entry = tk.Entry(self)
        self.duration_entry.insert(0, "1")
        self.duration_entry.grid()

        self.description_label = tk.Label(self, text="Description:")
        self.description_label.grid()
        self.description_entry = tk.Entry(self)
        self.description_entry.grid()

        self.importance_label = tk.Label(self, text="Importance:")
        self.importance_label.grid()
        self.importance_var = tk.StringVar(self)
        self.importance_var.set("normal")
        self.importance_menu = tk.OptionMenu(self, self.importance_var, "normal", "important")
        self.importance_menu.grid()

        self.add_button = tk.Button(self, text="Add Event", command=self.add_event)
        self.add_button.grid()

        self.event_list = tk.Listbox(self)
        self.event_list.grid()

        self.edit_button = tk.Button(self, text="Edit Event", command=self.edit_event)
        self.edit_button.grid()

        self.delete_button = tk.Button(self, text="Delete Event", command=self.delete_event)
        self.delete_button.grid()

    def add_event(self):
        title = self.title_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        duration = float(self.duration_entry.get())
        description = self.description_entry.get()
        importance = self.importance_var.get()
        event = App(title, date, time, duration, description, importance)
        self.events.append(event)
        self.event_list.insert(tk.END, event.title)

    def edit_event(self):
        pass

    def delete_event(self):
        pass

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
logo = Logo(root, "Mirai-nobg.png" , size=(1,0))
App(root).grid()
FechaFrame(root).grid(pady=0)
root.mainloop()