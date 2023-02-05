import tkinter as tk
from tkinter import ttk
import sys


#  attributes- свойство окна
class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.combo_win = None
        self.bar_2 = None
        self.bar = None
        self.title('CPU-RAM usage monitor bar')
        self.attributes('-alpha', 1)  # Параметр прозрачности окна
        self.attributes('-topmost', True)  # Делает окно поверх других окон
        self.overrideredirect(True)  # Удаляет рамки
        self.resizable(False, False)  # Запрещает менять размер окна
        self.set_ui()

    def set_ui(self):
        exit_but = ttk.Button(self, text='Exit', command=self.app_exit)
        exit_but.pack(fill=tk.X)
        self.bar_2 = ttk.LabelFrame(self, text='Hello')
        self.bar_2.pack(fill=tk.X)
        ttk.Button(self.bar_2, text='Move').pack(side=tk.LEFT)
        ttk.Button(self.bar_2, text='>>>').pack(side=tk.LEFT)
        self.combo_win = ttk.Combobox(self.bar_2, values=['Hide', "Don't hide", 'Min'], state='readonly', width=10)
        self.combo_win.current(1)
        self.combo_win.pack(side=tk.LEFT)
        self.bind_class('Tk', '<Enter>', self.enter_mouse)
        self.bind_class('Tk', '<Leave>', self.leave_mouse)
        self.bar = ttk.LabelFrame(self, text='Power')
        self.bar.pack(fill=tk.BOTH)  # tk.BOTH растягивает максимально по ширине

    def enter_mouse(self, event):
        if self.combo_win.current() == 0 or 1:
            self.geometry('')

    def leave_mouse(self, event):
        if self.combo_win.current() == 0:
            self.geometry(f'{self.winfo_width()}x1')

    def app_exit(self):
        self.destroy()
        sys.exit()


root = Application()
root.mainloop()
