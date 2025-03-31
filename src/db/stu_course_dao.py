class StuCourseDao():
    def __init__(self, db):
        self.db = db

    def get_courses_by_student(self, student_id):
        sql = """SELECT course_name
FROM course_student
WHERE student_id = %s;"""
        params = [student_id]
        res = self.db.fetchall(sql, params)
        # 将[(),()]转化为[,]
        res = [row[0] for row in res]
        return res
    
    def get_courses_not_selected_by_student(self, stu_id):
        sql = """
SELECT course_name
FROM course
WHERE course_name not in (
		select course_name
        FROM course_student
        WHERE student_id =%s
);"""
        params = [stu_id]
        res = self.db.fetchall(sql, params)
        # 将[(),()]转化为[,]
        res = [row[0] for row in res]
        return res


    def get_stu_by_course(self, course_name):
        sql = """
SELECT id, name 
FROM course_student JOIN student
ON course_student.student_id = student.id
WHERE course_name = %s;"""
        params = [course_name]
        res = self.db.fetchall(sql, params)
        return res

    def add_stu_to_courses(self, stu_id, course_list):
        wait_for_insert_data = []
        for course_name in course_list:
            wait_for_insert_data.append((course_name, stu_id))
        sql = "INSERT INTO course_student (course_name, student_id) VALUES(%s, %s);"
        self.db.execute_many(sql, wait_for_insert_data)

    def del_course_from_stu(self, stu_id, course_list):
        sql = """DELETE FROM course_student WHERE student_id = %s AND course_name = %s;"""
        data_for_del = []
        for course_name in course_list:
            data_for_del.append((stu_id, course_name))
        self.db.execute_many(sql, data_for_del)