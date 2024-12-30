# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QStackedWidget, QStatusBar, QTableView, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        if not AdminWindow.objectName():
            AdminWindow.setObjectName(u"AdminWindow")
        AdminWindow.resize(1187, 577)
        self.centralwidget = QWidget(AdminWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_9 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.tree_widget = QTreeWidget(self.centralwidget)
        QTreeWidgetItem(self.tree_widget)
        QTreeWidgetItem(self.tree_widget)
        QTreeWidgetItem(self.tree_widget)
        QTreeWidgetItem(self.tree_widget)
        self.tree_widget.setObjectName(u"tree_widget")

        self.horizontalLayout_9.addWidget(self.tree_widget)

        self.stacked_widget = QStackedWidget(self.centralwidget)
        self.stacked_widget.setObjectName(u"stacked_widget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout = QVBoxLayout(self.page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.table_view_teachers = QTableView(self.page)
        self.table_view_teachers.setObjectName(u"table_view_teachers")

        self.verticalLayout.addWidget(self.table_view_teachers)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_add_teacher = QPushButton(self.page)
        self.btn_add_teacher.setObjectName(u"btn_add_teacher")

        self.horizontalLayout_2.addWidget(self.btn_add_teacher)

        self.btn_delete_teacher = QPushButton(self.page)
        self.btn_delete_teacher.setObjectName(u"btn_delete_teacher")

        self.horizontalLayout_2.addWidget(self.btn_delete_teacher)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.stacked_widget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.table_view_classes = QTableView(self.page_2)
        self.table_view_classes.setObjectName(u"table_view_classes")

        self.verticalLayout_2.addWidget(self.table_view_classes)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_add_class = QPushButton(self.page_2)
        self.btn_add_class.setObjectName(u"btn_add_class")

        self.horizontalLayout_3.addWidget(self.btn_add_class)

        self.btn_delete_class = QPushButton(self.page_2)
        self.btn_delete_class.setObjectName(u"btn_delete_class")

        self.horizontalLayout_3.addWidget(self.btn_delete_class)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.stacked_widget.addWidget(self.page_2)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.horizontalLayout_7 = QHBoxLayout(self.page_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_camp_frame = QLabel(self.page_4)
        self.label_camp_frame.setObjectName(u"label_camp_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_camp_frame.sizePolicy().hasHeightForWidth())
        self.label_camp_frame.setSizePolicy(sizePolicy)
        self.label_camp_frame.setMinimumSize(QSize(600, 460))
        self.label_camp_frame.setStyleSheet(u"QLabel#label_camera { /* \u7ed9\u663e\u793a\u6444\u50cf\u5934\u753b\u9762\u7684 QLabel \u8bbe\u7f6e\u6837\u5f0f */\n"
"    border: 2px solid #3498db; /* \u84dd\u8272\u8fb9\u6846 */\n"
"    border-radius: 10px;       /* \u5706\u89d2\u8fb9\u6846 */\n"
"    background-color: #f0f0f0; /* \u6d45\u7070\u8272\u80cc\u666f */\n"
"    color: #888888;           /* \u9ed8\u8ba4\u6587\u5b57\u989c\u8272 */\n"
"    font: bold 14px;          /* \u9ed8\u8ba4\u6587\u5b57\u5b57\u4f53 */\n"
"    text-align: center;       /* \u6587\u5b57\u5c45\u4e2d */\n"
"}\n"
"")
        self.label_camp_frame.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_camp_frame.setWordWrap(False)

        self.horizontalLayout_7.addWidget(self.label_camp_frame)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_face = QLabel(self.page_4)
        self.label_face.setObjectName(u"label_face")
        self.label_face.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label_face.sizePolicy().hasHeightForWidth())
        self.label_face.setSizePolicy(sizePolicy)
        self.label_face.setMinimumSize(QSize(150, 150))
        self.label_face.setMaximumSize(QSize(150, 150))
        self.label_face.setStyleSheet(u"QLabel#label_face { /* \u7ed9\u663e\u793a\u6355\u83b7\u4eba\u8138\u753b\u9762\u7684 QLabel \u8bbe\u7f6e\u6837\u5f0f */\n"
"    border: 2px dashed #e74c3c; /* \u7ea2\u8272\u865a\u7ebf\u8fb9\u6846 */\n"
"    border-radius: 10px;        /* \u5706\u89d2\u8fb9\u6846 */\n"
"    background-color: #ffffff;  /* \u767d\u8272\u80cc\u666f */\n"
"    color: #cccccc;            /* \u9ed8\u8ba4\u6587\u5b57\u989c\u8272 */\n"
"    font: italic bold 12px;    /* \u9ed8\u8ba4\u6587\u5b57\u5b57\u4f53 */\n"
"    text-align: center;        /* \u6587\u5b57\u5c45\u4e2d */\n"
"}\n"
"")
        self.label_face.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_face)

        self.groupBox = QGroupBox(self.page_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid #8f8f91; /* \u8fb9\u6846\u989c\u8272 */\n"
"    border-radius: 10px;       /* \u5706\u89d2\u534a\u5f84 */\n"
"    margin-top: 10px;          /* \u6807\u9898\u6587\u5b57\u4e0e\u8fb9\u6846\u7684\u95f4\u8ddd */\n"
"    padding: 5px;              /* \u5185\u5bb9\u4e0e\u8fb9\u6846\u7684\u95f4\u8ddd */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin; /* \u6807\u9898\u4f4d\u7f6e\u76f8\u5bf9\u4e8e margin */\n"
"    subcontrol-position: top center; /* \u6807\u9898\u4f4d\u7f6e\uff1a\u9876\u90e8\u5c45\u4e2d */\n"
"    padding: 0 5px;            /* \u6807\u9898\u4e0e\u8fb9\u6846\u7684\u95f4\u8ddd */\n"
"    background-color: #f7f7f7; /* \u80cc\u666f\u989c\u8272 */\n"
"    color: #333333;            /* \u6587\u5b57\u989c\u8272 */\n"
"    border-radius: 5px;        /* \u6807\u9898\u7684\u5706\u89d2\u534a\u5f84 */\n"
"    font: bold 12px;           /* \u6807\u9898\u5b57\u4f53 */\n"
"}\n"
"")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(34)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.line_edit_name_2 = QLineEdit(self.groupBox)
        self.line_edit_name_2.setObjectName(u"line_edit_name_2")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.line_edit_name_2)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.rbtn_male = QRadioButton(self.groupBox)
        self.rbtn_male.setObjectName(u"rbtn_male")

        self.horizontalLayout_8.addWidget(self.rbtn_male)

        self.rbtn_female = QRadioButton(self.groupBox)
        self.rbtn_female.setObjectName(u"rbtn_female")

        self.horizontalLayout_8.addWidget(self.rbtn_female)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_8)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.line_edit_age_2 = QLineEdit(self.groupBox)
        self.line_edit_age_2.setObjectName(u"line_edit_age_2")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.line_edit_age_2)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_confirm_collect = QPushButton(self.page_4)
        self.btn_confirm_collect.setObjectName(u"btn_confirm_collect")
        self.btn_confirm_collect.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db; /* \u6309\u94ae\u80cc\u666f\u989c\u8272\uff08\u84dd\u8272\uff09 */\n"
