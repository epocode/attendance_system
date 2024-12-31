from src.db.database import DataBase

class ClassDAO:
    def __init__(self, db:DataBase, username=None):
        self.db = db
        self.username = username

    def get_class_num(self):
        if self.username is None:
            #这是查询所有的班级
            query = 'SELECT COUNT(*) FROM class;'
            res = self.db.fetchall(query)
        else:
            #这是查询对应老师的班级
            query = 'SELECT COUNT(*) FROM class WHERE teacher_username = %s;'
            params = [self.username]
            res = self.db.fetchall(query, params)
        return res[0][0]
    
    def get_class_names(self):
        if self.username is None:
            query = 'SELECT * FROM class;'
            res = self.db.fetchall(query)
        else:
            query = 'SELECT class_name FROM class  WHERE teacher_username = %s;'
            params = [self.username]
            res = self.db.fetchall(query, params)
        return res
    
    def create_class(self, class_name):
        query = 'INSERT INTO class (class_name, teacher_username) VALUES (%s, %s);'
        params = [class_name, self.username]
        self.db.execute(query, params)

    def delete_class(self, class_name):
        query = 'DELETE FROM class WHERE class_name = %s and teacher_username = %s;'
        params = [class_name, self.username]
        self.db.execute(query, params)

    def delete_class_by_row(self, row):
        query = 'SELECT * FROM class;'
        res = self.db.fetchall(query)
        class_name = res[row][0]
        query = 'DELETE FROM class WHERE class_name = %s;'
        params = [class_name]
        self.db.execute(query, params)


    def check_single_class_name(self, class_name):
        query = 'SELECT COUNT(*) FROM class WHERE class_name = %s;'
        params = [class_name]
        res = self.db.fetchall(query, params)[0][0]
        if res == 0:
            return True
        else:
            return False
        
    def add_new(self, class_name, teacher_username):
        query = 'INSERT INTO class (class_name, teacher_username) VALUES (%s, %s);'
        params = [class_name, teacher_username]
        self.db.execute(query, params)
        