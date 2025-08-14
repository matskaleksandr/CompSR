# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CompInfo.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_CompInfo(object):
    def setupUi(self, CompInfo):
        if not CompInfo.objectName():
            CompInfo.setObjectName(u"CompInfo")
        CompInfo.resize(1011, 645)
        self.centralwidget = QWidget(CompInfo)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 0, 171, 41))
        font = QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(810, 570, 191, 41))
        self.pushButton_2.setFont(font)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 50, 991, 481))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(480, 0, 281, 41))
        self.textEdit_2 = QTextEdit(self.frame)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(480, 40, 281, 41))
        self.textEdit_3 = QTextEdit(self.frame)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(480, 80, 281, 41))
        self.textEdit_4 = QTextEdit(self.frame)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(480, 120, 281, 41))
        self.textEdit_5 = QTextEdit(self.frame)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(480, 160, 281, 41))
        self.textEdit_6 = QTextEdit(self.frame)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(480, 200, 281, 41))
        self.textEdit_7 = QTextEdit(self.frame)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setGeometry(QRect(480, 240, 281, 41))
        self.textEdit_8 = QTextEdit(self.frame)
        self.textEdit_8.setObjectName(u"textEdit_8")
        self.textEdit_8.setGeometry(QRect(480, 280, 281, 41))
        self.textEdit_9 = QTextEdit(self.frame)
        self.textEdit_9.setObjectName(u"textEdit_9")
        self.textEdit_9.setGeometry(QRect(480, 320, 281, 41))
        self.textEdit_10 = QTextEdit(self.frame)
        self.textEdit_10.setObjectName(u"textEdit_10")
        self.textEdit_10.setGeometry(QRect(480, 360, 281, 41))
        self.textEdit_11 = QTextEdit(self.frame)
        self.textEdit_11.setObjectName(u"textEdit_11")
        self.textEdit_11.setGeometry(QRect(480, 400, 281, 41))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 171, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 40, 171, 31))
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 80, 171, 31))
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 120, 171, 31))
        self.label_4.setFont(font1)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 160, 171, 31))
        self.label_5.setFont(font1)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 200, 171, 31))
        self.label_6.setFont(font1)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 240, 171, 31))
        self.label_7.setFont(font1)
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 280, 171, 31))
        self.label_8.setFont(font1)
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 320, 171, 31))
        self.label_9.setFont(font1)
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 360, 171, 31))
        self.label_10.setFont(font1)
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 400, 171, 31))
        self.label_11.setFont(font1)
        self.textEdit_12 = QTextEdit(self.frame)
        self.textEdit_12.setObjectName(u"textEdit_12")
        self.textEdit_12.setGeometry(QRect(480, 440, 281, 41))
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 440, 171, 31))
        self.label_12.setFont(font1)
        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(170, 0, 311, 41))
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"background-color: rgb(54, 54, 54);\n"
"border: 1px solid black;\n"
"")
        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(170, 40, 311, 41))
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"background-color: rgb(54, 54, 54);\n"
"border: 1px solid black;\n"
"")
        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(170, 80, 311, 41))
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u"background-color: rgb(54, 54, 54);\n"
"border: 1px solid black;\n"
"")
        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(170, 120, 311, 41))
        self.label_16.setFont(font1)
        self.label_16.setStyleSheet(u"background-color: rgb(54, 54, 54);\n"
"border: 1px solid black;\n"
"")
        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(170, 160, 311, 41))
        self.label_17.setFont(font1)
        self.label_17.setStyleSheet(u"background-color: rgb(54, 54, 54);\n"
"border: 1px solid black;\n"
"")
        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(170, 200, 311, 41))
        self.label_18.setFont(font1)
        self.label_18.setStyleSheet(u"background-color: rgb(54, 54, 54);\n"
"border: 1px solid black;\n"
"")
        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(170, 240, 311, 41))
        self.label_19.setFont(font1)
        self.label_19.setStyleSheet(u"background-color: rgb(54, 54, 54);\n"
"border: 1px solid black;\n"
"")
        self.label_20 = QLabel(self.frame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(170, 280, 311, 41))
        self.label_20.setFont(font1)
        self.label_20.setStyleSheet(u"background-color: rgb(54, 54, 54);\n"
"border: 1px solid black;\n"
"")
        self.label_21 = QLabel(self.frame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(170, 320, 311, 41))
        self.label_21.setFont(font1)
        self.label_21.setStyleSheet(u"background-color: rgb(54, 54, 54);\n"
"border: 1px solid black;\n"
"")
        self.label_22 = QLabel(self.frame)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(170, 360, 311, 41))
        self.label_22.setFont(font1)
        self.label_22.setStyleSheet(u"background-color: rgb(54, 54, 54);\n"
"border: 1px solid black;\n"
"")
        self.label_23 = QLabel(self.frame)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(170, 400, 311, 41))
        self.label_23.setFont(font1)
        self.label_23.setStyleSheet(u"background-color: rgb(54, 54, 54);\n"
"border: 1px solid black;\n"
"")
        self.label_24 = QLabel(self.frame)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(170, 440, 311, 41))
        self.label_24.setFont(font1)
        self.label_24.setStyleSheet(u"background-color: rgb(54, 54, 54);\n"
"border: 1px solid black;\n"
"")
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(760, 0, 41, 41))
        self.pushButton_3.setFont(font)
        icon = QIcon()
        icon.addFile(u"png/copy.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QSize(25, 25))
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(760, 40, 41, 41))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QSize(25, 25))
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(760, 80, 41, 41))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QSize(25, 25))
        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(760, 120, 41, 41))
        self.pushButton_6.setFont(font)
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setIconSize(QSize(25, 25))
        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(760, 160, 41, 41))
        self.pushButton_7.setFont(font)
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setIconSize(QSize(25, 25))
        self.pushButton_8 = QPushButton(self.frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(760, 200, 41, 41))
        self.pushButton_8.setFont(font)
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setIconSize(QSize(25, 25))
        self.pushButton_9 = QPushButton(self.frame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(760, 240, 41, 41))
        self.pushButton_9.setFont(font)
        self.pushButton_9.setIcon(icon)
        self.pushButton_9.setIconSize(QSize(25, 25))
        self.pushButton_10 = QPushButton(self.frame)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(760, 280, 41, 41))
        self.pushButton_10.setFont(font)
        self.pushButton_10.setIcon(icon)
        self.pushButton_10.setIconSize(QSize(25, 25))
        self.pushButton_11 = QPushButton(self.frame)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(760, 320, 41, 41))
        self.pushButton_11.setFont(font)
        self.pushButton_11.setIcon(icon)
        self.pushButton_11.setIconSize(QSize(25, 25))
        self.pushButton_12 = QPushButton(self.frame)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(760, 360, 41, 41))
        self.pushButton_12.setFont(font)
        self.pushButton_12.setIcon(icon)
        self.pushButton_12.setIconSize(QSize(25, 25))
        self.pushButton_13 = QPushButton(self.frame)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(760, 400, 41, 41))
        self.pushButton_13.setFont(font)
        self.pushButton_13.setIcon(icon)
        self.pushButton_13.setIconSize(QSize(25, 25))
        self.pushButton_14 = QPushButton(self.frame)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(760, 440, 41, 41))
        self.pushButton_14.setFont(font)
        self.pushButton_14.setIcon(icon)
        self.pushButton_14.setIconSize(QSize(25, 25))
        self.textEdit_13 = QTextEdit(self.frame)
        self.textEdit_13.setObjectName(u"textEdit_13")
        self.textEdit_13.setGeometry(QRect(800, 0, 191, 41))
        self.textEdit_14 = QTextEdit(self.frame)
        self.textEdit_14.setObjectName(u"textEdit_14")
        self.textEdit_14.setGeometry(QRect(800, 40, 191, 41))
        self.textEdit_15 = QTextEdit(self.frame)
        self.textEdit_15.setObjectName(u"textEdit_15")
        self.textEdit_15.setGeometry(QRect(800, 80, 191, 41))
        self.textEdit_16 = QTextEdit(self.frame)
        self.textEdit_16.setObjectName(u"textEdit_16")
        self.textEdit_16.setGeometry(QRect(800, 120, 191, 41))
        self.textEdit_17 = QTextEdit(self.frame)
        self.textEdit_17.setObjectName(u"textEdit_17")
        self.textEdit_17.setGeometry(QRect(800, 160, 191, 41))
        self.textEdit_18 = QTextEdit(self.frame)
        self.textEdit_18.setObjectName(u"textEdit_18")
        self.textEdit_18.setGeometry(QRect(800, 200, 191, 41))
        self.textEdit_19 = QTextEdit(self.frame)
        self.textEdit_19.setObjectName(u"textEdit_19")
        self.textEdit_19.setGeometry(QRect(800, 240, 191, 41))
        self.textEdit_20 = QTextEdit(self.frame)
        self.textEdit_20.setObjectName(u"textEdit_20")
        self.textEdit_20.setGeometry(QRect(800, 280, 191, 41))
        self.textEdit_21 = QTextEdit(self.frame)
        self.textEdit_21.setObjectName(u"textEdit_21")
        self.textEdit_21.setGeometry(QRect(800, 320, 191, 41))
        self.textEdit_22 = QTextEdit(self.frame)
        self.textEdit_22.setObjectName(u"textEdit_22")
        self.textEdit_22.setGeometry(QRect(800, 360, 191, 41))
        self.textEdit_23 = QTextEdit(self.frame)
        self.textEdit_23.setObjectName(u"textEdit_23")
        self.textEdit_23.setGeometry(QRect(800, 400, 191, 41))
        self.textEdit_24 = QTextEdit(self.frame)
        self.textEdit_24.setObjectName(u"textEdit_24")
        self.textEdit_24.setGeometry(QRect(800, 440, 191, 41))
        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(810, 530, 191, 41))
        self.label_25.setFont(font1)
        self.label_25.setStyleSheet(u"background-color: rgb(144, 139, 70);\n"
"border: 1px solid black;\n"
"")
        CompInfo.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CompInfo)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1011, 33))
        CompInfo.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(CompInfo)
        self.statusbar.setObjectName(u"statusbar")
        CompInfo.setStatusBar(self.statusbar)

        self.retranslateUi(CompInfo)

        QMetaObject.connectSlotsByName(CompInfo)
    # setupUi

    def retranslateUi(self, CompInfo):
        CompInfo.setWindowTitle(QCoreApplication.translate("CompInfo", u"CompSR", None))
        self.pushButton.setText(QCoreApplication.translate("CompInfo", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.pushButton_2.setText(QCoreApplication.translate("CompInfo", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("CompInfo", u"\u041f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440", None))
        self.label_2.setText(QCoreApplication.translate("CompInfo", u"\u041c\u0430\u0442\u0435\u0440\u0438\u043d\u0441\u043a\u0430\u044f \u043f\u043b\u0430\u0442\u0430", None))
        self.label_3.setText(QCoreApplication.translate("CompInfo", u"\u041e\u0445\u043b\u0430\u0436\u0434\u0435\u043d\u0438\u0435", None))
        self.label_4.setText(QCoreApplication.translate("CompInfo", u"\u041e\u0417\u0423", None))
        self.label_5.setText(QCoreApplication.translate("CompInfo", u"SSD/HDD 1", None))
        self.label_6.setText(QCoreApplication.translate("CompInfo", u"SSD/HDD 2", None))
        self.label_7.setText(QCoreApplication.translate("CompInfo", u"SSD/HDD 3", None))
        self.label_8.setText(QCoreApplication.translate("CompInfo", u"SSD/HDD 4", None))
        self.label_9.setText(QCoreApplication.translate("CompInfo", u"SSD/HDD 5", None))
        self.label_10.setText(QCoreApplication.translate("CompInfo", u"\u0412\u0438\u0434\u0435\u043e\u043a\u0430\u0440\u0442\u0430", None))
        self.label_11.setText(QCoreApplication.translate("CompInfo", u"\u0411\u043b\u043e\u043a \u043f\u0438\u0442\u0430\u043d\u0438\u044f", None))
        self.label_12.setText(QCoreApplication.translate("CompInfo", u"\u041a\u043e\u0440\u043f\u0443\u0441", None))
        self.label_13.setText(QCoreApplication.translate("CompInfo", u"...", None))
        self.label_14.setText(QCoreApplication.translate("CompInfo", u"...", None))
        self.label_15.setText(QCoreApplication.translate("CompInfo", u"...", None))
        self.label_16.setText(QCoreApplication.translate("CompInfo", u"...", None))
        self.label_17.setText(QCoreApplication.translate("CompInfo", u"...", None))
        self.label_18.setText(QCoreApplication.translate("CompInfo", u"...", None))
        self.label_19.setText(QCoreApplication.translate("CompInfo", u"...", None))
        self.label_20.setText(QCoreApplication.translate("CompInfo", u"...", None))
        self.label_21.setText(QCoreApplication.translate("CompInfo", u"...", None))
        self.label_22.setText(QCoreApplication.translate("CompInfo", u"...", None))
        self.label_23.setText(QCoreApplication.translate("CompInfo", u"...", None))
        self.label_24.setText(QCoreApplication.translate("CompInfo", u"...", None))
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        self.pushButton_8.setText("")
        self.pushButton_9.setText("")
        self.pushButton_10.setText("")
        self.pushButton_11.setText("")
        self.pushButton_12.setText("")
        self.pushButton_13.setText("")
        self.pushButton_14.setText("")
        self.textEdit_13.setHtml(QCoreApplication.translate("CompInfo", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ff0000;\">0</span></p></body></html>", None))
        self.textEdit_14.setHtml(QCoreApplication.translate("CompInfo", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ff0000;\">0</span></p></body></html>", None))
        self.textEdit_15.setHtml(QCoreApplication.translate("CompInfo", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ff0000;\">0</span></p></body></html>", None))
        self.textEdit_16.setHtml(QCoreApplication.translate("CompInfo", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ff0000;\">0</span></p></body></html>", None))
        self.textEdit_17.setHtml(QCoreApplication.translate("CompInfo", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ff0000;\">0</span></p></body></html>", None))
        self.textEdit_18.setHtml(QCoreApplication.translate("CompInfo", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ff0000;\">0</span></p></body></html>", None))
        self.textEdit_19.setHtml(QCoreApplication.translate("CompInfo", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ff0000;\">0</span></p></body></html>", None))
        self.textEdit_20.setHtml(QCoreApplication.translate("CompInfo", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ff0000;\">0</span></p></body></html>", None))
        self.textEdit_21.setHtml(QCoreApplication.translate("CompInfo", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ff0000;\">0</span></p></body></html>", None))
        self.textEdit_22.setHtml(QCoreApplication.translate("CompInfo", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ff0000;\">0</span></p></body></html>", None))
        self.textEdit_23.setHtml(QCoreApplication.translate("CompInfo", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ff0000;\">0</span></p></body></html>", None))
        self.textEdit_24.setHtml(QCoreApplication.translate("CompInfo", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ff0000;\">0</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("CompInfo", u"...", None))
    # retranslateUi

