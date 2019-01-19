# coding=utf-8

# 公共库
import os  # 转换内容 ，并提取数据
from datetime import datetime

# 私有库
from tm51.tool import get_mini,new_folder,action_to_cn,make_pie,dde

class_list = [20,50,100,150]  # 根据操作次数分文件夹保存
tops_num = 8  # 设置显示前几名的内容
_split_ = '\t'  # 统计报告的分隔符号
path = 'res/user_action_report'


# xml中只出现一次的设备的操作记录，并生成操作次数统计报告
class action_count:
    def __init__(self):
        self.name = 'user_action_report'
        self.path = new_folder('res/%s' % self.name)  # 创建数据文件夹,并返回path

        # self.useful_key = ['from_client','client_version','app_version','action_type','uid','device_id','info','remote_ip','created_at']  # 全字段
        self.useful_key = ['action_type','uid','device_id','created_at']  # 简版字段

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

    # 提取uid，并生成每个uid的操作记录列表
    def get_list_by_uid(self):
        print('开始生成uid文件')
        site_field = self.useful_key.index('uid')

        # 获取所有UID
        uid_list = []
        for i in self.mini_list:
            if i[site_field] == '0':  # 去掉游客0
                continue

            _uid = str(i[site_field])  # 获取用户ID
            _date = str(datetime.strptime(i[3],"%Y-%m-%d %H:%M:%S").date())  # 获取操作日期

            _i = (_uid,_date)
            uid_list.append(_i)  # 添加记录

        # 去重，使得每个ID一天只有一条记录
        uid_list = list(set(uid_list))
        print('本月独立用户登录天/次：%s' % len(uid_list))

        # 给每个设备计数，统计每个设备ID登录了多少天
        login_times = {}
        for i in uid_list:
            if i[0] in login_times:
                login_times[i[0]] += 1
            else:
                login_times[i[0]] = 1
        print('本月独立用户:%s' % len(login_times))

        uid_path = new_folder('%s/%s' % (self.path,'uid'))  # 新建文件夹

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

    # 获取device_id列表
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

        self.get_list_by_device_id()  # 按设备生成用户列表

        self.get_list_by_uid()  # 按UID生成用户列表

        # 整理整个月只登录过一天的用户数据，生成报告，并保存在action文件夹中
        # only_1day_user_list = self._only_1day_user_list  # 对列表进行单独处理，获取只登录了一天的用户设备ID列表
        # self.user_to_list(only_1day_user_list)  # 根据用户列表做单独处理，并把action翻译陈中文，并保存

        # 整理整个月登录超过X天的用户数据，生成报告，并保存在action_day_x文件夹中
        #
        # useful_list = self.get_list(days,type)  # 获得需要的列表
        # print(useful_list)
        # self.extract_data(useful_list)  # 根据列表，搜索对应的数据


