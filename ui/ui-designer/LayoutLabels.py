# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout-labels.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDoubleSpinBox,
    QFormLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_LayoutLabel(object):
    def setupUi(self, LayoutLabel):
        if not LayoutLabel.objectName():
            LayoutLabel.setObjectName(u"LayoutLabel")
        LayoutLabel.resize(491, 575)
        self.verticalLayout = QVBoxLayout(LayoutLabel)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(LayoutLabel)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit = QLineEdit(LayoutLabel)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_2 = QLabel(LayoutLabel)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.dateEdit = QDateEdit(LayoutLabel)
        self.dateEdit.setObjectName(u"dateEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.dateEdit)

        self.label_3 = QLabel(LayoutLabel)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.comboBox = QComboBox(LayoutLabel)
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBox)

        self.label_4 = QLabel(LayoutLabel)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.comboBox_2 = QComboBox(LayoutLabel)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.comboBox_2)

        self.label_5 = QLabel(LayoutLabel)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.doubleSpinBox = QDoubleSpinBox(LayoutLabel)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.doubleSpinBox)

        self.label_6 = QLabel(LayoutLabel)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.textEdit = QTextEdit(LayoutLabel)
        self.textEdit.setObjectName(u"textEdit")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.textEdit)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(148, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(LayoutLabel)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(LayoutLabel)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(LayoutLabel)

        QMetaObject.connectSlotsByName(LayoutLabel)
    # setupUi

    def retranslateUi(self, LayoutLabel):
        LayoutLabel.setWindowTitle(QCoreApplication.translate("LayoutLabel", u"Form", None))
        self.label.setText(QCoreApplication.translate("LayoutLabel", u"Employee Name:", None))
        self.label_2.setText(QCoreApplication.translate("LayoutLabel", u"Employee Date", None))
        self.label_3.setText(QCoreApplication.translate("LayoutLabel", u"Department", None))
        self.label_4.setText(QCoreApplication.translate("LayoutLabel", u"Position", None))
        self.label_5.setText(QCoreApplication.translate("LayoutLabel", u"Annual salary", None))
        self.label_6.setText(QCoreApplication.translate("LayoutLabel", u"Job description", None))
        self.pushButton.setText(QCoreApplication.translate("LayoutLabel", u"Cancel", None))
        self.pushButton_2.setText(QCoreApplication.translate("LayoutLabel", u"Ok", None))
    # retranslateUi

