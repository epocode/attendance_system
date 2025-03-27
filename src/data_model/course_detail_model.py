from PySide6.QtCore import QAbstractTableModel
from PySide6.QtGui import Qt


class CourseDetailModel(QAbstractTableModel):
    def __init__(self, attendance_info_dao, course_name):
        super().__init__()
        self.attendance_info_dao = attendance_info_dao
        self.course_name = course_name
<<<<<<< HEAD
        self.data_cache = self.load_data()
    
    def load_data(self):
        return self.attendance_info_dao.get_daily_attendance_info_by_course(self.course_name)

=======
    
>>>>>>> 414d9db09c1ed6c339657fb7b26933b73b2fe16e
    def headerData(self, section, orientation, role = ...):
        headers = ['日期', '总人数', '出勤人数', '出勤率', '出勤详情']
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return headers[section]
    
    def rowCount(self, parent = ...):
<<<<<<< HEAD
        return len(self.data_cache)
=======
        return self.attendance_info_dao.get_daily_attendance_num_by_course(self.course_name)
>>>>>>> 414d9db09c1ed6c339657fb7b26933b73b2fe16e
    
    def columnCount(self, parent = ...):
        return 5
    
    def data(self, index, role= ...):
        if role == Qt.DisplayRole:
            if index.column() < 4:
<<<<<<< HEAD
                if index.column() == 0:
                    return self.data_cache[index.row()][0].strftime('%Y-%m-%d')
                elif index.column() == 3:
                    return f"{float(self.data_cache[index.row()][3]) * 100:2f}%"
                else:
                    return self.data_cache[index.row()][index.column()]
        
            else:
                return '查看'
            
    def refresh(self):
        self.data_cache = self.load_data()
        self.layoutChanged.emit()
        
=======
                res = self.attendance_info_dao.get_daily_attendance_info_by_course(self.course_name)
                if index.column() == 0:
                    return res[index.row()][0].strftime('%Y-%m-%d')
                elif index.column() == 3:
                    return f"{float(res[index.row()][3]) * 100:2f}%"
                else:
                    return res[index.row()][index.column()]
        
            else:
                return '查看'
>>>>>>> 414d9db09c1ed6c339657fb7b26933b73b2fe16e
