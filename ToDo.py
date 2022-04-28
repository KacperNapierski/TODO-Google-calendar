from tkinter import Frame, Listbox, ttk
import tkinter as tk
from turtle import left

App = tk.Tk()
App.geometry('1000x500+200+100')
App.title('ToDo')
App['bg']='#292929'
App.resizable(width=True, height=True)

list_part=Frame(master=App, width=480, height=490, bg='#525252' )
list_part.pack(padx=5, pady=5, side=tk.LEFT , expand= True)

detail_part=Frame(master=App, width=480, height=490, bg='#525252' )
detail_part.pack(padx=5, pady=5, side=tk.RIGHT , expand= True)

listbox=Listbox(
    list_part,
    width=50,
    height=50,
    bg='#525252',
    fg='#ffffff'
)
listbox.pack(padx=5, pady=5, expand=True)

App.mainloop()
