from config import my_config
import faiss
import os

class VecDB:
    def __init__(self):

        #创建或者读取该表对应的向量数据库
        self.vec_db = faiss.IndexIDMap(faiss.IndexFlatIP(my_config.VEC_FEATURE_LEN))
        vec_db_path = os.path.join(my_config.VEC_DB_PATH, 'vecdb' + '.faiss')


        if os.path.exists(vec_db_path):
            try:
                self.vec_db = faiss.read_index(vec_db_path)
                print('索引中的向量数目为：', self.vec_db.ntotal)

            except Exception as e:
                print(e)
        else:
            print('数据库不存在，创建新的数据库')
    


    def search(self, feature, k):
        return self.vec_db.search(feature, k)
    
    def add_with_ids(self, features, ids):
        self.vec_db.add_with_ids(features, ids)
    
    def save(self):
        try:
            faiss.write_index(self.vec_db, os.path.join(my_config.VEC_DB_PATH, 'vecdb' + '.faiss'))
            print('保存成功')
        except Exception as e:
            print('保存失败')

    def delete(self, id):
        self.vec_db.remove_ids(id)
        
