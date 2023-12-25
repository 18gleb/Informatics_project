from PyQt5.QtWidgets import QDialog

from CRUD import update_bool_liberty_word
from qt.exam_result_window import Ui_Dialog


class ExamResult(QDialog, Ui_Dialog):
    def __init__(self, user_id: int, lessons: list):
        super().__init__()
        self.setupUi(self)
        self.user_id = user_id
        self.lessons = lessons
        self.next = None
        self.pushButton_end.clicked.connect(self.exit)
        self.output_list = [(self.word1, self.result1), (self.word2, self.result2), (self.word3, self.result3)]

    def exit(self):
        self.close()
        self.next.update_progress()
        self.next.show()

    def result(self):
        result = {}
        for i in self.lessons:
            word_on_eng = i.correct_word.on_eng
            right = i.right
            if word_on_eng not in result:
                result[word_on_eng] = right
            else:
                if result[word_on_eng] is False:
                    continue
                else:
                    if right is False:
                        result[word_on_eng] = False
                    else:
                        continue
        return result

    def output_result(self):
        result = self.result()
        items = []
        for word, res in result.items():
            items.append((word, res))
        for i in range(0, len(items)):
            self.output_list[i][0].setText(items[i][0])
            if items[i][1]:
                self.output_list[i][1].setStyleSheet("color: rgb(0, 255, 0);")
                self.output_list[i][1].setText("Зачёт")
                update_bool_liberty_word(self.user_id, items[i][0])
            else:
                self.output_list[i][1].setStyleSheet("color: rgb(255, 0, 0);")
                self.output_list[i][1].setText("Незачёт")

    def __str__(self):
        return "ExamResult"
