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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListView, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStackedWidget,
    QStatusBar, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1169, 669)
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
        self.btn_jump_to_face_detect = QPushButton(self.page_home)
        self.btn_jump_to_face_detect.setObjectName(u"btn_jump_to_face_detect")
        self.btn_jump_to_face_detect.setGeometry(QRect(430, 180, 93, 28))
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
        self.label_disp_video_2 = QLabel(self.page_face_detect)
        self.label_disp_video_2.setObjectName(u"label_disp_video_2")
        self.label_disp_video_2.setGeometry(QRect(20, 0, 700, 460))
        self.label_disp_video_2.setStyleSheet(u"border: 5px solid red;")
        self.label_disp_video_2.setWordWrap(False)
        self.btn_confirm_face_detect = QPushButton(self.page_face_detect)
        self.btn_confirm_face_detect.setObjectName(u"btn_confirm_face_detect")
        self.btn_confirm_face_detect.setGeometry(QRect(190, 510, 93, 28))
        self.table_view_show_absent = QTableView(self.page_face_detect)
        self.table_view_show_absent.setObjectName(u"table_view_show_absent")
        self.table_view_show_absent.setGeometry(QRect(790, 180, 256, 192))
        self.btn_end_face_detect = QPushButton(self.page_face_detect)
        self.btn_end_face_detect.setObjectName(u"btn_end_face_detect")
        self.btn_end_face_detect.setGeometry(QRect(400, 510, 75, 23))
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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_disp_video.sizePolicy().hasHeightForWidth())
        self.label_disp_video.setSizePolicy(sizePolicy)
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
        self.label_face.setGeometry(QRect(810, 30, 150, 150))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(150)
        sizePolicy1.setVerticalStretch(150)
        sizePolicy1.setHeightForWidth(self.label_face.sizePolicy().hasHeightForWidth())
        self.label_face.setSizePolicy(sizePolicy1)
        self.label_face.setStyleSheet(u"border: 5px solid red;")
        self.table_view_show_stu = QTableView(self.page_face_collect)
        self.table_view_show_stu.setObjectName(u"table_view_show_stu")
        self.table_view_show_stu.setGeometry(QRect(780, 390, 271, 171))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(150)
        sizePolicy2.setVerticalStretch(150)
        sizePolicy2.setHeightForWidth(self.table_view_show_stu.sizePolicy().hasHeightForWidth())
        self.table_view_show_stu.setSizePolicy(sizePolicy2)
        self.layoutWidget1 = QWidget(self.page_face_collect)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(780, 190, 213, 91))
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(150)
        sizePolicy3.setVerticalStretch(150)
        sizePolicy3.setHeightForWidth(self.layoutWidget1.sizePolicy().hasHeightForWidth())
        self.layoutWidget1.setSizePolicy(sizePolicy3)
        self.gridLayout = QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.line_edit_name = QLineEdit(self.layoutWidget1)
        self.line_edit_name.setObjectName(u"line_edit_name")

        self.gridLayout.addWidget(self.line_edit_name, 0, 1, 1, 2)

        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.line_edit_gender = QLineEdit(self.layoutWidget1)
        self.line_edit_gender.setObjectName(u"line_edit_gender")

        self.gridLayout.addWidget(self.line_edit_gender, 1, 1, 1, 2)

        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 2)

        self.line_edit_age = QLineEdit(self.layoutWidget1)
        self.line_edit_age.setObjectName(u"line_edit_age")

        self.gridLayout.addWidget(self.line_edit_age, 2, 2, 1, 1)

        self.layoutWidget2 = QWidget(self.page_face_collect)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(790, 340, 195, 30))
        sizePolicy3.setHeightForWidth(self.layoutWidget2.sizePolicy().hasHeightForWidth())
        self.layoutWidget2.setSizePolicy(sizePolicy3)
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_confirm = QPushButton(self.layoutWidget2)
        self.btn_confirm.setObjectName(u"btn_confirm")

        self.horizontalLayout_2.addWidget(self.btn_confirm)

        self.btn_pass = QPushButton(self.layoutWidget2)
        self.btn_pass.setObjectName(u"btn_pass")

        self.horizontalLayout_2.addWidget(self.btn_pass)

        self.stackedWidget.addWidget(self.page_face_collect)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1169, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_collect_face.setText(QCoreApplication.translate("MainWindow", u"\u5f55\u5165\u4eba\u8138", None))
        self.btn_jump_to_face_detect.setText(QCoreApplication.translate("MainWindow", u"\u7b7e\u5230", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6570\u636e\u5e93", None))
        self.btn_confirm_table.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9", None))
        self.btn_create_table.setText(QCoreApplication.translate("MainWindow", u"\u521b\u5efa", None))
        self.btn_drop_table.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.label_disp_video_2.setText("")
        self.btn_confirm_face_detect.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.btn_end_face_detect.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"dispaly", None))
        self.label_disp_video.setText("")
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5f55\u5165", None))
        self.btn_end.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u5f55\u5165", None))
        self.label_face.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u6027\u522b", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u5e74\u9f84", None))
        self.btn_confirm.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4\u5f55\u5165", None))
        self.btn_pass.setText(QCoreApplication.translate("MainWindow", u"\u653e\u5f03", None))
    # retranslateUi

