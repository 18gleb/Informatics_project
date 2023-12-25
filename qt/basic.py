import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from CRUD import found_all_words_in_liberty, get_nikname, get_studied_words, get_not_studied_words
from functions_for_qt import update_my_liberty, create_training, create_exam
from qt.basic_window import Ui_MainWindow
from qt.change import Change
from qt.deleting_word import DeletingWord
from qt.dialog_add_word import AddWord
from qt.exam_result import ExamResult


class Basic(QMainWindow, Ui_MainWindow):
    def __init__(self, user_id=1):
        super().__init__()
        self.setupUi(self)
        self.user_id = user_id
        self.first_lesson = None

        update_my_liberty(self.user_id, self)

        self.exam.clicked.connect(self.exam_func)
        self.treining.clicked.connect(self.training_func)
        self.delete_word.clicked.connect(self.delete_word_func)
        self.add_word.clicked.connect(self.add_word_func)
        self.change.clicked.connect(self.change_funk)
        self.phone.toggled.connect(self.func_for_phone)
        self.mail.toggled.connect(self.func_for_mail)

        self.dialog_add = AddWord(self.user_id)
        self.dialog_del = DeletingWord(self.user_id)
        self.change_win = Change(self.user_id, self)

        self.dialog_add.main_adres = self
        self.dialog_del.main_adres = self

        self.update_progress()

    def exam_func(self):
        exam = create_exam(self.user_id)
        for i in range(0, len(exam) - 1):
            exam[i].next = exam[i + 1]
        result = ExamResult(self.user_id, exam)
        result.next = self
        exam[-1].next = result
        self.first_exam = exam[0]
        self.first_exam.show()
        self.close()

    def training_func(self):
        training = create_training(self.user_id)
        for i in range(0, len(training) - 1):
            training[i].next = training[i + 1]
        training[-1].next = self
        self.first_lesson = training[0]
        self.first_lesson.show()
        self.close()

    def add_word_func(self):
        self.dialog_add.input_word.setText("")
        self.dialog_add.error.setText("")
        self.dialog_add.show()

    def delete_word_func(self):
        self.dialog_del.error.setText("")
        self.dialog_del.create_columns()
        self.dialog_del.show()

    def change_funk(self):
        self.change_win.error.setText("")
        nikname = self.nikname.isChecked()
        password = self.password.isChecked()
        mail = self.mail.isChecked()
        phone = self.phone.isChecked()
        if nikname:
            self.change_win.input.setText(get_nikname(self.user_id))
            self.change_win.setWindowTitle("Изменение никнейма")
            self.change_win.show()
        elif password:
            self.change_win.input.setText("")
            self.change_win.error.setStyleSheet("color: rgb(0, 0, 0);")
            self.change_win.error.setText("Введите старый пароль")
            self.change_win.pushButton.setText("Ввести")
            self.change_win.setWindowTitle("Изменение пароля")
            self.change_win.show()
        elif phone:
            if self.change.text() == "Добавить":
                self.change_win.setWindowTitle("Добавление номера телефона")
                self.change_win.pushButton.setText("Добавить")
                self.change_win.input.setText("")
                self.change_win.show()
            else:
                self.change_win.setWindowTitle("Изменение номера телефона")
                self.change_win.input.setText(self.output_phone.text())
                self.change_win.pushButton.setText("Изменить")
                self.change_win.show()
        elif mail:
            if self.change.text() == "Добавить":
                self.change_win.setWindowTitle("Добавление адреса электронной почты")
                self.change_win.pushButton.setText("Добавить")
                self.change_win.input.setText("")
                self.change_win.show()
            else:
                self.change_win.setWindowTitle("Изменение адреса электронной почты")
                self.change_win.input.setText(self.output_phone.text())
                self.change_win.pushButton.setText("Изменить")
                self.change_win.show()

    def func_for_phone(self):
        if self.phone.isChecked():
            if self.output_phone.text() == "Вы не добавили номер телефона":
                self.change.setText("Добавить")
        else:
            self.change.setText("Изменить")

    def func_for_mail(self):
        if self.mail.isChecked():
            if self.output_mail.text() == "Вы не добавили адрес электронной почты":
                self.change.setText("Добавить")
        else:
            self.change.setText("Изменить")

    def update_progress(self):
        if found_all_words_in_liberty(self.user_id) == 0:
            self.output_progress.setText("В вашей библиотеке нет слов")
        else:
            not_studied = len(get_not_studied_words(self.user_id))
            studied = len(get_studied_words(self.user_id))
            all = not_studied + studied
            percent = int(studied * 100 / all)
            self.progressBar.setValue(percent)

    def __str__(self):
        return "Basic"


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Basic()
    ex.show()
    sys.exit(app.exec())
