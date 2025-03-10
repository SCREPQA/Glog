import tkinter as tk
from tkinter import filedialog

class LogView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self._setup_gui()

    def _setup_gui(self):
        """Настраивает графический интерфейс."""
        self.root.title('GLOG')
        self.root.geometry('1000x607')
        self.root.resizable(False, False)
        self.root.iconbitmap("icon.ico")

        # Frame для поиска и загрузки
        self.frame_search = tk.Frame(self.root, bg="lightgray", width=1000, height=49)
        self.frame_search.place(x=0, y=0)

        # Поле ввода
        self.input_message = tk.Entry(self.frame_search, width=70, font=12)
        self.input_message.place(x=20, y=10)

        # Кнопка поиска
        self.button_search = tk.Button(
            self.frame_search,
            text='search',
            font='10',
            bg="lightgray",
            relief=tk.GROOVE,
            activebackground="lightgray",
            width='10'
        )
        self.button_search.place(x=805, y=5)

        # Кнопка загрузки
        self.button_download = tk.Button(
            self.frame_search,
            text='📁',
            font='12',
            bg="lightgray",
            relief=tk.GROOVE,
            activebackground="lightgray",
            command=self.controller.on_download_clicked
        )
        self.button_download.place(x=935, y=5)

        # Frame для отображения логов
        self.frame_info = tk.Frame(self.root, width=1000, height=551)
        self.frame_info.place(x=0, y=51)

    def create_buttons(self, logs):
        """Создает кнопки для отображения логов."""
        if logs is None:
            print("Нет данных для отображения.")
            return

        canvas = tk.Canvas(self.frame_info, width=980, height=551)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(self.frame_info, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        inner_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")

        # def on_mousewheel(event):
        #     canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        # canvas.bind("<MouseWheel>", on_mousewheel)

        # Привязываем событие прокрутки колеса мыши к Canvas
        def on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        # Привязываем событие <MouseWheel> к Canvas
        canvas.bind_all("<MouseWheel>", on_mousewheel)

        for log in logs:
            button = tk.Button(
                inner_frame,
                text=log,
                wraplength=930,
                relief=tk.GROOVE,
                justify=tk.LEFT,
                width=137,
                height=10,
                padx=5,
                pady=1,
                anchor="w",
                font='8',
                command=lambda text=log: self.controller.on_log_clicked(text)
            )
            button.pack(pady=0, fill=tk.X)