# 公共库
import math
import jieba.analyse
import re
import nltk


def dd():
    with open('res/test1.txt','r') as file:
        test1 = file.read()

    with open('res/test2.txt','r') as file:
        test2 = file.read()

    # 过滤停用词
    with open('res/stop_words.txt','r',encoding='utf-8') as file:
        stop_words = file.read()

    stop_word = re.compile('[a-zA-Z0-9]+')  # 过滤掉纯数字和字母传

    txt1 = jieba.cut(test1)

    #过滤停用词
    counts = []
    for i in txt1:
        _bool = stop_word.match(i)
        if i not in stop_words and not _bool:
            counts.append(i)

    print(counts)

def ddf():
    gg='xxx'
    tet = r'%s%s'%(gg,gg)
    print(tet)
ddf()


# xml中只出现一次的设备的操作记录，并生成操作次数统计报告
class action_count:
    def __init__(self):
        self.name = 'user_action_report'
        self.path = new_folder('res/%s' % self.name)  # 创建数据文件夹,并返回path

        self.useful_key = ['client_version','action_type','uid','device_id','created_at']  # 简版字段

        self.mini_list = []  # 转换数据，获取想要的字段

    # 传入要求，来判断用户登录的天数，返回符合条件的用户列表
    def get_list(self,mark_value,work_type='is'):
        # 生成用于统计的列表
        use_list = []
        for i in self.mini_list:
            useer_id = str(i[3])  # 获取用户ID
            date = str(datetime.strptime(i[1],"%Y-%m-%d %H:%M:%S").date())  # 获取操作日期

            _i = (useer_id,date)
            use_list.append(_i)  # 添加记录

        # 去重，使得每个ID一天只有一条记录
        use_list = list(set(use_list))
        print('去重成，剩余条数：%s' % len(use_list))

        # 给每个设备计数，统计每个设备ID登录了多少天
        login_times = {}
        for i in use_list:
            if i[0] in login_times:
                login_times[i[0]] += 1
            else:
                login_times[i[0]] = 1
        print('计数成功，统计条数:%s' % len(login_times))

        # 筛选出数量和传入数值符合的内容，元素是带有key和数字的元组
        useful_list = []
        if work_type == 'up':  # 筛选大于标准值的内容
            for key,value in login_times.items():
                if value > mark_value:
                    _tuple = (key,value)
                    useful_list.append(_tuple)  # 添加元组，为了之后可以做一个相关的统计文档
        elif work_type == 'down':  # 筛选小于标准值的内容
            for key,value in login_times.items():
                if value <= mark_value:
                    _tuple = (key,value)
                    useful_list.append(_tuple)
        else:  # 等于标准值
            for key,value in login_times.items():
                if value == mark_value:
                    _tuple = (key,value)
                    useful_list.append(_tuple)
        print('生成列表，数据条数：%s' % len(useful_list))
        # 输入号码和数量
        return useful_list

    # 根据device_id，每个device_id生成一个文件
    def get_list_by_device_id(self):
        print('开始生成device_id文件')
        site_field = self.useful_key.index('device_id')  # device_id 的位置

        # 获取所有UID
        uid_list = []
        for i in self.mini_list:
            _uid = str(i[site_field])  # 获取用户ID
            _date = str(datetime.strptime(i[3],"%Y-%m-%d %H:%M:%S").date())  # 获取操作日期

            _i = (_uid,_date)
            uid_list.append(_i)  # 添加记录

        # 去重，使得每个device_id一天只有一条记录
        uid_list = list(set(uid_list))  # 去重
        print('本月独立设备登录天/次：%s' % len(uid_list))

        # 给每个设备计数，统计每个设备ID登录了多少天
        login_times = {}
        for i in uid_list:
            if i[0] in login_times:
                login_times[i[0]] += 1
            else:
                login_times[i[0]] = 1
        print('本月独立设备:%s' % len(login_times))

        uid_path = new_folder('%s/%s' % (self.path,'device_id'))  # 新建文件夹

        # 根据login_times，生成文件夹，并根据uid生成独立文件夹
        for _k,_v in login_times.items():
            # 建立文件，保存内容
            with open('%s/%02d_%s.txt' % (uid_path,int(_v),_k),'w',encoding='utf-8') as file:

                # 遍历数据表，符合条件，则添加到_one_list
                for i_mini in self.mini_list:
                    if _k == i_mini[site_field]:
                        action_time = i_mini[3]  # 提取用户时间
                        action_cn = action_to_cn(i_mini[0])  # 在这里做中文翻译

                        file.write('%s\t%s\r' % (action_time,action_cn))  # 写入数据
                # print('单个用户的所有操作%s'%_one_list)

    # 根据列表，获得对应的数据，并根据对应的的值做分类
    def extract_data(self,todo_list):
        # 遍历设备ID列表，并统计每个设备id的动作
        for i_list in todo_list:
            # 用于保存一个用户的所有操作
            _one_list = []
            for i_mini in self.mini_list:
                # print(i_list,i_mini[3])
                if i_list[0] == i_mini[3]:
                    _tuple = (i_mini[1],i_mini[2])  # 生成一个元组，元组中的0：时间，1：动作
                    _one_list.append(_tuple)  # 添加一个元组
            # print('单个用户的所有操作%s'%_one_list)

            # 建立文件，保存内容
            with open('%s/%03d_%s.txt' % (self.path,i_list[1],i_list[0]),'w',encoding='utf-8') as file:
                for i in _one_list:
                    action_time = i[0]  # 提取用户时间
                    action_cn = action_to_cn(i[1])  # 在这里做中文翻译

                    file.write('%s\t%s\r' % (action_time,action_cn))  # 写入数据

    # 设置要处理数据的方式，最终返回数据
    def make_file(self):
        # 生成mini文件，并获得此列表
        self.mini_list = get_mini(self.name,self.useful_key)
        print('获取列表成功，条数:%s' % len(self.mini_list))

        # self.get_list_by_device_id()  # 按设备生成用户列表

        self.get_list_by_uid()  # 按UID生成用户列表
