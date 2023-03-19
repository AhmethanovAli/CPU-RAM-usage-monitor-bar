class Configure_widgets:
    def configure_cpu_bar(self):
        r = self.cpu.cpu_percent_return()
        for i in range(self.cpu.cpu_count_logical):
            self.list_label[i].configure(text=f'core {i + 1} usage: {r[i]}%')
            self.list_pbar[i].configure(value=r[i])
        r2 = self.cpu.ram_usage()
        self.ram_lbl.configure(text=f'RAM usage: {r2[2]}%, used {round(r2[3] / 1048576)} Mb, '
                                    f'available: {round(r2[1] / 1048576)} Mb')
        self.ram_bar.configure(value=r2[2])
        self.wheel = self.after(1000, self.configure_cpu_bar)

    def configure_win(self):
        if self.wm_overrideredirect():  # Проверяем, что у окна есть рамки
            self.overrideredirect(False)
        else:
            self.overrideredirect(True)
        self.update()

    def configure_minimal_win(self):
        self.bar_one.configure(value=self.cpu.cpu_one_return())
        self.ram_bar.configure(value=self.cpu.ram_usage()[2])
        self.wheel = self.after(1000, self.configure_cpu_bar)

    def clear_win(self):
        for i in self.winfo_children():  # winfo_children - список виджетов на главном окне
            i.destroy()
