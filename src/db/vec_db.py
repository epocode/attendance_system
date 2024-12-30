from config import my_config
import faiss
import os

class VecDB:
    def __init__(self, teacher_username, class_name):
        self.teacher_username = teacher_username
        self.class_name = class_name

        #创建或者读取该表对应的向量数据库
        self.vec_db = faiss.IndexIDMap(faiss.IndexFlatIP(my_config.VEC_FEATURE_LEN))
        vec_db_path = os.path.join(my_config.VEC_DB_PATH, self.teacher_username + '_' +
                                   self.class_name + '.faiss')


        if os.path.exists(vec_db_path):
            try:
                self.vec_db = faiss.read_index(vec_db_path)
                print('索引中的向量数目为：', self.vec_db.ntotal)

            except Exception as e:
                print(e)


    