import tkinter as tk
from unicodedata import name

from tables import Description


class list_slot(tk.Frame):
    def __init__(self, task_name, task_description, task_date, task_time, master=tk.Frame):
        self.task_name = task_name
        self.task_description = task_description
        self.task_date = task_date
        self.task_time = task_time
        super().__init__(master)
        self.pack()

    def hover():

        