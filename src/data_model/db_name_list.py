from PySide6.QtCore import Qt, QAbstractListModel, QAbstractTableModel
from PySide6.QtWidgets import QApplication, QMainWindow, QListView
from mysql import connector
import mysql
import os
import sys
from annoy import AnnoyIndex
import faiss
import mysql.connector
import numpy as np
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import config.my_config as my_config

class TableNameListModel(QAbstractListModel):
    def __init__(self):
        super().__init__()
        self.cursor = None
        self.cur_table_name = ""

        try:
            self.conn = connector.connect(
                host=my_config.HOST,
                database=my_config.DATABASE_NAME,
                user=my_config.USER_NAME,
                password=my_config.PSWD
            )
            if self.conn.is_connected():
                print("连接成功")
                self.cursor = self.conn.cursor()
        except Exception as e:
            print('数据库连接失败， 错误信息：', e)

    def rowCount(self, index):
        sql = 'SHOW TABLES'
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return len(results)
        except Exception as e:
            print('获取表格行数错误')
            print(e)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            sql = 'SHOW TABLES'
            try:
                self.cursor.execute(sql)
                results = self.cursor.fetchall()
                return results[index.row()][0]
            except Exception as e:
                print('获取模型数据失败')
                print(e)
            
        
    def create_new_table(self, table_name):
        sql = f"""create table {table_name} (id  INT AUTO_INCREMENT, name VARCHAR(100),
          gender ENUM('male', 'female'), age INT, PRIMARY KEY (id));"""
        try:
            self.cursor.execute(sql)
            print(f"成功创建新表{table_name}")
            #创建sql后继续创建对应的向量数据库
            
        except Exception as e:
            print('创建新的表格失败')
            print(e) 
        self.layoutChanged.emit()
    
    def drop_selected_table(self, table_name):
        sql = f"DROP TABLE IF EXISTS {table_name}"
        try:
            self.cursor.execute(sql)
            print(f'成功删除{table_name}')
            self.layoutChanged.emit()
            #同时删除对应的向量数据库文件
            vec_file_path = os.path.join(my_config.VEC_DB_PATH, table_name + '.faiss')
            if os.path.exists(vec_file_path):
                os.remove(vec_file_path)
                print('成功删除')

        except Exception as e:
            print('删除表格失败')
            print(e)
        

class PersonInfoModel(QAbstractTableModel):
    def __init__(self, conn, table_name):
        super().__init__()
        self.cursor = conn.cursor()
        self.conn = conn
        self.table_name = table_name

        #创建或者读取该表对应的向量数据库
        self.vec_db = faiss.IndexIDMap(faiss.IndexFlatIP(512))
        vec_db_path = os.path.join(my_config.VEC_DB_PATH, self.table_name + '.faiss')


        if os.path.exists(vec_db_path):
            try:
                self.vec_db = faiss.read_index(vec_db_path)
                print('索引中的向量数目为：', self.vec_db.ntotal)

            except Exception as e:
                print(e)


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

if __name__ == '__main__':
    db_model = TableNameListModel()
