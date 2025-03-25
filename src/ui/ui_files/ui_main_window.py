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
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStackedWidget, QStatusBar, QTableView, QTreeWidget,
    QTreeWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1174, 637)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
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
        self.class_teacher_table_view = QTableView(self.page_home)
        self.class_teacher_table_view.setObjectName(u"class_teacher_table_view")
        self.class_teacher_table_view.setGeometry(QRect(20, 10, 951, 501))
        self.stackedWidget.addWidget(self.page_home)
        self.page_face_detect = QWidget()
        self.page_face_detect.setObjectName(u"page_face_detect")
        self.label_disp_video_2 = QLabel(self.page_face_detect)
        self.label_disp_video_2.setObjectName(u"label_disp_video_2")
        self.label_disp_video_2.setGeometry(QRect(10, 29, 381, 441))
        self.label_disp_video_2.setStyleSheet(u"border: 5px solid red;")
        self.label_disp_video_2.setWordWrap(False)
        self.btn_confirm_face_detect = QPushButton(self.page_face_detect)
        self.btn_confirm_face_detect.setObjectName(u"btn_confirm_face_detect")
        self.btn_confirm_face_detect.setGeometry(QRect(100, 500, 93, 28))
        self.table_view_show_absent = QTableView(self.page_face_detect)
        self.table_view_show_absent.setObjectName(u"table_view_show_absent")
        self.table_view_show_absent.setGeometry(QRect(430, 20, 231, 171))
        self.btn_end_face_detect = QPushButton(self.page_face_detect)
        self.btn_end_face_detect.setObjectName(u"btn_end_face_detect")
        self.btn_end_face_detect.setGeometry(QRect(270, 500, 75, 23))
        self.stackedWidget.addWidget(self.page_face_detect)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.horizontalLayout.setStretch(0, 1)
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

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtreewidgetitem = self.tree_widget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u529f\u80fd\u9009\u9879", None));

        __sortingEnabled = self.tree_widget.isSortingEnabled()
        self.tree_widget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.tree_widget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"\u5207\u6362\u767b\u9646", None));
        ___qtreewidgetitem2 = self.tree_widget.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"\u73ed\u7ea7\u4fe1\u606f", None));
        ___qtreewidgetitem3 = self.tree_widget.topLevelItem(2)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u7b7e\u5230", None));
        self.tree_widget.setSortingEnabled(__sortingEnabled)

        self.label_disp_video_2.setText("")
        self.btn_confirm_face_detect.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.btn_end_face_detect.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
    # retranslateUi

