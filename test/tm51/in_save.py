# 保存数据

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')



class Dog:

    def __init__(self, name,info):
        self.mydb = myclient["runoobdb"]
        self.mycol = self.mydb[name]
        self.info =info


    def in_save(self):

        print(self.info)
        # self.mycol.insert_one(self.info)

