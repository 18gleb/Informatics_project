import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from exceptions import AccountNumberExist, AccountMailExist
from functions_for_qt import check_mail_or_phone, check_password, nikname_check
from qt.basic import Basic
from qt.reg_window import Ui_MainWindow
from CRUD import check_nikname, create_User, found_user_using_phone, found_user_using_mail


class Registration(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.basic = Basic()
        self.pushButton.clicked.connect(self.reg)

    def reg(self):
        mail_or_phone = self.input_mail.text()
        password = self.input_paasword.text()
        nikname = self.input_nikname.text()
        mail = check_mail_or_phone(mail_or_phone)
        if not isinstance(mail, tuple):
            self.label_error.setText(mail.error())
        elif not isinstance(nikname_check(nikname), str):
            self.label_error.setText(nikname_check(nikname).error())
        elif not isinstance(check_password(password), str):   #TODO: Сделай нормальную проверку пароля
            self.label_error.setText(check_password(password).error())
        else:
            if mail[0] == "phone":
                if found_user_using_phone(mail[1]) is not None:
                    self.label_error.setText(AccountNumberExist().error())
                else:
                    create_User(None, mail[1], password, nikname)
                    user = found_user_using_phone(mail[1])
                    self.basic = Basic(user.id)
                    self.basic.show()
                    self.close()
            else:
                if found_user_using_mail(mail[1]) is not None:
                    self.label_error.setText(AccountMailExist().error())
                else:
                    create_User(mail[1], None, password, nikname)
                    user = found_user_using_mail(mail[1])
                    self.basic = Basic(user.id)
                    self.basic.show()
                    self.close()





sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

if __name__ == '__main__':
    # Создадим класс приложения PyQT
    app = QApplication(sys.argv)
    # А теперь создадим и покажем пользователю экземпляр
    # нашего виджета класса Example
    ex = Registration()
    ex.show()

    # Будем ждать, пока пользователь не завершил исполнение QApplication,
    # а потом завершим и нашу программу
    sys.exit(app.exec())
