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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTableView, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)
from src.ui.ui_files import resources_rc

class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        if not AdminWindow.objectName():
            AdminWindow.setObjectName(u"AdminWindow")
        AdminWindow.resize(1213, 633)
        AdminWindow.setStyleSheet(u"/* \u6574\u4f53\u80cc\u666f\u4e0e\u5b57\u4f53\u8bbe\u7f6e */\n"
"QWidget {\n"
"    /* \u80cc\u666f\u8272\uff0c\u53ef\u4ee5\u6839\u636e\u9700\u8981\u8c03\u6574 */\n"
"    background-color: #F5F5F5;\n"
"    \n"
"    /* \u5b57\u4f53\u8bbe\u7f6e\uff0c\u53ef\u6362\u6210\u4f60\u9700\u8981\u7684\u5b57\u4f53\u548c\u5927\u5c0f */\n"
"    font-family: \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QPushButton[class=\"custom-btn\"] {\n"
"        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"            stop:0 #ffffff, stop:1 #f0f0f0);\n"
"        border: 1px solid #ddd;\n"
"        border-radius: 4px;\n"
"        padding: 5px;\n"
"        min-width: 80px;\n"
"        transition: all 0.2s;\n"
"    }\n"
"\n"
"    /* \u60ac\u505c\u72b6\u6001 */\n"
"    QPushButton[class=\"custom-btn\"]:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"            stop:0 #f8f8f8, stop:1 #e0e0e0);\n"
"        border-color: #ccc;\n"
"    }\n"
"\n"
"    /* \u6309\u4e0b\u72b6\u6001 */\n"
""
                        "    QPushButton[class=\"custom-btn\"]:pressed {\n"
"        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"            stop:0 #e0e0e0, stop:1 #d0d0d0);\n"
"    }\n"
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
"/* \u6587\u672c\u8f93\u5165\u6846 */\n"
"QLineEdit {\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 4px;\n"
"    padding: 2px 4px;\n"
"    background-color: #ffffff;\n"
"    color: #333333;\n"
"}\n"
"\n"
"/* \u6587\u672c\u8f93\u5165\u6846\u83b7"
                        "\u5f97\u7126\u70b9\u65f6\u8fb9\u6846\u9ad8\u4eae */\n"
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
"    font-size: 12px;\n"
"}\n"
"\n"
"    /* \u9488\u5bf9\u6240\u6709\u5e26 custom-btn \u5c5e\u6027\u7684 QPushButton */\n"
"    QPushButton[class=\"custom-btn\"] {\n"
"        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"  "
                        "          stop:0 #ffffff, stop:1 #f0f0f0);\n"
"        border: 1px solid #ddd;\n"
"        border-radius: 4px;\n"
"        padding: 5px;\n"
"        min-width: 80px;\n"
"        transition: all 0.2s;\n"
"    }\n"
"\n"
"    /* \u60ac\u505c\u72b6\u6001 */\n"
"    QPushButton[class=\"custom-btn\"]:hover {\n"
"        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"            stop:0 #f8f8f8, stop:1 #e0e0e0);\n"
"        border-color: #ccc;\n"
"    }\n"
"\n"
"    /* \u6309\u4e0b\u72b6\u6001 */\n"
"    QPushButton[class=\"custom-btn\"]:pressed {\n"
"        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"            stop:0 #e0e0e0, stop:1 #d0d0d0);\n"
"    }")
        self.centralwidget = QWidget(AdminWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_9 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.tree_widget = QTreeWidget(self.centralwidget)
        QTreeWidgetItem(self.tree_widget)
        QTreeWidgetItem(self.tree_widget)
        QTreeWidgetItem(self.tree_widget)
        QTreeWidgetItem(self.tree_widget)
        QTreeWidgetItem(self.tree_widget)
        self.tree_widget.setObjectName(u"tree_widget")
        self.tree_widget.setStyleSheet(u"QTreeWidget::item:selected {\n"
"background-color:#2E3B4E;\n"
"color: white;\n"
"}")

        self.horizontalLayout_9.addWidget(self.tree_widget)

        self.stacked_widget = QStackedWidget(self.centralwidget)
        self.stacked_widget.setObjectName(u"stacked_widget")
        self.page_teacher = QWidget()
        self.page_teacher.setObjectName(u"page_teacher")
        self.verticalLayout = QVBoxLayout(self.page_teacher)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.page_teacher)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.table_view_teachers = QTableView(self.page_teacher)
        self.table_view_teachers.setObjectName(u"table_view_teachers")

        self.verticalLayout.addWidget(self.table_view_teachers)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_add_teacher = QPushButton(self.page_teacher)
        self.btn_add_teacher.setObjectName(u"btn_add_teacher")

        self.horizontalLayout_2.addWidget(self.btn_add_teacher)

        self.btn_delete_teacher = QPushButton(self.page_teacher)
        self.btn_delete_teacher.setObjectName(u"btn_delete_teacher")

        self.horizontalLayout_2.addWidget(self.btn_delete_teacher)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.stacked_widget.addWidget(self.page_teacher)
        self.page_course = QWidget()
        self.page_course.setObjectName(u"page_course")
        self.verticalLayout_2 = QVBoxLayout(self.page_course)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.page_course)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.table_view_course = QTableView(self.page_course)
        self.table_view_course.setObjectName(u"table_view_course")

        self.verticalLayout_2.addWidget(self.table_view_course)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_add_course = QPushButton(self.page_course)
        self.btn_add_course.setObjectName(u"btn_add_course")

        self.horizontalLayout_3.addWidget(self.btn_add_course)

        self.btn_delete_course = QPushButton(self.page_course)
        self.btn_delete_course.setObjectName(u"btn_delete_course")

        self.horizontalLayout_3.addWidget(self.btn_delete_course)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.stacked_widget.addWidget(self.page_course)
        self.page_stu = QWidget()
        self.page_stu.setObjectName(u"page_stu")
        self.verticalLayout_3 = QVBoxLayout(self.page_stu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.page_stu)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.table_view_students = QTableView(self.page_stu)
        self.table_view_students.setObjectName(u"table_view_students")

        self.verticalLayout_3.addWidget(self.table_view_students)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_add_stu_without_face = QPushButton(self.page_stu)
        self.btn_add_stu_without_face.setObjectName(u"btn_add_stu_without_face")

        self.horizontalLayout_4.addWidget(self.btn_add_stu_without_face)

        self.btn_add_stu = QPushButton(self.page_stu)
        self.btn_add_stu.setObjectName(u"btn_add_stu")

        self.horizontalLayout_4.addWidget(self.btn_add_stu)

        self.btn_delete_stu = QPushButton(self.page_stu)
        self.btn_delete_stu.setObjectName(u"btn_delete_stu")

        self.horizontalLayout_4.addWidget(self.btn_delete_stu)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.stacked_widget.addWidget(self.page_stu)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.layoutWidget = QWidget(self.page)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(23, 0, 821, 511))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_6.addWidget(self.label_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.table_view_stu_course = QTableView(self.layoutWidget)
        self.table_view_stu_course.setObjectName(u"table_view_stu_course")

        self.horizontalLayout_5.addWidget(self.table_view_stu_course)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btn_del_course_for_stu = QPushButton(self.layoutWidget)
        self.btn_del_course_for_stu.setObjectName(u"btn_del_course_for_stu")
        icon = QIcon()
        icon.addFile(u":/icons/assets/icons/arrow_right.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_del_course_for_stu.setIcon(icon)

        self.verticalLayout_5.addWidget(self.btn_del_course_for_stu)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.btn_add_course_for_stu = QPushButton(self.layoutWidget)
        self.btn_add_course_for_stu.setObjectName(u"btn_add_course_for_stu")
        icon1 = QIcon()
        icon1.addFile(u":/icons/arrow_right", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_add_course_for_stu.setIcon(icon1)

        self.verticalLayout_5.addWidget(self.btn_add_course_for_stu)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.table_view_stu_course_availabel = QTableView(self.layoutWidget)
        self.table_view_stu_course_availabel.setObjectName(u"table_view_stu_course_availabel")

        self.horizontalLayout_5.addWidget(self.table_view_stu_course_availabel)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.stacked_widget.addWidget(self.page)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.layoutWidget1 = QWidget(self.page_4)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(30, 12, 901, 551))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_camp_frame = QLabel(self.layoutWidget1)
        self.label_camp_frame.setObjectName(u"label_camp_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_camp_frame.sizePolicy().hasHeightForWidth())
        self.label_camp_frame.setSizePolicy(sizePolicy)
        self.label_camp_frame.setWordWrap(False)

        self.verticalLayout_4.addWidget(self.label_camp_frame)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_start_enter = QPushButton(self.layoutWidget1)
        self.btn_start_enter.setObjectName(u"btn_start_enter")

        self.horizontalLayout_6.addWidget(self.btn_start_enter)

        self.combo_box_video_source = QComboBox(self.layoutWidget1)
        self.combo_box_video_source.setObjectName(u"combo_box_video_source")

        self.horizontalLayout_6.addWidget(self.combo_box_video_source)

        self.btn_end_enter = QPushButton(self.layoutWidget1)
        self.btn_end_enter.setObjectName(u"btn_end_enter")

        self.horizontalLayout_6.addWidget(self.btn_end_enter)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.verticalLayout_4.setStretch(0, 5)

        self.horizontalLayout_7.addLayout(self.verticalLayout_4)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_face = QLabel(self.layoutWidget1)
        self.label_face.setObjectName(u"label_face")
        self.label_face.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_face.sizePolicy().hasHeightForWidth())
        self.label_face.setSizePolicy(sizePolicy1)
        self.label_face.setMinimumSize(QSize(150, 150))
        self.label_face.setMaximumSize(QSize(150, 150))

        self.verticalLayout_7.addWidget(self.label_face)

        self.groupBox = QGroupBox(self.layoutWidget1)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(34)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.line_edit_name = QLineEdit(self.groupBox)
        self.line_edit_name.setObjectName(u"line_edit_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.line_edit_name)

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

        self.line_edit_age = QLineEdit(self.groupBox)
        self.line_edit_age.setObjectName(u"line_edit_age")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.line_edit_age)


        self.verticalLayout_7.addWidget(self.groupBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_confirm_collect = QPushButton(self.layoutWidget1)
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

        self.btn_pass_collect = QPushButton(self.layoutWidget1)
        self.btn_pass_collect.setObjectName(u"btn_pass_collect")
        self.btn_pass_collect.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.btn_pass_collect)


        self.verticalLayout_7.addLayout(self.horizontalLayout)


        self.horizontalLayout_7.addLayout(self.verticalLayout_7)

        self.horizontalLayout_7.setStretch(0, 3)
        self.stacked_widget.addWidget(self.page_4)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_11 = QHBoxLayout(self.page_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lable_display_cap_1 = QLabel(self.page_2)
        self.lable_display_cap_1.setObjectName(u"lable_display_cap_1")
        sizePolicy.setHeightForWidth(self.lable_display_cap_1.sizePolicy().hasHeightForWidth())
        self.lable_display_cap_1.setSizePolicy(sizePolicy)
        self.lable_display_cap_1.setStyleSheet(u"  border: 1px solid black;")

        self.verticalLayout_9.addWidget(self.lable_display_cap_1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btn_start_cap_face_1 = QPushButton(self.page_2)
        self.btn_start_cap_face_1.setObjectName(u"btn_start_cap_face_1")

        self.horizontalLayout_10.addWidget(self.btn_start_cap_face_1)

        self.combo_box_select_video_source = QComboBox(self.page_2)
        self.combo_box_select_video_source.setObjectName(u"combo_box_select_video_source")

        self.horizontalLayout_10.addWidget(self.combo_box_select_video_source)

        self.btn_end_cap_face_1 = QPushButton(self.page_2)
        self.btn_end_cap_face_1.setObjectName(u"btn_end_cap_face_1")

        self.horizontalLayout_10.addWidget(self.btn_end_cap_face_1)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.verticalLayout_9.setStretch(0, 1)

        self.horizontalLayout_11.addLayout(self.verticalLayout_9)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_display_cap_face_1 = QLabel(self.page_2)
        self.label_display_cap_face_1.setObjectName(u"label_display_cap_face_1")
        self.label_display_cap_face_1.setStyleSheet(u"  border: 1px solid black;")

        self.verticalLayout_8.addWidget(self.label_display_cap_face_1)

        self.groupBox_2 = QGroupBox(self.page_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout_2 = QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_10)

        self.label_id_1 = QLabel(self.groupBox_2)
        self.label_id_1.setObjectName(u"label_id_1")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.label_id_1)

        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_12)

        self.label_name_1 = QLabel(self.groupBox_2)
        self.label_name_1.setObjectName(u"label_name_1")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.label_name_1)

        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_14)

        self.label_gender_1 = QLabel(self.groupBox_2)
        self.label_gender_1.setObjectName(u"label_gender_1")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.label_gender_1)

        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_16)

        self.label_age_1 = QLabel(self.groupBox_2)
        self.label_age_1.setObjectName(u"label_age_1")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.label_age_1)


        self.verticalLayout_8.addWidget(self.groupBox_2)

        self.btn_confirm_this_face_1 = QPushButton(self.page_2)
        self.btn_confirm_this_face_1.setObjectName(u"btn_confirm_this_face_1")

        self.verticalLayout_8.addWidget(self.btn_confirm_this_face_1)

        self.btn_pass_this_face_1 = QPushButton(self.page_2)
        self.btn_pass_this_face_1.setObjectName(u"btn_pass_this_face_1")

        self.verticalLayout_8.addWidget(self.btn_pass_this_face_1)

        self.verticalLayout_8.setStretch(0, 2)
        self.verticalLayout_8.setStretch(1, 3)

        self.horizontalLayout_11.addLayout(self.verticalLayout_8)

        self.horizontalLayout_11.setStretch(0, 4)
        self.horizontalLayout_11.setStretch(1, 1)
        self.stacked_widget.addWidget(self.page_2)

        self.horizontalLayout_9.addWidget(self.stacked_widget)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 4)
        AdminWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AdminWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1213, 22))
        AdminWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AdminWindow)
        self.statusbar.setObjectName(u"statusbar")
        AdminWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AdminWindow)

        self.stacked_widget.setCurrentIndex(2)


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
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("AdminWindow", u"\u8bfe\u7a0b\u7ba1\u7406", None));
        ___qtreewidgetitem4 = self.tree_widget.topLevelItem(3)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("AdminWindow", u"\u5b66\u751f\u7ba1\u7406", None));
        ___qtreewidgetitem5 = self.tree_widget.topLevelItem(4)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("AdminWindow", u"\u8fd4\u56de", None));
        self.tree_widget.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("AdminWindow", u"\u8001\u5e08\u4fe1\u606f", None))
        self.btn_add_teacher.setText(QCoreApplication.translate("AdminWindow", u"\u65b0\u589e", None))
        self.btn_delete_teacher.setText(QCoreApplication.translate("AdminWindow", u"\u5220\u9664", None))
        self.label_3.setText(QCoreApplication.translate("AdminWindow", u"\u5168\u90e8\u8bfe\u7a0b\u4fe1\u606f", None))
        self.btn_add_course.setText(QCoreApplication.translate("AdminWindow", u"\u65b0\u589e", None))
        self.btn_delete_course.setText(QCoreApplication.translate("AdminWindow", u"\u5220\u9664", None))
        self.label_4.setText(QCoreApplication.translate("AdminWindow", u"\u5168\u90e8\u5b66\u751f\u4fe1\u606f", None))
        self.btn_add_stu_without_face.setText(QCoreApplication.translate("AdminWindow", u"\u5f55\u5165\u5b66\u751f\u4fe1\u606f", None))
        self.btn_add_stu.setText(QCoreApplication.translate("AdminWindow", u"\u6279\u91cf\u5f55\u5165\u4eba\u8138\u4fe1\u606f", None))
        self.btn_delete_stu.setText(QCoreApplication.translate("AdminWindow", u"\u5220\u9664", None))
        self.label_5.setText(QCoreApplication.translate("AdminWindow", u"\u5b66\u751f\u8bfe\u7a0b\u7ba1\u7406", None))
