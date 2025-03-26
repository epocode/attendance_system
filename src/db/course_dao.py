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
        query = 'SELECT * FROM course;'
        res = self.db.fetchall(query)
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
    def get_course_count_by_teacher(self, teacher_username):
        #得到对应老师的课程数量
        query = 'SELECT COUNT(*) FROM course WHERE teacher_username = %s;'
        params = [teacher_username]
        res = self.db.fetchall(query, params)[0][0]
        return res
    
    def get_courses_by_teacher(self, teacher_username):
        # 查询该老师的课程
        query = 'SELECT course_name FROM course WHERE teacher_username = %s;'
        params = [teacher_username]
        res = self.db.fetchall(query, params)
        return res 
        

