from PySide6.QtCore import QAbstractTableModel
from PySide6.QtGui import Qt

class StudentTableModel(QAbstractTableModel):
    def __init__(self, student_dao):
        super().__init__()
        self.student_dao = student_dao
        self.data_cache = self.load_data()
        self.all_stu_course_map = self.load_all_stu_selected_course()

    def load_data(self):
        return self.student_dao.get_student_info()  
    
    def load_all_stu_selected_course(self): 
        # 返回一个map， 键为学生ID，值为所选课程列表
        return self.student_dao.get_all_stu_selected_course()


    def headerData(self, section, orientation, role = ...):
        headers = ['ID', '姓名', '性别', '年龄', '是否已录入人脸', '所选课程', '管理课程', '录入人脸']
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return headers[section]
            
    def rowCount(self, parent = ...):
        return len(self.data_cache)
    
    def columnCount(self, parent = ...):
        return 8
    
    def data(self, index, role= ...):
        if role == Qt.DisplayRole:
            if index.column() <5:
                if index.column() == 4:
                    if self.data_cache[index.row()][4] == 1:
                        return "是"
                    else:
                        return "否"
                else:
                    return self.data_cache[index.row()][index.column()]
            elif index.column() == 5:
                return "所选课程"
            elif index.column() == 6:
                return "管理课程"
            elif index.column() == 7:
                return "录入人脸"
        
        if role == Qt.UserRole:
            if index.column() == 5:
                stu_id = self.data_cache[index.row()][0]
                return self.all_stu_course_map.get(stu_id, [])
    


    def refresh(self):
        self.data_cache = self.load_data()
        self.all_stu_course_map = self.load_all_stu_selected_course()
        self.layoutChanged.emit()  