from PySide6.QtCore import QAbstractTableModel
from PySide6.QtGui import Qt
from datetime import datetime


class AttendanceDetailModel(QAbstractTableModel):
    def __init__(self, attendance_info_dao, course_name, date: str):
        super().__init__()
        self.attendance_info_dao = attendance_info_dao
        self.course_name = course_name
        if isinstance(date, str):
            self.date = datetime.strptime(date, '%Y-%m-%d')
        else:
            self.date = date

        self.attendance_data = self.load_data()

    def load_data(self):
        return self.attendance_info_dao.get_attendance_detail_by_course_date(self.course_name, self.date)   
    

    def headerData(self, section, orientation, role = ...):
        headers = ['姓名', 'ID', '是否出勤', '出勤详情']
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return headers[section]
    
    def rowCount(self, parent = ...):
        return  len(self.attendance_data) if self.attendance_data else 0
    
    def columnCount(self, parent = ...):
        return 4
    
    def data(self, index, role= ...):
        if role == Qt.DisplayRole:
            if index.column() < 3:
                if index.column() == 2:
                    return '是' if self.attendance_data[index.row()][2] == 1 else '否'
                else:
                    return self.attendance_data[index.row()][index.column()]
            else:
                return '查看'
            
    def refresh(self):
        self.attendance_data = self.load_data()
        self.layoutChanged.emit()