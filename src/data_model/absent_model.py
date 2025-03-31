from PySide6.QtCore import QAbstractTableModel
from PySide6.QtGui import Qt
from datetime import datetime


class AbsentModel(QAbstractTableModel):
    def __init__(self, stu_course_dao, course_name):
        super().__init__()
        self.stu_course_dao = stu_course_dao
        self.course_name = course_name
        self.data_cache = self.load_data()

    def load_data(self):
        return self.stu_course_dao.get_stu_by_course(self.course_name)   
    

    def headerData(self, section, orientation, role = ...):
        headers = ['ID', '姓名']
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return headers[section]
    
    def rowCount(self, parent = ...):
        return  len(self.data_cache)
    
    def columnCount(self, parent = ...):
        return 2
    
    def data(self, index, role= ...):
        if role == Qt.DisplayRole:
            return self.data_cache[index.row()][index.column()]
            
    def remove_row(self, row):
        if 0 <= row < len(self.data_cache):
            del self.data_cache[row]
            self.layoutChanged.emit()

    def refresh(self):
        self.data_cache = self.load_data()
        self.layoutChanged.emit()