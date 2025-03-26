from PySide6.QtCore import QAbstractTableModel
from PySide6.QtGui import Qt

class StudentTableModel(QAbstractTableModel):
    def __init__(self, student_dao):
        super().__init__()
        self.student_dao = student_dao
        self.data_cache = self.load_data()


    def load_data(self):
        return self.student_dao.get_student_info()  

    def headerData(self, section, orientation, role = ...):
        headers = ['ID', '姓名', '性别', '年龄']
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return headers[section]
            
    def rowCount(self, parent = ...):
        return len(self.data_cache)
    
    def columnCount(self, parent = ...):
        return 4
    
    def data(self, index, role= ...):
        if role == Qt.DisplayRole:
            if index.column() <4:
                return self.data_cache[index.row()][index.column()]
            else:
                return "加入班级"
            
    def flags(self, index):
        if index.column() == 4:  # 假设按钮在第5列 (索引为4)
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable  # 其他列可选但不可编辑
    
    def refresh(self):
        self.data_cache = self.load_data()
        self.layoutChanged.emit()  