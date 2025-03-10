# main.py
import tkinter as tk
from controller import LogController  # Импортируем класс LogController

if __name__ == "__main__":
    root = tk.Tk()
    app = LogController(root)  # Создаем экземпляр класса LogController
    root.mainloop()