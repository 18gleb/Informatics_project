from PyQt5.QtWidgets import QDialog, QTableWidgetItem

from CRUD import get_words, del_word_in_liberty_word
from qt.deleting_word_window import Ui_Dialog


class DeletingWord(QDialog, Ui_Dialog):   #TODO: Сделать нормальную проверку
    def __init__(self, user_id):
        super().__init__()
        self.setupUi(self)
        self.user_id = user_id
        self.main_adres = None
        self.pushButton.clicked.connect(self.del_word)

    def create_columns(self):
        words = get_words(self.user_id)
        counter = 0
        if words:
            self.tableWidget.setRowCount(len(words))
            for i in words:
                self.tableWidget.setItem(counter, 0, QTableWidgetItem(i.on_rus))
                self.tableWidget.setItem(counter, 1, QTableWidgetItem(i.on_eng))
                counter += 1
        else:
            self.tableWidget.setRowCount(0)
            self.error.setText("В ВАШЕЙ БИБЛИОТЕКЕ НЕТ СЛОВ")

    def del_word(self):
        pos = self.tableWidget.selectedItems()
        if pos:
            del_word_in_liberty_word(self.user_id, pos[0].text())
            self.create_columns()
        else:
            if self.error.text() != "В ВАШЕЙ БИБЛИОТЕКЕ НЕТ СЛОВ":
                self.error.setText("ВЫБЕРЕТЕ СЛОВО")
        self.main_adres.update_progress()





