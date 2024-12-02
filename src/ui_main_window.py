# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1080, 645)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.btn_collect_face = QPushButton(self.page_home)
        self.btn_collect_face.setObjectName(u"btn_collect_face")
        self.btn_collect_face.setGeometry(QRect(290, 160, 93, 28))
        self.btn_face_detect = QPushButton(self.page_home)
        self.btn_face_detect.setObjectName(u"btn_face_detect")
        self.btn_face_detect.setGeometry(QRect(290, 210, 93, 28))
        self.stackedWidget.addWidget(self.page_home)
        self.page_face_detect = QWidget()
        self.page_face_detect.setObjectName(u"page_face_detect")
        self.label_2 = QLabel(self.page_face_detect)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(320, 200, 69, 19))
        self.stackedWidget.addWidget(self.page_face_detect)
        self.page_info_display = QWidget()
        self.page_info_display.setObjectName(u"page_info_display")
        self.label_3 = QLabel(self.page_info_display)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(300, 230, 69, 19))
        self.stackedWidget.addWidget(self.page_info_display)
        self.page_face_collect = QWidget()
        self.page_face_collect.setObjectName(u"page_face_collect")
        self.label_disp_video = QLabel(self.page_face_collect)
        self.label_disp_video.setObjectName(u"label_disp_video")
        self.label_disp_video.setGeometry(QRect(10, 10, 691, 461))
        self.label_disp_video.setStyleSheet(u"border: 5px solid red;")
        self.label_disp_video.setWordWrap(False)
        self.btn_start = QPushButton(self.page_face_collect)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setGeometry(QRect(10, 530, 93, 28))
        self.btn_end = QPushButton(self.page_face_collect)
        self.btn_end.setObjectName(u"btn_end")
        self.btn_end.setGeometry(QRect(130, 530, 93, 28))
        self.label_face = QLabel(self.page_face_collect)
        self.label_face.setObjectName(u"label_face")
        self.label_face.setGeometry(QRect(820, 30, 128, 128))
        self.label_face.setStyleSheet(u"border: 5px solid red;")
        self.btn_confirm = QPushButton(self.page_face_collect)
        self.btn_confirm.setObjectName(u"btn_confirm")
        self.btn_confirm.setGeometry(QRect(800, 170, 93, 28))
        self.btn_pass = QPushButton(self.page_face_collect)
        self.btn_pass.setObjectName(u"btn_pass")
        self.btn_pass.setGeometry(QRect(920, 170, 93, 28))
        self.stackedWidget.addWidget(self.page_face_collect)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1080, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_collect_face.setText(QCoreApplication.translate("MainWindow", u"\u5f55\u5165\u4eba\u8138", None))
        self.btn_face_detect.setText(QCoreApplication.translate("MainWindow", u"\u7b7e\u5230", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"face detection", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"dispaly", None))
        self.label_disp_video.setText("")
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5f55\u5165", None))
        self.btn_end.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u5f55\u5165", None))
        self.label_face.setText("")
        self.btn_confirm.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4\u5f55\u5165", None))
        self.btn_pass.setText(QCoreApplication.translate("MainWindow", u"\u653e\u5f03", None))
    # retranslateUi

