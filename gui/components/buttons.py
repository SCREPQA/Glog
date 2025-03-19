import tkinter as tk
import json
import re

def create_buttons(frame, logs):
    if logs is None:
        print("Нет данных для отображения.")
        return

    for widget in frame.winfo_children():
        widget.destroy()

    button_width = 137
    button_height = 8
    y_padding = 0

    def button_click(text):
        # Сворачиваем основное окно root
        frame.master.master.master.iconify()  # Сворачиваем root

        try:
            parsed_json = json.loads(text)
            if "sql" in parsed_json:
                parsed_json["sql"] = parsed_json["sql"].replace("\n", " ").strip()
            formatted_text = json.dumps(parsed_json, indent=4, ensure_ascii=False)

            if "args" in parsed_json and isinstance(parsed_json["args"], list):
                args = parsed_json["args"]
                sql_query = parsed_json.get("sql", "")
                for i, arg in enumerate(args, start=1):
                    sql_query = sql_query.replace(f"${i}", str(arg))
                formatted_text += f"\n\n--- SQL Запрос ---\n{sql_query}"

        except json.JSONDecodeError:
            formatted_text = text

        new_window = tk.Toplevel()
        new_window.title('json')
        new_window.geometry('400x490')
        new_window.resizable(False, False)
        new_window.iconbitmap("icons\icon.ico")

        output_text = tk.Text(new_window, wrap=tk.WORD, height=100, width=70, font="Arial 10")
        output_text.pack(pady=2, padx=2)

        output_text.tag_configure("bold", font="Arial 10 bold")
        output_text.insert(tk.END, formatted_text)

        for match in re.finditer(r'"(\w+)":', formatted_text):
            start = f"1.0 + {match.start()} chars"
            end = f"1.0 + {match.end()} chars"
            output_text.tag_add("bold", start, end)

        def copy_text():
            new_window.clipboard_clear()
            new_window.clipboard_append(output_text.get("sel.first", "sel.last"))

        context_menu = tk.Menu(new_window, tearoff=0)
        context_menu.add_command(label="Копировать", command=copy_text)

        def show_context_menu(event):
            context_menu.post(event.x_root, event.y_root)

        output_text.bind("<Button-3>", show_context_menu)

        def on_closing():
            new_window.destroy()
            frame.master.master.master.deiconify()

        new_window.protocol("WM_DELETE_WINDOW", on_closing)

    for log in logs:
        button = tk.Button(
            frame,
            text=log,
            wraplength=930,
            relief=tk.GROOVE,
            justify=tk.LEFT,
            width=button_width,
            height=button_height,
            padx=5,
            pady=1,
            anchor="w",
            command=lambda text=log: button_click(text)
        )
        button.pack(pady=y_padding, fill=tk.X)

    frame.update_idletasks()
    frame.master.configure(scrollregion=frame.master.bbox("all"))