"    color: white;             /* \u6309\u94ae\u6587\u5b57\u989c\u8272\uff08\u767d\u8272\uff09 */\n"
"    border: 2px solid #2980b9; /* \u8fb9\u6846\u989c\u8272\uff08\u6df1\u84dd\uff09 */\n"
"    border-radius: 5px;       /* \u5706\u89d2\u534a\u5f84 */\n"
"    padding: 5px 10px;        /* \u5185\u8fb9\u8ddd */\n"
"    font: bold 12px;          /* \u5b57\u4f53\u52a0\u7c97 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9; /* \u9f20\u6807\u60ac\u505c\u65f6\u80cc\u666f\u989c\u8272 */\n"
"    border-color: #1c5c92;    /* \u9f20\u6807\u60ac\u505c\u65f6\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c5c92; /* \u6309\u4e0b\u65f6\u80cc\u666f\u989c\u8272 */\n"
"    border-color: #15486d;    /* \u6309\u4e0b\u65f6\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btn_confirm_collect)

        self.btn_pass_2 = QPushButton(self.page_4)
        self.btn_pass_2.setObjectName(u"btn_pass_2")
        self.btn_pass_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db; /* \u6309\u94ae\u80cc\u666f\u989c\u8272\uff08\u84dd\u8272\uff09 */\n"
