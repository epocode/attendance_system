from src.db.database import DataBase
from src.db.vec_db import VecDB
import numpy as np

class StudentDAO:
    def __init__(self, db:DataBase):
        self.db = db
        self.vec_db = VecDB()

    def get_student_num(self):
        query = 'SELECT COUNT(*) FROM student;'
        res = self.db.fetchall(query)
        return res[0][0]
    
    def get_student_info(self):
        query = 'SELECT id, name, gender, age FROM student;'
        res = self.db.fetchall(query)
        return res
    
    def add_student(self, face_feature, name, gender, age):
        dis, ids = self.vec_db.search(face_feature, 1)
        if dis[0][0] > 0.9:
            print('当前人脸已经录入')
            return
        query = 'INSERT INTO student (name, gender, age) VALUES (%s, %s, %s);'
        params = (name, gender, age)  
        last_id = self.db.execute_with_lastid(query, params)  
        if last_id != 0:
            self.vec_db.add_with_ids(face_feature, np.array([last_id]))

    def save_vec_db(self):
        self.vec_db.save()