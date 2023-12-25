from pickle import dump

from PyQt5.QtWidgets import QMainWindow
from playsound import playsound

from qt.lesson2_window import Ui_MainWindow


class Lesson2(QMainWindow, Ui_MainWindow):
    def __init__(self, correct_word):
        super().__init__()
        self.setupUi(self)
        self.correct_word = correct_word
        self.next = None
        self.voice.clicked.connect(self.funck_for_voice)
        self.check.clicked.connect(self.funck_for_check)
        self.right = False

    def funck_for_voice(self):
        with open("word.mp3", "wb") as output:
            dump(self.correct_word.how_to_listen, output)
        playsound("word.mp3")

    def funck_for_check(self):
        if self.check.text() == "Проверить":  # TODO: Переделать ввод слов например: В начале в output_word писать "Введите слово на английском" или "Введите слово на русском"
            answer = self.output_word.text().lower()
            if self.correct_word.on_eng == answer:
                self.output_word.setText("Верно")
                self.right = True
            elif self.correct_word.on_rus == answer:
                self.output_word.setText("Верно")
                self.right = True
            else:
                self.output_word.setText("Неверно")
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
