from PySide6.QtCore import (
    QAbstractTableModel
)
from PySide6.QtGui import Qt


class TeacherTableModel(QAbstractTableModel):
    def __init__(self, teacher_dao):
        super().__init__()
        self.teacher_dao = teacher_dao

    def headerData(self, section, orientation, role = ...):
        headers = ['姓名', '用户名']
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return headers[section]
    def rowCount(self, parent = ...):
        return self.teacher_dao.get_len()
    
    def columnCount(self, parent = ...):
        return 2

    def data(self, index, role = ...):
        if role == Qt.DisplayRole:
            res = self.teacher_dao.get_data()
            return res[index.row()][index.column()]