# 统计不同操作数区间的用户，他们各种操作占有的比例
def create_report():
    total_dict = {}  # 数据报告列表
    txt_dict = {}  # 迷你报告内容

    # 扫描文件夹，提取其中的文件夹
    file_list = os.listdir(path)  # 获取文件夹的所有文件和目录
    for i in file_list:
        if os.path.isdir('%s/%s' % (path,i)):  # 如果是一个文件夹，则扫描
            txt_dict[i] = {}  # 建立一个元素
            # print(file_path)

            file_list = os.listdir('%s/%s' % (path,i))  # 获取文件名列表
            print('%s文件夹数量：%s' % (i,len(file_list)))

            file_times = {}  # 所有操作进行计数
            times_total = 0  # 总操作次数

            # 统计文件夹中所有文件中的操作数量
            for i_file_list in file_list:  # 遍历文件表
                with open('%s/%s' % ('%s/%s' % (path,i),i_file_list),'r',encoding='utf-8') as _file:
                    _list = _file.readlines()

                    for i_list in _list:
                        _i_list = i_list.replace('\n','').split("\t")
                        # print(_i_list)
                        # 如果在字典中，就+1，不在则=1
                        if _i_list[1] not in file_times:
                            file_times[_i_list[1]] = 1
                            times_total += 1
                        else:
                            file_times[_i_list[1]] += 1
                            times_total += 1
                    # break
            print('总操作次数:%s\n' % times_total)

            # 将统计内容添加到数组
            txt_dict[i]['统计独立设备数'] = len(file_list)
            txt_dict[i]['总操作次数'] = times_total
            txt_dict[i]['人平均操作次数'] = times_total / len(file_list)

            # 将内容汇总到一个字典中
            total_dict[i] = file_times

        else:
            print('%s不是文件夹\n' % i)

    # 填充表头，保证每个不同的表中包含的所有表头都添加进去
    total_list = []
    for i in total_dict.values():
        for _i in i:
            if _i not in total_list:
                total_list.append(_i)

    # 直接在表中原表中加入汇总，这样就不用单独用一个数了
    total_total_dict = {}
    # 向汇总表中填充空列表，用于占位置
    for i in total_list:
        total_total_dict[i] = [0,0,0,0]

    # 向汇总的列表total_total_dict中，填充已有的数量
    for key,value in total_dict.items():  # 遍历total_dict中的每种分组：20、50、100、1000
        site_num = class_list.index(int(key))  # 当前分组所在的位置

        # print('site_num' , key , site_num)
        for _i in value:  # 遍历分组中的所有操作记录
            total_total_dict[_i][site_num] = value[_i]  # 赋值

    # print('total_dict:\n%s\n' % total_dict)
    # print('txt_dict:\n%s\n' % txt_dict)
    # print('total_total_dict:\n%s\n' % total_total_dict)

    # 生成数据报告文件
    with open('res/action/statistics_report.txt','w',encoding='utf-8') as save_file:

        # 添加表头
        save_file.write('类型/数量')
        for i in class_list:
            save_file.write('\t%s次' % i)
        save_file.write('\r\n')

        # 显示数量
        for key,value in total_total_dict.items():
            save_file.write(key)

            for i_value in value:
                # print(i_value)
                save_file.write('\t')
                save_file.write(str(i_value))

            save_file.write('\r\n')

        save_file.write('\r\n\r\n\r\n############################################\r\n\r\n\r\n')

        # 添加表头
        save_file.write('类型/几率')
        for i in class_list:
            save_file.write('\t%s次' % i)
        save_file.write('\r\n')

        # 按比例显示
        for key,value in total_total_dict.items():
            save_file.write(key)

            a = 0  # 用来标记怎么取值
            for i_value in value:
                if i_value == 0:
                    save_file.write('\t')
                    save_file.write('0')
                    a += 1
                else:
                    r_key = class_list[a]
                    _total = txt_dict[str(r_key)]['总操作次数']  # 总数
                    # print(i_value)
                    save_file.write('\t')
                    save_file.write('%.2f%%' % (i_value / _total * 100))
                    a += 1

            save_file.write('\r\n')

    # 生成迷你报告文件
    with open('res/action/mini_report.txt','w',encoding='utf-8') as save_file:
        for key,value in txt_dict.items():
            save_file.write('操作在%s以下的用户操作数据:' % key)
            for i,j in value.items():
                save_file.write('\r\n%s:%0.1f' % (i,j))
            save_file.write('\r\n\r\n\r\n############################################\r\n\r\n\r\n')


