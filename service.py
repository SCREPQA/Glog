import json
from tkinter import filedialog

class LogService:
    @staticmethod
    def open_file():
        """
        Открывает файл для чтения, ищет строки с указанными подстроками и возвращает массив.
        """
        file_path = filedialog.askopenfilename(
            title="Выберите файл",
            filetypes=(("JSON файлы", "*.json"), ("Все файлы", "*.*"))
        )
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                return LogService._recursive_search(data)
            except Exception as e:
                print(f"Ошибка при чтении файла: {e}")
        return None

    @staticmethod
    def _recursive_search(obj):
        """
        Рекурсивно ищет строки с указанными подстроками в JSON.
        """
        data_value_string = []

        def search(obj):
            if isinstance(obj, dict):
                for value in obj.values():
                    search(value)
            elif isinstance(obj, list):
                for item in obj:
                    search(item)
            elif isinstance(obj, str):
                if any(substring in obj for substring in ["@cee:{", "{\"level\":", "{\"msec\":", "{\"backend_id\":"]):
                    if obj.startswith("@cee:"):
                        obj = obj.replace("@cee:", "", 1)
                    data_value_string.append(obj)

        search(obj)
        return data_value_string