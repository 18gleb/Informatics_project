class PasswordError:
    def __init__(self, message):
        self.message = message

    def error(self):
        return f'Нужно добавить 1 {self.message} в пароль'
