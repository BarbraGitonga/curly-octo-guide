# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledGMMrpE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(577, 614)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMouseTracking(True)
        self.horizontalLayout_6 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        palette = QPalette()
        brush = QBrush(QColor(8, 8, 7, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush1 = QBrush(QColor(240, 240, 240, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.frame.setPalette(palette)
        self.frame.setCursor(QCursor(Qt.ArrowCursor))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.title_label = QLabel(self.frame)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setStyleSheet(u"color: rgb(255, 253, 242);\n"
"font: 14pt \"Segoe Print\";\n"
"")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.title_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.exit_biutton = QPushButton(self.frame)
        self.exit_biutton.setObjectName(u"exit_biutton")
        self.exit_biutton.setMinimumSize(QSize(30, 30))
        self.exit_biutton.setMaximumSize(QSize(30, 30))
        self.exit_biutton.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.exit_biutton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(20)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)

        self.index1 = QPushButton(self.frame)
        self.index1.setObjectName(u"index1")
        self.index1.setMinimumSize(QSize(120, 120))
        self.index1.setMaximumSize(QSize(150, 150))
        self.index1.setCursor(QCursor(Qt.OpenHandCursor))
        self.index1.setStyleSheet(u"border: none;\n"
"border-radius: 8px;\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(170, 0, 255);")

        self.horizontalLayout_9.addWidget(self.index1)

        self.index2 = QPushButton(self.frame)
        self.index2.setObjectName(u"index2")
        self.index2.setMinimumSize(QSize(120, 120))
        self.index2.setMaximumSize(QSize(150, 150))
        self.index2.setCursor(QCursor(Qt.OpenHandCursor))
        self.index2.setStyleSheet(u"border: none;\n"
"border-radius: 8px;\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(170, 0, 255);")

        self.horizontalLayout_9.addWidget(self.index2)

        self.index3 = QPushButton(self.frame)
        self.index3.setObjectName(u"index3")
        self.index3.setMinimumSize(QSize(120, 120))
        self.index3.setMaximumSize(QSize(150, 150))
        self.index3.setCursor(QCursor(Qt.OpenHandCursor))
        self.index3.setStyleSheet(u"border: none;\n"
"border-radius: 8px;\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(170, 0, 255);")

        self.horizontalLayout_9.addWidget(self.index3)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_10)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(20)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)

        self.index4 = QPushButton(self.frame)
        self.index4.setObjectName(u"index4")
        self.index4.setMinimumSize(QSize(120, 120))
        self.index4.setMaximumSize(QSize(150, 150))
        self.index4.setCursor(QCursor(Qt.OpenHandCursor))
        self.index4.setStyleSheet(u"border: none;\n"
"border-radius: 8px;\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(170, 0, 255);")

        self.horizontalLayout_8.addWidget(self.index4)

        self.index5 = QPushButton(self.frame)
        self.index5.setObjectName(u"index5")
        self.index5.setMinimumSize(QSize(120, 120))
        self.index5.setMaximumSize(QSize(150, 150))
        self.index5.setCursor(QCursor(Qt.OpenHandCursor))
        self.index5.setStyleSheet(u"border: none;\n"
"border-radius: 8px;\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(170, 0, 255);")

        self.horizontalLayout_8.addWidget(self.index5)

        self.index6 = QPushButton(self.frame)
        self.index6.setObjectName(u"index6")
        self.index6.setMinimumSize(QSize(120, 120))
        self.index6.setMaximumSize(QSize(150, 150))
        self.index6.setCursor(QCursor(Qt.OpenHandCursor))
        self.index6.setStyleSheet(u"border: none;\n"
"border-radius: 8px;\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(170, 0, 255);")

        self.horizontalLayout_8.addWidget(self.index6)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(20)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_11)

        self.index7 = QPushButton(self.frame)
        self.index7.setObjectName(u"index7")
        self.index7.setMinimumSize(QSize(120, 120))
        self.index7.setMaximumSize(QSize(150, 150))
        self.index7.setCursor(QCursor(Qt.OpenHandCursor))
        self.index7.setStyleSheet(u"border: none;\n"
"border-radius: 8px;\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(170, 0, 255);")

        self.horizontalLayout_10.addWidget(self.index7)

        self.index8 = QPushButton(self.frame)
        self.index8.setObjectName(u"index8")
        self.index8.setMinimumSize(QSize(120, 120))
        self.index8.setMaximumSize(QSize(150, 150))
        self.index8.setCursor(QCursor(Qt.OpenHandCursor))
        self.index8.setStyleSheet(u"border: none;\n"
"border-radius: 8px;\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(170, 0, 255);")

        self.horizontalLayout_10.addWidget(self.index8)

        self.index9 = QPushButton(self.frame)
        self.index9.setObjectName(u"index9")
        self.index9.setMinimumSize(QSize(120, 120))
        self.index9.setMaximumSize(QSize(150, 150))
        self.index9.setCursor(QCursor(Qt.OpenHandCursor))
        self.index9.setStyleSheet(u"border: none;\n"
"border-radius: 8px;\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(170, 0, 255);")

        self.horizontalLayout_10.addWidget(self.index9)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_12)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout_6.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 577, 21))
        self.menutic_tac_toe = QMenu(self.menubar)
        self.menutic_tac_toe.setObjectName(u"menutic_tac_toe")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menutic_tac_toe.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.exit_biutton.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.index1.setText("")
        self.index2.setText("")
        self.index3.setText("")
        self.index4.setText("")
        self.index5.setText("")
        self.index6.setText("")
        self.index7.setText("")
        self.index8.setText("")
        self.index9.setText("")
        self.menutic_tac_toe.setTitle(QCoreApplication.translate("MainWindow", u"tic tac toe", None))
    # retranslateUi

