from random import choice

from PyQt5.QtWidgets import QMainWindow, QPushButton

from qt.lesson3_window import Ui_MainWindow


class Lesson3(QMainWindow, Ui_MainWindow):
    def __init__(self, words, correct_word):
        super().__init__()
        self.setupUi(self)
        self.words = words.copy()
        self.next = None
        self.right = False
        self.correct_word = correct_word
        self.word.setText(self.correct_word.on_eng)
        self.buttons = []
        for i in self.findChildren(QPushButton):
            i.clicked.connect(self.check)
            self.buttons.append(i)
        self.create_button()

    def create_button(self):
        random_but = choice(self.buttons)
        self.buttons.remove(random_but)
        random_but.setText(self.correct_word.on_rus)
        if self.correct_word in self.words:
            self.words.remove(self.correct_word)
        for i in range(0, 4):
            word = choice(self.words)
            button = choice(self.buttons)
            self.words.remove(word)
            self.buttons.remove(button)
            button.setText(word.on_rus)

    def check(self):
        if self.sender().text() != "Продолжить" and self.sender().text() != "Завершить":
            answer = self.sender().text()
            if answer == self.correct_word.on_rus:
                self.word.setText("Верно")
                self.right = True
            else:
                self.word.setText("Неверно")
                self.right = False
            if str(self.next) == "Basic":
                self.sender().setText("Завершить")
            else:
                self.sender().setText("Продолжить")
        else:
            if str(self.next) == "ExamResult":
                self.next.output_result()
            self.close()
            self.next.show()

