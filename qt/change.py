from PyQt5.QtWidgets import QDialog

from CRUD import get_nikname, check_nikname, update_user_nikname, get_password, update_password, get_phone, check_phone, \
    update_phone, get_mail, check_mail, update_mail
from functions_for_qt import update_my_liberty, check_password, nikname_check
from qt.change_window import Ui_Dialog


class Change(QDialog, Ui_Dialog):
    def __init__(self, user_id, page):
        super().__init__()
        self.setupUi(self)
        self.user_id = user_id
        self.page = page

        self.pushButton.clicked.connect(self.change)

    def change(self):
        if self.windowTitle() == "Изменение никнейма":
            old_nik = get_nikname(self.user_id)
            new_nik = self.input.text()
            if self.error.text() != "Ваш никнейм успешно изменён":
                if old_nik == new_nik:
                    self.error.setStyleSheet("color: rgb(255, 0, 0);")
                    self.error.setText("Введите новый никнейм")
                elif isinstance(nikname_check(new_nik), str):
                    update_user_nikname(self.user_id, new_nik)
                    self.error.setStyleSheet("color: rgb(0, 255, 0);")
                    self.error.setText("Ваш никнейм успешно изменён")
                    update_my_liberty(self.user_id, self.page)
                else:
                    self.error.setStyleSheet("color: rgb(255, 0, 0);")
                    self.error.setText(nikname_check(new_nik).error())
        elif self.windowTitle() == "Изменение пароля":
            old_pas = get_password(self.user_id)
            if self.pushButton.text() == "Ввести":
                in_pas = self.input.text()
                if old_pas == in_pas:
                    self.pushButton.setText("Изменить")
                    self.error.setStyleSheet("color: rgb(0, 0, 0);")
                    self.error.setText("Введите новый пароль")
                    self.input.setText("")
                else:
                    self.error.setStyleSheet("color: rgb(255, 0, 0);")
                    self.error.setText("Пароль не совпадает")
            elif self.error.text() != "Ваш пароль успешно изменён":
                new_pas = self.input.text()
                if new_pas == old_pas:
                    self.error.setStyleSheet("color: rgb(255, 0, 0);")
                    self.error.setText("Введите новый пароль")
                elif isinstance(check_password(new_pas), str):
                    update_password(self.user_id, new_pas)
                    self.error.setStyleSheet("color: rgb(0, 255, 0);")
                    self.error.setText("Ваш пароль успешно изменён")
                    update_my_liberty(self.user_id, self.page)
                else:
                    self.error.setStyleSheet("color: rgb(255, 0, 0);")
                    self.error.setText(check_password(new_pas).error())
        elif self.windowTitle().split()[1] == "номера":
            old_phone = get_phone(self.user_id)
            new_phone = self.input.text()
            if self.error.text() != "Ваш номер телефона успешно изменён" and self.error.text() != "Ваш номер телефона успешно добавлен":
                if old_phone == new_phone:
                    self.error.setStyleSheet("color: rgb(255, 0, 0);")
                    self.error.setText("Введите новый номер телефона")
                elif check_phone(new_phone):
                    update_phone(self.user_id, new_phone)
                    self.error.setStyleSheet("color: rgb(0, 255, 0);")
                    if self.pushButton.text() == "Добавить":
                        self.error.setText("Ваш номер телефона успешно добавлен")
                    else:
                        self.error.setText("Ваш номер телефона успешно изменён")
                    update_my_liberty(self.user_id, self.page)
                else:
                    self.error.setStyleSheet("color: rgb(255, 0, 0);")
                    self.error.setText("Этот номер телефона уже занят")
        elif self.windowTitle().split()[1] == "адреса":
            old_mail = get_mail(self.user_id)
            new_mail = self.input.text()
            if self.error.text() != "Ваш адрес электронной почты успешно изменён" and self.error.text() != "Ваш адрес электронной почты успешно добавлен":
                if old_mail == new_mail:
                    self.error.setStyleSheet("color: rgb(255, 0, 0);")
                    self.error.setText("Введите новый адрес электронной почты телефона")
                elif check_mail(new_mail):
                    update_mail(self.user_id, new_mail)
                    self.error.setStyleSheet("color: rgb(0, 255, 0);")
                    if self.pushButton.text() == "Добавить":
                        self.error.setText("Ваш адрес электронной почты успешно добавлен")
                    else:
                        self.error.setText("Ваш адрес электронной почты успешно изменён")
                    update_my_liberty(self.user_id, self.page)
                else:
                    self.error.setStyleSheet("color: rgb(255, 0, 0);")
                    self.error.setText("Этот адрес уже занят")




