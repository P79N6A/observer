import pandas as pd
import os.path


def list_to_csv(LIST=[{'a': 1}, {'b': 2}], NAME='test.csv'):
    # 读取列表内容
    _data = pd.DataFrame(LIST)
    # _data.head()

    # 保存csv
    _data.to_csv(NAME, encoding='UTF-8')

    print(_data, '\n', _data.b, '\n', _data.index.values)


def list_to_db():
    print(1)


def csv_to_db():
    print('1')


def db_to_csv():
    print('1')


def csv_to_data():
    con = pd.DataFrame(pd.read_csv('/Users/apple/Documents/observer/res/contents.csv',header=None, encoding='UTF-8')).values
    doi = pd.DataFrame(pd.read_csv('/Users/apple/Documents/observer/res/doings.csv',header=None, encoding='UTF-8')).values

    print(len(doi[468:]))
    print(len(con[468:]))

    #看看原来的运动表是否也是这样的数字，如果是的话，再校对一遍，然后就可以添加内容了


    # for i in eval(f.values[0][2]):
    #     i['title'] = '测试数据'
    #     print(i)

    #做完之后，去掉文本中的空格
    # print(str(a).replace(' ', ''))

if __name__ == '__main__':
    csv_to_data()
