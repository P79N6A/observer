import json

# model={'fav': '总冠军', 'age': 31} #数据
# with open("test.json",'w',encoding='utf-8') as json_file:
#         json.dump(model,json_file,ensure_ascii=False)

def XX():

    with open("test.json",'r',encoding='utf-8') as json_file:
        model=json.load(json_file)
        print(model['fav'])




    db_name = {'剧目':'plans'}




#用正则提取内容
import re

def tiqu():
    test = '口碑佳作《驴得水》被许多剧迷称作"神剧"'

    _info = re.search('《[^》]+》', test, flags=0).group()
    print(_info)


#时间计算的实验
import datetime
def time():
    a ='2018-02-20'
    b ='2018-03-20'
    startTime = datetime.datetime.strptime(a, '%Y-%m-%d')
    endTime = datetime.datetime.strptime(b, '%Y-%m-%d')
    print(startTime-endTime)


#去掉头尾的空格
def cleam():

    a = [{"situation":1,"level":4,"description":"准妈妈很适合吃包子，包子皮是发面食品，富含B族维生素，而且很容易消化。包子搭配了多种蔬菜和肉类，能够为准妈妈提供各种营养。"},{"situation":2,"level":4,"description":"坐月子能吃包子，包子皮是发面食品，比较容易消化，适合月子期间食用。"},{"situation":3,"level":4,"description":"一般情况下，包子都会同时搭配多种蔬菜和肉类，能够做到基本的膳食平衡，适合哺乳妈妈。"},{"situation":4,"level":4,"description":"包子可以通过改变面皮和馅料，做出很多花样来，促排期间和移植后吃包子改善饮食搭配，为人体提供各种营养，所以试管期间是可以吃包子的！"}]

    for i in a:
        i['title'] = '测试数据'

    print(str(a).replace(' ',''))


#获得上级地址
import os
def get_path():
    # 获得当前路径的上级路径
    curPath2 = os.path.dirname(os.getcwd())

    #获得项目的路径
    curPath =os.path.abspath(__file__)
    print(curPath)

def words():
    dd={'ddd':11,'fff':222}
    print(list(dd.items()))
if __name__ == '__main__':
    words()