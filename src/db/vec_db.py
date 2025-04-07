from config import my_config
import faiss
import os
import json

class VecDB:
    def __init__(self):
        # 拿到数据库路径
        vec_db_path = os.path.join(my_config.VEC_DB_PATH, 'vecdb' + '.faiss')
        json_db_path = os.path.join(my_config.VEC_DB_PATH, 'vecdb' + '.json')

        # 初始化JSON对象
        self.json_data = {}

        if os.path.exists(vec_db_path):
            try:
                self.vec_db = faiss.read_index(vec_db_path)
                print('索引中的向量数目为：', self.vec_db.ntotal)

                # 读取JSON文件内容
                if os.path.exists(json_db_path):
                    with open(json_db_path, 'r') as json_file:
                        self.json_data = json.load(json_file)
                        print('JSON数据加载成功')
                else:
                    print('JSON文件不存在，创建新的JSON对象')

            except Exception as e:
                print(e)
        else:
            print('数据库不存在，创建新的数据库')
            self.vec_db = faiss.IndexIDMap(faiss.IndexFlatIP(my_config.VEC_FEATURE_LEN))
            # 创建新的JSON对象
            self.json_data = {}

    def search(self, feature, k):
        return self.vec_db.search(feature, k)
    
    def add_with_ids(self, features, ids):
        try:
            self.vec_db.add_with_ids(features, ids)
            # 更新JSON对象
            for i, id in enumerate(ids):
                self.json_data[str(id)] = features[i].tolist()
            self.save()
        except Exception as e:
            print(f"添加向量失败:{e}")

    def save(self):
        try:
            # 保存FAISS索引
            faiss.write_index(self.vec_db, os.path.join(my_config.VEC_DB_PATH, 'vecdb' + '.faiss'))
            # 保存JSON数据
            json_db_path = os.path.join(my_config.VEC_DB_PATH, 'vecdb' + '.json')
            with open(json_db_path, 'w') as json_file:
                json.dump(self.json_data, json_file)
            print('保存成功')
        except Exception as e:
            print('保存失败')

    def delete(self, id):
        try:
            self.vec_db.remove_ids(id)
            # 从JSON对象中删除对应的ID
            id_str = str(id)
            if id_str in self.json_data:
                del self.json_data[id_str]
            self.save()
        except Exception as e:
            print(f"删除向量失败:{e}")

