import tkinter as tk
from unicodedata import name
from tables import Description
import App

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
        

class task_slot:
    def __init__(self, master=App.tasks_frame):
        super().__init__(master)
        self.pack()


# def Add_task():
