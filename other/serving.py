
# 操作数据库
import pymongo


class todo:

    # info 为一个数组，type是字符串"douban"/"damai"
    def __init__(self, info, type):

        self.myclient = pymongo.MongoClient('mongodb://localhost:27017/')

        self.mydb = self.myclient["swarm"]

        self.info = info
        self.type = type

    # 豆瓣数据储存
    def save(self):
        if self.type == 'douban':
            _db_name = 'douban'
        elif self.type == 'damai':
            _db_name = 'damai'
        else:
            print('输入的储存类型无效')

        mycol = self.mydb[_db_name]

        _test = mycol.insert_many(self.info)

        # 测试数据
        print('保存成功！')


# 储存测试,更新时间@1221
if __name__ == '__main__':
    _list = []
    _list.append({"name":"小明","age":20})

    #豆瓣储存测试
    _douban =todo(_list,'douban')
    _douban.save()

    # #大麦储存测试
    # _damai = todo(_list,'damai')
    # _damai.save()




# 在活动详情中，可以添加的内容包括：
# 封面地址、标题、发起人ID、参加的用户ID名单、演出时间、演出地点、演出票价、
# 照片¥视频、导演介绍&访谈、故事&编剧、演员相关、周边新闻、口碑剧评
# 演出标签、用于分析的关键词标签
