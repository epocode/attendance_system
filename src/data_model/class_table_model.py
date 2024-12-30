from PySide6.QtCore import QAbstractTableModel
from PySide6.QtGui import Qt


class ClassTableModel(QAbstractTableModel):
    def __init__(self, class_dao):
        super().__init__()
        self.class_dao = class_dao
    
    def headerData(self, section, orientation, role = ...):
        headers = ['班级名', '老师']
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return headers[section]
    
    def rowCount(self, parent = ...):
        return self.class_dao.get_class_num()
    
    def columnCount(self, parent = ...):
        return 2
    
    def data(self, index, role= ...):
        if role == Qt.DisplayRole:
            res = self.class_dao.get_class_names()
            return res[index.row()][index.column()]