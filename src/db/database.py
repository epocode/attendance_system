from mysql import connector
import config.my_config as my_config
from mysql.connector import pooling

class DataBase:
    _pool = None
    
    @classmethod
    def initialize_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pooling.MySQLConnectionPool(
                    pool_name="mypool",
                    pool_size=10,
                    host=my_config.HOST,
                    database=my_config.DATABASE_NAME,
                    user=my_config.USER_NAME,
                    password=my_config.PSWD,
                )
                print("连接池创建成功")
            except Exception as e:
                print(f"创建连接池失败:{e}")


    def __init__(self):
        if DataBase._pool is None:
            DataBase.initialize_pool()
        self.conn = None
    
    def get_connection(self):
        try:
            if self.conn is None or not self.conn.is_connected():
                self.conn = DataBase._pool.get_connection()
            return self.conn
        except Exception as e:
            print(f"获取连接失败: {e}")
            return None


    def fetchall(self, query, params:list=None):
        conn = self.get_connection()
        if conn is None:
            print("无法获取数据库连接")
            return None
        
        with conn.cursor() as cursor:
            try:
                if params is None:
                    cursor.execute(query)
                else:
                    cursor.execute(query, params)
                res = cursor.fetchall()
                return res
            except Exception as e:
                print(f"执行查询时出错: {e}")
                return []
        

    
    def execute(self, query, params):
        conn = self.get_connection()
        if conn is None:
            print("无法获取数据库连接")
            return False
        
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(query, params)
                self.conn.commit()
            except Exception as e:
                print(e)


    def execute_with_lastid(self, query, params):
        conn = self.get_connection()
        if conn is None:
            print("无法获取数据库连接")
            return False
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(query, params)
                self.conn.commit()
                return cursor.lastrowid
            except Exception as e:
                print(e)
        return False
    
    def execute_many(self, query, params):
        conn = self.get_connection()
        if conn is None:
            print("无法获取数据库连接")
            return False
        with self.conn.cursor() as cursor:
            try:
                cursor.executemany(query, params)
                self.conn.commit()
                return True
            except Exception as e:
                print(e)
        
        return False   
    
    def close(self):
        if self.conn:
            try:
                if self.conn.is_connected():
                    self.conn.close()
                    print("数据库连接关闭成功")
                self.conn = None
            except:
                print("关闭数据库连接失败")
        
