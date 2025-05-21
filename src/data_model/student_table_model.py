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
        self.beginResetModel()
        self.data_cache = self.load_data()
        self.all_stu_course_map = self.load_all_stu_selected_course() # This might need specific updates too if a student is added/deleted
        self.endResetModel()  

    def delete_student_by_index(self, row_index):
        if not (0 <= row_index < len(self.data_cache)):
            print(f"Error: Row index {row_index} for deletion is out of bounds.")
            return False

        # student_id = self.data_cache[row_index][0] # ID for potential use if DAO needed it

        self.beginRemoveRows(self.index(row_index, 0).parent(), row_index, row_index)
        success = self.student_dao.delete_student(row_index) # DAO's delete_student now takes row_index
        
        if success:
            del self.data_cache[row_index]
            # Note: self.all_stu_course_map might become inconsistent if not updated.
            # For now, a full refresh() might be needed if course maps are critical after deletion
            # or specific logic to remove student's courses from map.
            # For this step, focusing on data_cache and signals.
            self.endRemoveRows()
            return True
        else:
            self.endRemoveRows() # Must be called to keep Qt's internal state consistent
            print(f"Error deleting student at index {row_index}: DAO reported failure.")
            return False

    def add_student_data(self, name, gender, age, is_face_collected, face_feature=None):
        # DAO's add_student returns (id, name, gender, age, is_face_collected) or None
        new_student_data = self.student_dao.add_student(name, gender, age, is_face_collected, face_feature)
        
        if new_student_data:
            new_row_index = len(self.data_cache)
            
            self.beginInsertRows(self.index(new_row_index, 0).parent(), new_row_index, new_row_index)
            self.data_cache.append(new_student_data)
            # Note: self.all_stu_course_map will not have this new student's courses yet.
            # This might require an update to all_stu_course_map or a refresh later for course column.
            self.endInsertRows()
            return True
        else:
            print(f"Error adding student '{name}': DAO returned None.")
            return False