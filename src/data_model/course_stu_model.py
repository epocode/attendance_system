from PySide6.QtCore import QAbstractTableModel
from PySide6.QtGui import Qt


class CourseStuModel(QAbstractTableModel):
    def __init__(self, stu_course_dao, stu_id):
        super().__init__()
        self.stu_course_dao = stu_course_dao
        self.stu_id = stu_id
        self.course_list = self.load_data()

    def load_data(self):
        return self.stu_course_dao.get_courses_by_student(self.stu_id)

    def headerData(self, section, orientation, role = ...):
        headers = ['课程名']
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return headers[section]
    
    def rowCount(self, parent = ...):
        return len(self.course_list)
    
    def columnCount(self, parent = ...):
        return 1
    
    def data(self, index, role= ...):
        if role == Qt.DisplayRole:
            return self.course_list[index.row()]
            
    def refresh(self):
        self.course_list = self.load_data()
        self.layoutChanged.emit() 