"    color: white;             /* \u6309\u94ae\u6587\u5b57\u989c\u8272\uff08\u767d\u8272\uff09 */\n"
"    border: 2px solid #2980b9; /* \u8fb9\u6846\u989c\u8272\uff08\u6df1\u84dd\uff09 */\n"
"    border-radius: 5px;       /* \u5706\u89d2\u534a\u5f84 */\n"
"    padding: 5px 10px;        /* \u5185\u8fb9\u8ddd */\n"
"    font: bold 12px;          /* \u5b57\u4f53\u52a0\u7c97 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9; /* \u9f20\u6807\u60ac\u505c\u65f6\u80cc\u666f\u989c\u8272 */\n"
"    border-color: #1c5c92;    /* \u9f20\u6807\u60ac\u505c\u65f6\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c5c92; /* \u6309\u4e0b\u65f6\u80cc\u666f\u989c\u8272 */\n"
"    border-color: #15486d;    /* \u6309\u4e0b\u65f6\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btn_pass_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_start = QPushButton(self.page_4)
        self.btn_start.setObjectName(u"btn_start")

        self.horizontalLayout_6.addWidget(self.btn_start)

        self.btn_end = QPushButton(self.page_4)
        self.btn_end.setObjectName(u"btn_end")

        self.horizontalLayout_6.addWidget(self.btn_end)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 4)
        self.verticalLayout_4.setStretch(2, 1)
        self.verticalLayout_4.setStretch(3, 1)

        self.horizontalLayout_7.addLayout(self.verticalLayout_4)

        self.stacked_widget.addWidget(self.page_4)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_3 = QVBoxLayout(self.page_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.table_view_students = QTableView(self.page_3)
        self.table_view_students.setObjectName(u"table_view_students")

        self.verticalLayout_3.addWidget(self.table_view_students)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_add_stu = QPushButton(self.page_3)
        self.btn_add_stu.setObjectName(u"btn_add_stu")

        self.horizontalLayout_4.addWidget(self.btn_add_stu)

        self.btn_delete_stu = QPushButton(self.page_3)
        self.btn_delete_stu.setObjectName(u"btn_delete_stu")

        self.horizontalLayout_4.addWidget(self.btn_delete_stu)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.stacked_widget.addWidget(self.page_3)

        self.horizontalLayout_9.addWidget(self.stacked_widget)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 5)
        AdminWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AdminWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1187, 21))
        AdminWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AdminWindow)
        self.statusbar.setObjectName(u"statusbar")
        AdminWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AdminWindow)

        self.stacked_widget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(AdminWindow)
    # setupUi

    def retranslateUi(self, AdminWindow):
        AdminWindow.setWindowTitle(QCoreApplication.translate("AdminWindow", u"MainWindow", None))
        ___qtreewidgetitem = self.tree_widget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("AdminWindow", u"\u529f\u80fd\u9009\u9879", None));

        __sortingEnabled = self.tree_widget.isSortingEnabled()
        self.tree_widget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.tree_widget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("AdminWindow", u"\u9000\u51fa", None));
        ___qtreewidgetitem2 = self.tree_widget.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("AdminWindow", u"\u8001\u5e08\u7ba1\u7406", None));
        ___qtreewidgetitem3 = self.tree_widget.topLevelItem(2)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("AdminWindow", u"\u73ed\u7ea7\u7ba1\u7406", None));
        ___qtreewidgetitem4 = self.tree_widget.topLevelItem(3)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("AdminWindow", u"\u5b66\u751f\u7ba1\u7406", None));
        self.tree_widget.setSortingEnabled(__sortingEnabled)

        self.btn_add_teacher.setText(QCoreApplication.translate("AdminWindow", u"\u65b0\u589e", None))
        self.btn_delete_teacher.setText(QCoreApplication.translate("AdminWindow", u"\u5220\u9664", None))
        self.btn_add_class.setText(QCoreApplication.translate("AdminWindow", u"\u65b0\u589e", None))
        self.btn_delete_class.setText(QCoreApplication.translate("AdminWindow", u"\u5220\u9664", None))
        self.label_camp_frame.setText(QCoreApplication.translate("AdminWindow", u"\u6444\u50cf\u5934\u6355\u83b7\u753b\u9762", None))
        self.label_face.setText(QCoreApplication.translate("AdminWindow", u"\u6355\u83b7\u7684\u4eba\u8138", None))
        self.groupBox.setTitle(QCoreApplication.translate("AdminWindow", u"\u5b66\u751f\u4fe1\u606f ", None))
        self.label_2.setText(QCoreApplication.translate("AdminWindow", u"\u59d3\u540d", None))
        self.line_edit_name_2.setText("")
        self.label_6.setText(QCoreApplication.translate("AdminWindow", u"\u6027\u522b", None))
        self.rbtn_male.setText(QCoreApplication.translate("AdminWindow", u"\u7537", None))
        self.rbtn_female.setText(QCoreApplication.translate("AdminWindow", u"\u5973", None))
        self.label_7.setText(QCoreApplication.translate("AdminWindow", u"\u5e74\u9f84", None))
        self.btn_confirm_collect.setText(QCoreApplication.translate("AdminWindow", u"\u786e\u8ba4\u5f55\u5165", None))
        self.btn_pass_2.setText(QCoreApplication.translate("AdminWindow", u"\u653e\u5f03", None))
        self.btn_start.setText(QCoreApplication.translate("AdminWindow", u"\u5f00\u59cb\u5f55\u5165", None))
        self.btn_end.setText(QCoreApplication.translate("AdminWindow", u"\u505c\u6b62\u5f55\u5165", None))
        self.btn_add_stu.setText(QCoreApplication.translate("AdminWindow", u"\u5f55\u5165", None))
        self.btn_delete_stu.setText(QCoreApplication.translate("AdminWindow", u"\u5220\u9664", None))
    # retranslateUi

