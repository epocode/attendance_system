from PySide6.QtCore import (
    QAbstractTableModel
)
from PySide6.QtGui import Qt


class TeacherTableModel(QAbstractTableModel):
    def __init__(self, teacher_dao):
        super().__init__()
        self.teacher_dao = teacher_dao
        self.data_cache = self.load_data()

    def load_data(self):
        return self.teacher_dao.get_data()
    
    def headerData(self, section, orientation, role = ...):
        headers = ['姓名', '用户名']
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return headers[section]
            
    def rowCount(self, parent = ...):
        return len(self.data_cache)
    
    def columnCount(self, parent = ...):
        return 2

    def data(self, index, role = ...):
        if role == Qt.DisplayRole:
            return self.data_cache[index.row()][index.column()]
    def refresh(self):
        self.data_cache = self.load_data()
        self.layoutChanged.emit()