# coding=utf-8

# 公共库
import os  # 转换内容 ，并提取数据
from datetime import datetime
from bs4 import BeautifulSoup as bs
import time
from datetime import datetime

# 私有库
from tm51.tool import get_mini, new_folder, out_com, only_one, change_action

class_list = [20, 50, 100, 150]  # 根据操作次数分文件夹保存
tops_num = 8  # 设置显示前几名的内容
_split_ = '\t'  # 统计报告的分隔符号


# xml中只出现一次的设备的操作记录，并生成操作次数统计报告
class action_count:
    def __init__(self):
        self.path = new_folder('res/action')  # 创建数据文件夹,并返回path

        self.useful_key = ['device_id', 'created_at', 'action_type']  # 设置需要获取的字段

        self.mini_list = []  # 转换数据，获取想要的字段

    # 提取只登录一天的用户设备ID
    @property
    def _only_1day_user_list(self):
        clean_list = []  # 提取时间中的日期和设备ID
        for i in self.mini_list:
            _created_at = datetime.strptime(i[self.useful_key.index('created_at')], "%Y-%m-%d %H:%M:%S").date()
            _device_id = i[self.useful_key.index('device_id')]

            _i = (_device_id, _created_at)  # 做成元组，可以快速去重
            clean_list.append(i)

        _clean_list = list(set(clean_list))  # 去重，使得每个设备ID一天只有一条记录
        print('去重结束，单设备登录天次%s' % len(_clean_list))

        # 给每个设备计数，统计每个设备ID登录了多少天
        machine_list = {}
        for i in _clean_list:
            if i[0] not in machine_list:
                machine_list[i[0]] = 1
            else:
                machine_list[i[0]] += 1
        print('设备数:%s' % len(machine_list))

        # 只登录一天的用户设备ID
        day_machine_list = []
        for i in machine_list:  # 如果数字为1，则记录下来
            if machine_list[i] == 1:
                day_machine_list.append(i)
        print('获取只登录一天的设备信息：完成，数据条数：%s' % len(day_machine_list))

        # 返回设备ID的列表
        return day_machine_list

    # 根据用户列表做单独处理，然后调用分类
    def user_to_list(self, list):

        # 遍历设备ID列表，并统计每个设备id的动作
        for i_list in list:

            # 用于保存一个用户的所有操作
            _one_list = []
            for i_mini in self.mini_list:
                if i_list == i_mini[0]:
                    _tuple = (i_mini[1], i_mini[2])  # 生成一个元组，元组中的0：时间，1：动作
                    _one_list.append(_tuple)  # 添加一个元组

            # 根据用户操作的次数，分文件夹保存数据，_one_list：动作列表，i_list：设备名字
            for j in class_list:  # 遍历分段的数值判断是否符合条件
                if len(_one_list) < j:
                    _paht = new_folder('%s/%s' % (self.path, str(j)))

                    with open('%s/%s.txt' % (_paht, i_list), 'w', encoding='utf-8') as _save:
                        for i in _one_list:
                            _save.write('%s\t%s\r' % (i[0], i[1]))

                    print(i_list, len(_one_list))
                    return  # 不加这个就会不停判断，导致重复放入不同的文件夹

    # 可以单独执行，调整列表中的数据
    def _clean_list(self):
        pass

    # 设置要处理数据的方式，最终返回数据
    def main(self):
        self.mini_list = get_mini('user_action_report', self.useful_key)  # 生成mini文件，并获得此列表
        print('获取列表成功，条数:%s' % len(self.mini_list))

        translation = change_action(self.mini_list, self.useful_key)  # 将操作代码翻译成中文，并获取译文
        print('翻译完成，条数:%s' % len(translation))

        only_1day_user_list = self._only_1day_user_list  # 对列表进行单独处理，获取只登录了一天的用户设备ID列表

        self.user_to_list(only_1day_user_list)  # 根据用户列表做单独处理，然后调用分类


