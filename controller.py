# controller.py
import json
from model import LogModel
from service import LogService
from view import LogView  # Добавьте этот импорт, если используете LogView в контроллере
import tkinter as tk


class LogController:
    def __init__(self, root):
        self.model = LogModel()
        self.view = LogView(root, self)
        self.service = LogService()

    def on_download_clicked(self):
        """Обрабатывает нажатие кнопки загрузки."""
        logs = self.service.open_file()
        if logs:
            self.model.clear_logs()
            for log in logs:
                self.model.add_log(log)
            self.view.create_buttons(self.model.get_logs())

    def on_log_clicked(self, log):
        """Обрабатывает нажатие на кнопку с логом."""
        try:
            parsed_json = json.loads(log)
            formatted_text = json.dumps(parsed_json, indent=4, ensure_ascii=False)
        except json.JSONDecodeError:
            formatted_text = log

        new_window = tk.Toplevel(self.view.root)
        new_window.title('level')
        new_window.geometry('502x599')
        new_window.resizable(False, False)
        new_window.iconbitmap("icon.ico")

        output_text = tk.Text(new_window, wrap=tk.WORD, height=37, width=70, font="Arial 10")
        output_text.insert(tk.END, formatted_text)
        output_text.place(x=3, y=0)