from src.db.database import DataBase

class CourseDAO:
    def __init__(self, db: DataBase, username=None):
        self.db = db
        self.username = username

    def get_course_num(self):
        #这是查询所有的班级
        query = 'SELECT COUNT(*) FROM course;'
        res = self.db.fetchall(query)
       
        return res[0][0]
    
    def get_course_names(self):
        if self.username is None:
            query = 'SELECT * FROM course;'
            res = self.db.fetchall(query)
        else:
            query = 'SELECT course_name FROM course WHERE teacher_username = %s;'
            params = [self.username]
            res = self.db.fetchall(query, params)
        return res
    
    def create_course(self, course_name):
        query = 'INSERT INTO course (course_name, teacher_username) VALUES (%s, %s);'
        params = [course_name, self.username]
        self.db.execute(query, params)

    def delete_course(self, course_name):
        query = 'DELETE FROM course WHERE course_name = %s and teacher_username = %s;'
        params = [course_name, self.username]
        self.db.execute(query, params)

    def delete_course_by_row(self, row):
        query = 'SELECT * FROM course;'
        res = self.db.fetchall(query)
        course_name = res[row][0]
        query = 'DELETE FROM course WHERE course_name = %s;'
        params = [course_name]
        self.db.execute(query, params)

    def check_single_course_name(self, course_name):
        query = 'SELECT COUNT(*) FROM course WHERE course_name = %s;'
        params = [course_name]
        res = self.db.fetchall(query, params)[0][0]
        if res == 0:
            return True
        else:
            return False
        
    def add_new(self, course_name, teacher_username):
        query = 'INSERT INTO course (course_name, teacher_username) VALUES (%s, %s);'
        params = [course_name, teacher_username]
        self.db.execute(query, params)

    # 下面是关于根据老师查询课程信息
    def get_course_count_by_teacher(self, username):
        #得到对应老师的课程数量
        query = 'SELECT COUNT(*) FROM course WHERE teacher_username = %s;'
        params = [username]
        res = self.db.fetchall(query, params)[0][0]
        return res
