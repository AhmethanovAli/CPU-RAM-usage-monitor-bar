import tkinter as tk
from tkinter import ttk
import sys
from Process import CpuBar
from Widget_update import Configure_widgets


#  attributes- свойство окна
class Application(tk.Tk, Configure_widgets):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('CPU-RAM usage monitor bar')
        self.attributes('-alpha', 1)  # Параметр прозрачности окна
        self.attributes('-topmost', True)  # Делает окно поверх других окон
        self.overrideredirect(True)  # Удаляет рамки
        self.resizable(False, False)  # Запрещает менять размер окна
        self.cpu = CpuBar()
        self.run_set_ui()

    def run_set_ui(self):
        self.set_ui()
        self.make_bar_cpu_usage()
        self.configure_cpu_bar()

    def set_ui(self):
        exit_but = ttk.Button(self, text='Exit', command=self.app_exit)
        exit_but.pack(fill=tk.X)
        self.bar_2 = ttk.LabelFrame(self, text='Hello')
        self.bar_2.pack(fill=tk.X)
        ttk.Button(self.bar_2, text='Move', command=self.configure_win).pack(side=tk.LEFT)
        ttk.Button(self.bar_2, text='>>>').pack(side=tk.LEFT)
        self.combo_win = ttk.Combobox(self.bar_2, values=['Hide', "Don't hide", 'Min'], state='readonly', width=10)
        self.combo_win.current(1)
        self.combo_win.pack(side=tk.LEFT)
        self.bind_class('Tk', '<Enter>', self.enter_mouse)
        self.combo_win.bind('<<ComboboxSelected>>', self.choice_combo)
        self.bind_class('Tk', '<Leave>', self.leave_mouse)
        self.bar = ttk.LabelFrame(self, text='Power')
        self.bar.pack(fill=tk.BOTH)  # tk.BOTH растягивает максимально по ширине

    def make_min_win(self):
        #  Процессор
        self.bar_one = ttk.Progressbar(self, length=100)  # Общая загрузка процессора
        self.bar_one.pack(side=tk.LEFT)

        #  Оперативная память
        self.ram_bar = ttk.Progressbar(self, length=100)
        self.ram_bar.pack(side=tk.LEFT)

        #  Кнопка для перехода в полный режим
        ttk.Button(self, text='Full', command=self.make_full_win, width=5).pack(side=tk.RIGHT)
        ttk.Button(self, text='Move', command=self.configure_win, width=5).pack(side=tk.RIGHT)
        self.update()
        self.configure_minimal_win()

    def make_full_win(self):
        self.after_cancel(self.wheel)
        self.clear_win()
        self.update()
        self.run_set_ui()
        self.enter_mouse('')
        self.combo_win.current(1)

    def enter_mouse(self, event):
        if self.combo_win.current() == 0 or 1:
            self.geometry('')

    def leave_mouse(self, event):
        if self.combo_win.current() == 0:
            self.geometry(f'{self.winfo_width()}x1')

    def app_exit(self):
        self.destroy()
        sys.exit()

    def make_bar_cpu_usage(self):
        ttk.Label(self.bar, text=f'Physical cores: {self.cpu.cpu_count}, Logical cores: {self.cpu.cpu_count_logical}',
                  anchor=tk.CENTER).pack(fill=tk.X)
        self.list_label = []
        self.list_pbar = []
        for i in range(self.cpu.cpu_count_logical):
            # Добавляем надписи и progressbar-ы в списке
            self.list_label.append(ttk.Label(self.bar, anchor=tk.CENTER))
            self.list_pbar.append((ttk.Progressbar(self.bar, length=100)))
        for i in range(self.cpu.cpu_count_logical):
            self.list_label[i].pack(fill=tk.X)
            self.list_pbar[i].pack(fill=tk.X)

        # Оперативная память
        self.ram_lbl = ttk.Label(self.bar, text='', anchor=tk.CENTER)
        self.ram_lbl.pack(fill=tk.X)
        self.ram_bar = ttk.Progressbar(self.bar, length=100)
        self.ram_bar.pack(fill=tk.X)

    def choice_combo(self, event):
        if self.combo_win.current() == 2:  # Если выбран режим min
            self.enter_mouse('')
            self.unbind_class('Tk', '<Enter>')
            self.unbind_class('Tk', '<Leave>')
            self.combo_win.unbind('<<ComboboxSelected>>')
            self.after_cancel(self.wheel)  # Останавливаем обновление виджетов
            self.clear_win()
            self.update()
            self.make_min_win()


root = Application()
root.mainloop()
