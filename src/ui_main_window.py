# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListView, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStackedWidget, QStatusBar,
    QTableView, QVBoxLayout, QWidget)

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
        self.btn_collect_face.setGeometry(QRect(430, 110, 93, 28))
        self.btn_face_detect = QPushButton(self.page_home)
        self.btn_face_detect.setObjectName(u"btn_face_detect")
        self.btn_face_detect.setGeometry(QRect(430, 180, 93, 28))
        self.listview_table_select = QListView(self.page_home)
        self.listview_table_select.setObjectName(u"listview_table_select")
        self.listview_table_select.setGeometry(QRect(340, 250, 256, 192))
        self.label_6 = QLabel(self.page_home)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(350, 230, 111, 19))
        self.layoutWidget = QWidget(self.page_home)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(330, 450, 295, 30))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_confirm_table = QPushButton(self.layoutWidget)
        self.btn_confirm_table.setObjectName(u"btn_confirm_table")

        self.horizontalLayout.addWidget(self.btn_confirm_table)

        self.btn_create_table = QPushButton(self.layoutWidget)
        self.btn_create_table.setObjectName(u"btn_create_table")

        self.horizontalLayout.addWidget(self.btn_create_table)

        self.btn_drop_table = QPushButton(self.layoutWidget)
        self.btn_drop_table.setObjectName(u"btn_drop_table")

        self.horizontalLayout.addWidget(self.btn_drop_table)

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
        self.label_disp_video.setGeometry(QRect(10, 10, 700, 460))
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
        self.label_face.setGeometry(QRect(820, 30, 150, 150))
        self.label_face.setStyleSheet(u"border: 5px solid red;")
        self.btn_confirm = QPushButton(self.page_face_collect)
        self.btn_confirm.setObjectName(u"btn_confirm")
        self.btn_confirm.setGeometry(QRect(790, 340, 93, 28))
        self.btn_pass = QPushButton(self.page_face_collect)
        self.btn_pass.setObjectName(u"btn_pass")
        self.btn_pass.setGeometry(QRect(930, 340, 93, 28))
        self.label = QLabel(self.page_face_collect)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(780, 190, 69, 19))
        self.line_edit_name = QLineEdit(self.page_face_collect)
        self.line_edit_name.setObjectName(u"line_edit_name")
        self.line_edit_name.setGeometry(QRect(850, 190, 113, 25))
        self.label_4 = QLabel(self.page_face_collect)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(790, 230, 69, 19))
        self.line_edit_gender = QLineEdit(self.page_face_collect)
        self.line_edit_gender.setObjectName(u"line_edit_gender")
        self.line_edit_gender.setGeometry(QRect(860, 230, 113, 25))
        self.label_5 = QLabel(self.page_face_collect)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(800, 270, 69, 19))
        self.line_edit_age = QLineEdit(self.page_face_collect)
        self.line_edit_age.setObjectName(u"line_edit_age")
        self.line_edit_age.setGeometry(QRect(870, 270, 113, 25))
        self.table_view_show_stu = QTableView(self.page_face_collect)
        self.table_view_show_stu.setObjectName(u"table_view_show_stu")
        self.table_view_show_stu.setGeometry(QRect(780, 390, 271, 171))
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
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6570\u636e\u5e93", None))
        self.btn_confirm_table.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9", None))
        self.btn_create_table.setText(QCoreApplication.translate("MainWindow", u"\u521b\u5efa", None))
        self.btn_drop_table.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"face detection", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"dispaly", None))
        self.label_disp_video.setText("")
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5f55\u5165", None))
        self.btn_end.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u5f55\u5165", None))
        self.label_face.setText("")
        self.btn_confirm.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4\u5f55\u5165", None))
        self.btn_pass.setText(QCoreApplication.translate("MainWindow", u"\u653e\u5f03", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u6027\u522b", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u5e74\u9f84", None))
    # retranslateUi

