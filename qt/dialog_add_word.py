from PyQt5.QtWidgets import QDialog

from functions_for_qt import check_word_in_liberty
from qt.dialog_add_word_window import Ui_Dialog


class AddWord(QDialog, Ui_Dialog):
    def __init__(self, user_id):
        super().__init__()
        self.setupUi(self)
        self.user_id = user_id
        self.main_adres = None
        self.add_word.clicked.connect(self.add_word_func)

    def add_word_func(self):
        if self.error.text() != "Слово успешно добавлено":
            word = self.input_word.text().lower()
            result = check_word_in_liberty(word, self.user_id)
            if isinstance(result, str):
                self.error.setStyleSheet("color: rgb(0, 255, 0);")
                self.error.setText("Слово успешно добавлено")
                self.main_adres.update_progress()
            else:
                self.error.setStyleSheet("color: rgb(255, 0, 0);")
                self.error.setText(result.error())

