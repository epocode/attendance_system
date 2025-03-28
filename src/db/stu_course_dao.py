class StuCourseDao():
    def __init__(self, db):
        self.db = db

    def add_course(self, student_id, course_id):
        sql = "INSERT INTO stu_course (student_id, course_id) VALUES (?, ?)"
        

    def remove_course(self, student_id, course_id):
        sql = "DELETE FROM stu_course WHERE student_id = %s AND course_id = %s"
        

    def get_courses_by_student(self, student_id):
        sql = """SELECT course_name
FROM course_student
WHERE student_id = %s;"""
        params = [student_id]
        res = self.db.fetchall(sql, params)
        # 将[(),()]转化为[,]
        res = [row[0] for row in res]
        return res