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

# ===== Task List =====

langs = ('Java', 'C#', 'C', 'C++', 'Python',
        'Go', 'JavaScript', 'PHP', 'Swift', 'V',
        'Java', 'C#', 'C', 'C++', 'Python',
        'Java', 'C#', 'C', 'C++', 'Python',
        'Java', 'C#', 'C', 'C++', 'Python',
        'Java', 'C#', 'C', 'C++', 'Python',
        'Java', 'C#', 'C', 'C++', 'Python',
        'Java', 'C#', 'C', 'C++', 'Python',
        'Java', 'C#', 'C', 'C++', 'Python',
        'Java', 'C#', 'C', 'C++', 'Python',
        'Java', 'C#', 'C', 'C++', 'Python',)

langs_var = tk.StringVar(value=langs)

task_list = tk.Listbox(
    master= tasks_frame,
    listvariable=langs_var,
    height=50,
    width=100,
    bg='#525252',
    relief=tk.FLAT,
    borderwidth=0,
    selectmode='extended')

task_list.grid(
    column=0,
    row=0,
    sticky='nwes'
)
#  link a scrollbar to a list
scrollbar = ttk.Scrollbar(
    master=tasks_frame,
    orient='vertical',
    command=task_list.yview
)

task_list['yscrollcommand'] = scrollbar.set

scrollbar.grid(
    column=1,
    row=0,
    sticky='ns')

task_list.bind('<<ListboxSelect>>', lg.items_selected(task_list))


App.mainloop()
