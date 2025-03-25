import os
import sys 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PySide6.QtCore import Qt, QAbstractListModel, QAbstractTableModel
import config.my_config as my_config
from src.db.course_dao import CourseDAO

class CourseListModel(QAbstractListModel):
    def __init__(self, db, username):
        super().__init__()

        self.course_dao = CourseDAO(db, username)
        self.cur_course_name = ""

    def rowCount(self, index):
        return self.course_dao.get_course_num()

    def data(self, index, role):
        if role == Qt.DisplayRole:
            res = self.course_dao.get_course_names()
            return res[index.row()][0]
            
        
    def create_new_course(self, course_name):
        self.course_dao.create_course(course_name)
        self.layoutChanged.emit()
    
    def delete_course(self, course_name):
        self.course_dao.delete_course(course_name)
        self.layoutChanged.emit()
        vec_file_path = os.path.join(my_config.VEC_DB_PATH, course_name + '.faiss')
        if os.path.exists(vec_file_path):
            os.remove(vec_file_path)
            print('成功删除')

class PersonInfoModel(QAbstractTableModel):
    def __init__(self, conn, table_name):
        super().__init__()
        self.conn = conn
        self.table_name = table_name
        self.load_data()

    def load_data(self):
        query = f"SELECT * FROM {self.table_name}"
        self.data = self.conn.execute(query).fetchall()

    def rowCount(self, index):
        return len(self.data)

    def columnCount(self, index):
        return len(self.data[0]) if self.data else 0

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.data[index.row()][index.column()]

    def insert_data(self, name, gender, age, face_feature):
        query = f"INSERT INTO {self.table_name} (name, gender, age, face_feature) VALUES (?, ?, ?, ?)"
        self.conn.execute(query, (name, gender, age, face_feature))
        self.conn.commit()
        self.load_data()
        self.layoutChanged.emit()

    def save_vec_db(self):
        # Save vector database logic
        pass

class AbsentTableModel(QAbstractTableModel):
    def __init__(self, cursor, table_name):
        super().__init__()
        self.cursor = cursor
        self.table_name = table_name
        self.load_data()

    def load_data(self):
        query = f"SELECT * FROM {self.table_name} WHERE status = 'absent'"
        self.data = self.cursor.execute(query).fetchall()

    def rowCount(self, index):
        return len(self.data)

    def columnCount(self, index):
        return len(self.data[0]) if self.data else 0

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.data[index.row()][index.column()]

    def delete_row(self, id):
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        self.cursor.execute(query, (id,))
        self.cursor.connection.commit()
        self.load_data()
        self.layoutChanged.emit()