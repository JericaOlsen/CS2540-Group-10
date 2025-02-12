import tkinter as tk

from computer import Memory, CPU
from gui import MainWindow

def main():

    memory = Memory()
    cpu = CPU(memory)

    root = tk.Tk()
    main_window = MainWindow(root, cpu)
    main_window.mainloop()

if __name__ == "__main__":
    main()
