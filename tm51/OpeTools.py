# 预期日活模型


# 通过增加每日新增用户，预测40天日活用户数
# 可以通过数据库中的统计，获得真实的近30日每日留存，作为参照值，来算出更加贴合实际的30日预测
# 可以生成视图
import pandas as pd


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

    list_to_csv(_clean,'clean.csv')


# fenxi
def gg(_clean):

    _data = {}
    for _info in range(len(_clean)):
        print(_clean['日期'])
        print(_clean.loc[_info])
        # if _info['日期'] not in _clean:
        #     _data[_info['日期']] = {'注册用户ID': [], '注册用户数': 0, '游客数': 0, '设备ID': [], '设备数': 0, 'IP': [], 'IP数': 0,
        #                            '留存': []}
        #
        # if _info['用户ID'] == 0:
        #     _data[_info['日期']]['游客数'] += 1
        # else:
        #     _data[_info['日期']]['注册用户数'] += 1
        # if _info['用户ID'] not in _clean[_info['日期']]['用户ID']:
        #     _data[_info['日期']]['用户ID'].append(_info['用户ID'])
        #     _data[_info['日期']]['用户数'] += 1
        #
        # if _info['设备ID'] not in _clean[_info['日期']]['设备ID']:
        #     _data[_info['日期']]['设备ID'].append(_info['设备ID'])
        #     _data[_info['日期']]['设备数'] += 1
        #
        # if _info['IP'] not in _clean[_info['日期']]['IP']:
        #     _data[_info['日期']]['IP'].append(_info['IP'])
        #     _data[_info['日期']]['IP数'] += 1
        break
    #     print(len(_data))
    # print(_data)

# 生成csv
def list_to_csv(Data, Name):
    # 读取列表内容
    _data = pd.DataFrame(Data)
    _data.head()

    # 保存csv
    _data.to_csv(Name, index=False, header=True, encoding='UTF-8')

    # print('显示列表', _data, '\n', _data.values)


if __name__ == '__main__':
    # user = pd.DataFrame(pd.read_csv('uesr.csv', header=0, encoding='UTF-8')).values
    # action_log = pd.DataFrame(pd.read_csv('action_log.csv', header=0, encoding='UTF-8')).values
    clean= pd.DataFrame(pd.read_csv('clean.csv',header=0, encoding='UTF-8'))
    # 洗掉无用的数据，并去重
    _clean = gg(clean)
