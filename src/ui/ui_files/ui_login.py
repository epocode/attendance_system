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

