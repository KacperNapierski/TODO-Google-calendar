from tkinter import SOLID, Frame, Listbox, Scrollbar, ttk
import tkinter as tk
from turtle import left
import Logic as lg

# ===== Varaibles =====

tasks_number =50


# ===== App Window =====

App = tk.Tk()
App.title('ToDo')
App['bg']='#292929'
App['padx'] = 20
App.resizable(width=True, height=True)

# ===== Layout Frames =====

list_part = tk.Frame(
    master=App,
    width=600,
    height=800,
    bg='#525252'
)
list_part.pack(
    side=tk.LEFT,
    expand=True,
    fill=tk.BOTH,
    padx=5
)

detail_part = tk.Frame(
    master=App,
    width=400,
    height=800,
    bg='#525252'
)
detail_part.pack(
    side=tk.RIGHT,
    expand=True,
    fill=tk.BOTH,
    padx=5
)


action_frame = tk.Frame(
    master = list_part,
    width=600,
    height=50,
    relief=tk.FLAT,
    borderwidth=2,
    bg='#00a800'
)
action_frame.pack(
    side=tk.TOP,
    expand=False,
    fill=tk.X
)

tasks_frame = tk.Frame(
    master=list_part,
    width=600,
    height=750,
    bg='#525252'
)
tasks_frame.pack(
    side=tk.BOTTOM,
    expand=True,
    fill=tk.BOTH
)

# ===== Task Grid =====

for i in range(tasks_number):
    tasks_frame.columnconfigure(0, weight=1, minsize=400)
    
    task= tk.Frame(
        master=tasks_frame,
        relief=tk.FLAT,
        borderwidth=1,
        width=600
    )
    task.grid(row=i, column=0)
    label = tk.Label(
        master=task,
        text =f'task {i}',
        bg='#525252',
        width=100,
        # height=1
    )
    label.pack(
        side=tk.TOP,
        expand=True,
        fill=tk.BOTH
    )

App.mainloop()
