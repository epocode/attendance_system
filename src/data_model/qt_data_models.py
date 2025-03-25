from PySide6.QtCore import Qt, QAbstractListModel, QAbstractTableModel
from PySide6.QtWidgets import QApplication, QMainWindow, QListView
from mysql import connector
import mysql
import os
import sys
from annoy import AnnoyIndex
import faiss
import numpy as np
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import config.my_config as my_config
from src.db.course_dao import CourseDAO
from src.db.vec_db import VecDB

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
    def __init__(self, db, teacher_username, course_name):
        super().__init__()
        self.db = db
        self.teacher_username = teacher_username
        self.course_name = course_name

        #创建向量数据库
        self.vec_db = VecDB(self.teacher_username)


    def data(self, index, role):
        if role == Qt.DisplayRole:
            sql = 'SELECT * FROM %s' % self.table_name
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results[index.row()][index.column()]
        
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                self.cursor.execute("""
                    SELECT COLUMN_NAME
                    FROM INFORMATION_SCHEMA.COLUMNS
                    WHERE TABLE_NAME = '%s'
                """ % self.table_name)
                results = self.cursor.fetchall()
                return results[section][0]
            else:
                return section + 1  # 设置行头

    def rowCount(self, index):
        self.cursor.execute('SELECT COUNT(*) FROM %s' % self.table_name)
        return self.cursor.fetchall()[0][0]

    def columnCount(self, index):
        return 2

    def insert_data(self, name, gender, age, face_feature=None):
        dis, ids = self.vec_db.search(face_feature, 1)
        if dis[0][0] > 0.9:
            print('当前人脸已经录入')
            return
        try:
            sql = f"INSERT INTO {self.table_name} (name, gender, age) VALUES(%s, %s, %s)"
            self.cursor.execute(sql, [name, gender, age])
            self.conn.commit()
            last_id = self.cursor.lastrowid
            if last_id != 0:
                self.vec_db.add_with_ids(face_feature, np.array([last_id]))
            self.layoutChanged.emit()
        except Exception as e:
            print('sql insert failed.', e)

    def save_vec_db(self):
        try:
            faiss.write_index(self.vec_db, os.path.join(my_config.VEC_DB_PATH, self.table_name + '.faiss'))
        except Exception as e:
            print('保存失败')

    def search_id_by_feature(self, feature):
        dis, ids = self.vec_db.search(feature, 1)
        if dis[0][0] > 0.9:
            return ids[0][0]
        return None
    
    def face_info(self, id):
        q = f"SELECT name FROM {self.table_name} WHERE id = {id}"
        self.cursor.execute(q)
        res = self.cursor.fetchall()
        return res[0][0]
    
class AbsentTableModel(QAbstractTableModel):
    def __init__(self, cursor, table_name):
        super().__init__()
        self.cursor = cursor
        self.table = None #用于保存id与name的键值对
        try:
            sql = f'SELECT id, name FROM {table_name}'
            self.cursor.execute(sql)
            self.table = self.cursor.fetchall()
        except Exception as e:
            print(e)
    
    def rowCount(self, idx):
        return len(self.table)
    
    def columnCount(self, parent = ...):
        return 2
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.table[index.row()][index.column()]
        
    def headerData(self, section, orientation, role = ...):
        header = ['id', 'name']
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return header[section]

    def delete_row(self, id):
        for i, line in enumerate(self.table):
            if line[0] == id:
                del self.table[i]
        
        self.layoutChanged.emit()