#if QT_CONFIG(tooltip)
        self.btn_del_course_for_stu.setToolTip(QCoreApplication.translate("AdminWindow", u"<html><head/><body><p>\u4ece\u5f53\u524d\u6240\u9009\u8bfe\u7a0b\u4e2d\u79fb\u9664</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_del_course_for_stu.setText("")
#if QT_CONFIG(tooltip)
        self.btn_add_course_for_stu.setToolTip(QCoreApplication.translate("AdminWindow", u"<html><head/><body><p>\u6dfb\u52a0\u6240\u9009\u8bfe\u7a0b</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_add_course_for_stu.setText("")
        self.label_camp_frame.setText(QCoreApplication.translate("AdminWindow", u"\u6444\u50cf\u5934\u6355\u83b7\u753b\u9762", None))
        self.btn_start_enter.setText(QCoreApplication.translate("AdminWindow", u"\u5f00\u59cb", None))
        self.btn_end_enter.setText(QCoreApplication.translate("AdminWindow", u"\u505c\u6b62", None))
        self.label_face.setText(QCoreApplication.translate("AdminWindow", u"\u6355\u83b7\u7684\u4eba\u8138", None))
        self.groupBox.setTitle(QCoreApplication.translate("AdminWindow", u"\u5b66\u751f\u4fe1\u606f ", None))
        self.label_2.setText(QCoreApplication.translate("AdminWindow", u"\u59d3\u540d", None))
        self.line_edit_name.setText("")
        self.label_6.setText(QCoreApplication.translate("AdminWindow", u"\u6027\u522b", None))
        self.rbtn_male.setText(QCoreApplication.translate("AdminWindow", u"\u7537", None))
        self.rbtn_female.setText(QCoreApplication.translate("AdminWindow", u"\u5973", None))
        self.label_7.setText(QCoreApplication.translate("AdminWindow", u"\u5e74\u9f84", None))
        self.btn_confirm_collect.setText(QCoreApplication.translate("AdminWindow", u"\u786e\u8ba4\u5f55\u5165", None))
        self.btn_pass_collect.setText(QCoreApplication.translate("AdminWindow", u"\u8df3\u8fc7", None))
        self.lable_display_cap_1.setText(QCoreApplication.translate("AdminWindow", u"\u663e\u793a\u6444\u50cf\u5934\u6355\u83b7\u7684\u56fe\u50cf", None))
        self.btn_start_cap_face_1.setText(QCoreApplication.translate("AdminWindow", u"\u5f00\u59cb\u6355\u83b7\u4eba\u8138", None))
        self.btn_end_cap_face_1.setText(QCoreApplication.translate("AdminWindow", u"\u505c\u6b62", None))
        self.label_display_cap_face_1.setText(QCoreApplication.translate("AdminWindow", u"TextLabel", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("AdminWindow", u"GroupBox", None))
        self.label_10.setText(QCoreApplication.translate("AdminWindow", u"ID", None))
        self.label_id_1.setText("")
        self.label_12.setText(QCoreApplication.translate("AdminWindow", u"\u59d3\u540d", None))
        self.label_name_1.setText("")
        self.label_14.setText(QCoreApplication.translate("AdminWindow", u"\u6027\u522b", None))
        self.label_gender_1.setText("")
        self.label_16.setText(QCoreApplication.translate("AdminWindow", u"\u5e74\u9f84", None))
        self.label_age_1.setText("")
        self.btn_confirm_this_face_1.setText(QCoreApplication.translate("AdminWindow", u"\u5f55\u5165", None))
        self.btn_pass_this_face_1.setText(QCoreApplication.translate("AdminWindow", u"\u653e\u5f03", None))
    # retranslateUi

