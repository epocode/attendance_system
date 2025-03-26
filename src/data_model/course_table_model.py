from PySide6.QtCore import QAbstractTableModel
from PySide6.QtGui import Qt


class CourseTableModel(QAbstractTableModel):
    def __init__(self, course_dao):
        super().__init__()
        self.course_dao = course_dao
        self.data_cache = self.load_data()

    def load_data(self):
        return self.course_dao.get_course_names()
    
    def headerData(self, section, orientation, role = ...):
        headers = ['课程名', '老师']
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return headers[section]
    
    def rowCount(self, parent = ...):
        return len(self.data_cache)
    
    def columnCount(self, parent = ...):
        return 2
    
    def data(self, index, role= ...):
        if role == Qt.DisplayRole:
            return self.data_cache[index.row()][index.column()]
        
    def refresh(self):
        self.data_cache = self.load_data()
        self.layoutChanged.emit()   