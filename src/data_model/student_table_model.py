from PySide6.QtCore import QAbstractTableModel
from PySide6.QtGui import Qt

class StudentTableModel(QAbstractTableModel):
    def __init__(self, student_dao):
        super().__init__()
        self.student_dao = student_dao
    
    def headerData(self, section, orientation, role = ...):
        headers = ['ID', '姓名', '性别', '年龄']
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return headers[section]
            
    def rowCount(self, parent = ...):
        return self.student_dao.get_student_num()
    
    def columnCount(self, parent = ...):
        return 4
    
    def data(self, index, role= ...):
        if role == Qt.DisplayRole:
            res = self.student_dao.get_student_info()
            return res[index.row()][index.column()]