from PySide6.QtCore import QAbstractTableModel
from PySide6.QtGui import Qt


class CourseTableModel(QAbstractTableModel):
    def __init__(self, course_dao):
        super().__init__()
        self.course_dao = course_dao
    
    def headerData(self, section, orientation, role = ...):
        headers = ['课程名', '老师']
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return headers[section]
    
    def rowCount(self, parent = ...):
        return self.course_dao.get_course_num()
    
    def columnCount(self, parent = ...):
        return 2
    
    def data(self, index, role= ...):
        if role == Qt.DisplayRole:
            res = self.course_dao.get_course_names()
            return res[index.row()][index.column()]