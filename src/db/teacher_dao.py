from src.db.database import DataBase

class TeacherDAO:
    def __init__(self, db):
        self.db = db

    def check_login(self, username, pswd):
        query = 'SELECT * FROM teacher WHERE username = %s and password = %s;'
        params = [username, pswd]
        res = self.db.fetchall(query, params)

        if res == False or len(res) == 0:
            return None
        else:
            #这里先假设第一个是姓名，第二个是username
            return (res[0][0], res[0][1])
        
    def register(self, name, username, pswd):
        query = 'SELECT * FROM teacher WHERE username = %s;'
        res = self.db.fetchall(query, [username])
        if len(res) != 0:
            return False
        
        query = 'INSERT INTO teacher (name, username, password) VALUES (%s, %s, %s);'
        params = [name, username, pswd]
        res = self.db.execute(query, params)
        return res
    
    def get_len(self):
        query = 'SELECT COUNT(*) FROM  teacher;'
        res = self.db.fetchall(query)
        return res[0][0]
    
    def get_data(self):
        #->[(name, username)]
        query = 'SELECT name, username FROM teacher;'
        res = self.db.fetchall(query)
        return res

    def check_single_username(self, username):
        query = 'SELECT COUNT(*) FROM teacher WHERE  username = %s;'
        params = [username]
        res = self.db.fetchall(query, params)
        if res[0][0] == 0:
            return True
        else:
            return False
        
    def add_new(self, name, username, pswd):
        query = 'INSERT INTO teacher (name, username, password) VALUES(%s, %s, %s);'
        params = [name, username, pswd]
        success = self.db.execute(query, params)
        if success: # Assuming execute returns True on success or similar
            return (name, username)
        return None # Or raise an exception

    def delete_row(self, row):
        res = self.get_data()
        username = res[row][1]
        query = 'DELETE FROM teacher WHERE username = %s;'
        params = [username]
        self.db.execute(query, params)