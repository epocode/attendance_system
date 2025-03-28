from PySide6.QtWidgets import QComboBox, QStyledItemDelegate
from PySide6.QtCore import Signal, Qt

class MyComboDelegate(QStyledItemDelegate):
    
    def __init__(self, parent=None):
        super().__init__(parent)

    def createEditor(self, parent, option, index):
        combo_box = QComboBox(parent)
        return combo_box



    def setEditorData(self, editor, index):
        editor.clear()
        course_list = index.data(Qt.UserRole)  # 获取用户角色数据，即课程列表
        if course_list:
            for course in course_list:
                editor.addItem(course)

    def setModelData(self, editor, model, index):
        model.setData(index, editor.currentText(), Qt.EditRole)