# 提取在所有用户中，随着操作数量的增加，某个属性的变化趋势
def trend_key(key):
    import matplotlib.pyplot as plt

    x_list = []  # x轴
    y_list = []  # y轴

    # 遍历区间数组，统计用户的操作
    for i_class_list in class_list:
        file_path = 'res/action/%s' % str(i_class_list)  # 文件夹路径
        # print(file_path)

        file_list = os.listdir(file_path)  # 获取文件名列表
        print('设备数：%s' % len(file_list))

        # 统计文件夹中所有文件中的操作数量
        for i_file_times in file_list:  # 遍历文件表
            with open('%s/%s' % (file_path,i_file_times),'r',encoding='utf-8') as _file:
                _list = _file.readlines()

                file_times = {}  # 所有操作进行计数
                times_total = 0  # 总操作次数

                for i_list in _list:
                    _i_list = i_list.replace('\n','').split("\t")

                    # 如果在字典中，就+1，不在则=1
                    if _i_list[1] not in file_times:
                        file_times[_i_list[1]] = 1
                        times_total += 1
                    else:
                        file_times[_i_list[1]] += 1
                        times_total += 1

                # print(file_times)
                # 添加数组
                x_list.append(times_total)
                if key in file_times:
                    y_list.append(file_times[key])
                else:
                    y_list.append(0)

    plt.scatter(x_list,y_list,s=10,alpha=0.5)  # 折线 1 x 2 y 3 color
    # plt.plot(x , y , 'g' , lw=10)  # 4 line w
    # # 折线 饼状 柱状
    # x = np.array([ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ])
    # y = np.array([ 13 , 25 , 17 , 36 , 21 , 16 , 10 , 15 ])
    # plt.bar(x , y , 0.2 , alpha=1 , color='b')  # 5 color 4 透明度 3 0.9
    plt.show()

    # print(x_list)
    # print(y_list)


# 不区分日期，统计ID的行为频率
def outside_date():
    file_path = 'res/action'

    if not os.path.exists(file_path):  # 如果没有文件，则结束
        print('找不到文件夹：%s\n' % file_path)
        exit()

    file_list = os.listdir(path)  # 获取文件夹的所有文件和目录
    # print(file_list)

    # 扫描文件夹，将内容中的操作按照时间的方式分类计数，生成列表
    action_list = [{} for i in range(31)]  # 创建一个包含31个字典的list，每天list中是包含各种行为数量的字典
    for i in file_list:  # 遍历文件列表
        if i[0] == '.':
            continue
        with open('%s/%s' % (file_path,i),'r',encoding='UTF-8') as _file:
            _list = _file.readlines()

            for i_list in _list:
                _action = i_list.replace('\n','').split("\t")[1]  # 获取动作
                _day = int(i_list.split(" ")[0].split("-")[2])  # 获取日期
                # print(i_list.split(" "))

                if _action in action_list[_day - 1]:
                    action_list[_day - 1][_action] += 1
                else:
                    action_list[_day - 1][_action] = 1
        # break
    print('扫描文件完成：%s' % len(action_list))

    # 将所有的操作汇集在一个表中
    total = {}
    for i in action_list:
        if i:  # 如果不为空
            for key,value in i.items():
                if key in total:
                    total[key] += value
                else:
                    total[key] = value

    # print(total)

    # 将汇总内容保存下来
    with open('res/dee.txt','w') as file:
        for key,value in total.items():
            file.write('%s\t%s\r' % (key,value))

    # 将每日操作计数，展示出来
    for i in action_list:
        if i:  # 如果不为空
            key_list = []
            value_list = []
            for key,value in i.items():
                key_list.append(key)
                value_list.append(value)

            # make_pie(key_list,value_list)
        break

    #
    dfgd = dde(total,5)
    _dict = list(dfgd.items())  # 排序后的list
    _dict.sort(key=lambda x:x[1],reverse=True)  # 降序排序

    make_pie(_dict)  # shur


