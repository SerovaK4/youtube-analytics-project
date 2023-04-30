class HttpError(Exception):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Получен пустой ответ"

    def __str__(self):
        return self.message
