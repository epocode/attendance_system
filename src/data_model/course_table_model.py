from PySide6.QtCore import QAbstractTableModel
from PySide6.QtGui import Qt


class CourseTableModel(QAbstractTableModel):
    def __init__(self, course_dao):
        super().__init__()
        self.course_dao = course_dao
        self.data_cache = self.load_data()

    def load_data(self):
        # Ensure this matches the DAO method that returns (course_name, teacher_actual_name)
        return self.course_dao.get_data() 
    
    def headerData(self, section, orientation, role = ...):
        headers = ['课程名', '老师']
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return headers[section]
    
    def rowCount(self, parent = ...):
        return len(self.data_cache)
    
    def columnCount(self, parent = ...):
        return 2
    
    def data(self, index, role= ...):
        if role == Qt.DisplayRole:
            return self.data_cache[index.row()][index.column()]
        
    def refresh(self):
        self.beginResetModel()
        self.data_cache = self.load_data()
        self.endResetModel()

    def delete_course_by_index(self, row_index):
        if 0 <= row_index < len(self.data_cache):
            # course_to_delete = self.data_cache[row_index] # For logging or further use if needed
            
            self.beginRemoveRows(self.index(row_index, 0).parent(), row_index, row_index)
            success = self.course_dao.delete_course_by_row(row_index) # DAO method uses row_index based on its get_data()
            if success:
                del self.data_cache[row_index]
                self.endRemoveRows()
                return True
            else:
                # If DAO failed, rollback the view change
                self.endRemoveRows() # Must be called even on failure to keep state consistent
                print(f"Error deleting course at index {row_index}: DAO reported failure.")
                return False
        return False

    def add_course(self, course_name, teacher_username):
        # DAO's add_new is expected to return (course_name, teacher_actual_name)
        new_course_data = self.course_dao.add_new(course_name, teacher_username)
        if new_course_data:
            new_row_index = len(self.data_cache)
            
            self.beginInsertRows(self.index(new_row_index, 0).parent(), new_row_index, new_row_index)
            self.data_cache.append(new_course_data) # new_course_data is (course_name, teacher_actual_name)
            self.endInsertRows()
            return True
        else:
            print(f"Error adding course '{course_name}': DAO returned None or False.")
            return False