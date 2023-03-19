import time

import psutil as pt


class CpuBar:
    def __init__(self):
        self.cpu_count = pt.cpu_count(logical=False)  # Кол-во ядер
        self.cpu_count_logical = pt.cpu_count()  # Кол-во потоков

    def cpu_percent_return(self):
        return pt.cpu_percent(percpu=True)

    def ram_usage(self):
        return pt.virtual_memory()

    def cpu_one_return(self):
        return pt.cpu_percent()


if __name__ == '__main__':
    print(__name__)
    x = CpuBar()
    print(pt.virtual_memory())  # svmem(total=8517951488, available=3495079936, percent=59.0, used=5022871552,
    # free=3495079936)
    for i in range(10):
        print(x.cpu_percent_return())
        time.sleep(1)