# 根据设备登录次数，生成用户报告
def report_for_days_by_device_id(tab):
    if not os.path.exists('%s/%s' % (path,'device_id')):  # 如果文件夹不存在，则新建
        print('文件夹不存在，生成中……')
        action_count().get_list_by_device_id()

    file_list = os.listdir('%s/%s' % (path,'device_id'))  # 获取文件夹的所有文件和目录
    # print(file_list)

    txt_dict = [[0,0,0,0,0],[0,0,0,0,0]]  # 概括报告,第一个为设备数，第二个为次数,[0,0]中,最后一个是总的报告数

    re_list = [{},{},{},{}]  # 生成列表：[{},{},{},{}] #统计用户操作次数
    # 遍历文件列表，根据当天的操作次数，统计每种操作的次数
    for i_file in file_list:
        if int(i_file.split('_')[0]) == 1:  # 提取登录天数，如果等于1 则继续

            txt_dict[0][-1] += 1  # 统计设备+1

            with open('res/user_action_report/device_id/%s' % i_file) as file:
                _list = file.readlines()

                # 遍历每一行内容,根据操作数，统计操作数
                for i in range(len(tab)):  # 遍历区间
                    if len(_list) < tab[i]:  # 如果满足当前的区间,则在对应的区间统计用户的操作次数

                        txt_dict[0][i] += 1  # 对应区间的设备数+1

                        for i_list in _list:
                            _key = i_list.split('\t')[1]  # 获得操作名
                            if _key in re_list[i]:
                                re_list[i][_key] += 1  # 对用区间的操作数 +1

                                txt_dict[1][i] += 1  # 对应区间的总操作 +1
                                txt_dict[1][-1] += 1  # 总设备数+1
                            else:
                                re_list[i][_key] = 1  # 对用区间的操作数 =1

                                txt_dict[1][i] += 1  # 对应区间的总操作 +1
                                txt_dict[1][-1] += 1  # 总操作数+1
                        break

    print('概括报告:%s' % txt_dict)

    # 遍历后，把内容放入数据报告
    total_dict = {}  # 数据报告,根据区间统计每个操作的数量
    for i in range(len(re_list)):  # 获取每个区间的数值

        for _i in re_list[i]:
            if _i in total_dict:  # 如果报告中有此相操作，则把值放到对应位置
                total_dict[_i][i] = re_list[i][_i]
            else:  # 如果报告中没有此类操作，则新建，并把值放到对应位置
                total_dict[_i] = [0,0,0,0]
                total_dict[_i][i] = re_list[i][_i]

    # 为了排序，所以要把字典变成列表，以后单独做
    print('数据报告:%s' % total_dict)

    ################################################################################################################################
    # 保存total_dict数据报告
    with open('%s/%s' % (path,'statistics_report.txt'),'w') as file:
        # 写入表头
        file.write('%s' % '操作类型')
        for i in tab:
            file.write('\t%s次' % i)
        file.write('\r')

        # 写入主体
        for key,value in total_dict.items():
            file.write('%s' % key.replace('\n',''))
            for i in range(len(value)):
                # print(value[i],txt_dict[i][1])
                file.write('\t%.2f%%' % (value[i]/txt_dict[1][i]* 100)) #用百分比显示
            file.write('\r')
    print('生成数据报告')

    # 保存txt_dict概括报告
    with open('%s/%s' % (path,'mini_report.txt'),'w') as file:
        # 写入表头
        file.write('种类')
        for i in tab:
            file.write('\t%s次' % i)
        file.write('\r')

        #写入设备数
        file.write('设备数')
        for i in txt_dict[0]:
            file.write('\t%s' % i)
        file.write('\r')

        #写入操作数
        file.write('操作总数')
        for i in txt_dict[1]:
            file.write('\t%s' % i)
        file.write('\r')

        #写入设备/操作数
        file.write('单设备操作数')
        for i in range(len(txt_dict)):
            file.write('\t%.2f' % (txt_dict[1][i]/txt_dict[0][i]))
        file.write('\r')
    print('生成数据报告')

if __name__ == '__main__':
    # a = action_count()  # 生成初始文档
    # a.make_file()  # 生成文件夹

    # 输入区间，将只上线一天的设备统计并报告
    TAB = [20,50,100,1000]
    report_for_days_by_device_id(TAB)

    # create_report()  # 生成统计报告
    #
    # key = '社区首页'
    # trend_key(key)
    #
    # outside_date()  # 不区分日期，统计ID的行为频率
