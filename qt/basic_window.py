# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New_basic_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.output_progress = QtWidgets.QLabel(self.tab)
        self.output_progress.setText("")
        self.output_progress.setObjectName("output_progress")
        self.horizontalLayout.addWidget(self.output_progress)
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.exam = QtWidgets.QPushButton(self.tab)
        self.exam.setObjectName("exam")
        self.horizontalLayout_2.addWidget(self.exam)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.treining = QtWidgets.QPushButton(self.tab)
        self.treining.setObjectName("treining")
        self.horizontalLayout_2.addWidget(self.treining)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_13.addLayout(self.verticalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(20, 176, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem6)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.nikname = QtWidgets.QRadioButton(self.tab_2)
        self.nikname.setText("")
        self.nikname.setObjectName("nikname")
        self.horizontalLayout_5.addWidget(self.nikname)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.output_nikname = QtWidgets.QLabel(self.tab_2)
        self.output_nikname.setText("")
        self.output_nikname.setObjectName("output_nikname")
        self.horizontalLayout_3.addWidget(self.output_nikname)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.phone = QtWidgets.QRadioButton(self.tab_2)
        self.phone.setText("")
        self.phone.setObjectName("phone")
        self.horizontalLayout_6.addWidget(self.phone)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.output_phone = QtWidgets.QLabel(self.tab_2)
        self.output_phone.setText("")
        self.output_phone.setObjectName("output_phone")
        self.horizontalLayout_4.addWidget(self.output_phone)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.mail = QtWidgets.QRadioButton(self.tab_2)
        self.mail.setText("")
        self.mail.setObjectName("mail")
        self.horizontalLayout_7.addWidget(self.mail)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.output_mail = QtWidgets.QLabel(self.tab_2)
        self.output_mail.setText("")
        self.output_mail.setObjectName("output_mail")
        self.horizontalLayout_8.addWidget(self.output_mail)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem9)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.password = QtWidgets.QRadioButton(self.tab_2)
        self.password.setText("")
        self.password.setObjectName("password")
        self.horizontalLayout_9.addWidget(self.password)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_11.addWidget(self.label_5)
        self.output_password = QtWidgets.QLabel(self.tab_2)
        self.output_password.setText("")
        self.output_password.setObjectName("output_password")
        self.horizontalLayout_11.addWidget(self.output_password)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem10)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_11)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem11)
        self.change = QtWidgets.QPushButton(self.tab_2)
        self.change.setObjectName("change")
        self.horizontalLayout_12.addWidget(self.change)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem12)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_10.addLayout(self.verticalLayout_2)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem13)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        spacerItem14 = QtWidgets.QSpacerItem(20, 176, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem14)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem15 = QtWidgets.QSpacerItem(20, 226, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem15)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem16)
        self.add_word = QtWidgets.QPushButton(self.tab_3)
        self.add_word.setObjectName("add_word")
        self.horizontalLayout_14.addWidget(self.add_word)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem17)
        self.delete_word = QtWidgets.QPushButton(self.tab_3)
        self.delete_word.setObjectName("delete_word")
        self.horizontalLayout_14.addWidget(self.delete_word)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem18)
        self.verticalLayout_5.addLayout(self.horizontalLayout_14)
        spacerItem19 = QtWidgets.QSpacerItem(20, 226, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem19)
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayout_15.addWidget(self.tabWidget)
        spacerItem20 = QtWidgets.QSpacerItem(20, 536, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_15.addItem(spacerItem20)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Основная страница"))
        self.label.setText(_translate("MainWindow", "Прогресс:"))
        self.exam.setText(_translate("MainWindow", "Экзамен"))
        self.treining.setText(_translate("MainWindow", "Тренировка"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Основная страница"))
        self.label_2.setText(_translate("MainWindow", "Ваш никнейм:"))
        self.label_3.setText(_translate("MainWindow", "Ваш номер телефона:"))
        self.label_4.setText(_translate("MainWindow", "Ваш адрес электронной почты:"))
        self.label_5.setText(_translate("MainWindow", "Ваш пароль:"))
        self.change.setText(_translate("MainWindow", "Изменить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Мой профиль"))
        self.add_word.setText(_translate("MainWindow", "Добавить слово"))
        self.delete_word.setText(_translate("MainWindow", "Удалить слово"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Библиотека"))
