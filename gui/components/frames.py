import tkinter as tk
from gui.components.scrollable_frame import ScrollableFrame

class SearchFrame(tk.Frame):
    def __init__(self, parent, open_file_callback, create_buttons_callback, info_frame):
        super().__init__(parent, bg="lightgray", width=1000, height=49)
        self.place(x=0, y=0)

        self.info_frame = info_frame  # Сохраняем info_frame как атрибут

        self.input_message = tk.Entry(self, width=73, font=12)
        self.input_message.place(x=10, y=10)

        self.button_search = tk.Button(
            self,
            text='search',
            font='10',
            bg="lightgray",
            relief=tk.GROOVE,
            activebackground="lightgray",
            width='10'
        )
        self.button_search.place(x=825, y=5)

        self.button_download = tk.Button(
            self,
            text='📁',
            font='12',
            bg="lightgray",
            relief=tk.GROOVE,
            activebackground="lightgray",
            command=lambda: create_buttons_callback(self.info_frame.inner_frame, open_file_callback())
        )
        self.button_download.place(x=950, y=5)

class InfoFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=1000, height=551)
        self.place(x=0, y=51)

        self.scrollable_frame = ScrollableFrame(self)
        self.inner_frame = self.scrollable_frame.inner_frame