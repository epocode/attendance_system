from src.db.database import DataBase
from src.db.vec_db import VecDB
import numpy as np
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class StudentDAO:
    def __init__(self, db:DataBase):
        self.db = db
        self.vec_db = VecDB()

    def get_student_num(self):
        query = 'SELECT COUNT(*) FROM student;'
        res = self.db.fetchall(query)
        return res[0][0]
    
    def get_student_info(self):
        query = 'SELECT id, name, gender, age, is_face_collected FROM student;'
        res = self.db.fetchall(query)
        return res
    
    def get_all_stu_selected_course(self):
        query = """SELECT id, course_name
FROM student JOIN course_student
ON student.id = course_student.student_id;"""
        all_stu_course_map = {}
        res = self.db.fetchall(query)
        for row in res:
            stu_id = row[0]
            course_name = row[1]
            if stu_id not in all_stu_course_map:
                all_stu_course_map[stu_id] = []
            all_stu_course_map[stu_id].append(course_name)
        return all_stu_course_map
     
    def add_student(self,  name, gender, age, is_face_collected, face_feature=None,):
        if face_feature is not None:
            """如果人脸特征存在"""
            dis, ids = self.vec_db.search(face_feature, 1)
            if dis[0][0] > 0.9:
                print('当前人脸已经录入')
                return
            query = 'INSERT INTO student (name, gender, age, is_face_collected) VALUES (%s, %s, %s, %s);'
            params = (name, gender, age, is_face_collected)  
            last_id = self.db.execute_with_lastid(query, params)  
            if last_id != 0:
                self.vec_db.add_with_ids(face_feature, np.array([last_id]))
        else:
            query = 'INSERT INTO student (name, gender, age, is_face_collected) VALUES (%s, %s, %s, %s);'
            params = (name, gender, age, is_face_collected)  
            last_id = self.db.execute_with_lastid(query, params)


    def reset_face(self, id, face_feature):
        try:
            self.vec_db.delete(np.array([id]))
            self.vec_db.add_with_ids(face_feature, np.array([id]))
            query = """UPDATE student
            SET is_face_collected = %s  
            WHERE id = %s;"""
            params = (1, id)
            self.db.execute(query, params)
            return True
        except Exception as e:
            print(e)
            return False

    def delete_student(self, row):
        res = self.get_student_info()
        id = res[row][0]
        query = 'DELETE FROM student WHERE id = %s;'    
        params = (id,)
        self.db.execute(query, params)
        self.vec_db.delete(np.array([id]))

    def get_name_by_id(self, id):
        """根据id查询姓名"""
        query = 'SELECT name FROM student WHERE id = %s;'
        params = [id]
        res = self.db.fetchall(query, params)

        if res:
            logger.debug(f"查询到的姓名为{res[0][0]}")
            return res[0][0]
        else:
            return None

    def search_id_by_feature(self, face_feature):
        """根据人脸特征查询id"""
        dis, ids = self.vec_db.search(face_feature, 1)
        if dis[0][0] < 0.9:
            return ids[0][0]
        else:
            return None

    def save_vec_db(self):
        self.vec_db.save()

