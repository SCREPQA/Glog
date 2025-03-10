class LogModel:
    def __init__(self):
        self.logs = []  # Массив для хранения логов

    def add_log(self, log):
        """Добавляет лог в массив."""
        self.logs.append(log)

    def get_logs(self):
        """Возвращает все логи."""
        return self.logs

    def clear_logs(self):
        """Очищает массив логов."""
        self.logs.clear()