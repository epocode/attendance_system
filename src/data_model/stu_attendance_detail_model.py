from PySide6.QtCore import QAbstractTableModel
from PySide6.QtGui import Qt
from datetime import datetime


class StuAttendanceDetailModel(QAbstractTableModel):
    def __init__(self, attendance_info_dao, stu_id):
        super().__init__()
        self.attendance_info_dao = attendance_info_dao
        self.stu_id = stu_id

        self.data_cache = self.load_data()

    def load_data(self):
        return self.attendance_info_dao.get_stu_attendance_detail(self.stu_id)
    

    def headerData(self, section, orientation, role = ...):
        headers = ['日期', '课程名']
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return headers[section]
    
    def rowCount(self, parent = ...):
        return  len(self.data_cache)
    
    def columnCount(self, parent = ...):
        return 2
    
    def data(self, index, role= ...):
        if role == Qt.DisplayRole:
            if index.column() == 0:
                return datetime.strftime(self.data_cache[index.row()][0], "%Y-%m-%d")
            else:   
                return self.data_cache[index.row()][index.column()]
            
    def refresh(self):
        self.attendance_data = self.load_data()
        self.layoutChanged.emit()