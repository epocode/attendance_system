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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QTableView,
    QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1174, 637)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"/* \u6574\u4f53\u80cc\u666f\u4e0e\u5b57\u4f53\u8bbe\u7f6e */\n"
"QWidget {\n"
"    /* \u80cc\u666f\u8272\uff0c\u53ef\u4ee5\u6839\u636e\u9700\u8981\u8c03\u6574 */\n"
"    background-color: #F5F5F5;\n"
"    \n"
"    /* \u5b57\u4f53\u8bbe\u7f6e\uff0c\u53ef\u6362\u6210\u4f60\u9700\u8981\u7684\u5b57\u4f53\u548c\u5927\u5c0f */\n"
"    font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"\n"
"/* \u6309\u94ae\u57fa\u7840\u6837\u5f0f */\n"
"QPushButton {\n"
"    background-color: #3498db; /* \u4e3b\u8272\u8c03 */\n"
"    color: #ffffff;           /* \u6587\u5b57\u989c\u8272 */\n"
"    border-radius: 5px;       /* \u5706\u89d2 */\n"
"    padding: 5px 10px;        /* \u5185\u8fb9\u8ddd */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"}\n"
"\n"
"/* \u6309\u94ae\u9f20\u6807\u60ac\u505c\u4e0e\u70b9\u51fb\u6548\u679c */\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1f6391;\n"
"}\n"
"\n"
"/* \u6587\u672c\u8f93"
                        "\u5165\u6846 */\n"
"QLineEdit {\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 4px;\n"
"    padding: 2px 4px;\n"
"    background-color: #ffffff;\n"
"    color: #333333;\n"
"}\n"
"\n"
"/* \u6587\u672c\u8f93\u5165\u6846\u83b7\u5f97\u7126\u70b9\u65f6\u8fb9\u6846\u9ad8\u4eae */\n"
"QLineEdit:focus {\n"
"    border: 2px solid #3498db;\n"
"}\n"
"\n"
"/* GroupBox \u5916\u89c2 */\n"
"QGroupBox {\n"
"    border: 1px solid gray; \n"
"    border-radius: 5px;     \n"
"    margin-top: 1em;        \n"
"    background-color: #ffffff;\n"
"    /* \u53ef\u4ee5\u6839\u636e\u9700\u8981\u589e\u52a0 padding\u3001margin \u7b49 */\n"
"}\n"
"\n"
"/* GroupBox \u6807\u9898\u7684\u4f4d\u7f6e\u548c\u6837\u5f0f */\n"
"QGroupBox:title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 5px;\n"
"    color: #333333;\n"
"    font-weight: bold; /* \u6807\u9898\u52a0\u7c97 */\n"
"}\n"
"\n"
"/* Label \u57fa\u672c\u6837\u5f0f\uff08\u53ef\u9009\uff09 */\n"
"QLabel {\n"
"    color: #333333;\n"
""
                        "    font-size: 12px;\n"
"}\n"
"QLabel#label_display_cap {\n"
"border: 2px solid black; \n"
"}\n"
"\n"
"\n"
"/* \u5176\u5b83\u4f60\u9700\u8981\u7684\u63a7\u4ef6\u6837\u5f0f\u90fd\u53ef\u4ee5\u5728\u8fd9\u91cc\u7ee7\u7eed\u6dfb\u52a0 */\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tree_widget = QTreeWidget(self.centralwidget)
        QTreeWidgetItem(self.tree_widget)
        QTreeWidgetItem(self.tree_widget)
        QTreeWidgetItem(self.tree_widget)
        self.tree_widget.setObjectName(u"tree_widget")

        self.horizontalLayout.addWidget(self.tree_widget)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.table_view_course_teacher = QTableView(self.page_home)
        self.table_view_course_teacher.setObjectName(u"table_view_course_teacher")
        self.table_view_course_teacher.setGeometry(QRect(20, 10, 951, 501))
        self.stackedWidget.addWidget(self.page_home)
        self.page_course_detail = QWidget()
        self.page_course_detail.setObjectName(u"page_course_detail")
        self.table_view_course_detail = QTableView(self.page_course_detail)
        self.table_view_course_detail.setObjectName(u"table_view_course_detail")
        self.table_view_course_detail.setGeometry(QRect(30, 10, 801, 501))
        self.btn_enter_attendance = QPushButton(self.page_course_detail)
        self.btn_enter_attendance.setObjectName(u"btn_enter_attendance")
        self.btn_enter_attendance.setGeometry(QRect(190, 530, 93, 28))
        self.stackedWidget.addWidget(self.page_course_detail)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.table_view_attendance_detail = QTableView(self.page)
        self.table_view_attendance_detail.setObjectName(u"table_view_attendance_detail")
        self.table_view_attendance_detail.setGeometry(QRect(20, 20, 791, 461))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.table_view_stu_attendance_detail = QTableView(self.page_2)
        self.table_view_stu_attendance_detail.setObjectName(u"table_view_stu_attendance_detail")
        self.table_view_stu_attendance_detail.setGeometry(QRect(40, 30, 681, 471))
        self.stackedWidget.addWidget(self.page_2)
        self.page_face_detect = QWidget()
        self.page_face_detect.setObjectName(u"page_face_detect")
        self.btn_start_detect_face = QPushButton(self.page_face_detect)
        self.btn_start_detect_face.setObjectName(u"btn_start_detect_face")
        self.btn_start_detect_face.setGeometry(QRect(100, 500, 93, 28))
        self.table_view_show_absent = QTableView(self.page_face_detect)
        self.table_view_show_absent.setObjectName(u"table_view_show_absent")
        self.table_view_show_absent.setGeometry(QRect(570, 50, 231, 171))
        self.btn_end_detect_face = QPushButton(self.page_face_detect)
        self.btn_end_detect_face.setObjectName(u"btn_end_detect_face")
        self.btn_end_detect_face.setGeometry(QRect(340, 500, 75, 23))
        self.label_display_cap = QLabel(self.page_face_detect)
        self.label_display_cap.setObjectName(u"label_display_cap")
        self.label_display_cap.setGeometry(QRect(30, 20, 491, 421))
        self.combo_box_video_source = QComboBox(self.page_face_detect)
        self.combo_box_video_source.setObjectName(u"combo_box_video_source")
        self.combo_box_video_source.setGeometry(QRect(230, 500, 83, 25))
        self.stackedWidget.addWidget(self.page_face_detect)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.horizontalLayout.setStretch(1, 6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1174, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtreewidgetitem = self.tree_widget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u529f\u80fd\u9009\u9879", None));

        __sortingEnabled = self.tree_widget.isSortingEnabled()
        self.tree_widget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.tree_widget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u767b\u5f55", None));
        ___qtreewidgetitem2 = self.tree_widget.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"\u73ed\u7ea7\u4fe1\u606f", None));
        ___qtreewidgetitem3 = self.tree_widget.topLevelItem(2)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"\u8fd4\u56de\u4e0a\u4e00\u7ea7", None));
        self.tree_widget.setSortingEnabled(__sortingEnabled)

        self.btn_enter_attendance.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8003\u52e4", None))
        self.btn_start_detect_face.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.btn_end_detect_face.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.label_display_cap.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

