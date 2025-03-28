from PySide6.QtCore import QAbstractTableModel
from PySide6.QtGui import Qt


class CoursecherTableModel(QAbstractTableModel):
    def __init__(self, course_dao, teacher_username):
        super().__init__()
        self.teacher_username = teacher_username
        self.course_dao = course_dao
        self.data_cache = self.load_data()

    def load_data(self):
        return self.course_dao.get_courses_by_teacher(self.teacher_username)

    def headerData(self, section, orientation, role = ...):
        headers = ['课程名', '操作']
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return headers[section]
    
    def rowCount(self, parent = ...):
        return len(self.data_cache)
    
    def columnCount(self, parent = ...):
        return 2
    
    def data(self, index, role= ...):
        if role == Qt.DisplayRole:
            if index.column() == 0:
                return self.data_cache[index.row()][0]
            else:
                return '签到'
            
    def refresh(self):
        self.data_cache = self.load_data()
        self.layoutChanged.emit()