# 统计不同操作数区间的用户，他们各种操作占有的比例
def create_report():
    total_dict = {}  # 数据报告列表
    txt_dict = {}  # 迷你报告内容

    # 提取操作记录次数到class_list，不同的区间被依次添加到数组
    for i_class_list in class_list:
        txt_dict[i_class_list] = {}
        file_path = 'res/action/%s' % str(i_class_list)  # 文件夹路径
        # print(file_path)

        file_list = os.listdir(file_path)  # 获取文件名列表
        print('%s文件夹数量：%s' % (i_class_list, len(file_list)))

        file_times = {}  # 所有操作进行计数
        times_total = 0  # 总操作次数

        # 统计文件夹中所有文件中的操作数量
        for i_file_list in file_list:  # 遍历文件表
            with open('%s/%s' % (file_path, i_file_list), 'r', encoding='utf-8') as _file:
                _list = _file.readlines()

                for i_list in _list:
                    _i_list = i_list.replace('\n', '').split("\t\t")
                    print(_i_list)
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
        txt_dict[i_class_list]['统计独立设备数'] = len(file_list)
        txt_dict[i_class_list]['总操作次数'] = times_total
        txt_dict[i_class_list]['人平均操作次数'] = times_total / len(file_list)

        # 将内容汇总到一个字典中
        total_dict[i_class_list] = file_times

    print('显示%s' % total_dict)
    print('显示%s' % txt_dict)

    # 操作列表
    total_list = []
    for i in total_dict.values():
        for _i in i:
            if _i not in total_list:
                total_list.append(_i)
    total_dict['汇总'] = {}
    # 向汇总表中填充列表
    for i in total_list:
        total_dict['汇总'][i] = [0, 0, 0, 0]

    for i in range(len(class_list)):
        for _total_list in total_list:
            if _total_list in total_dict[class_list[i]]:
                total_dict['汇总'][_total_list][i] = total_dict[class_list[i]][_total_list]

    # print('dd%s' % total_dict[ '汇总' ])

    # 生成文件
    with open('res/action/statistics_report.txt', 'w', encoding='utf-8') as save_file:

        # 添加表头
        save_file.write('类型/数量')
        for i in class_list:
            save_file.write('\t%s次' % i)
        save_file.write('\r\n')

        for key, value in total_dict['汇总'].items():
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
        for key, value in total_dict['汇总'].items():
            save_file.write(key)

            for i in range(len(value)):
                _total = txt_dict[class_list[i]]['总操作次数']  # 总数

                save_file.write('\t')
                save_file.write('%.2f%%' % (int(value[i]) / int(_total) * 100))

            save_file.write('\r\n')

    # 生成文件
    with open('res/action/mini_report.txt', 'w', encoding='utf-8') as save_file:
        for key, value in txt_dict.items():
            save_file.write('操作在%s以下的用户操作数据:' % key)
            for i, j in value.items():
                save_file.write('\r\n%s:%0.1f' % (i, j))
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
            with open('%s/%s' % (file_path, i_file_times), 'r', encoding='utf-8') as _file:
                _list = _file.readlines()

                file_times = {}  # 所有操作进行计数
                times_total = 0  # 总操作次数

                for i_list in _list:
                    _i_list = i_list.replace('\n', '').split("\t\t")

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

    plt.scatter(x_list, y_list, s=10, alpha=0.5)  # 折线 1 x 2 y 3 color
    # plt.plot(x , y , 'g' , lw=10)  # 4 line w
    # # 折线 饼状 柱状
    # x = np.array([ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ])
    # y = np.array([ 13 , 25 , 17 , 36 , 21 , 16 , 10 , 15 ])
    # plt.bar(x , y , 0.2 , alpha=1 , color='b')  # 5 color 4 透明度 3 0.9
    plt.show()

    print(x_list)
    print(y_list)


if __name__ == '__main__':
    a = action_count()
    a.main()  # 生成数据

    # create_report()  # 生成统计报告

    # key = '帖子详情'
    # trend_key(key)
