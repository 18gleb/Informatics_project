import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QAction

from CRUD import found_user_using_phone, found_user_using_mail
from functions_for_qt import check_mail_or_phone
from qt.entrance_window import Ui_MainWindow
from qt.registration import Registration
from qt.basic import Basic


class Entrance(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.registration_class = Registration()
        self.basic = Basic()
        self.registration.clicked.connect(self.reg)
        self.entry.clicked.connect(self.entry_func)

    def reg(self):
        self.registration_class.show()
        self.close()

    def entry_func(self):
        mail_or_phone = self.input_phone_mail.text()
        password = self.input_password.text()
        mail = check_mail_or_phone(mail_or_phone)
        if not isinstance(mail, tuple):
            self.label_error.setText(mail.error())
        elif len(password) < 8:
            self.label_error.setText("Пароль слишком маленький")
        else:
            if mail[0] == "phone":
                user = found_user_using_phone(mail[1])
                if user is not None:
                    real_password = user.password
                    if real_password == password:
                        self.close()
                        self.basic = Basic(user.id)
                        self.basic.show()
                    else:
                        self.label_error.setText("Неверный пароль")
                else:
                    self.label_error.setText("Мы не смогли найти ваш аккаунт по номеру телефона")
            else:
                user = found_user_using_mail(mail[1])
                if user is not None:
                    real_password = user.password
                    if real_password == password:
                        self.close()
                        self.basic = Basic(user.id)
                        self.basic.show()
                    else:
                        self.label_error.setText("Неверный пароль")
                else:
                    self.label_error.setText("Мы не смогли найти ваш аккаунт по электронной почте")


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Entrance()
    ex.show()
    sys.exit(app.exec())
