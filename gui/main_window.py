import tkinter as tk
from gui.components.frames import SearchFrame, InfoFrame
from gui.components.buttons import create_buttons
from utils.file_utils import open_file

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('GLOG')
        self.root.geometry('1000x607')
        self.root.resizable(False, False)
        self.root.iconbitmap("icons\icon.ico")

        # Создаем InfoFrame
        self.info_frame = InfoFrame(self.root)

        # Передаем info_frame в SearchFrame
        self.search_frame = SearchFrame(self.root, open_file, create_buttons, self.info_frame)

    def run(self):
        self.root.mainloop()