# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDateEdit,
    QDialog, QDialogButtonBox, QDoubleSpinBox, QFormLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MyDialog(object):
    def setupUi(self, MyDialog):
        if not MyDialog.objectName():
            MyDialog.setObjectName(u"MyDialog")
        MyDialog.resize(543, 541)
        self.verticalLayout = QVBoxLayout(MyDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(MyDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit = QLineEdit(MyDialog)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_2 = QLabel(MyDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.dateEdit = QDateEdit(MyDialog)
        self.dateEdit.setObjectName(u"dateEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.dateEdit)

        self.label_3 = QLabel(MyDialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.comboBox = QComboBox(MyDialog)
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBox)

        self.label_4 = QLabel(MyDialog)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.comboBox_2 = QComboBox(MyDialog)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.comboBox_2)

        self.label_5 = QLabel(MyDialog)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.doubleSpinBox = QDoubleSpinBox(MyDialog)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.doubleSpinBox)

        self.label_6 = QLabel(MyDialog)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.textEdit = QTextEdit(MyDialog)
        self.textEdit.setObjectName(u"textEdit")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.textEdit)

        self.pushButton = QPushButton(MyDialog)
        self.pushButton.setObjectName(u"pushButton")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.pushButton)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(MyDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.lineEdit)
        self.label_2.setBuddy(self.dateEdit)
        self.label_3.setBuddy(self.comboBox)
        self.label_4.setBuddy(self.comboBox_2)
        self.label_5.setBuddy(self.doubleSpinBox)
        self.label_6.setBuddy(self.textEdit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.lineEdit, self.dateEdit)
        QWidget.setTabOrder(self.dateEdit, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.comboBox_2)
        QWidget.setTabOrder(self.comboBox_2, self.doubleSpinBox)
        QWidget.setTabOrder(self.doubleSpinBox, self.textEdit)

        self.retranslateUi(MyDialog)
        self.buttonBox.accepted.connect(MyDialog.accept)
        self.buttonBox.rejected.connect(MyDialog.reject)

        QMetaObject.connectSlotsByName(MyDialog)
    # setupUi

    def retranslateUi(self, MyDialog):
        MyDialog.setWindowTitle(QCoreApplication.translate("MyDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("MyDialog", u"&Employee name:", None))
        self.label_2.setText(QCoreApplication.translate("MyDialog", u"&Employment date:", None))
        self.label_3.setText(QCoreApplication.translate("MyDialog", u"&Department", None))
        self.label_4.setText(QCoreApplication.translate("MyDialog", u"&Position", None))
        self.label_5.setText(QCoreApplication.translate("MyDialog", u"&Annual salary", None))
        self.label_6.setText(QCoreApplication.translate("MyDialog", u"&Job description", None))
        self.pushButton.setText(QCoreApplication.translate("MyDialog", u"clear", None))
    # retranslateUi

