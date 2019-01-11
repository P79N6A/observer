# coding=utf-8

# 公共库
import os  # 转换内容 ，并提取数据
from datetime import datetime
from bs4 import BeautifulSoup as bs
import time
from datetime import datetime

# 私有库
from tm51.tool import get_value , get_id , new_folder , out_com , only_one , change_action


# 判断最近50个发日记的人的名单
def dd(self):
    _list = bs(self.text , 'lxml').find_all('row')

    # 排出内容人员的用户名
    _v = [ ]
    for i in com_name:
        _v.append(str(i[ 0 ]))

    # 排出内容人员
    value = [ ]
    for i in _list:
        if i.find_all('field')[ 1 ].text not in _v:
            _g = {'帖子id':i.find_all('field')[ 0 ].text , '用户ID':i.find_all('field')[ 1 ].text}
            value.append(i.find_all('field')[ 1 ].text)

    print('一共有 %d 个用户，用户ID为：%s' % (len(value) , value))


# 查看没有发帖的用户在做什么，保存到了res文件夹
def action():
    # 创建文件夹
    file_50 = Tool().new_flie(50)
    file_100 = Tool().new_flie(100)
    file_1000 = Tool().new_flie(1000)

    _v_forum_thread = get_value().forum_thread  # 今天发帖的记录
    _uid_forum_thread = Tool().get_uid(_v_forum_thread)  # 今天发帖用户的ID列表
    print('发帖人数：%d' % len(_uid_forum_thread))

    _uid_forum_thread = Tool().out_com(_uid_forum_thread)  # 排出自己人
    print('排出自己人后，发帖人数：%d' % len(_uid_forum_thread))

    # 今天操作用户的ID列表
    _v_user_action_report = get_value().user_action_report  # 今天操作记录
    _uid_user_action_report = Tool().get_uid(_v_user_action_report)  # 今天操作的用户列表
    print('活跃人数：%d' % len(_uid_user_action_report))

    _uid_user_action_report = Tool().out_com(_uid_user_action_report)  # 排出自己人
    print('排出自己人后，发帖人数：%d' % len(_uid_user_action_report))

    # 将今日发帖的用户从操作的用户中去除
    _out_list = [ ]
    for i in _uid_user_action_report:
        if i not in _uid_forum_thread:
            _out_list.append(i)

    # 提取用户在操作中的记录
    for _uid in _out_list:  # 逐个处理列表中的数据
        # 用于保存一个用户到所有操作
        _list = [ ]

        # 从操作列表中提取对用用户ID的行动
        for j in _v_user_action_report:

            if _uid == j[ 'uid' ]:  # 如果在操作记录中找到这个人到ID
                # 用于保存一条操作：时间和操作
                _v = [ ]

                # 时间
                _v.append(datetime.strptime(j[ 'created_at' ] , "%Y-%m-%d %H:%M:%S").time())

                # 动作
                if j[ 'action_type' ] in actin_list:
                    _v.append(actin_list[ j[ 'action_type' ] ])

                # 去重
                if _v not in _list:
                    _list.append(_v)

        # 根据用户操作到次数，分文件夹保存数据
        if len(_list) <= 50:
            # 创建文件
            _save = open('%s/%s.txt' % (file_50 , _uid) , 'w+' , encoding='utf-8')
            for i in _list:
                for j in range(len(i)):
                    _save.write(str(i[ j ]))
                    _save.write(' ')
                _save.write('\r\n')
            _save.close()
        elif len(_list) > 50 and len(_list) <= 100:
            # 创建文件
            _save = open('%s/%s.txt' % (file_100 , i) , 'w+' , encoding='utf-8')
            for i in _list:
                for j in range(len(i)):
                    _save.write(str(i[ j ]))
                    _save.write(' ')
                _save.write('\r\n')
            _save.close()
        else:
            # 创建文件
            _save = open('%s/%s.txt' % (file_1000 , i) , 'w+' , encoding='utf-8')
            for i in _list:
                for j in range(len(i)):
                    _save.write(str(i[ j ]))
                    _save.write(' ')
                _save.write('\r\n')
            _save.close()

        # 在这里做一个统计，用户进行了多少次操作
        print(str(_uid) + ',' + str(len(_list)) + '\n')
        # break

    print('50条操作的用户有：' + str(len(os.listdir(file_50))))
    print('100条操作的用户有：' + str(len(os.listdir(file_100))))
    print('50条操作的用户有：' + str(len(os.listdir(file_1000))))


# 传入文件名，得出用户的记录条数
def numbers(Path):
    file_path = './res/' + str(Path)  # 文件路径
    file_name = './res/file_' + str(Path)  # 文件名

    _file_list = os.listdir(file_path)  # 文件名列表

    # 所有操作进行计数
    _file_time = {}
    for i in _file_list:
        _file = open(file_path + '/' + i , 'r' , encoding='utf-8')
        _list = _file.readlines()

        for j in _list:
            _d = j.split(" ")
            if _d[ 1 ] not in _file_time:
                _file_time[ _d[ 1 ] ] = 1
            else:
                _file_time[ _d[ 1 ] ] += 1

        _file.close()

    # 打印数据
    _end = open(file_name + '.txt' , 'w' , encoding='utf-8')

    # 操作记录的总条数
    _times = 0

    _list_50 = [ ]
    for i in _file_time:
        # 计算总数
        _times += _file_time[ i ]

        # 写入到文件中
        _end.write(str(i) + ',' + str(_file_time[ i ]))
        _end.write('\r\n')

    _end.write('一共有：%s 个用户记录，总共有 %s 条操作记录' % (len(_file_list) , _times))

    _end.close()


