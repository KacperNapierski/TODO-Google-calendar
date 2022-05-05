import tkinter as tk
from unicodedata import name
from tables import Description

class task_data:
    def __init__(
        self,
        task_name,
        task_description,
        task_date,
        task_time
    ):

        self.task_name = task_name
        self.task_description = task_description
        self.task_date = task_date
        self.task_time = task_time
        super().__init__()
        

# class task_slot:
#     def __init__(self, master=App.tasks_frame):
#         super().__init__(master)
#         self.pack()

def items_selected(event, list):
    """ handle item selected event
    """
    # get selected indices
    selected_indices = list.curselection()
    # get selected items
    selected_langs = ",".join([list.get(i) for i in selected_indices])
    msg = f'You selected: {selected_langs}'

    tk.showinfo(
        title='Information',
        message=msg)

# def Add_task():
