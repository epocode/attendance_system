from PySide6.QtCore import QAbstractTableModel
from PySide6.QtGui import Qt


class CoursecherTableModel(QAbstractTableModel):
    def __init__(self, course_dao, teacher_username):
        super().__init__()
        self.teacher_username = teacher_username
        self.course_dao = course_dao
    
    def headerData(self, section, orientation, role = ...):
        headers = ['课程名', '操作']
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return headers[section]
    
    def rowCount(self, parent = ...):
        return self.course_dao.get_course_count_by_teacher(self.teacher_username)
    
    def columnCount(self, parent = ...):
        return 2
    
    def data(self, index, role= ...):
        if role == Qt.DisplayRole:
            if index.column() == 0:
                res = self.course_dao.get_courses_by_teacher(self.teacher_username)
                return res[index.row()][0]
            else:
                return '签到'