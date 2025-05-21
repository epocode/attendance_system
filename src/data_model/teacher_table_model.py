from PySide6.QtCore import (
    QAbstractTableModel,
    Signal,
    )
from PySide6.QtGui import Qt


class TeacherTableModel(QAbstractTableModel):
    def __init__(self, teacher_dao):
        super().__init__()
        self.teacher_dao = teacher_dao
        self.data_cache = self.load_data()

    def load_data(self):
        return self.teacher_dao.get_data()
    
    def headerData(self, section, orientation, role = ...):
        headers = ['姓名', '用户名']
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return headers[section]
            
    def rowCount(self, parent = ...):
        return len(self.data_cache)
    
    def columnCount(self, parent = ...):
        return 2

    def data(self, index, role = ...):
        if role == Qt.DisplayRole:
            return self.data_cache[index.row()][index.column()]
    def refresh(self):
        self.beginResetModel()
        self.data_cache = self.load_data()
        self.endResetModel()

    def delete_teacher_by_index(self, row_index):
        if 0 <= row_index < len(self.data_cache):
            self.beginRemoveRows(self.index(row_index, 0).parent(), row_index, row_index)
            # Assuming username is the second element in the tuple from data_cache
            # and delete_row in DAO can handle the actual deletion from DB
            # The current DAO's delete_row takes a row index, which is fine.
            self.teacher_dao.delete_row(row_index) 
            del self.data_cache[row_index]
            self.endRemoveRows()
            return True
        return False

    def add_teacher(self, name, username, pswd):
        try:
            # DAO's add_new is now expected to return (name, username) on success
            new_teacher_data = self.teacher_dao.add_new(name, username, pswd)
            if new_teacher_data:
                # Data is typically appended to the end
                new_row_index = len(self.data_cache)
                
                self.beginInsertRows(self.index(new_row_index,0).parent(), new_row_index, new_row_index)
                self.data_cache.append(new_teacher_data)
                self.endInsertRows()
                return True
            else:
                # DAO indicates failure (e.g. username exists, DB error)
                print(f"Error adding teacher: DAO returned None or False")
                return False
        except Exception as e:
            # Log error or handle appropriately
            print(f"Exception when adding teacher: {e}")
            # Optionally, re-raise or handle more gracefully
            return False