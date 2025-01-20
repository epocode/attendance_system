from mysql import connector
import config.my_config as my_config

class DataBase:
    def __init__(self):
        try:
            self.conn = connector.connect(
                host=my_config.HOST,
                database=my_config.DATABASE_NAME,
                user=my_config.USER_NAME,
                password=my_config.PSWD
            )
            if self.conn.is_connected():
                print("连接成功")
        except Exception as e:
            print(e)

    def close(self):
        self.conn.close()

    def fetchall(self, query, params:list=None):
        with self.conn.cursor() as cursor:
            try:
                if params is None:
                    cursor.execute(query)
                else:
                    cursor.execute(query, params)
                res = cursor.fetchall()
                return res
            except Exception as e:
                print(e)
            
        return False
    
    

    
    def execute(self, query, params):
        with self.conn.cursor() as cursor:
            try: 
                cursor.execute(query, params)
                self.conn.commit()
                return True
            except Exception as e:
                print(e)

        
        return False

    def execute_with_lastid(self, query, params):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(query, params)
                self.conn.commit()
                return cursor.lastrowid
            except Exception as e:
                print(e)
        
        return False
