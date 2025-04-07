# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(421, 233)
        Form.setStyleSheet(u"/* \u6574\u4f53\u80cc\u666f\u4e0e\u5b57\u4f53\u8bbe\u7f6e */\n"
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
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(25)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setContentsMargins(-1, 11, -1, -1)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.line_edit_uername = QLineEdit(self.groupBox)
        self.line_edit_uername.setObjectName(u"line_edit_uername")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.line_edit_uername)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.line_edit_pswd = QLineEdit(self.groupBox)
        self.line_edit_pswd.setObjectName(u"line_edit_pswd")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.line_edit_pswd)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.btn_login = QPushButton(self.groupBox)
        self.btn_login.setObjectName(u"btn_login")

        self.horizontalLayout.addWidget(self.btn_login)

        self.btn_register = QPushButton(self.groupBox)
        self.btn_register.setObjectName(u"btn_register")

        self.horizontalLayout.addWidget(self.btn_register)

        self.btn_admin = QPushButton(self.groupBox)
        self.btn_admin.setObjectName(u"btn_admin")

        self.horizontalLayout.addWidget(self.btn_admin)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u767b\u9646", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801", None))
        self.btn_login.setText(QCoreApplication.translate("Form", u"\u767b\u9646", None))
        self.btn_register.setText(QCoreApplication.translate("Form", u"\u6ce8\u518c", None))
        self.btn_admin.setText(QCoreApplication.translate("Form", u"\u7ba1\u7406\u5458", None))
    # retranslateUi

