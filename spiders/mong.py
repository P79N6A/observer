import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient["runoobdb"]
mycol = mydb["sites"]

mydict = [{"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}]

# x = mycol.insert_many(mydict)
n = {"name": "RUNOOB1"}
newvalues = {"$unset": {"alexa": '0002300'}}
y = mycol.update_one(n, newvalues)
# print(x)
print(y)

# 在活动详情中，可以添加的内容包括：
# 封面地址、标题、发起人ID、参加的用户ID名单、演出时间、演出地点、演出票价、
# 照片¥视频、导演介绍&访谈、故事&编剧、演员相关、周边新闻、口碑剧评
# 演出标签、用于分析的关键词标签
