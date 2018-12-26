#保存数据
import pandas as pd
import os

#获得当前路径的上级路径
curPath = os.path.dirname(os.getcwd())

#将列表保存在csv中
def list_to_csv(LIST=[{'a': 1}, {'b': 2}], NAME='test.csv'):
    # 读取列表内容
    _data = pd.DataFrame(LIST)
    _data.head()

    # 保存csv,index代表是否有序列号，header代表是否有表头
    _data.to_csv(NAME,index=True,header=True, encoding='UTF-8')

    # # _data显示表头，_data.values显示表体
    # print(_data,  '\n', _data.values)


def list_to_db():
    print(1)


def csv_to_db():
    print('1')


def db_to_csv():
    print('1')


def csv_to_data():
    con = pd.DataFrame(pd.read_csv(curPath+'/res/contents.csv',header=None, encoding='UTF-8')).values
    doi = pd.DataFrame(pd.read_csv(curPath+'/res/doings.csv',header=None, encoding='UTF-8')).values
    yun = pd.DataFrame(pd.read_csv(curPath + '/res/yundong.csv', header=0, encoding='UTF-8')).values
    test = pd.DataFrame(pd.read_csv('test.csv', header=0, encoding='UTF-8'))
    #
    # print('列表数：',len(doi[468:]),'\n',doi[468])
    # print('列表数：',len(con[468:]),'\n',con[468:])
    # print('列表数：',len(yun[0:]),'\n',yun[0])


    # #测试两个表中的数据是否相同
    # c = 0
    # for i in range(402):
    #     a = doi[i+468][2]
    #     b = yun[i][1]
    #     if a==b:
    #         c +=1
    #     # break
    # print(c)

    # #看看原来的运动表是否也是这样的数字，如果是的话，再校对一遍，然后就可以添加内容了
    # _re =[]
    # for  i in range(len(con[468:])):
    #     # print(len(con[i+468]))
    #     _de =[]
    #
    #     a = eval(con[i+468][2])
    #     b= yun[i]
    #
    #     for j in range(len(a)):
    #         a[j]['title']=b[j*3+4]
    #
    #     _de.append(str(con[i + 468][0]))
    #     _de.append(str(con[i + 468][1]))
    #     _de.append(str(a).replace(' ', ''))
    #     _de.append(str(con[i + 468][3]))
    #     _de.append(str(con[i + 468][4]))
    #
    #     _re.append(_de)
    #     # print(_de)
    #     # break

    print(test[''][0])

    # return _re

    # 做完之后，去掉文本中的空格


if __name__ == '__main__':
    csv_to_data()
    # list_to_csv()
    # print(curPath)
