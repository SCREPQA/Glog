import json
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(
        title="Выберите файл",
        filetypes=(("JSON файлы", "*.json"), ("Все файлы", "*.*"))
    )
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            data_value_string = []

            def recursive_search(obj):
                if isinstance(obj, dict):
                    for key, value in obj.items():
                        recursive_search(value)
                elif isinstance(obj, list):
                    for item in obj:
                        recursive_search(item)
                elif isinstance(obj, str):
                    if any(substring in obj for substring in ["@cee:{", "{\"level\":", "{\"msec\":", "{\"backend_id\":"]):
                        if obj.startswith("@cee:"):
                            obj = obj.replace("@cee:", "", 1)
                        data_value_string.append(obj)

            recursive_search(data)
            return data_value_string

        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return None
    return None