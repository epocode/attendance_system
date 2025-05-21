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
    
    def get_data(self):
        # Returns list of (course_name, teacher_actual_name)
        query = '''
            SELECT c.course_name, t.name 
            FROM course c
            JOIN teacher t ON c.teacher_username = t.username;
        '''
        res = self.db.fetchall(query)
        return res
    
    def create_course(self, course_name):
        query = 'INSERT INTO course (course_name, teacher_username) VALUES (%s, %s);'
        params = [course_name, self.username]
        self.db.execute(query, params)

    def delete_course(self, course_name):
        query = 'DELETE FROM course WHERE course_name = %s and teacher_username = %s;'
        params = [course_name, self.username]
        self.db.execute(query, params) # Returns True on success, False or raises exception

    def delete_course_by_row(self, row_index):
        # To correctly delete by row_index based on the current data view (course_name, teacher_name)
        # we first fetch the data as the model sees it.
        current_courses = self.get_data() 
        if 0 <= row_index < len(current_courses):
            course_name_to_delete = current_courses[row_index][0]
            # Assuming course_name is unique, or we need teacher_username too for precise deletion.
            # The original query 'DELETE FROM course WHERE course_name = %s;' implies course_name is key enough.
            query = 'DELETE FROM course WHERE course_name = %s;'
            params = [course_name_to_delete]
            return self.db.execute(query, params) # Return True on success, False otherwise
        return False

    def check_single_course_name(self, course_name):
        query = 'SELECT COUNT(*) FROM course WHERE course_name = %s;'
        params = [course_name]
        res = self.db.fetchall(query, params)[0][0]
        if res == 0:
            return True
        else:
            return False
        
    def add_new(self, course_name, teacher_username):
        # Inserts new course and returns (course_name, teacher_actual_name)
        insert_query = 'INSERT INTO course (course_name, teacher_username) VALUES (%s, %s);'
        insert_params = [course_name, teacher_username]
        
        success = self.db.execute(insert_query, insert_params)
        
        if success:
            # Fetch the teacher's actual name
            teacher_name_query = 'SELECT name FROM teacher WHERE username = %s;'
            teacher_name_params = [teacher_username]
            teacher_res = self.db.fetchall(teacher_name_query, teacher_name_params)
            
            if teacher_res and len(teacher_res) > 0:
                teacher_actual_name = teacher_res[0][0]
                return (course_name, teacher_actual_name)
            else:
                # This case should ideally not happen if teacher_username is valid
                # Or handle as an error: course inserted but teacher name not found
                print(f"Warning: Course '{course_name}' added, but teacher '{teacher_username}' not found.")
                return (course_name, "Unknown Teacher") # Fallback or error
        return None # Insertion failed

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
        

