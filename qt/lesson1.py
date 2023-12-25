import sys

from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

from qt.lesson1_window import Ui_MainWindow


class Lesson1(QMainWindow, Ui_MainWindow):
    def __init__(self, correct_word):
        super().__init__()
        self.setupUi(self)
        self.correct_word = correct_word
        self.check.clicked.connect(self.funk_for_check)
        self.output_buttons = []
        self.input_buttons = []
        self.next = None
        self.right = False
        self.pushButton.clicked.connect(self.del_aplha)
        for button in self.findChildren(QPushButton):
            if button.objectName()[-1].isdigit():
                button.clicked.connect(self.del_aplha)
                self.output_buttons.append(button)
            elif button.objectName()[-2] == "_":
                if button.objectName()[-1].isalpha():
                    button.clicked.connect(self.input_alpha)
                    self.input_buttons.append(button)
        self.output_buttons.sort(key=lambda x: int(x.objectName().split("_")[-1]))
        self.output_buttons.insert(0, self.pushButton)
        self.word.setText(self.correct_word.on_rus)  # on_rus
        self.update_button(len(self.correct_word.on_eng))  # on_eng

    def update_button(self, len_word):
        count = 0
        while len_word < 16:
            if count % 2 == 0:
                button = self.output_buttons.pop(0)
                button.hide()
                count += 1
                len_word += 1
            else:
                button = self.output_buttons.pop(-1)
                button.hide()
                count += 1
                len_word += 1

    def input_alpha(self):
        if self.check.text() == "Проверить":
            text = self.sender().text()
            for i in self.output_buttons:
                if i.text() == "":
                    i.setText(text)
                    break

    def del_aplha(self):
        if self.check.text() == "Проверить":
            self.sender().setText("")

    def funk_for_check(self):
        if self.check.text() == "Проверить":
            answer = ""
            for i in self.output_buttons:
                answer += i.text()
            if answer == self.correct_word.on_eng:
                self.word.setStyleSheet("color: rgb(0, 255, 0);")
                self.word.setText("Верно")
                self.right = True
            else:
                self.word.setStyleSheet("color: rgb(255, 0, 0);")
                self.word.setText(f"Неверно.\n Правильный ответ: {self.correct_word.on_eng}")
                self.right = False
            if str(self.next) == "Basic":
                self.check.setText("Завершить")
            else:
                self.check.setText("Продолжить")
        else:
            if str(self.next) == "ExamResult":
                self.next.output_result()
            self.close()
            self.next.show()


class Word:
    def __init__(self, on_rus, on_eng):
        self.on_rus = on_rus
        self.on_eng = on_eng


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Lesson1(Word("линейка", "rulerdasfads"))
    ex.show()
    sys.exit(app.exec())
