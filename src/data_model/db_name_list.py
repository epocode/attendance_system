from PySide6.QtCore import Qt, QAbstractListModel, QAbstractTableModel
from PySide6.QtWidgets import QApplication, QMainWindow, QListView
from mysql import connector
import mysql
import os
import sys

import mysql.connector
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import config.my_config as my_config

class TableNameListModel(QAbstractListModel):
    def __init__(self):
        super().__init__()
        self.cursor = None
        self.table_names = []
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
        except e:
            print('数据库连接失败， 错误信息：', e)

        query = '''
        SHOW TABLES'''

        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for table_name in result:
                self.table_names.append(table_name[0])
        except connector.Error as e:
            print(e)

    def rowCount(self, index):
        return len(self.table_names)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.table_names[index.row()]
        


class personInfoModel(QAbstractTableModel):
    def __init__(self, conn, table_name):
        super().__init__()
        self.cursor = conn.cursor()
        self.conn = conn
        self.table_name = table_name

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
#         sql = """
#             SELECT COUNT(*)
#             FROM INFORMATION_SCHEMA.COLUMNS
#             WHERE table_name = '%s'
# """   % self.table_name   
#         self.cursor.execute(sql)
#         results = self.cursor.fetchone()
#         return results[0]
        return 2

    def insert_data(self, name, gender, age, face_feature=None):
        try:
            sql = f"INSERT INTO {self.tabel_name} (name, gender, age) VALUES(%s, %s, %s)"
            self.cursor.execute(sql, [name, gender, age])
            last_id = self.cursor.lastrowid
            if last_id != 0:
                #将face的特征跟id存放到向量数据库中
                pass

        except e:
            print('sql insert failed.', e)

if __name__ == '__main__':
    db_model = TableNameListModel()
