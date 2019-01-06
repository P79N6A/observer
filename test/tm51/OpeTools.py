# 预期日活模型


# 通过增加每日新增用户，预测40天日活用户数
# 可以通过数据库中的统计，获得真实的近30日每日留存，作为参照值，来算出更加贴合实际的30日预测
# 可以生成视图
import pandas as pd
import datetime

def Day_live():
    # 基础用户，不用新增就得到的
    jichu = 375

    # 基础新增用户
    xinzeng = 27

    # 新用户流程
    D = [100, 33.2292857142857, 23.7835714285714, 20.5335714285714, 15.7907142857143, 13.1621428571429,
         11.0485714285714, 13.7942857142857, 10]

    # 日新增用户
    KPI = 150

    for i in range(40):
        if i > 7:
            jichu += KPI * D[8] / 100
        else:
            # 日活跃
            jichu += KPI * D[i] / 100

        # 显示
        print('第', i + 1, '天日活跃用户数：', int(jichu))

    print(40 * 150)

    pass


def clean(action_log):
    _clean = []

    for i in action_log:
        _info = {}
        _info['用户ID'] = i[5]
        _info['设备ID'] = i[6]
        _info['IP'] = i[8]
        _info['日期'] = i[9].split()[0]

        # 去重
        if _info not in _clean:
            _clean.append(_info)
        print(len(_clean))

    list_to_csv(_clean, 'clean.csv')


# fenxi
def Day_data(_clean):
    _data = {}
    for i in range(len(_clean)):
        _info = _clean.loc[i]

        #如果没有此日期 就创建一个
        if _info['日期'] not in _data:
            _data[_info['日期']] = {'注册用户ID': [], '注册用户数': 0, '游客数': 0, '设备ID': [], '设备数': 0, 'IP': [], 'IP数': 0,
                                  '留存': []}
        #如果用户ID是零，说明是游客，如果不是，并且不在集合中，则添加。有可能是用户换了设备登入，但但账号是同一个
        if _info['用户ID'] == 0:
            _data[_info['日期']]['游客数'] += 1
        elif _info['用户ID'] not in _data[_info['日期']]['注册用户ID']:
            _data[_info['日期']]['注册用户ID'].append(_info['用户ID'])
            _data[_info['日期']]['注册用户数'] += 1

        if _info['设备ID'] not in _data[_info['日期']]['设备ID']:
            _data[_info['日期']]['设备ID'].append(_info['设备ID'])
            _data[_info['日期']]['设备数'] += 1

        if _info['IP'] not in _data[_info['日期']]['IP']:
            _data[_info['日期']]['IP'].append(_info['IP'])
            _data[_info['日期']]['IP数'] += 1

    list_to_csv(_data,'Day_data.csv')


# 生成csv
def list_to_csv(Data, Name):
    # 读取列表内容
    _data = pd.DataFrame(Data)
    _data.head()

    # 保存csv
    _data.to_csv(Name, index=True, header=True, encoding='UTF-8')

    # print('显示列表', _data, '\n', _data.values)


def test(_Day_data,user):
    #定义一个显示留存的集合嵌套集合
    aa = {}
    for i in _Day_data.head():
        if i == 'Unnamed: 0':
           continue

        aa[i]={}
        for n in range(31):
            aa[i][n]=0


    #遍历所有日期
    for i in aa:
        #注册用户id集合
        info_ID =_Day_data.loc[2,i]

        #将时间戳变成时间
        info_day =datetime.datetime.strptime(i, '%Y-%m-%d')

        # print(info_ID,info_day)

        #遍历所有用户
        for j in range(len(user.values)):

            if str(user.loc[j]["id"]) in info_ID:

                #用户注册时间
                ge = user.loc[j]["created_at"].split(' ', 1)[0]
                user_data = datetime.datetime.strptime(ge, '%Y-%m-%d')

                be =int((info_day-user_data).days)



                aa[ge][be] += 1
            print(aa)




if __name__ == '__main__':
    user = pd.DataFrame(pd.read_csv('uesr.csv', header=0, encoding='UTF-8'))
    # action_log = pd.DataFrame(pd.read_csv('action_log.csv', header=0, encoding='UTF-8')).values
    clean = pd.DataFrame(pd.read_csv('clean.csv', header=0, encoding='UTF-8'))
    Day_data = pd.DataFrame(pd.read_csv('Day_data.csv',header=0, encoding='UTF-8'))
    # 洗掉无用的数据，并去重
    _clean = test(Day_data,user)