# 近7天，只来过一次的用户的名单
class DaysLostUser:
    def __init__(self):
        self.path = 'res/action'  # 创建数据文件夹,并返回path

        self.data = []  # 获取用户操作记录的数据

        self.mini_list = []  # 获取想要的字段

        self.class_list = [ 20 , 50 , 100 , 150 ]  # 根据操作次数分文件夹保存

    # 显示只登录一天的用户设备ID
    @property
    def _get_user_list(self):
        clean_list = [ ]
        for i in self.mini_list:  # 获取只有date的部分,删除操作记录
            _i_list_date = {}
            _i_list_date[ 'created_at' ] = datetime.strptime(i[ 'created_at' ] , "%Y-%m-%d %H:%M:%S").date()
            _i_list_date[ 'device_id' ] = i[ 'device_id' ]
            clean_list.append(_i_list_date)

        clean_list = only_one(clean_list , False)  # 去重
        # print('_list_date：%s' % clean_list[ 0 ])

        _times = {}  # 给每个设备计数
        for i in clean_list:
            if i[ 'device_id' ] not in _times:
                _times[ i[ 'device_id' ] ] = 1
            else:
                _times[ i[ 'device_id' ] ] += 1
        print('设备计数:完成，数据条数：%s' % len(_times))

        _list = [ ]  # 只登录一天的用户设备ID
        for i in _times:  # 如果数字为1，则记录下来
            if _times[ i ] == 1:
                _list.append(i)
        print('获取只登录一天的设备信息：完成，数据条数：%s' % len(_list))
        # print('_list_1：%s' % _list[ 0 ])

        return _list

    # 将数据分类放入不同的文件夹
    def _classify(self , list , userId):
        for j in self.class_list: #遍历判断是否符合条件
            if len(list) < j:
                _paht = new_folder('%s/%s' % (self.path , str(j)))

                with open('%s/%s.txt' % (_paht , userId) , 'w' , encoding='utf-8') as _save:
                    for i in list:
                        _save.write(str(datetime.strptime(i[ 'created_at' ] , "%Y-%m-%d %H:%M:%S").time()))
                        _save.write(' ')
                        _save.write(i[ 'action_type' ])
                        _save.write('\r\n')

                print(userId,len(list))
                return  #不加这个就会不停判断

    def make_file(self):
        self.path = new_folder('res/action')  # 创建数据文件夹,并返回path

        self.data = get_value('user_action_report')  # 获取用户操作记录的数据

        self.mini_list = get_id(self.data , [ 'device_id' , 'action_type' , 'created_at' ])  # 获取想要的字段

        user_list = self._get_user_list  # 返回设备ID列表

        # 提取数据
        for i in user_list:
            # 用于保存一个用户到所有操作
            _one_list = [ ]
            for j in self.mini_list:
                if i == j[ 'device_id' ]:
                    _one_list.append(dict(created_at=j[ 'created_at' ] , action_type=j[ 'action_type' ]))

            # 转换为可以看懂的中文
            _one_list = change_action(_one_list)

            # 根据用户操作到次数，分文件夹保存数据
            self._classify(_one_list , i)

    # 统计不同的操作的数量
    def total_action(self):
        for num in self.class_list:
            _file_path = '%s/%s'%(self.path , str(num))  # 文件夹路径
            # print(_file_path)

            _file_list = os.listdir(_file_path)  # 文件名列表
            # print(_file_list)

            print('设备数：%s' % len(_file_list))

            _file_times = {}  # 所有操作进行计数
            _times = 0  # 总操作次数

            for i in _file_list:  # 遍历文件表
                with open('%s/%s' % (_file_path , i) , 'r' , encoding='utf-8') as _file:
                    _list = _file.readlines()

                    for j in _list:
                        _d = j.split(" ")
                        print(_d)
                        if _d[ 1 ] not in _file_times:
                            _file_times[ _d[ 1 ] ] = 1
                            _times +=1
                        else:
                            _file_times[ _d[ 1 ] ] += 1
                            _times += 1
            print('总操作次数:%s'%_times)

            _top3_action = [ ]  # 操作最多前三名。0：操作名次，1：操作次数，2：占百分比

            #排序获取数据
            top3_list=sorted(_file_times.items(),key=lambda items:items[1],reverse=True)[:8]
            print(top3_list)
            for i in top3_list:
                _top3_action.append([str(i[0]),str(i[1])])
            print(_top3_action)

            # 打印数据
            with open('%s/%s.txt' % (self.path , num) , 'w' , encoding='utf-8') as save_file:
                save_file.write('统计独立设备数：%s，总操作次数：%s。人平均操作次数：%s\r\n'%(len(_file_list),_times,_times/len(_file_list)))
                save_file.write('操作最多前三名：\r\n' )
                for i in _top3_action:
                    save_file.write('%s %s次 %.2f%%\r\n' % (i[0].replace('\n', ''),i[1],int(i[1])/_times*100))

                save_file.write('############################################\r\n')

                #单条数据
                for num in sorted(_file_times.items(),key=lambda items:items[1],reverse=True):
                    save_file.write('%s %s %.2f%%\r\n' % (num[0].replace('\n', '') , num[1] , num[1]/_times*100))

if __name__ == '__main__':
    # DaysLostUser().make_file()
    DaysLostUser().total_action()