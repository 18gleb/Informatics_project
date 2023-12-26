class ShortPassword:
    def __init__(self, count=1):
        self.count = count

    def error(self):
        return f"""В пароле нужно увеличить число символов - {self.count}"""
