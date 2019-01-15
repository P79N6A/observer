# model={'fav': '总冠军', 'age': 31} #数据
# with open("test.json",'w',encoding='utf-8') as json_file:
#         json.dump(model,json_file,ensure_ascii=False)

def json():
    import json
    with open("test.json", 'a', encoding='utf-8') as json_file:
        model = json.load(json_file)
        print(model['fav'])

    db_name = {'剧目': 'plans'}



# 处理文件到读写
def text():
    #https://blog.csdn.net/ztf312/article/details/47259805

    # a+是接着写，w+是覆盖
    with open("res/test.txt", 'a+', encoding='utf-8') as test:
        # dd = test.read() + '99'  # 读取内容，然后处理后，覆盖源文件
        test.write('测试数据')


#字符
def zifu():
    pass
    # string = "hello"# %s打印时结果是hello 
    # print("string=%s" % string)# output: string=hello 
    #    
    # # %2s意思是字符串长度为2，当原字符串的长度超过2时，按原长度打印，所以%2s的打印结果还是hello 
    # print
    # "string=%2s" % string    # output: string=hello 
    #    
    # # %7s意思是字符串长度为7，当原字符串的长度小于7时，在原字符串左侧补空格， 
    # # 所以%7s的打印结果是 hello 
    # print
    # "string=%7s" % string    # output: string= hello 
    #    
    # # %-7s意思是字符串长度为7，当原字符串的长度小于7时，在原字符串右侧补空格， 
    # # 所以%-7s的打印结果是 hello 
    # print
    # "string=%-7s!" % string    # output: string=hello ! 
    #    
    # # %.2s意思是截取字符串的前2个字符，所以%.2s的打印结果是he 
    # print
    # "string=%.2s" % string   # output: string=he 
    #    
    # # %.7s意思是截取字符串的前7个字符，当原字符串长度小于7时，即是字符串本身， 
    # # 所以%.7s的打印结果是hello 
    # print
    # "string=%.7s" % string   # output: string=hello 
    #    
    # # %a.bs这种格式是上面两种格式的综合，首先根据小数点后面的数b截取字符串， 
    # # 当截取的字符串长度小于a时，还需要在其左侧补空格 
    # print
    # "string=%7.2s" % string   # output: string=   he 
    # print
    # "string=%2.7s" % string   # output: string=hello 
    # print
    # "string=%10.7s" % string  # output: string=   hello 
    #    
    # # 还可以用%*.*s来表示精度，两个*的值分别在后面小括号的前两位数值指定 
    # print
    # "string=%*.*s" % (7, 2, string)    # output: string=   he
    #
    # num = 14
    #
    # # %d打印时结果是14
    # print
    # "num=%d" % num  # output: num=14
    #
    # # %1d意思是打印结果为1位整数，当整数的位数超过1位时，按整数原值打印，所以%1d的打印结果还是14
    # print
    # "num=%1d" % num  # output: num=14
    #
    # # %3d意思是打印结果为3位整数，当整数的位数不够3位时，在整数左侧补空格，所以%3d的打印结果是 14
    # print
    # "num=%3d" % num  # output: num= 14
    #
    # # %-3d意思是打印结果为3位整数，当整数的位数不够3位时，在整数右侧补空格，所以%3d的打印结果是14_
    # print
    # "num=%-3d" % num  # output: num=14_
    #
    # # %05d意思是打印结果为5位整数，当整数的位数不够5位时，在整数左侧补0，所以%05d的打印结果是00014
    # print
    # "num=%05d" % num  # output: num=00014
    #
    # # %.3d小数点后面的3意思是打印结果为3位整数，
    # # 当整数的位数不够3位时，在整数左侧补0，所以%.3d的打印结果是014
    # print
    # "num=%.3d" % num  # output: num=014
    #
    # # %.0003d小数点后面的0003和3一样，都表示3，意思是打印结果为3位整数，
    # # 当整数的位数不够3位时，在整数左侧补0，所以%.3d的打印结果还是014
    # print
    # "num=%.0003d" % num  # output: num=014
    #
    # # %5.3d是两种补齐方式的综合，当整数的位数不够3时，先在左侧补0，还是不够5位时，再在左侧补空格，
    # # 规则就是补0优先，最终的长度选数值较大的那个，所以%5.3d的打印结果还是 014
    # print
    # "num=%5.3d" % num  # output: num= 014
    #
    # # %05.3d是两种补齐方式的综合，当整数的位数不够3时，先在左侧补0，还是不够5位时，
    # # 由于是05，再在左侧补0，最终的长度选数值较大的那个，所以%05.3d的打印结果还是00014
    # print
    # "num=%05.3d" % num  # output: num=00014
    #
    # # 还可以用%*.*d来表示精度，两个*的值分别在后面小括号的前两位数值指定
    # # 如下，不过这种方式04就失去补0的功能，只能补空格，只有小数点后面的3才能补0
    # print
    # "num=%*.*d" % (04, 3, num)  # output: num= 014
    #
    # import math
    #
    # # %a.bf，a表示浮点数的打印长度，b表示浮点数小数点后面的精度
    #
    # # 只是%f时表示原值，默认是小数点后5位数
    # print
    # "PI=%f" % math.pi  # output: PI=3.141593
    #
    # # 只是%9f时，表示打印长度9位数，小数点也占一位，不够左侧补空格
    # print
    # "PI=%9f" % math.pi  # output: PI=_3.141593
    #
    # # 只有.没有后面的数字时，表示去掉小数输出整数，03表示不够3位数左侧补0
    # print
    # "PI=%03.f" % math.pi  # output: PI=003
    #
    # # %6.3f表示小数点后面精确到3位，总长度6位数，包括小数点，不够左侧补空格
    # print
    # "PI=%6.3f" % math.pi  # output: PI=_3.142
    #
    # # %-6.3f表示小数点后面精确到3位，总长度6位数，包括小数点，不够右侧补空格
    # print
    # "PI=%-6.3f" % math.pi  # output: PI=3.142_
    #
    # # 还可以用%*.*f来表示精度，两个*的值分别在后面小括号的前两位数值指定
    # # 如下，不过这种方式06就失去补0的功能，只能补空格
    # print
    # "PI=%*.*f" % (06, 3, math.pi)  # output: PI=_3.142




#字符串转时间的系列实验
def _datetime():
    from datetime import datetime
    datetime_str = "2016-11-30 13:53:59"
    date_str = '2018-02-20'
    time_str = '13:53:59'

    print(datetime.strptime(date_str , "%Y-%m-%d").date())
    print(datetime.strptime(time_str , "%H:%M:%S").time())
    print(datetime.strptime(datetime_str , "%Y-%m-%d %H:%M:%S"))

    startTime = datetime.strptime('2018-02-20', '%Y-%m-%d')
    endTime = datetime.strptime('2018-03-20', '%Y-%m-%d')
    print((startTime - endTime).days)


# 去掉头尾的空格
def cleam():
    a = [{"situation": 1, "level": 4, "description": "准妈妈很适合吃包子，包子皮是发面食品，富含B族维生素，而且很容易消化。包子搭配了多种蔬菜和肉类，能够为准妈妈提供各种营养。"},
         {"situation": 2, "level": 4, "description": "坐月子能吃包子，包子皮是发面食品，比较容易消化，适合月子期间食用。"},
         {"situation": 3, "level": 4, "description": "一般情况下，包子都会同时搭配多种蔬菜和肉类，能够做到基本的膳食平衡，适合哺乳妈妈。"},
         {"situation": 4, "level": 4,
          "description": "包子可以通过改变面皮和馅料，做出很多花样来，促排期间和移植后吃包子改善饮食搭配，为人体提供各种营养，所以试管期间是可以吃包子的！"}]

    for i in a:
        i['title'] = '测试数据'

    print(str(a).replace(' ', ''))


# 获得上级地址
def get_path():
    import os
    # 获得当前路径的上级路径
    curPath2 = os.path.dirname(os.getcwd())

    # 获得项目的路径
    curPath = os.path.abspath(__file__)
    print(curPath)


# 查找data
def find():
    import pandas as pd
    test2 = [{'标题': '禾空间儿童剧嘉年华十次卡演出票', '副标题': '多部儿童剧', '地点城市': '武汉', '演出场所': '禾空间小剧场', '演出时间': '2018.10.01-2019.02.28',
              '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 164857, 'imgurl': '1648', '最低票价': 199.0, '最高票价': 199.0,
              '信息属性': 0},
             {'标题': '禾空间儿童剧嘉年华《维小鲸历险记之乘风破浪》', '副标题': '虎鲸偷偷跟上了这艘神秘大船，开启了它的海洋历险。', '地点城市': '武汉', '演出场所': '禾空间小剧场',
              '演出时间': '2018.12.30-2019.01.05', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 165097, 'imgurl': '1650',
              '最低票价': 49.0, '最高票价': 59.0, '信息属性': 0, '剧名': '《维小鲸历险记之乘风破浪》'},
             {'标题': '禾空间嘉年华儿童剧《大头爸爸和小头儿子》', '副标题': '在奇幻森林的南边，有一个奇幻小镇。发生了意想不到的事情', '地点城市': '武汉', '演出场所': '禾空间小剧场',
              '演出时间': '2018.12.12-2019.01.06', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 164860, 'imgurl': '1648',
              '最低票价': 49.0, '最高票价': 59.0, '信息属性': 0, '剧名': '《大头爸爸和小头儿子》'},
             {'标题': '禾空间原创亲子互动剧《神奇动物在这里》', '副标题': '本剧由《格林童话》中《金鸟》、《牧鹅女》、《金鹅》三个故事略加改编而成', '地点城市': '武汉', '演出场所': '禾空间小剧场',
              '演出时间': '2018.12.23-2019.01.13', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 167809, 'imgurl': '1678',
              '最低票价': 59.0, '最高票价': 69.0, '信息属性': 0, '剧名': '《神奇动物在这里》'},
             {'标题': '禾空间首部原创IP人偶儿童剧《熊猫飞飞历险记2之安徒生童话城堡的迷宫》', '副标题': '熊猫飞飞一个人踏上了寻找金禾的旅程。', '地点城市': '武汉', '演出场所': '禾空间小剧场',
              '演出时间': '2019.01.01-01.12', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 168875, 'imgurl': '1688',
              '最低票价': 59.0,
              '最高票价': 69.0, '信息属性': 0, '剧名': '《熊猫飞飞历险记2之安徒生童话城堡的迷宫》'},
             {'标题': '大型系列儿童剧《恐龙王国》之《恐龙王国之南极之旅》', '副标题': '一个好题材，一个好故事', '地点城市': '武汉', '演出场所': '禾空间小剧场',
              '演出时间': '2019.01.06',
              '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 170700, 'imgurl': '1707', '最低票价': 80.0, '最高票价': 100.0,
              '信息属性': 0,
              '剧名': '《恐龙王国》'},
             {'标题': '禾空间小剧场原创惊悚爆笑舞台剧——《goodbye旅行社之黑白先生》', '副标题': '如果一黑一白两个人，非要请你去他们的地盘旅游，你敢去吗？', '地点城市': '武汉',
              '演出场所': '禾空间小剧场', '演出时间': '2018.12.29-2019.01.26', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 168874,
              'imgurl': '1688', '最低票价': 60.0, '最高票价': 100.0, '信息属性': 0, '剧名': '《goodbye旅行社之黑白先生》'},
             {'标题': '武汉·2019年1月大型儿童剧《白雪公主》', '副标题': '根据《格林童话》经典故事改编了《白雪公主》这部儿童剧。', '地点城市': '武汉', '演出场所': '珞珈山剧院',
              '演出时间': '2019.01.06', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 169845, 'imgurl': '1698', '最低票价': 39.0,
              '最高票价': 79.0, '信息属性': 0, '剧名': '《白雪公主》'},
             {'标题': '有趣戏剧第四回 话剧《杏仁豆腐心》武汉站', '副标题': '《杏仁豆腐心》不是年轻情侣间的撕X大戏，而是想借助两颗灵魂的孤独唏嘘，找回我们原本柔软而温暖的内心。', '地点城市': '武汉',
              '演出场所': '403国际艺术中心·红椅剧场', '演出时间': '2019.01.05-01.06', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 170709,
              'imgurl': '1707', '最低票价': 80.0, '最高票价': 280.0, '信息属性': 0, '剧名': '《杏仁豆腐心》'},
             {'标题': '经典成长童话《匹诺曹》--武汉站', '副标题': '经典成长童话《匹诺曹》将给观众带来感动与趣味。', '地点城市': '武汉', '演出场所': '武汉工人文化宫职工剧场',
              '演出时间': '2019.06.15  10:30/15:00', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 171025, 'imgurl': '1710',
              '最低票价': 50.0, '最高票价': 260.0, '信息属性': 0, '剧名': '《匹诺曹》'},
             {'标题': '浪漫经典童话剧《灰姑娘》--武汉站', '副标题': '王子能否找到舞会上的灰姑娘？美丽的童话将在今夜绽放！', '地点城市': '武汉', '演出场所': '武汉工人文化宫职工剧场',
              '演出时间': '2019.07.06 10:30/15:00', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 171179, 'imgurl': '1711',
              '最低票价': 50.0, '最高票价': 260.0, '信息属性': 0, '剧名': '《灰姑娘》'},
             {'标题': '梦幻互动亲子剧《人鱼公主》--武汉站', '副标题': '这是一次友情、亲情与爱情的启蒙童话之旅', '地点城市': '武汉', '演出场所': '武汉工人文化宫职工剧场',
              '演出时间': '2019.09.07', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 171140, 'imgurl': '1711', '最低票价': 50.0,
              '最高票价': 260.0, '信息属性': 0, '剧名': '《人鱼公主》'},
             {'标题': '奇幻亲子音乐剧《绿野仙踪》--武汉站', '副标题': '华丽多变的舞蹈与原创音乐相得益彰，拉开奇幻视觉盛宴的序幕', '地点城市': '武汉', '演出场所': '武汉工人文化宫职工剧场',
              '演出时间': '2019.11.02 10:30/15:00', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 171186, 'imgurl': '1711',
              '最低票价': 50.0, '最高票价': 260.0, '信息属性': 0, '剧名': '《绿野仙踪》'},
             {'标题': '寻梦亲子音乐剧《Flight School 飞行学校》--武汉站', '副标题': '励志的故事，动听的音乐，让孩子在音乐剧的世界里找到乐趣，教你在友情、团结中找到梦想。',
              '地点城市': '武汉',
              '演出场所': '武汉工人文化宫职工剧场', '演出时间': '2019.08.10', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 171157,
              'imgurl': '1711', '最低票价': 50.0, '最高票价': 260.0, '信息属性': 0, '剧名': '《Flight School 飞行学校》'},
             {'标题': '2019经典再现贺岁喜剧《海底捞月》', '副标题': '本剧通过六十年的麻将生涯，折射出普通百姓酸甜苦辣、大起大落的人生变迁，传奇、暴笑、又让人感慨万千', '地点城市': '武汉',
              '演出场所': '湖北剧院', '演出时间': '2018.12.28-2019.01.22', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 171241,
              'imgurl': '1712', '最低票价': 80.0, '最高票价': 480.0, '信息属性': 0, '剧名': '《海底捞月》'},
             {'标题': '武汉说唱团贺岁剧2019经典再现《海底捞月》', '副标题': '通过六十年的麻将生涯，折射出普通百姓酸甜苦辣、大起大落的人生变迁，传奇、暴笑、又让人感慨万千……', '地点城市': '武汉',
              '演出场所': '湖北剧院', '演出时间': '2018.12.18-2019.01.02', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 168943,
              'imgurl': '1689', '最低票价': 80.0, '最高票价': 480.0, '信息属性': 0, '剧名': '《海底捞月》'},
             {'标题': '江湖爆笑喜剧《萨瓦迪大咖》', '副标题': '一条暧昧微信引发婚姻信任危机！', '地点城市': '武汉', '演出场所': '湖北剧院', '演出时间': '2019.01.16-02.09',
              '演出状态': '售票中', '演出类型': '话剧', 'projectid': 172236, 'imgurl': '1722', '最低票价': 100.0, '最高票价': 380.0,
              '信息属性': 0,
              '剧名': '《萨瓦迪大咖》'},
             {'标题': '音乐剧《搭错车》武汉站', '副标题': '音乐剧坛震撼聚焦，殿堂级音乐剧《搭错车》2019年3月8日经典重现武汉！', '地点城市': '武汉', '演出场所': '湖北剧院',
              '演出时间': '2019.03.08 19:30', '演出状态': '预售', '演出类型': '音乐剧', 'projectid': 172514, 'imgurl': '1725',
              '最低票价': 199.0,
              '最高票价': 999.0, '信息属性': 0, '剧名': '《搭错车》'},
             {'标题': '话剧《蒋公的面子》', '副标题': '这是一个后辈学生根据校史传说虚构的关于前辈老师和校长的故事。', '地点城市': '武汉', '演出场所': '湖北剧院',
              '演出时间': '2019.04.27 19:30', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 172018, 'imgurl': '1720',
              '最低票价': 100.0,
              '最高票价': 870.0, '信息属性': 0, '剧名': '《蒋公的面子》'},
             {'标题': '武汉年度C位爆笑喜剧《抹茶攻略》', '副标题': '有如手工钟表般精密的结构喜剧。', '地点城市': '武汉', '演出场所': '湖北剧院',
              '演出时间': '2019.12.09-2019.01.04', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 169604, 'imgurl': '1696',
              '最低票价': 110.0, '最高票价': 480.0, '信息属性': 0, '剧名': '《抹茶攻略》'},
             {'标题': '武汉人艺大型原创话剧《王荷波》专场演出', '副标题': '王荷波波澜壮阔的人生中，截取了建党初期、大革命高潮和陷入困境的三个不同时期的故事', '地点城市': '武汉',
              '演出场所': '中南剧场大剧场', '演出时间': '2019.01.09', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 172698,
              'imgurl': '1726',
              '最低票价': 30.0, '最高票价': 160.0, '信息属性': 0, '剧名': '《王荷波》'},
             {'标题': 'MaiLive 孟京辉戏剧作品《两只狗的生活意见》武汉站', '副标题': '他们决定勇敢地面对生活，不管生活有多艰辛，一定要勇敢地走下去！', '地点城市': '武汉',
              '演出场所': '中南剧场大剧场', '演出时间': '2019.01.11-01.13', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 163615,
              'imgurl': '1636', '最低票价': 100.0, '最高票价': 480.0, '信息属性': 0, '剧名': '《两只狗的生活意见》'},
             {'标题': 'MaiLive 孟京辉戏剧作品《九又二分之一爱情》武汉站', '副标题': '讲述了一个关于爱与复仇的当代寓言。', '地点城市': '武汉', '演出场所': '中南剧场大剧场',
              '演出时间': '2019.04.26-04.28', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 172118, 'imgurl': '1721',
              '最低票价': 100.0,
              '最高票价': 480.0, '信息属性': 0, '剧名': '《九又二分之一爱情》'},
             {'标题': 'MaiLive 孟京辉戏剧作品《我爱XXX》武汉站', '副标题': '语言本身不具备意义，却是我们生存的唯一现实，我们与它相依为命。', '地点城市': '武汉',
              '演出场所': '中南剧场大剧场',
              '演出时间': '2019.03.15-03.16', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 172094, 'imgurl': '1720',
              '最低票价': 100.0,
              '最高票价': 480.0, '信息属性': 0, '剧名': '《我爱XXX》'},
             {'标题': 'MaiLive孟京辉戏剧作品《一个陌生女人的来信》武汉站', '副标题': '讲述陌生女人和W先生"三次做饭与三次交欢"的疯狂爱情。', '地点城市': '武汉',
              '演出场所': '中南剧场大剧场',
              '演出时间': '2019.05.03-05.05', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 172121, 'imgurl': '1721',
              '最低票价': 100.0,
              '最高票价': 480.0, '信息属性': 0, '剧名': '《一个陌生女人的来信》'},
             {'标题': 'MaiLive 孟京辉经典戏剧作品《恋爱的犀牛》武汉站', '副标题': '当代中国戏剧旗帜性作品，永远的爱情圣经', '地点城市': '武汉', '演出场所': '中南剧场大剧场',
              '演出时间': '2019.03.29-03.31', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 172122, 'imgurl': '1721',
              '最低票价': 100.0,
              '最高票价': 480.0, '信息属性': 0, '剧名': '《恋爱的犀牛》'},
             {'标题': 'MaiLive 孟京辉经典音乐剧作品《空中花园谋杀案》武汉站', '副标题': '整个城市为了空中花园而疯狂!新的谋杀即将开始……', '地点城市': '武汉',
              '演出场所': '中南剧场大剧场',
              '演出时间': '2019.06.28-06.30', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 172089, 'imgurl': '1720',
              '最低票价': 100.0,
              '最高票价': 480.0, '信息属性': 0, '剧名': '《空中花园谋杀案》'},
             {'标题': '原创话剧《这些年》', '副标题': '以小人物的视角真实质朴的展现了普通人在时代大浪中的命运变化', '地点城市': '武汉', '演出场所': '武汉人民艺术剧院-D5空间',
              '演出时间': '2018.12.31-2019.01.26', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 172111, 'imgurl': '1721',
              '最低票价': 50.0, '最高票价': 50.0, '信息属性': 0, '剧名': '《这些年》'},
             {'标题': '儿童剧《小蝌蚪找妈妈》', '副标题': '青蛙妈妈和小蝌蚪们终于团聚。妈妈给孩子们上了有意义的人生第一课。', '地点城市': '武汉', '演出场所': '武汉人民艺术剧院-亲子剧场',
              '演出时间': '2018.01.05-01.27', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 170767, 'imgurl': '1707',
              '最低票价': 50.0,
              '最高票价': 50.0, '信息属性': 0, '剧名': '《小蝌蚪找妈妈》'},
             {'标题': '开心麻花2019爆笑贺岁舞台剧《窗前不止明月光》', '副标题': '开心麻花爆笑推荐超“毒舌”台词根本停不下来！', '地点城市': '武汉', '演出场所': '武汉剧院',
              '演出时间': '2019.01.18-01.19', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 169863, 'imgurl': '1698',
              '最低票价': 100.0,
              '最高票价': 880.0, '信息属性': 0, '剧名': '《窗前不止明月光》'},
             {'标题': '凡创文化·大型恐龙主题实景童话剧《你看起来好像很好吃》', '副标题': '《你看起来好像很好吃》给所有的恐龙们都编排了极富童趣的舞蹈。', '地点城市': '武汉',
              '演出场所': '武汉剧院',
              '演出时间': '2019.04.14 10:30', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 170724, 'imgurl': '1707',
              '最低票价': 100.0, '最高票价': 1500.0, '信息属性': 0, '剧名': '《你看起来好像很好吃》'},
             {'标题': '开心麻花2019爆笑贺岁舞台剧《谈判专家》', '副标题': '开心麻花原创贺岁舞台剧', '地点城市': '武汉', '演出场所': '武汉剧院',
              '演出时间': '2019.03.07-03.10',
              '演出状态': '售票中', '演出类型': '话剧', 'projectid': 172146, 'imgurl': '1721', '最低票价': 100.0, '最高票价': 1320.0,
              '信息属性': 0,
              '剧名': '《谈判专家》'},
             {'标题': '世界原版经典音乐剧《猫》CATS-武汉站', '副标题': '世界原版经典音乐剧《猫》2019中国“猫”年震撼回归', '地点城市': '武汉', '演出场所': '武汉剧院',
              '演出时间': '2019.06.21-06.26', '演出状态': '预售', '演出类型': '音乐剧', 'projectid': 172365, 'imgurl': '1723',
              '最低票价': 280.0,
              '最高票价': 1380.0, '信息属性': 0, '剧名': '《猫》'},
             {'标题': '托马斯&朋友—迷失宝藏', '副标题': '英国儿童电视动画剧《Thomas&Friends》改编', '地点城市': '武汉', '演出场所': '武汉剧院',
              '演出时间': '2019.06.01',
              '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 171837, 'imgurl': '1718', '最低票价': 80.0, '最高票价': 600.0,
              '信息属性': 0},
             {'标题': '小鬼当家系列亲子剧《神秘大盗》', '副标题': '寓教于乐，告诉小朋友们乐于助人、拾金不昧的教育理念', '地点城市': '武汉', '演出场所': '亦言堂·南湖天地剧场',
              '演出时间': '2019.01.05-01.26', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 171662, 'imgurl': '1716',
              '最低票价': 100.0, '最高票价': 100.0, '信息属性': 0, '剧名': '《神秘大盗》'},
             {'标题': '九町舞台剧《游侠小红帽》', '副标题': '经典儿童剧改编，让短小平淡的故事更加丰满', '地点城市': '武汉', '演出场所': '亦言堂·南湖天地剧场',
              '演出时间': '2018.12.22-2019.01.26', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 171665, 'imgurl': '1716',
              '最低票价': 50.0, '最高票价': 50.0, '信息属性': 0, '剧名': '《游侠小红帽》'},
             {'标题': '江城爱情故事系列舞台剧《缘来是你》', '副标题': '江诚也发现了自己爷爷的日记，一段民国时期的爱情故事呈现在两人眼前……', '地点城市': '武汉',
              '演出场所': '亦言堂·南湖天地剧场',
              '演出时间': '2018.12.21-2019.01.25', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 171652, 'imgurl': '1716',
              '最低票价': 100.0, '最高票价': 100.0, '信息属性': 0, '剧名': '《缘来是你》'},
             {'标题': '九町舞台剧《老婆梦工厂》', '副标题': '通过欢乐多彩的舞台呈现，讲述了"一见钟情"式的爱情体验。', '地点城市': '武汉', '演出场所': '亦言堂·南湖天地剧场',
              '演出时间': '2019.01.05-01.27', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 171664, 'imgurl': '1716',
              '最低票价': 50.0,
              '最高票价': 50.0, '信息属性': 0, '剧名': '《老婆梦工厂》'},
             {'标题': '《海底小纵队4：极地大冒险》武汉站', '副标题': '英国版权引进，海洋探险故事奇幻，开发想象力，魅力无穷。', '地点城市': '武汉', '演出场所': '武汉琴台大剧院',
              '演出时间': '2019.01.05 19:30', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 169531, 'imgurl': '1695',
              '最低票价': 60.0,
              '最高票价': 780.0, '信息属性': 0, '剧名': '《海底小纵队4：极地大冒险》'},
             {'标题': '舞台剧《剑网3·曲云传》武汉站', '副标题': '高度还原的游戏场景和故事剧情，让你笑着流泪，哭着感动！', '地点城市': '武汉', '演出场所': '武汉琴台大剧院',
              '演出时间': '2019-01-13 14:30', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 171016, 'imgurl': '1710',
              '最低票价': 188.0,
              '最高票价': 988.0, '信息属性': 0, '剧名': '《剑网3·曲云传》'},
             {'标题': '黑色喜剧《驴得水》武汉站', '副标题': '口碑佳作《驴得水》被许多剧迷称作"神剧"', '地点城市': '武汉', '演出场所': '武汉琴台大剧院',
              '演出时间': '2019-01-06',
              '演出状态': '售票中', '演出类型': '话剧', 'projectid': 171739, 'imgurl': '1717', '最低票价': 80.0, '最高票价': 380.0,
              '信息属性': 0,
              '剧名': '《驴得水》'},
             {'标题': '大型音乐舞台剧《犹太城》武汉站', '副标题': '讲述二战期间德国纳粹占领和控制下的维尔纽斯犹太城里发生的故事。', '地点城市': '武汉', '演出场所': '武汉琴台大剧院',
              '演出时间': '2019.01.20   19:30', '演出状态': '售票中', '演出类型': '歌舞剧', 'projectid': 169510, 'imgurl': '1695',
              '最低票价': 80.0, '最高票价': 1199.0, '信息属性': 0, '剧名': '《犹太城》'},
             {'标题': '大型冒险式儿童舞台剧《圆梦恐龙岛》武汉站', '副标题': '友情，亲情，团结，正能量', '地点城市': '武汉', '演出场所': '武汉琴台大剧院',
              '演出时间': '2019.01.27 19:30', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 172846, 'imgurl': '1728',
              '最低票价': 60.0,
              '最高票价': 560.0, '信息属性': 0, '剧名': '《圆梦恐龙岛》'},
             {'标题': '音乐剧《灰姑娘》中文版（武汉站）', '副标题': '', '地点城市': '武汉', '演出场所': '武汉琴台大剧院', '演出时间': '2019.01.03-01.04',
              '演出状态': '售票中', '演出类型': '音乐剧', 'projectid': 579053572399, 'imgurl': '1495568427', '最低票价': 50.0,
              '最高票价': 480.0,
              '信息属性': 0, '剧名': '《灰姑娘》'},
             {'标题': '保利原创儿童剧《故宫里的小不点》武汉站', '副标题': '为广大小朋友及家长们带来奇幻视觉盛宴', '地点城市': '武汉', '演出场所': '武汉琴台大剧院',
              '演出时间': '2019.01.15 19:30', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 171231, 'imgurl': '1712',
              '最低票价': 80.0,
              '最高票价': 760.0, '信息属性': 0, '剧名': '《故宫里的小不点》'},
             {'标题': '沉浸式儿童体验3D游戏剧《爱丽丝梦游仙境》', '副标题': '爱丽丝从小脑袋里就装着各种奇思妙想，因为追一只揣着怀表、会说话的兔子，她掉进了树洞，开始了一段奇幻之旅。',
              '地点城市': '武汉',
              '演出场所': '荟聚购物中心外广场南大门G区停车场', '演出时间': '2018.10.01-2019.01.20', '演出状态': '售票中', '演出类型': '儿童剧',
              'projectid': 164159, 'imgurl': '1641', '最低票价': 88.0, '最高票价': 88.0, '信息属性': 0, '剧名': '《爱丽丝梦游仙境》'},
             {'标题': '英国音乐戏剧秀《欢乐颂》', '副标题': '来自英国的JunNK剧团由四位神秘逗咖爆笑上演，', '地点城市': '武汉', '演出场所': '汤湖戏院',
              '演出时间': '2019.01.04',
              '演出状态': '售票中', '演出类型': '音乐剧', 'projectid': 171144, 'imgurl': '1711', '最低票价': 60.0, '最高票价': 120.0,
              '信息属性': 0,
              '剧名': '《欢乐颂》'},
             {'标题': '武汉说唱团爆笑神剧《海底捞月》', '副标题': '本剧通过六十年的麻将生涯，折射出普通百姓酸甜苦辣、大起大落的人生变迁。', '地点城市': '武汉', '演出场所': '汤湖戏院',
              '演出时间': '2018.12.29-2019.02.19', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 169619, 'imgurl': '1696',
              '最低票价': 80.0, '最高票价': 180.0, '信息属性': 0, '剧名': '《海底捞月》'}]

    test1 = [{'标题': '大型冒险式儿童舞台剧《圆梦恐龙岛》武汉站', '副标题': '友情，亲情，团结，正能量', '地点城市': '武汉', '演出场所': '武汉琴台大剧院',
              '演出时间': '2019.01.27 19:30', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 172846, 'imgurl': '1728',
              '最低票价': 60.0,
              '最高票价': 560.0, '信息属性': 0, '剧名': '《圆梦恐龙岛》'},
             {'标题': '音乐剧《灰姑娘》中文版（武汉站）', '副标题': '', '地点城市': '武汉', '演出场所': '武汉琴台大剧院', '演出时间': '2019.01.03-01.04',
              '演出状态': '售票中', '演出类型': '音乐剧', 'projectid': 579053572399, 'imgurl': '1495568427', '最低票价': 50.0,
              '最高票价': 480.0,
              '信息属性': 0, '剧名': '《灰姑娘》'},
             {'标题': '保利原创儿童剧《故宫里的小不点》武汉站', '副标题': '为广大小朋友及家长们带来奇幻视觉盛宴', '地点城市': '武汉', '演出场所': '武汉琴台大剧院',
              '演出时间': '2019.01.15 19:30', '演出状态': '售票中', '演出类型': '儿童剧', 'projectid': 171231, 'imgurl': '1712',
              '最低票价': 80.0,
              '最高票价': 760.0, '信息属性': 0, '剧名': '《故宫里的小不点》'},
             {'标题': '沉浸式儿童体验3D游戏剧《爱丽丝梦游仙境》', '副标题': '爱丽丝从小脑袋里就装着各种奇思妙想，因为追一只揣着怀表、会说话的兔子，她掉进了树洞，开始了一段奇幻之旅。',
              '地点城市': '武汉',
              '演出场所': '荟聚购物中心外广场南大门G区停车场', '演出时间': '2018.10.01-2019.01.20', '演出状态': '售票中', '演出类型': '儿童剧',
              'projectid': 164159, 'imgurl': '1641', '最低票价': 88.0, '最高票价': 88.0, '信息属性': 0, '剧名': '《爱丽丝梦游仙境》'},
             {'标题': '英国音乐戏剧秀《欢乐颂》', '副标题': '来自英国的JunNK剧团由四位神秘逗咖爆笑上演，', '地点城市': '武汉', '演出场所': '汤湖戏院',
              '演出时间': '2019.01.04',
              '演出状态': '售票中', '演出类型': '音乐剧', 'projectid': 171144, 'imgurl': '1711', '最低票价': 60.0, '最高票价': 120.0,
              '信息属性': 0,
              '剧名': '《欢乐颂》'},
             {'标题': '武汉说唱团爆笑神剧《海底捞月》', '副标题': '本剧通过六十年的麻将生涯，折射出普通百姓酸甜苦辣、大起大落的人生变迁。', '地点城市': '武汉', '演出场所': '汤湖戏院',
              '演出时间': '2018.12.29-2019.02.19', '演出状态': '售票中', '演出类型': '话剧', 'projectid': 169619, 'imgurl': '1696',
              '最低票价': 80.0, '最高票价': 180.0, '信息属性': 0, '剧名': '《海底捞月》'}]
    df = pd.DataFrame(test2)

    df2 = pd.DataFrame(test1)
    for i in df.iterrows():
        ddff = pd.concat([df, i[1]])
        print(ddff)

    # df3 = pd.DataFrame({'BoolCol': [3, 55]})

    # for i in df3.iterrows():
    #
    #     # 临时参数
    #     _i = i[1]
    #     print(df[df['BoolCol']==_i['BoolCol']])
    #
    #
    #
    #     #以X为依据，判断是否重复
    #     if df[df['BoolCol']==_i['BoolCol']].index.tolist():
    #         # if   _i['标题']:
    #         print('重复')
    # print(df ,'\n')
    # a = df[(df.BoolCol == 32) & (df.attr == 22)].index.tolist()
    # # print(df[(df.BoolCol == 3) & (df.attr == 22)])
    # # if df[df.BoolCol == 32].index.tolist() is True:
    # print(df[df.BoolCol BoolCol== 32].index.tolist())


# 保存data到csv
def to_csv():
    import pandas as pd
    df = pd.DataFrame({'BoolCol': [1, 2, 3, 3, 4], 'attr': [22, 33, 22, 44, 66]})
    df.to_csv('history.csv', )


# 测试代理是否可用
def GetUseProxies():
    # coding=utf-8
    import requests
    # '''测试代理是否可用'''
    UseProxiesList = []
    i = 1
    n = 0
    # 请求api返回代理列表
    api = "http://qsrdk.daili666api.com/ip/?&num=100&category=2&sortby=time"

    api_url = requests.get(api)

    proxies_list = api_url.content.split('\r\n')
    print('获得proiex%s' % len(proxies_list))
    for proxy in proxies_list:
        print('正在发送第%s个请求。\n\r' % i)
        i += 1
        proxies = {"http": "http://" + proxy, "https": "http://" + proxy, }
        try:
            requests.get('http://www.baidu.com', proxies=proxies, timeout=2)
            UseProxiesList.append(proxy)
        except:
            n += 1
            print('***已经有%s个代理被淘汰***' % n)
            print('UseProxiesList:', UseProxiesList)
            print('可用代理数量%s' % len(UseProxiesList))


# 分词测试
def fenxi():
    import jieba
    from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

    wc = WordCloud(background_color='white',  # 背景颜色
                   max_words=1000,  # 最大词数
                   # mask=back_color,  # 以该参数值作图绘制词云，这个参数不为空时，width和height会被忽略
                   max_font_size=100,  # 显示字体的最大值
                   stopwords=STOPWORDS.add('苟利国'),  # 使用内置的屏蔽词，再添加'苟利国'
                   font_path="C:/Windows/Fonts/STFANGSO.ttf",  # 解决显示口字型乱码问题，可进入C:/Windows/Fonts/目录更换字体
                   random_state=42,  # 为每个词返回一个PIL颜色
                   # width=1000,  # 图片的宽
                   # height=860  #图片的长
                   )

    jieba.add_word('海尔茂')

    txt = open('res/Init.txt', encoding='utf-8').read().replace("\n", "").replace(' ', '')

    txt2 = [line.strip() for line in open('res/stoptxt.txt', encoding='utf-8').readlines()]

    words = jieba.lcut(txt)
    en = {}

    for i in words:
        if i not in txt2:
            en[i] = en.get(i, 0) + 1

    items = list(en.items())

    items.sort(key=lambda x: x[1], reverse=True)

    for i in range(100):
        # word,count = items[i]
        print(items[i])
    wc.generate(txt)

#分词测试
def fdfdf():
    import pandas as pd
    # 加载解析HTML库
    from bs4 import BeautifulSoup as BS
    import jieba.analyse

    info = BS(open('data1.xml', 'r', encoding='utf-8'), 'html.parser')
    fog = info.find_all('row')

    inpu = []
    sirtl = {}
    for i in fog:
        n = i.find_all('field')
        ondu = {}
        ondu['id'] = i.find('field', class_='id').get_text()
        ondu['subject'] = n[3].get_text()
        ondu['message'] = n[4].get_text()
        ondu['views'] = n[5].get_text()
        ondu['replies'] = n[6].get_text()
        ondu['hots'] = n[7].get_text()

        # _fenci = jieba.lcut(ondu['message'])
        _fenci = jieba.analyse.extract_tags(ondu['message'], topK=20, withWeight=False)

        # print(ondu)
        # 分词内容
        counts = {}

        for word in _fenci:
            if len(word) == 1:
                continue
            else:
                counts[word] = counts.get(word, 0) + 1

        for i in counts:
            if i in sirtl:
                sirtl[i] = sirtl[i] + counts[i]
            else:
                sirtl[i] = counts[i]

        ondu['fenci'] = counts
        inpu.append(ondu)
        # print(ondu)
        # break

    # 停用词
    ddd = []
    stopd = open('tingyongci.txt', 'r', encoding='utf-8').readlines()
    for i in stopd:
        ddd.append(i)

    _deg = []
    for i in sirtl.items():
        if i not in ddd:
            _deg.append(i)

    _deg.sort(key=lambda x: x[1], reverse=True)
    print(_deg)

    # for j in ondu:
    #     j['fenci'].

    # ewwe=open('dde.txt','w',encoding='utf-8')
    # ewwe.write(str(inpu))
    # ewwe.close()
    # info.close()

# 停用此测试
def stopkey():
    import jieba
    path1 = 'stoptxt.txt'
    path2 = 'stop2.txt'
    test = '达郎向小叶子仔细描述他们夭折的孩子被火化的情景.'
    words = jieba.cut(test)  # 去除HTML标签


# 分词案例
def fenci():
    import jieba.analyse
    print("***案例1***" * 3)
    txt = open('res/Init.txt', encoding='utf-8').read().replace("\n", "").replace(' ', '')
    Key = jieba.analyse.extract_tags(txt, topK=3)
    print(Key)
    # -----------------------------------------------------------------------------------
    print("***案例2***" * 3)
    # 字符串前面加u表示使用unicode编码
    content = open('res/Init.txt', encoding='utf-8').read().replace("\n", "").replace(' ', '')
    # 第一个参数：待提取关键词的文本
    # 第二个参数：返回关键词的数量，重要性从高到低排序
    # 第三个参数：是否同时返回每个关键词的权重
    # 第四个参数：词性过滤，为空表示不过滤，若提供则仅返回符合词性要求的关键词
    keywords = jieba.analyse.extract_tags(content, topK=5, withWeight=True, allowPOS=())
    # 访问提取结果
    for item in keywords:
        # 分别为关键词和相应的权重
        print(item[0], item[1])

    # 同样是四个参数，但allowPOS默认为('ns', 'n', 'vn', 'v')
    # 即仅提取地名、名词、动名词、动词
    keywords = jieba.analyse.textrank(content, topK=5, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
    # 访问提取结果
    for item in keywords:
        # 分别为关键词和相应的权重
        print(item[0], item[1])


# 数据库操作
import pymongo


class get_db:

    # info 为一个数组，type是字符串"douban"/"damai"
    def __init__(self):
        self.test1 = [{'演出场所': '武汉琴台大剧院', '演出时间': '2019.01.27 19:30', '剧名': '《圆梦恐龙岛》'},
                      {'演出场所': '武汉琴台大剧院', '演出时间': '2019.01.03-01.04', '剧名': '《灰姑娘》'},
                      {'演出场所': '武汉琴台大剧院', '演出时间': '2019.01.15 19:30', '剧名': '《故宫里的小不点》'}
                      ]
        self.test2 = [{'演出场所': '武汉琴台大剧院', '演出时间': '2019.01.03-01.04', '剧名': '《灰姑娘》'},
                 {'演出场所': '武汉琴台大剧院', '演出时间': '2019.01.16', '剧名': '《故宫里的小不点》'},
                 {'演出场所': '荟聚购物中心外广场南大门G区停车场', '演出时间': '2018.10.01-2019.01.20', '剧名': '《爱丽丝梦游仙境》'},
                 {'演出场所': '汤湖戏院', '演出时间': '2019.01.04', '剧名': '《欢乐颂》'},
                 {'演出场所': '武汉琴台大剧院', '演出时间': '2018.12.29-2019.02.19', '剧名': '《海底捞月》'},
                 {'演出场所': '武汉琴台大剧院', '演出时间': '2019.01.15 19:30', '剧名': '《故宫里的小不点》'}
                 ]
        #数据库地址
        self.myclient = pymongo.MongoClient('mongodb://localhost:27017/')

        #数据库名字
        self.mydb = self.myclient["swarm"]

        #数据表名字
        self.db_name = 'test'

        self.type = type

    # 豆瓣数据储存
    def save(self):

        mycol = self.mydb[self.db_name]

        # _test = mycol.insert_many(self.test1)

        for i in mycol.find({'剧名': '《灰姑娘》'}):
            print(i)

        # 测试数据
        print('保存成功！')


#设置配置文件
def conf():
    pass



def dddd():
    from bs4 import BeautifulSoup as BS  # 加载解析HTML库
    test= """<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<meta name="spm-id" content="a2o6e" />
<meta name="renderer" content="webkit">
<meta name="force-rendering" content="webkit">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="cache-control" content="no-cache,must-revalidate">
<meta http-equiv="expires" content="0">
<title>武汉话剧歌剧 禾空间儿童剧嘉年华十次卡演出票【网上订票】– 大麦网</title> 
<meta name="create-time" content="2019-01-06 02:00:30" />
<meta name="keywords" content="武汉话剧歌剧,禾空间儿童剧嘉年华十次卡演出票,大麦网"/>
<meta name="description" content="大麦网（Damai.cn）武汉话剧歌剧 禾空间儿童剧嘉年华十次卡演出票将于2018.10.01-2019.02.28在禾空间小剧场上演，大麦网为禾空间小剧场话剧歌剧 禾空间儿童剧嘉年华十次卡演出票门票代理，更多门票价格及订票详情请咨询大麦网武汉站."/>
<meta name="aplus-auto-exp-visible" content="0.5">
<meta name="aplus-auto-exp-duration" content="500">
<meta name="aplus-auto-exp" content='[{"logkey":"/damai_pc.default.project_qr_purchase","tag":"div","filter":"data-spm-auto","props":["item_id"]}]'>
	<link rel="stylesheet" type="text/css" href="//dui.dmcdn.cn/??dm_2015/goods/css/style.css?v0.6.2,damai_v2/login_register3.0/css/style.css?v0.6.2" />
<link rel="stylesheet" type="text/css" href="//g.alicdn.com/??damai/pc-wx/0.1.0/index.css"></link>
<style type="text/css">
.chat-view-xiaoneng-version{opacity:0;}
.m-choose .tt { padding-top: 10px; }
.m-cart .tt { padding-top: 16px; }
.m-choose .lst .s_manjian { height: 71px; }
.jiathis_style  .jtico{text-align:left;overflow:hidden;display:block!important;height:16px!important;line-height:16px!important;padding-left:20px!important;cursor:pointer;}
.jiathis_style  .jtico:hover{opacity:0.8;}
.jiathis_style .jiathis_txt {float: left;font-size: 12px;line-height: 18px !important;text-decoration: none;}
</style>
<script type="text/javascript">
var projectInfo = {"ProjectID":164857,"CityID":586,"Name":"禾空间儿童剧嘉年华十次卡演出票","ShowTime":"2018.10.01-2019.02.28","Price":199.00,"SiteStatus":3,"VenueName":"禾空间小剧场","IsOnlyXuanZuo":false,"QuestionPass":false,"TicketValidateType":0,"htmlName":null,"Tabcontrol":0,"IsShowStartTime":false,"StartTicketTime":"\/Date(1538203382000)\/","SellStartTime":"\/Date(1538203382000)\/","OptimizationTicket":0};
var hostName = "wuhan", itemDomain = "piao.damai.cn", categoryId = 3, is_show_perform_calendar = 0;
is_show_perform_calendar = 1;
var PrivelegePId=108944;

var is_show_qr_code = 0;
</script>
</head>
<body data-spm='project'>
<script type="text/javascript" id="beacon-aplus" src="//g.alicdn.com/alilog/mlog/aplus_v2.js"  exparams="clog=o&aplus&sidx=aplusSidex&ckx=aplusCkx"></script>
<div class="g-hd" style="position:static;">
<div class="g-hdc">
<input type="hidden" value="%e7%a6%be%e7%a9%ba%e9%97%b4%e5%84%bf%e7%ab%a5%e5%89%a7%e5%98%89%e5%b9%b4%e5%8d%8e%e5%8d%81%e6%ac%a1%e5%8d%a1%e6%bc%94%e5%87%ba%e7%a5%a8" id="Hidden1"/>
<input type="hidden" value="我在@大麦网 『www.damai.cn』发现了一个非常不错的演出:『禾空间儿童剧嘉年华十次卡演出票』,时间是2018.10.01-2019.02.28，场馆在,强烈推荐！分享一下&gt;&gt;&gt;&gt;&gt;&gt;" id="Title"/>
<input type="hidden" value="%ba%cc%bf%d5%bc%e4%b6%f9%cd%af%be%e7%bc%ce%c4%ea%bb%aa%ca%ae%b4%ce%bf%a8%d1%dd%b3%f6%c6%b1" id="NameCN"/>
<input type="hidden" value="https%3a%2f%2fpiao.damai.cn%2f164857.html" id="LinkCN"/>
<input type="hidden" value="586" id="cityId"/>
<input type="hidden" value="武汉" id="cityName"/>
<input type="hidden" value="3" id="CategoryID" />
<input type="hidden" value="3" id="ChildCategoryID" />
<input type="hidden" value="120" id="epconfig" />
    <!-- logo begin -->
    <h1 class="m-logo"><a href="//www.damai.cn/" title="大麦网">大麦</a></h1>
    <!-- logo end -->

    <!-- 城市切换 begin -->
    <div class="m-citys">
      <span class="tt">武汉站</span>
    </div>
    <!-- 城市切换 end -->

    
    <!-- 顶部栏 begin -->
    <ul class="m-topbar">
      <li class="itm first">
        <!-- 搜索 begin -->
        <div class="m-sch">
          <input type="text" class="ipt" id="txtSearchText" placeholder="请输入演出、赛事、艺人、场馆名称..." />
          <a class="btn" href="javascript:;" id="btnSearch">搜索</a>
		  <div class="m-suggest" id="rlist_txtSearchText">
          </div>
        </div>
        <!-- 搜索 end -->
      </li>
      <li class="itm">
        <!-- 用户登录 begin -->
        <div class="m-sign m-sign-log">
			<label id="userLoginInfo">
			  <a class="user" href="javascript:;"><img original="//dui.dmcdn.cn/dm_2015/goods/images/user.png" /></a>
			  <span class="sign"><a href="//www.damai.cn/redirect.aspx?type=login">登录</a> | <a href="//www.damai.cn/redirect.aspx?type=reg">注册</a></span>
			</label>
			<div class="menu" my="menu" style="display:none;">
				<a href="//my.damai.cn/account/myinfo.aspx" target="_blank" class="first">个人信息</a>
				<a href="//order.damai.cn/index.aspx" target="_blank">订单管理</a>
				<a href="https://coupon.damai.cn/coupon-web-damai/mycoupon/myCoupon" target="_blank">我的优惠券</a>
				<a href="//www.damai.cn/redirect.aspx?type=loginout" class="exit">退出</a>
			</div>
		</div>
        <!-- 用户登录 end -->
      </li>
    </ul>
    <!-- 顶部栏 end -->
  </div>
</div>
<div class="g-bd" data-image="" data-color="">
  <div class="g-bdc">
    <div class="g-mn">
	  	
      <!-- 终极页项目信息 begin -->
      <div class="m-box m-box-col2 m-box-goods" id="projectInfo">
        <div class="hd">
          <!-- 面包屑 begin -->
          <p class="m-crm">
            			<strong>禾空间儿童剧嘉年华十次卡演出票</strong>
          </p>
          <!-- 面包屑 end -->
		          </div>

        <div class="mn">
          <!-- 项目海报 begin -->
          <div class="m-poster">
            <!-- 项目图 begin -->
            <div class="m-picbox">
                <img original="//pimg.dmcdn.cn/perform/project/1648/164857_n.jpg" title="禾空间儿童剧嘉年华十次卡演出票" alt="禾空间儿童剧嘉年华十次卡演出票" width="277" height="373" />
              
            </div>
            <!-- 项目图 end -->
            
            <!-- 分享 begin -->
            <div class="m-share" data-spm="click">
              <span class="txt">分享到：</span>
              <!-- JiaThis Button BEGIN -->
              <div class="jiathis_style">
                <a href="http://service.weibo.com/share/share.php?title=我在@大麦网 『www.damai.cn』发现了一个非常不错的演出:『禾空间儿童剧嘉年华十次卡演出票』,时间是2018.10.01-2019.02.28，场馆在,强烈推荐！分享一下&gt;&gt;&gt;&gt;&gt;&gt;&url=https%3a%2f%2fpiao.damai.cn%2f164857.html&source=bookmark&appkey=3588246140&pic=https%3A%2F%2Fpimg.dmcdn.cn%2Fperform%2Fproject%2F1648%2F164857_n.jpg&ralateUid=1722647874" class="jiathis_button_tsina" title="分享到微博" target="_blank" data-spm-click="gostr=/damai_pc.default.click;localid=share_0;dclicktitle=微博&ditem_id=164857"><span class="jiathis_txt jtico jtico_tsina"></span></a>
                <a class="jiathis_button_weixin" title="分享到微信" data-spm-click="gostr=/damai_pc.default.click;localid=share_1;dclicktitle=微信&ditem_id=164857"><span class="jiathis_txt jtico jtico_weixin"></span></a> 
                <a href="http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url=https%3A%2F%2Fpiao.damai.cn%2F164857.html&title=我在@大麦网 『www.damai.cn』发现了一个非常不错的演出:『禾空间儿童剧嘉年华十次卡演出票』,时间是2018.10.01-2019.02.28，场馆在,强烈推荐！分享一下&gt;&gt;&gt;&gt;&gt;&gt;&pics=http%3A%2F%2Fpimg.dmcdn.cn%2Fperform%2Fproject%2F1648%2F164857_n.jpg&summary=" class="jiathis_button_qzone" title="分享到QQ空间" target="_blank" data-spm-click="gostr=/damai_pc.default.click;localid=share_2;dclicktitle=QQ空间&ditem_id=164857"><span class="jiathis_txt jtico jtico_qzone"></span></a>
              </div>
              <!-- JiaThis Button END -->
            </div>
            <!-- 分享 end -->
           

          </div>
          <!-- 项目海报 end -->
          
          <!-- 项目模块 begin -->
          <div class="m-goods">
            <h2 class="tt" data-spm="click">
				 <span class="txt">禾空间儿童剧嘉年华十次卡演出票</span>
            </h2>
						<h3 class="stt">
              <span class="quotl"></span>
              <span class="txt">儿童剧嘉年华</span>
              <span class="quotr"></span>
            </h3>             
            <!-- 时间轴 begin -->
			            <div class="m-timeline m-timeline-3" id="projectAxis">
              <div class="wrap">
				                <div class="box">
                  <div class="bar"><div class="line" style="width:290px"></div></div>
				  				  <div class="itm itm-1 " style="width:145px"><h3 class="txt">项目待定</h3><div class="ico"></div><p class="date"></p></div>
				  				  <div class="itm itm-2 " style="width:145px"><h3 class="txt">预售/预订</h3><div class="ico"></div><p class="date"></p></div>
				  				  <div class="itm itm-3 itm-crt" style="width:145px"><h3 class="txt">售票中</h3><div class="ico"></div><p class="date"></p></div>
				  				  <div class="itm itm-4 " style="width:145px"><h3 class="txt">演出开始</h3><div class="ico"></div><p class="date"></p></div>
				                  </div>
              </div>
            </div>
			            <!-- 时间轴 end -->

            <!-- 产品模块 begin -->
            <div class="m-product m-product-2 -m-product-1 j_goodsDetails">
												<div class="m-goodstips m-goodstips-2" id="projectStatusDescn"  style="display:none;" >
					<div class="hd">
						<i class="ico"></i>
						<span class="txt txt-status" data-status="售票中">
						售票中						</span>
					</div>
					<div class="bd">
						<div class="tips">
							<div class="box z-hide"><p class="itm">
														
														</p></div>
							<div class="ops"><span class="btnsel"></span></div>
						</div>
					</div>
					<div class="mark" id="jinpaiMark" style="display:none;"></div>
				</div>
								
								<div id="toBeAboutTo" class="m-countdown" data-init="false" style="display:none;">
				<div class="ct"></div>
				<div class="tips"><i class="ico"></i><span class="txt j_endtime"></span></div>
				</div>
							  
                                                                                          <!-- 促销信息模块 begin -->
              <div class="" id="yhcx" data-row="4" data-col="1"></div>
			  <div class="m-load z-hide" id="getInfoFail"><p class="txt"><i></i>加载失败</p></div>
              <!-- 促销信息模块 end -->
                <!-- 选择日历模块 begin -->
                <div class="m-choose m-choose-picker" style="display:none" data-row="3" data-col="4">
                    <h3 class="tt" style="padding-top: 6px;">选择时间：</h3>
                    <div class="ct">
                    <div class="m-datepicker">
                        <div class="weekbox">
                        <div class="box"></div>
                        </div>
                        <div class="datebox">
                        <div class="box"></div>
                        </div>
                    </div>
                    </div>
                </div>
                <!-- 选择日历模块 end -->
              <!-- 选择日期模块 begin -->
			  <div class="m-choose m-choose-date  " id="performList" data-col="4" data-spm="clicktime">
                <h3 class="tt">
								演出时间：</h3>
                <div class="ct">
                  <ul class="lst lst-dis">
					<li style="line-height:32px;padding-left:10px" class="loading"><span>加载中，请稍后...</span></li>
				  </ul>
                </div>
              </div>
              <!-- 选择日期模块 end -->

			                <!-- 选择票价模块 begin -->
              <div class="m-choose m-choose-price " id="priceList" data-col="4" data-spm="clickprice">
                <h3 class="tt">选择票价：</h3>
                <div class="ct">
                  <ul class="lst lst-dis">
					<li style="line-height:32px;padding-left:10px" class="loading"><span>加载中，请稍后...</span></li>
				  </ul>
				  <div class="tips-warn z-hide" id="warnXiangou"><span class="txt"></span></div>
				  <div class="tips tips-oos"><span class="ico"></span><span class="txt">暂时无货，登录试试运气~</span></div>
                </div>
              </div>
              <!-- 选择票价模块 end -->
			                 
              <!-- 购物车模块 begin -->
              <div class="m-cart  " id="cartList" style="display:none;" data-spm="click">
                <h3 class="tt" style="display:none;">您选择了：</h3>
                <div class="ct" style="display:none;">
                  <ul class="lst"></ul>
                </div>

				<div class="ops">
				  				  <a href="javascript:;" class="u-btn u-btn-c1 u-btn-choose" id="btnXuanzuo" style="display:none;" data-spm-click="gostr=/damai_pc.default.click;localid=buyselectseatbtn;ditem_id=164857">选座购买</a>
				                                      <a class="u-btn u-btn-buynow" href="javascript:;" id="btnBuyNow" data-spm-click="gostr=/damai_pc.default.click;localid=fastbuybtn;ditem_id=164857">立即购买</a>
                                   </div>

              </div>
              <!-- 购物车模块 end -->

								<div class="m-probox m-remine" id="kaishoutixingLayer" style="display:none;">
				<input type="text" placeholder="请输入接收信息的手机号" class="u-ipt u-ipt-md" id="kaishoutixingPhone">
				<a class="u-btn u-btn-md u-btn-remind" href="javascript:kaishoutixing;" id="btnKaishoutixing"><i class="ico"></i><span class="txt">开售提醒</span></a>
				</div>
				
                                          
                            
                                          
                            <div id="jinpaiCounter" class="m-countdown" data-init="false" style="display:none;">
				<div class="ct"><span class="lab">距抢座开始：</span>
				<span class="num num-0">0</span><span class="num num-0">0</span><span class="txt">小时</span>
				<span class="num num-0">0</span><span class="num num-0">0</span><span class="txt">分</span>
				<span class="num num-0">0</span><span class="num num-0">0</span><span class="txt">秒</span></div>
				<div class="tips"><i class="ico"></i><span class="txt"></span></div>
			  </div>
              <div class="m-goodstab" id="jinpaiTabs" style="display:none;">
                <div class="hd">
                  <ul class="tab">
                    <li class="itm itm-tab j_tabOrders f-dn">我的抢座</li>
                    <li class="itm itm-tab z-crt j_tabLives">抢座实况</li>
                    <li class="itm itm-tab j_tabGroups f-dn">查看分组说明</li>
                  </ul>
                  <div class="sort" id="jinpaiMyRanking" style="margin-right:8px;">我的排名：<strong>-</strong></div>
                </div>
                <div class="bd">
                  <div class="itm itm-tab f-dn" id="jinpaiOrders">
                    <table rules="rows" class="m-table">
                      <thead>
                        <tr>
                          <th class="cola">订单号</th>
                          <th class="colb">票价（数量）</th>
                          <th class="cola">排名</th>
                          <th class="cola">分组</th>
                          <th class="colc">进场时间</th>
                          <th>操作</th>
                        </tr>
                      </thead>
                      <tbody></tbody>
                    </table>
                  </div>
                  <div class="itm itm-tab z-show" id="jinpaiLives">
                    <!-- 抢座实况 begin -->
                    <div class="m-grablive">
                      <div class="inner">
                        <ul class="lst" id="jinpaiLiveList"></ul>
                      </div>
                    </div>
                    <!-- 抢座实况 end -->
                  </div>
                  <div class="itm itm-tab f-dn" id="jinpaiGroupList">
                    <!-- 查看分组说明 begin -->
                    <div class="m-groupshow">
                      <div class="inner">
                        <ul class="lst"></ul>
                      </div>
                    </div>
                    <!-- 查看分组说明 end -->
                  </div>
                </div>
              </div>
              
                                          
                                          
			  			  <a name="projectPrivilege" id="privilegeAnchor"></a>
			  
                                <div class="m-qrcode"><!-- 大麦网客户端二维码 -->
                    <h3 class="tt"><span id="ErWeiMaTips">手机扫一扫<br />下单更快捷</span></h3>
                    <p class="ct"><img original="//static.dmcdn.cn/Erweima/1648/164857.jpg" alt="大麦网客户端" width="109" height="108"/></p>
                </div>
                              			  <div class="m_heighlight_tip"></div>
			              </div>
            <!-- 产品模块 end -->
          </div>
          <!-- 项目模块 end -->
        </div>
        
        <!-- 侧栏 begin -->
        <div class="sd">
		  		  		  
		  		  		  
		            <div class="m-sdbox m-showtime">
			

			            <h2 class="tt">演出时间</h2>
            <div class="ct">
              <span class="txt">2018.10.01-2019.02.28</span>
			                <a href="javascript:;" class="u-btn u-btn-cal" id="rili" onClick="showcalendar(event, this); return false;" onFocus="showcalendar(event, this);"><i>日历</i></a>
			              </div>
			
          </div>
		  

		            <!-- 演出场馆 begin -->
          <div class="m-sdbox m-venue">
            <h2 class="tt">演出场馆</h2>
            <div class="ct">
			  <p class="txt"> 禾空间小剧场 </p>
                          </div>
          </div>
          <!-- 演出场馆 end -->
		  
          <!-- 票品支持 begin -->
          <div class="m-sdbox m-support">
            <h2 class="tt">票品支持</h2>
            <div class="ct">
              <ul  class="m-mantab">
                                                                 <li class="itm"><a href="javascript:;" class="u-btn u-btn-super"><i></i>超级票</a>
					<div class="layer">
							<div class="hd"><a href="javascript:;" class="btn-close">关闭</a></div>
							<div class="bd">
								<p>1.本项目支持使用【电子钱包-超级票账户】消费，支付时优先扣减超级票余额。</p><p>2.超级票成功充值电子钱包后，享受全网通兑、分次消费、无有效期限制、无使用张数限制、秒杀、抢票等服务。</p>
							</div>
							<div class="ft">
								<a href="javascript:;" class="btn btn-close">关闭</a>
							</div>
						</div>
				  </li>
                                                  <li class="itm"><a href="javascript:;" class="u-btn u-btn-wallet"><i></i>电子钱包</a>
						<div class="layer">
							<div class="hd"><a href="javascript:;" class="btn-close">关闭</a></div>
							<div class="bd">
								<p>本项目支持电子钱包。</p>
              <p>1. 电子钱包是由大麦网自主研发的第三方支付平台</p>
              <p>2. 为每一个用户在购票过程中提供"简单、安全、快速"的在线支付解决方案</p>
							</div>
							<div class="ft">
								<a href="javascript:;" class="btn btn-close">关闭</a>
							</div>
						</div>
				  </li>

                                                                  <li class="itm"><a href="javascript:;" class="u-btn u-btn-credit"><i></i>返积分</a>
						<div class="layer">
							<div class="hd"><a href="javascript:;" class="btn-close">关闭</a></div>
							<div class="bd">
                                                                      <p>【会员多倍积分】 大麦会员按不同等级可分别获得消费金额×50%到100%比例的积分返还</p>
                                  								<p>您可以在积分商城兑换明星周边、演出票品、优惠卡券等商品，也可以参与抽奖活动，赢取幸运大礼。</p>
							</div>
							<div class="ft">
								<a href="javascript:;" class="btn btn-close">关闭</a>
							</div>
						</div>
				  </li>
                                                               <!-- -->

                
				
									<li class="itm"><a href="javascript:;" class="u-btn u-btn-selftake"><i></i>上门自取</a></li>
				
									<li class="itm"><a href="javascript:;" class="u-btn u-btn-express"><i></i>快递</a></li>
				              </ul>
            </div>
          </div>
          <!-- 票品支持 end -->
		  
		            <!-- 实票配送 begin -->
          <div class="m-sdbox m-entity" id="freight">
            <h2 class="tt"> 实票配送</h2>
            <div class="ct">
              <div class="u-sel u-sel-c1 u-sel-entity">
                <div class="hd">
                  <span class="txt">北京</span>
                  <span class="ico"></span>
                </div>
                <div class="menu">
                  <ul class="lst"></ul>
                </div>
              </div>
              <p class="tips">加载中...</p>
            </div>
          </div>
          <!-- 实票配送 end -->
		  
        </div>
        <!-- 侧栏 end -->
        
      </div>
      <!-- 终极页项目信息 end -->
      
      <!-- 终极页项目详情 begin -->
      <div class="m-box m-box-col2">
        <div class="mn">
          <!-- 项目详情 begin -->
          <div class="m-detail">
            <!-- 项目详情选项卡 begin -->
            <div class="m-infonav" id="m-infonav">
              <div class="hd">
                <div class="nav">
                    <ul class="tab">
                        <li><a data-href="#m-infonav" href="javascript:;" class="itm itm-tab first z-crt" id="tabProjectDescn" data-show="1,2" data-idx="0"><i></i><span class="txt">演出信息</span></a></li>
						<li><a data-href="#m-infonav" href="javascript:;" class="itm itm-tab" data-idx="3"><i></i><span class="txt">购买说明</span></a></li>
                        <li><a data-href="#m-infonav" href="javascript:;" class="itm itm-tab" data-idx="4"><i></i><span class="txt">付款方式</span></a></li>
						                    </ul>

															<div class="buy" id="buyButtonC" style="display:none;">
												<a href="javascript:;" class="u-btn u-btn-buy " id="btnXuanzuo2" style="display:none;"><i class="ico"></i><span class="txt">选座购买</span></a>
																		<a href="javascript:;" class="u-btn u-btn-cart " id="btnBuyNow2"><i class="ico"></i><span class="txt">立即购买</span></a>
											</div>
					                </div>
              </div>
              <div class="bd">
                <div class="itm-tab z-show" rel="0">
                  <!-- 演出信息 begin -->
                  <div class="m-infobase m-liveinfo">
										<dl class="infoitm">
                      <dt class="tt"><span class="txt">基本信息</span></dt>
                      <dd class="ct">
                        <div class="table-info">
							                          <table class="m-table2">
                            <tbody>
							  <tr>
							                                  <td width="90" class="bg">演出时间</td><td>2018.10.01-2019.02.28</td>  							                                  <td width="90" class="bg">演出场馆</td><td width="200">禾空间小剧场</td>                                 </tr><tr> 							                                  <td width="90" class="bg">演出时长</td><td>最低演出时长 60分钟</td> 							  							                                  <td width="90" class="bg">入场时间</td><td width="200">演出前约30分钟</td> 							   </tr><tr>                               							   </tr><tr>                                                              </tr><tr> 							                                 </tr><tr> 							  								<td class="bg">限购</td><td>立即购买每单限20张。</td>                               							  							  							                                							                                  <td class="bg">儿童入场提示</td><td>儿童一律凭票入场</td> 							  							   </tr><tr> 								<td class="bg">座位类型</td><td>不对号入座</td> 							  							  							  							    							  							    								<td class="bg">禁止携带物品</td>
								<td>由于安保和版权的原因，大多数演出、展览及比赛场所禁止携带食品、饮料、专业摄录设备、打火机等物品，请您注意现场工作人员和广播的提示，予以配合。</td>
																 </tr>  <tr>  															  							    								<td class="bg">付款时效提醒</td>
								<td>购票下单成功后需在15分钟内完成支付，未支付成功的订单，将在下单15分钟后系统自动取消，所选价位将自动释放后重新点亮，大家可及时刷新购票页面进行购买。</td>
																															  							    								<td class="bg">缺货登记提醒</td>
								<td>所需票价若为灰色，说明已经售完。您可以在当前页面进行缺货登记，后期如果有票会以短信形式及时通知。</td>
																 </tr>  <tr>  															  							    								<td class="bg">发票说明</td>
								<td>发票由现场提供，演出当天请持门票到演出场馆开具</td>
																															  							    							  							    								<td class="bg">座位类型</td>
								<td>无具体位置号，请听从现场安排，有序进场入座</td>
																 </tr>  <tr>  															  							    								<td class="bg">物品寄存</td>
								<td>无寄存处，请自行保管携带物品</td>
																															  							    								<td class="bg">有无中文字幕</td>
								<td>演出现场无字幕</td>
																 </tr>  <tr>  															  							    								<td class="bg">演出语言</td>
								<td>普通话</td>
																															  							    								<td class="bg">退换说明</td>
								<td>票品不支持退换。如无法正常观看，还请自行处理，给您带来不便敬请谅解</td>
																 </tr>  <tr>  															  							    								<td class="bg">主演演员（团体）</td>
								<td>不漏文化</td>
																															  							    								<td class="bg">大麦网首次开售时全场可售门票总张数</td>
								<td>1000张</td>
																 </tr>  <tr>  															  							    								<td class="bg">票品类型</td>
								<td>二维码电子票</td>
																															  							    								<td class="bg">入场方式</td>
								<td>纸质票入场</td>
																 </tr>  <tr>  															  							    								<td class="bg">取票方式</td>
								<td>场馆取票</td>
																															  							    								<td class="bg">表演形式</td>
								<td>真人表演</td>
																 </tr>  															  
							                              </tbody>
                          </table>
                        </div>
                      </dd>
                    </dl>
					
															
					
					
															<dl class="infoitm">
                      <dt class="tt"><span class="txt">项目介绍</span></dt>
                      <dd class="ct">
						<div class="pre"><h4>
	演出介绍
</h4>
时间：10月1日-10月31日<br />
地点：武汉市岳家嘴金禾时尚禾空间<br />
介绍：<br />
原价亲子双人199元/套<br />
（10月1日起开售至10月31日停售）<br />
内含：<br />
购票即日起至12月31日底，可观看禾空间小剧场十场演出，划次销卡。（儿童剧目及不low俱乐部出品演出，如有外包剧目不含在内）并送机构体验课券2张，盖章折纸一份，公仔一个（仅限预购和嘉年华期间）。</div>
                      </dd>
                    </dl>
										
					
															<dl class="infoitm">
                      <dt class="tt"><span class="txt">温馨提示</span></dt>
                      <dd class="ct">
                        <div class="table-info">
                          <table class="m-table2">
                            <tbody>
							  							  							  							  							  							                                <tr>
                                <td class="bg">发票说明</td><td>发票由现场提供，演出当天请持门票到演出场馆开具</td>
                              </tr>
							  							  							                              </tbody>
                          </table>
                        </div>
                      </dd>
                    </dl>
										                      
					                  </div>
                  <!-- 演出信息 end -->
                </div>
				<!-- 1 -->
                
                <div class="itm-tab" rel="3">
                  <!-- 购票说明 begin -->
                  <div class="m-infobase m-buydesc">
                    <dl class="infoitm">
                      <dt class="tt"><span class="txt">特别提示</span></dt>
                      <dd>
                        <h3 class="stt">售前提示</h3>
                        <p>1.为避免快递配送不能及时送达，演出距开场时间少于3天时不提供【快递配送】服务，请您谅解！您可以选择电子票或在线支付后上门自取纸质票。 <a href="//help.damai.cn/damai/contents/277/5966.html" target="_blank" title="点击查看上门取票地址">点击查看上门取票地址&gt;&gt;</a></p></dd>
                      <dd>
                        <p>2.凡演出票类商品，开票时间一般为演出前二到四周，正式开票后会第一时间短信通知您，请注意接收。</p>
                      </dd>
					  <dd>
                        <p>3.如您不是通过“选座购买”通道进行的票品购买，最终票品数量视项目主办方及场馆情况而定，正式开票后大麦网将根据用户付款先后顺序依次配票，可能存在票品不足不能为您配票的风险，如最终未能配票，大麦网承诺全额退款，但不承担其他损失。</p>
                      </dd>
                      <dd>
                        <h3 class="stt">支付方式</h3>
                        <p>网上银行（招商银行等） 支付平台（支付宝等） 转账汇款(招商银行等)　<a href="//help.damai.cn/damai/contents/281/5740.html" target="_blank" title="查看详情">查看详情&gt;&gt;</a></p>
                      </dd>
                      <dd>
                        <h3 class="stt">退/换货说明</h3>
                        <p>针对不可抗力和非不可抗力的退/换票情况和处理，请点击查阅<a title="大麦网退换货说明" target="_blank" href="//help.damai.cn/damai/contents/299/2228.html">大麦网退换货说明&gt;&gt;</a></p>
                      </dd>
                    </dl>
                    <dl class="infoitm">
                      <dt class="tt"><span class="txt">无线端购票</span></dt>
                      <dd>
                        <p>1.  使用智能设备用户在各应用商店中搜索"大麦"下载安装客户端，购票体验更流畅</p>
                        <p>2.  非智能设备用户可浏览器访问m.damai.cn进行演出查询，随时购票</p>
                      </dd>
                      <dd class="appdown">
                        <div class="applnk">
                          <a href="//mapi.damai.cn/href.aspx?id=1" target="_blank" class="iphone">iphone版</a>
                          <a href="//mapi.damai.cn/href.aspx?id=2" target="_blank" class="ipad">ipad版</a>
                          <a href="//mapi.damai.cn/href.aspx?id=5" target="_blank" class="android">android版</a>
                        </div>
                      </dd>
                    </dl>
                    <dl class="infoitm">
                      <dt class="tt"><span class="txt">网上订购</span></dt>
                      <dd><img original="//dui.dmcdn.cn/dm_2015/goods/images/process.jpg" -src="//dui.dmcdn.cn/dm_2015/goods/img/process.jpg"></dd>
                    </dl>
                                        <dl class="infoitm" id="orderOnCompany">
                      <dt class="tt"><span class="txt">上门订购</span></dt>
					  					  <dd>
						<p>大麦网武汉分部</p>
						<p>办公地址：武汉市武昌区临江大道96号武汉万达中心写字楼611-612 （积玉桥万达威斯汀酒店旁） <a href="//map.damai.cn/Traffic/goThere.aspx?endCity=%e6%ad%a6%e6%b1%89&to=1&end_x_y=114.308719,30.564207&end=%e5%a4%a7%e9%ba%a6%e7%bd%91%e6%ad%a6%e6%b1%89%e5%88%86%e9%83%a8" class="c7" target="_blank" title="点击查看如何到达">点击查看如何到达</a></p>
						<p>营业时间：周一至周六 9:00-18:00</p>
						<p>支付说明：上门支持现金支付和刷卡支付 <a href="//map.damai.cn/traffic/circumjacent.aspx?action=search&cityName=%e6%ad%a6%e6%b1%89&cityId=586&Keyword=%e5%a4%a7%e9%ba%a6%e7%bd%91%e6%ad%a6%e6%b1%89%e5%88%86%e9%83%a8&option=bank&CenterLngLat=114.308719,30.564207" target="_blank" title="点击查看周边提款" class="c7">点击查看周边提款</a></p>
					  </dd>
					                      </dl>
					                  </div>
                  <!-- 购票说明 end -->
                </div>
                <div class="itm-tab" rel="4">
                  <!-- 付款方式 begin -->
                  <div class="m-infobase m-paymode" style="display: block;">
                    <dl class="infoitm">
                      <dt class="tt"><span class="txt">在线支付</span></dt>
                      <dd><p>支持多家网上银行、支付平台（支付宝、快钱、银联、微信支付等）在线支付，<a href="//help.damai.cn/damai/channels/281.html" target="_blank">查看详情&gt;&gt;</a></p></dd>
                      <dd>
                        <h3 class="stt">支付平台：</h3>
                        <ul class="lst">
                                                      <li><img original="//static.dmcdn.cn/PayLogo/2.jpg" alt="支付宝" style="display: inline;" /></li>
                                                      <li><img original="//static.dmcdn.cn/PayLogo/57.jpg" alt="微信扫码支付" style="display: inline;" /></li>
                                                  </ul>
                      </dd>
                      <dd>
                        <h3 class="stt">网上银行：</h3>
                        <ul class="lst">
                                                        <li><img original="//static.dmcdn.cn/PayLogo/10.jpg" alt="招商银行" style="display: inline;" /></li>
                                                        <li><img original="//static.dmcdn.cn/PayLogo/11.jpg" alt="中国建设银行" style="display: inline;" /></li>
                                                        <li><img original="//static.dmcdn.cn/PayLogo/12.jpg" alt="中国工商银行" style="display: inline;" /></li>
                                                        <li><img original="//static.dmcdn.cn/PayLogo/13.jpg" alt="交通银行" style="display: inline;" /></li>
                                                        <li><img original="//static.dmcdn.cn/PayLogo/14.jpg" alt="中国农业银行" style="display: inline;" /></li>
                                                        <li><img original="//static.dmcdn.cn/PayLogo/15.jpg" alt="广东发展银行" style="display: inline;" /></li>
                                                        <li><img original="//static.dmcdn.cn/PayLogo/17.jpg" alt="中国银行" style="display: inline;" /></li>
                                                        <li><img original="//static.dmcdn.cn/PayLogo/23.jpg" alt="上海浦东发展银行" style="display: inline;" /></li>
                                                    </ul>
                      </dd>
                    </dl>
                    <dl class="infoitm">
                      <dt class="tt"><span class="txt">柜台付款</span></dt>
                      <dd><p>您也可以选择就近的公司网点，到柜台直接付款购买，<a href="//help.damai.cn/damai/channels/284.html" target="_blank">查看分公司上门地址&gt;&gt;</a></p></dd>
                    </dl>
                  </div>
                  <!-- 付款方式 end -->
                </div>

				<div class="itm-tab" rel="5">
                  <!-- 先付先抢 begin -->
                  <div class="m-infobase m-payrob">
                    <div class="infoitm">
                      <dt class="tt"><span class="txt">详情介绍</span></dt>
                      <dd>
                        <p>1.“先付先抢”是大麦网为广大用户推出的一项全新“特权”服务。凡是标有“先付先抢”活动图标的项目，只要在预售阶段付款成功，都将在正式开票前的2-24小时，获得优先于其他用户自主选座的权利。</p>
                        <p>2.付款成功后，您将在付款成功页面得到一个系统分配的排号，您也可以登录订单详情页面查看该号码。排号是完全按照付款成功的先后顺序分配，不区分票价。抢座开始前，会发送短信告知抢座时间，并对所有的排号进行分组，排号越靠前，被分入提前选座分组的机会越大，最大程度确保先付款用户的利益，所以，不要犹豫哦，马上占领先机！</p>
                        <p>3.大麦网提供所有可售座位进行抢座，由用户自行选择；相对于传统预售配票，更加透明化，保证公平、公正、公开！</p>
                        <p>4.如果因为时间关系或其他原因，未能及时参与抢座，您也无需担心。抢座结束后，大麦网工作人员会按照付款先后顺序依次挑选座位进行配票。</p>
                        <p><a href="//help.damai.cn/damai/contents/292/5706.html" target="_blank"><img original="//dui.dmcdn.cn/damai_v2/goods/img/grab-pic02.jpg" alt=""></a></p>
                      </dd>
                    </div>
                    <div class="infoitm">
                      <dt class="tt"><span class="txt">无线端先付先抢详情</span></dt>
                      <dd>
                        <p>为方便用户随时随地抢票，大麦客户端同样支持先付先抢功能，且比网站更快更流畅的购买成功。</p>
                        <p>请您按照如下提示下载大麦客户端：</p>
                        <ul class="tab-ul-txt">
                          <li>iPhone、iPad、Android、Windows Phone等智能设备用户可在各应用市场（如App Store、安卓市场等）搜索"大麦"进行下载安装</li>
                          <li>无法安装客户端的用户可浏览器访问m.damai.cn进行购票。</li>
                        </ul>
                      </dd>
                    </div>
                    <div class="infoitm">
                      <dt class="tt"><span class="txt">温馨提示</span></dt>
                      <dd>
                        <p>1.现金支付、转账汇款、第三方渠道购买和上门付款的订单不支持本次抢座活动，付款成功后您将获得系统分配的排号，请您留意支付成功页面，或登录网站“订单管理-订单详情”查看排号；</p>
                        <p>2.正式抢座从可以入场开始，直到抢座结束，期间任何时候都能进行抢座；</p>
                        <p>3.部分手机或软件存在短信屏蔽功能，可能导致您收不到大麦网发送的短信提醒。</p>
                        <div class="tab-grab-map-tis clear">
                          <a target="_blank" href="//mobile.damai.cn/" class="mtn fl"><img style="display:inline;" original="//dui.dmcdn.cn/damai_v2/goods/img/grab-pic03.png"></a>
                          <a target="_blank" href="//news.damai.cn/trends/a/20120528/1365.shtml" class="fr"><img style="display: inline;" original="//dui.dmcdn.cn/damai_v2/goods/img/grab-pic04.png"></a>
                        </div>
                      </dd>
                    </div>
                  </div>
                  <!-- 先付先抢 end -->
                </div>

              </div>
            </div>
            <!-- 项目详情选项卡 end -->
          </div>
          <!-- 项目详情 end -->
        </div>
        <div class="sd">
			<div class="subitem">
            <ul>
            	<li class="s-ion1">
                <a >
                  <p class="s-t1">大麦客户端</p><p class="s-t2">抢票神器！随时随地尊享优惠</p>
                  <span class="s-ewm" style="display: none;"><img src="//dui.dmcdn.cn/dm_2015/goods/img/kehuduan.png"><strong class="f14">比PC更迅猛</strong><br><strong>提前开抢</strong></span>
                </a>
              </li>
            </ul>
          </div>

				        		  <!-- 热门推荐 begin -->
          <div class="m-sdbox2-first" id="hotProjects"></div>
          <!-- 热门推荐 end-->
          
		<!-- 抢票速度榜 begin -->
                <!-- 抢票速度榜 end -->

		           <!-- 浏览历史 begin -->
          <div class="m-sdbox2 m-sdbox2-first m-history" id="lishiurl" style="display:none;">
            <div class="hd">
              <h2 class="tt">浏览历史</h2>
            </div>
              <div class="bd">
              <ul class='m-sdlst'></ul>
             </div>
          </div>
          <!-- 浏览历史 end -->
		          
       

          
		            <!-- 大麦微博 begin -->
          <div class="m-sdbox2  m-weibo">
            <div class="hd">
              <h2 class="tt">大麦微博</h2>
            </div>
            <div class="bd">
                <div class="player" id="weibo_con_"></div>
            </div>
          </div>
          <!-- 大麦微博 end -->
		  		  
        </div>
      </div>
      <!-- 终极页项目详情 end -->
    </div>
    
  </div>
</div>
<div class="g-ft">
  <div class="m-ft1">
    <div class="bd">
      <!-- 底部链接 begin -->
      <div class="m-lnks">
                           <a href="https://help.damai.cn/helpPage.htm" target="_blank">帮助中心</a>
                                |<a href="https://help.damai.cn/helpPage.htm?pageId=69" target="_blank">公司介绍</a>
                                |<a href="https://help.damai.cn/helpPage.htm?pageId=70" target="_blank">品牌识别</a>
                                |<a href="https://help.damai.cn/helpPage.htm?pageId=72" target="_blank">大麦大事记</a>
                                |<a href="https://help.damai.cn/helpPage.htm?pageId=40" target="_blank">隐私权专项政策</a>
                                |<a href="https://jubao.alibaba.com/internet/readme.htm" target="_blank">廉正举报</a>
                                |<a href="https://help.damai.cn/helpPage.htm?pageId=58" target="_blank">联系合作</a>
                                |<a href="https://job.alibaba.com/zhaopin/positionList.htm" target="_blank">招聘信息</a>
                                |<a href="https://x.damai.cn/markets/special/fangzhapian" target="_blank">防骗秘籍</a>
                          </div>
      <!-- 底部链接 end -->
    </div>
  </div>
  <div class="m-ft2">
    <div class="bd">
      <!-- 版权信息 begin -->
      <div class="m-cprt">
        <p>
			<a href="http://www.miitbeian.gov.cn" target="_blank">京ICP证031057号</a><span>|</span>
			<a href="http://www.miitbeian.gov.cn" target="_blank">京ICP备11043884号</a><span>|</span>
			<a href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010102000430" target="_blank">
				<img src="//dui.dmcdn.cn/dm_2014/common/img/police.png" class="vm" />京公网安备11010102000430号
			</a>
			<a href="//dui.dmcdn.cn/dm_2014/common/img/logo/gbdsjm.jpg" target="_blank">广播电视节目制作经营许可证 (京)字第02253号</a>
			<br>
			<a href="//dui.dmcdn.cn/dm_2014/common/img/logo/wlwhjy.jpg?v2016" target="_blank">网络文化经营许可证 京网文[2016]3438-413号</a><span>|</span>
			<a href="//dui.dmcdn.cn/dm_2014/common/img/logo/yyxyc.jpg" target="_blank">营业性演出许可证 京市演587号</a>
		</p>
		<p>北京红马传媒文化发展有限公司 版权所有 大麦网 Copyright 2003-2019 All Rights Reserved</p>
        <p>
          <a rel="nofollow" title="中国票务在线" target="_blank" href="//www.damai.cn/"><img class="mr10" alt="" original="//dui.dmcdn.cn/dm_2014/common/img/logo/piao.png"></a>
          		  <a href="//dui.dmcdn.cn/dm_2014/common/img/logo/dzyyzz.jpg" target="_blank" title="电子营业执照" rel="nofollow"><img original="//dui.dmcdn.cn/dm_2014/common/img/logo/dzyy.png" alt="" class="mr10" src="//dui.dmcdn.cn/dm_2014/common/img/logo/dzyy.png" style="display: inline;"></a>
          		  <span id="siteseal">
		   <script async="" type="text/javascript">
	function verifySeal() {
		var bgHeight = "null";
		var bgWidth = "593";
		var url = "https:\/\/seal.godaddy.com\/verifySeal?sealID=LU6rXPgk5BZ67ZEYpYS2JcN3AyCJOs6aD3HBo4dwA3iGeqp6csKFmqgB0zLL";
		window.open(url,'SealVerfication','menubar=no,toolbar=no,personalbar=no,location=yes,status=no,resizable=yes,fullscreen=no,scrollbars=no,width=' + bgWidth + ',height=' + bgHeight);
	}
</script>
<img style="cursor:pointer;cursor:hand" src="//www.damai.cn/dm2015/images/siteseal_gd_3_h_l_m.gif" onclick="verifySeal();" alt="SSL site seal - click to verify">		  </span>
          <a rel="nofollow" target="_blank" href="https://www.pcisecuritystandards.org/"><img original="//dui.dmcdn.cn/dm_2014/common/img/logo/pci.png" class="mr10"></a>
          <a rel="nofollow" target="_blank" href="http://www.itrust.org.cn/home/index/itrust_certifi/wm/1756737221"><img original="//dui.dmcdn.cn/dm_2014/common/img/logo/xin.png" class="mr10"></a>
          <a target="_blank" href="https://search.szfw.org/cert/l/CX20130327002367002885" id="___szfw_logo___"><img original="//www.damai.cn/images/chengxin.png"></a>
		          </p>
      </div>
      <!-- 版权信息 end -->
    </div>
  </div>
</div>

<!-- 蒙版 begin -->
<div class="m-mask z-hide"></div>
<!-- 蒙版 end -->


<!-- 缺货登记弹层 begin -->
<div class="m-layer m-layer-oos z-hide -m-hu" id="layerQuehuodengji">
<form>
  <div class="hd">
    <h2 class="tt">缺货登记</h2>
    <a href="javascript:;" class="u-btn u-btn-close"><span class="ico"></span></a>
  </div>
  <div class="bd">
    <!-- 缺货登记模块 begin -->
    <div class="m-oos">
      <div class="desc">
        <p>此价格票品暂时缺货，您可以进行缺货登记。</p>
        <p>为了方便有票时能够按照登记顺序通知您，我们将记录您的相关信息；若始终缺货，将不做另行通知。</p>
      </div>
      <ul class="fm">
        <li class="fmitm">
          <label class="lab">数&nbsp;&nbsp;&nbsp;&nbsp;量：</label>
          <div class="ipt">
            <!-- <div class="u-sel"> -->
            <div class="u-sel" data-context=".fmitm">
              <div class="hd">
				<span class="txt">1</span>
                <span class="btnsel"></span>
              </div>
              <div class="menu">
                <ul class="lst j_count">
				  <li><a class="itm z-crt" href="javascript:;">1</a></li>
				  <script type="text/javascript">
					for(var i = 2; i <= 20; i++) {
						document.write('<li><a class="itm" href="javascript:;">' + i + '</a></li>');
					}
				  </script>
                </ul>
				<input type="hidden" name="count" value="1" />
              </div>
            </div>
          </div>
        </li>
        <li class="fmitm">
          <label class="lab">手机号码：</label>
          <div class="ipt">
            <input type="text" name="mobilePhone" class="u-ipt u-ipt-sm" value="" />
			<span class="c1">*</span>
          </div>
        </li>
        <li class="fmitm">
          <label class="lab">留&nbsp;&nbsp;&nbsp;&nbsp;言：</label>
          <div class="ipt">
            <textarea class="u-ipt u-ipt-lg" name="notes"></textarea>
          </div>
        </li>
        <li class="fmitm fmitm-1">
          <div class="ipt"><a href="javascript:;" class="u-btn" id="btnQuehuodengji">提交</a></div>
        </li>
      </ul>
    </div>
	<!-- 缺货登记模块 end -->
  </div>
  <input type="hidden" name="performId" value="" />
  <input type="hidden" name="performName" value="" />
  <input type="hidden" name="performTime" value="" />
  <input type="hidden" name="priceId" value="" />
  <input type="hidden" name="price" value="" />
  <input type="hidden" name="pricename" value="" />
  <input type="hidden" name="enStr" value="" />
</form>
</div>
<!-- 缺货登记弹层 end -->

<!-- 手机客户端下载弹层 begin -->
<div class="m-layer m-layer-appdown z-hide" id="appDownLayer">
  <div class="hd">
    <h2 class="tt">手机客户端下载</h2>
    <a href="javascript:;" class="u-btn u-btn-close"><span class="ico"></span></a>
  </div>
  <div class="bd">
    <div class="m-appdown">
      <div class="qrcode">
        <div class="code"></div>
        <p class="txt">手机扫描快速下载</p>
      </div>
      <ul class="lst">
        <li class="itm iphone"><a href="http://itunes.apple.com/cn/app/da-mai/id513829338?mt=8" target="_blank">iPhone版</a></li>
        <li class="itm android"><a href="//mapi.damai.cn/href.aspx?id=11" target="_blank">Android版</a></li>
        <li class="itm ipad"><a href="http://itunes.apple.com/cn/app//id481947980?mt=8" target="_blank">iPad版</a></li>
      </ul>
    </div>
  </div>
</div>
<!-- 手机客户端下载弹层 end -->

<!-- 开售提醒弹层 begin -->
<div class="m-layer m-layer-remind z-hide" id="layerRemind">
  <div class="hd">
    <h2 class="tt">提示</h2>
    <a href="javascript:;" class="u-btn u-btn-close"><span class="ico"></span></a>
  </div>
  <div class="bd">
    <!-- 开售提醒模块 begin -->
    <div class="m-remind">
      <p class="tips"><i class="ico ico-succ"></i><span class="txt">成功设置项目开售提醒！</span></p>
      <p class="desc">我们将在项目开售前以短信的方式通知您</p>
	      <!-- 开售提醒模块 end -->
	</div>
  </div>
</div>
<!-- 开售提醒弹层 end -->


<!--您输入的特权码无效，请重试 begin-->
<div class="m-layer m-layer-error z-hide" id="privilege_error">
  <div class="hd">
    <a href="javascript:;" class="u-btn u-btn-close"><span class="ico"></span></a>
  </div>
  <div class="bd">
    <div class="m-error">
      <p class="tips"><i class="ico-tips"></i><span class="txt" id="privilegeErrorMsg">您输入的特权码无效，请重试</span></p>
      <div class="ops">
        <a href="javascript:;" class="u-btn j_btnOk">确定</a>
      </div>
    </div>
  </div>
</div>
<!--您输入的特权码无效，请重试 end-->

<!--您的操作过于频繁，请稍后重试 begin-->
<div class="m-layer m-layer-error z-hide" id="privilege_error_307">
  <div class="hd">
    <a href="javascript:;" class="u-btn u-btn-close"><span class="ico"></span></a>
  </div>
  <div class="bd">
    <div class="m-error">
      <p class="tips"><i class="ico-tips"></i><span class="txt">您的操作过于频繁，请稍后重试</span></p>
      <div class="ops">
        <a href="javascript:;" class="u-btn">确定</a>
      </div>
    </div>
  </div>
</div>
<!--您的操作过于频繁，请稍后重试 end-->

<!--本项目需M3、M4 会员等级用户才可购买 begin-->
<div class="m-layer m-layer-error z-hide">
  <div class="hd">
    <a href="javascript:;" class="u-btn u-btn-close"><span class="ico"></span></a>
  </div>
  <div class="bd">
    <div class="m-error">
      <p class="tips"><i class="ico-tips"></i><span class="txt">本项目需M3、M4 <br/>会员等级用户才可购买</span></p>
      <div class="ops">
        <a href="javascript:;" class="u-btn">查看等级</a>
        <a href="javascript:;" class="u-btn u-btn-c2">取消</a>
      </div>
    </div>
  </div>
</div>
<!--本项目需M3、M4 会员等级用户才可购买 end-->

<!--您的账户未完成实名认证 begin-->
<div class="m-layer m-layer-error z-hide">
  <div class="hd">
    <a href="javascript:;" class="u-btn u-btn-close"><span class="ico"></span></a>
  </div>
  <div class="bd">
    <div class="m-error">
      <p class="tips"><i class="ico-tips"></i><span class="txt">您的账户未完成实名认证</span></p>
      <div class="ops">
        <a href="javascript:;" class="u-btn">去认证</a>
        <a href="javascript:;" class="u-btn u-btn-c2">取消</a>
      </div>
    </div>
  </div>
</div>
<!--您的账户未完成实名认证 end-->

<!--请输入特权码 begin-->
<div class="m-layer m-layer-code z-hide" id="privilege_error_404">
  <div class="bd">
    <div class="m-error">
      <p class="tips"><i class="ico-tips"></i><span class="txt">请输入用户特权码</span></p>
      <div class="ops">
        <a href="javascript:;" class="u-btn">确定</a>
      </div>
    </div>
  </div>
</div>
<!--请输入特权码 end-->

<div class="m-layer z-hide" id="layerWeiShare">
  <div class="hd">
    <h2 class="tt" style="font-size:12px;">分享到微信朋友圈</h2>
    <a href="javascript:;" class="u-btn u-btn-close"><span class="ico"></span></a>
  </div>
  <div class="bd">
    <div class="m-viewseat" style="background:#fff url(img/loading.gif) no-repeat center center;">
      <div class="seat" style="padding:20px 60px;width:220px; height: 220px;"><img lazy-src="//piao.damai.cn/ShowBarcode.aspx?content=https%3A%2F%2Fpiao.damai.cn%2F164857.html" alt="" style="width:220px; height: 220px; display:none;" /></div>
    </div>
  </div>
  <div style="background:#fff;border-top:1px solid #e6e6e6; padding:8px 0px 8px 20px">
	<p>打开微信，点击底部的“发现”，使用 “扫一扫”<br />即可将网页分享到我的朋友圈。</p>
  </div>
</div>


<!-- 选择商品弹层 begin -->
<div class="m-layer m-layer-choosegoods z-hide" id="chooseGoodsLayer">
  <div class="hd">
    <h2 class="tt">请选择您要的商品信息</h2>
    <a href="javascript:;" class="u-btn u-btn-close"><span class="ico"></span></a>
  </div>
  <div class="bd">
    <div class="m-choosegoods j_goodsDetails">
      <!-- 选择日期模块 begin -->
      <div class="m-choose m-choose-date " data-row="2" data-col="4">
        <h3 class="tt">选择时间：</h3>
        <div class="ct">
          <ul class="lst"></ul>
        </div>
      </div>
      <!-- 选择日期模块 end -->

      <!-- 选择票价模块 begin -->
      <div class="m-choose m-choose-price" data-row="3" data-col="4">
        <h3 class="tt">选择票价：</h3>
        <div class="ct">
          <ul class="lst"></ul>
          <div class="tips tips-oos"><span class="ico"></span><span class="txt">暂时无货，登录试试运气~</span></div>
        </div>
      </div>
      <!-- 选择票价模块 end -->
       
      <!-- 购物车模块 begin -->
      <div class="m-cart">
        <h3 class="tt" style="display:none;">您选择了：</h3>
        <div class="ct" style="display:none;">
          <ul class="lst"></ul>
        </div>
        <div class="ops">
		  <a class="u-btn u-btn-c1 u-btn-choose" href="javascript:;" id="btnXuanzuo3" style="display:none;">选座购买</a>
		  		  <a class="u-btn u-btn-buynow" href="javascript:;" id="btnBuyNow3">立即购买</a>
		          </div>
      </div>
      <!-- 购物车模块 end -->
    </div>
  
  </div>
</div>
<!-- 选择商品弹层 end -->

<!-- 固定侧栏 begin -->
<div class="m-sdfix">
  <span class="itm weixin xiaonengService" style="cursor:pointer;">在线<br/>客服</span>
	
  <a class="itm resch" target="_blank" href="//www.wenjuan.com/s/QV7vm2/">
    <i class="ico"></i>
    <span class="txt">调查问卷</span>
  </a>
  <a class="itm weixin" href="javascript:;" id="siteWeixinQR" style="display:none;">
    <i class="ico"></i>
    <span class="code"><img original="img/qrcode.png" alt="大麦网" /></span>
  </a>
  <a class="itm totop" href="javascript:;" id="gotop">
    <i class="ico"></i>
    <span class="txt">返回顶部</span>
  </a>
</div>
<!-- 固定侧栏 end -->
<script type="text/javascript" src="//dui.dmcdn.cn/dm_2015/goods/js/jquery-1.8.2.min.js"></script>
<script type="text/javascript">
        var performCount = 0;
    </script>
<iframe id="mapview" name="mapview" scrolling="no" frameborder="no" border="0" style="display:none;"></iframe>
<script type="text/javascript">
var showCalendar = 0;
</script>
<!-- 日历插件 begin -->
<div class="m-calendar">
  <div class="hd"></div>
  <div class="bd"></div>
</div>
<!-- 日历插件 end -->
<script type="text/javascript">
var projectDates={};
showCalendar = 1;
</script>
	<script src="//dui.dmcdn.cn/??dm_2015/goods/site/js/common-min.js?v0.6.2,dm_2015/goods/site/js/search-min.js?v0.6.2,dm_2015/goods/site/js/widgetUIDs-min.js?v0.6.2,dm_2015/goods/site/js/calendarSettings-min.js,dm_2015/goods/site/js/calendar-min.js,dm_2015/goods/site/js/weixin-min.js,dm_2015/goods/site/js/json2-min.js,dm_2015/goods/site/js/datepicker-min.js,dm_2015/goods/site/js/app-min.js?v0.6.2" type="text/javascript"></script>
	<script src="/js/min/item-min.js?v0.6.2" type="text/javascript"></script>
	<script src="/js/min/qa-min.js?v0.6.2" type="text/javascript"></script>
<script type="text/javascript" src="//www.damai.cn/staticfile/Announcement/Announcement.js?937492837"></script>
<script type="text/javascript">
    var title = $("#Title").val();
	var ShowSpeedList=0,ShowTotalMoney=0;
		ShowSpeedList=0;
			ShowTotalMoney=0;
		(function () {
		$('#showVenueMap').on('click', function() {
			$('#mapview').on('load', dm_mapview.show).attr("src", jQuery(this).attr("map-src")).show();
			return false;
		});
	})();
</script>
<script type="text/javascript" src="https://secure.damai.cn/static/jquery.playalert3.js?0001" async="async"></script>
<script type="text/javascript" src="//cp.damai.cn/js/Service51La/SeoFlowStatistics.js?45" async="async"></script>
<script type="text/javascript" src="//dui.dmcdn.cn/dm_2015/goods/site/map/js/mapview.js" async="async"></script>
<script type="text/javascript">
$(document).on("click", ".xiaonengService", function() {
	 window.open("https://online.damai.cn/alime/toalime?from=damai_itemdetail&page=" + encodeURIComponent(location.href));
});
</script>
<!-- start Dplus --><script type="text/javascript">!function(a,b){if(!b.__SV){var c,d,e,f;window.dplus=b,b._i=[],b.init=function(a,c,d){function g(a,b){var c=b.split(".");2==c.length&&(a=a[c[0]],b=c[1]),a[b]=function(){a.push([b].concat(Array.prototype.slice.call(arguments,0)))}}var h=b;for("undefined"!=typeof d?h=b[d]=[]:d="dplus",h.people=h.people||[],h.toString=function(a){var b="dplus";return"dplus"!==d&&(b+="."+d),a||(b+=" (stub)"),b},h.people.toString=function(){return h.toString(1)+".people (stub)"},e="disable track track_links track_forms register unregister get_property identify clear set_config get_config get_distinct_id track_pageview register_once track_with_tag time_event people.set people.unset people.delete_user".split(" "),f=0;f<e.length;f++)g(h,e[f]);b._i.push([a,c,d])},b.__SV=1.1,c=a.createElement("script"),c.type="text/javascript",c.charset="utf-8",c.async=!0,c.src="//w.cnzz.com/dplus.php?token=7415364c9dab5n09ff68",d=a.getElementsByTagName("script")[0],d.parentNode.insertBefore(c,d)}}(document,window.dplus||[]),dplus.init("7415364c9dab5n09ff68");</script><!-- end Dplus --> 
<!-- start Dplus Define -->
<script type="text/javascript">!function(a,b){var c,d;window.__dplusDefineCacheQueue=[],b.define=function(){window.__dplusDefineCacheQueue.push(Array.prototype.slice.call(arguments))},c=a.createElement("script"),c.type="text/javascript",c.charset="utf-8",c.async=!0,c.src="//w.cnzz.com/dplus.define.php",d=a.getElementsByTagName("script")[0],d.parentNode.insertBefore(c,d)}(document,window.dplus);</script>
<!-- end Dplus Define -->
<script type="text/javascript">
	(function() {
		dplus.define('page', function(page){
			page.init("7415364c9dab5n09ff68", {
				'page_duration': true, //默认不跟踪页面停留时间
				'clean_url': true //默认是clean url
			});
		});
		dplus.define('page', function(page){
			page.setType('project');//设置页面类型
			page.setTitle("禾空间儿童剧嘉年华十次卡演出票");//设置页面标题,不填默认取document.title，建议填演出名
			page.setCategory(['话剧歌剧', '话剧歌剧']);//该演出对应的三级类目
			page.setTags(["儿童亲子"]);//该演出的其他TAG
			page.view({
				'$avn':"禾空间小剧场",
				'$alr':"",
				'$aad': "武汉"
			});
		});
	})();
	$(document)
	.on("click", "#gexhTuijian li a", function() {
		var $this = $(this);
		dplus.track('recclick',{
			'$tti':'project',
			'$tul':location.href,
			'$tna':'热门推荐',
			'$tdx':$this.closest("li").index() - 0 + 1,
			'$pid':$this.attr("data-projectId"),
			'tag':$this.attr('id'),
			'$na':$this.attr('title')
		});//
	}).on("click", "#dysbmit:not(.u-btn-dis)", function() {
		jQuery.getJSON("/ajax/GetUserInfo.html", { projectId: projectInfo.ProjectID, t: Math.random() }, function(rsp) {
			abc(rsp.Data.userInfo.code);
		});
		function abc(code) {
			var params = { "$tti": "project", "$pid": projectInfo.ProjectID + "", "$userid": code + "" };
			dplus.track('rssclick',params);
		}
	});
	$(document).ready(function() {
	    var cityid = projectInfo.CityID;
	    if (cityid != "" && cityid == "2279") {
	        cityid = "2148";
	    }
	    var uid = getwidgetUID(cityid);
	    if (location.protocol == "http:" && uid) {
			$("#weibo_con_").html("<iframe width=\"100%\" height=\"550\" class=\"share_self\"  frameborder=\"0\" scrolling=\"no\" src=\"http://service.t.sina.com.cn/widget/WeiboShow.php?width=0&height=550&fansRow=2&ptype=1&speed=0&skin=5&isTitle=0&noborder=0&isWeibo=1&isFans=0&uid=" + uid + "\"></iframe>");
			$("div.m-weibo").show();
			var uuid = uid.split('&')[0];
			$("#wbFollowIframe_").attr("src", "http://widget.weibo.com/relationship/followbutton.php?btn=light&style=2&uid={0}&width=136&height=24&language=zh_cn".format(uuid));
	    } else if (location.protocol == "https:" && uid) {
	        var uuid = uid.split('&')[0];
	        $("#wbFollowIframe_").attr("src", "//www.damai.cn/WeiboAgent.aspx?uid={0}".format(uuid));
	        $("#weibo_con_").parent().parent().remove();
	    } else {
	        $("#wbFollowIframe_").parent().remove();
	        $("#weibo_con_").parent().parent().remove();
	    }
	});
	</script>
<script src="//g.alicdn.com/mtb/lib-mtop/2.3.16/mtop.js"></script>
<script src="//g.alicdn.com/??damai/pc-wx/0.1.4/index.js"></script>
</body>
</html>"""
    a =BS(test,'lxml')
    b =a.find_all('h4',string='演出介绍')
    for i in b:
        print(i)


def ggeee():
    import pandas as pd
    import os

    # 获得当前路径的上级路径
    curPath = os.path.dirname(os.getcwd())
    print(curPath)

    def list_to_csv(List):
        # 读取列表内容
        _data = pd.DataFrame(List)
        # _data.head()
        NAME = curPath + '/tm51/history.csv'
        # 保存csv
        _data.to_csv(NAME, index=False, header=False, encoding='UTF-8')

        print(_data, '\n', _data.values)

    def list_to_db():
        print(1)

    def csv_to_db():
        print('1')

    def db_to_csv():
        print('1')

    def csv_to_data():
        con = pd.DataFrame(pd.read_csv(curPath + '/res/contents.csv', header=None, encoding='UTF-8')).values
        doi = pd.DataFrame(pd.read_csv(curPath + '/res/doings.csv', header=None, encoding='UTF-8')).values
        yun = pd.DataFrame(pd.read_csv(curPath + '/res/yundong.csv', header=0, encoding='UTF-8')).values
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

        # 看看原来的运动表是否也是这样的数字，如果是的话，再校对一遍，然后就可以添加内容了
        _re = []
        for i in range(len(con[468:])):
            # print(len(con[i+468]))
            _de = []

            a = eval(con[i + 468][2])
            b = yun[i]

            for j in range(len(a)):
                a[j]['title'] = b[j * 3 + 4]

            _de.append(str(con[i + 468][0]))
            _de.append(str(con[i + 468][1]))
            _de.append(str(a).replace(' ', ''))
            _de.append(str(con[i + 468][3]))
            _de.append(str(con[i + 468][4]))

            _re.append(_de)
            # print(_de)
            # break

        print(_re)

        return _re

        # 做完之后，去掉文本中的空格

    if __name__ == '__main__':
        list_to_csv(csv_to_data())
        # print(curPath)


# 若将数据写入txt文件时使用 \n 无法换行则使用 \r\n(回车+换行)
def osdd():
    _data = 20190107
    path = "res/"+str(_data)

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        os.makedirs(path)

    print(path)

#逐行读取txt
def dgggd():
    de = open('./tm51/res/50/56776.txt').readlines()

    print(len(de))
    i =0
    while i<5:
        i+=1

        print(de[i])

#读取文件列表
def dwww():
    file_50 = os.listdir('./res/50')

#打开文件，并转换成代码
def  get_code():
    t = open('res/code.txt','r',encoding='utf-8').read()
    # print(type(t))
    # for i in t:
    #     print(i)
    #     for j in i:
    #         print(j)
    #         break
    #     break
    f =eval(t)
    for i in f:
        print(i)
        for j in i:
            print(j)
            break
        break

#文件查询
def yide():
    # ddd=open('./res/action_list.txt','r',encoding='utf-8').read()
    # gg=eval(ddd)
    # print(type(gg),gg['startAPP'])
    ddd=open('res/test.txt','r',encoding='utf-8').read()
    gg=eval(ddd)
    print(len(gg))


#字符串切片变成列表
def str_to_list():
    test ='/location/drama/30256059/comments'
    print(test.split('/'))

    a = [{"situation": 1, "level": 4, "description": "准妈妈很适合吃包子，包子皮是发面食品，富含B族维生素，而且很容易消化。包子搭配了多种蔬菜和肉类，能够为准妈妈提供各种营养。"},
         {"situation": 2, "level": 4, "description": "坐月子能吃包子，包子皮是发面食品，比较容易消化，适合月子期间食用。"},
         {"situation": 3, "level": 4, "description": "一般情况下，包子都会同时搭配多种蔬菜和肉类，能够做到基本的膳食平衡，适合哺乳妈妈。"},
         {"situation": 4, "level": 4,
          "description": "包子可以通过改变面皮和馅料，做出很多花样来，促排期间和移植后吃包子改善饮食搭配，为人体提供各种营养，所以试管期间是可以吃包子的！"}]

    for i in a:
        i['title'] = '测试数据'

    print(str(a).replace(' ', ''))


#拆解提取URL
def to_url():
    from urllib.parse import urlparse  # 拆分URL
    it =['http://mini.eastday.com/a/180714221632914-2.html', 'http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%D0%D3%C8%CA%B6%B9%B8%AF%D0%C4&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=000000', 'http://www.piaoniu.com/activity/65867', 'https://m.piaoniu.com/activity/65867', 'http://piao.jd.com/114927.html', 'https://piao.damai.cn/161166.html', 'http://blog.sina.com.cn/s/blog_6d9713960102yjm3.html', 'http://www.dahepiao.com/news1/yanchu/2018120958827.html', 'http://www.nuomi.com/deal/c00vtx214.html', 'https://www.228.com.cn/ticket-448679229.html', 'http://epaper.oeeee.com/epaper/A/html/2019-01/12/content_1300.htm', 'http://www.51goupiao.com/t_10839.html', 'http://m.dahepiao.com/news/2018122059666.html', 'http://www.yidianzixun.com/article/0J7c4Uf5', 'https://jingyan.baidu.com/article/17bd8e52ff4ed385ab2bb8c6.html', 'http://www.ypiao.com/t_62898/', 'https://www.meishij.net/tianpindianxin/xingrendoufu_11.html', 'http://www.dianping.com/toutiao/75855435', 'https://www.xinshipu.com/zuofadaquan/6752/', 'https://m.nuomi.com/w/expired/p00vuaieu', 'http://blog.sina.com.cn/s/blog_4dbc922e0102ykor.html', 'http://heju.jinciwei.cn/426401.html', 'http://www.dahepiao.com/yanchupiaowu1/hj/2018120858779.html', 'http://wemedia.ifeng.com/88288519/wemedia.shtml', 'http://mini.eastday.com/a/181117184905524-3.html', 'https://www.xiaohongshu.com/discovery/item/598c206ea9b2ed283b192e0d', 'https://www.228.com.cn/ticket-508914816.html', 'https://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=https%3A%2F%2Fweibo.com%2F1762768245%2FHbnIWyCi7&domain=.weibo.com&ua=php-sso_sdk_client-0.6.28&_rand=1547273333.9928', 'http://bangumi.tv/person/14879', 'https://jingyan.baidu.com/article/ed15cb1b2b9f2f1be2698149.html']
    print(len(it))

    for i in it:

        # print(i)
        # print(urlparse(i))
        # print(urlparse(i).netloc,)
        # print(urlparse(i).path.split('/'))
        # break
        if urlparse(i).netloc =='blog.sina.com.cn':
            print(i)

#画图
def plt():
    import numpy as np
    import matplotlib.pyplot as plt




    x = np.array([ 1 , 6 , 3 , 4 , 5 , 6 , 7 , 8 ])
    y = np.array([ 3 , 5 , 7 , 6 , 2 , 6 , 10 , 15 ])
    plt.scatter(x , y , s = 75, alpha = 0.5)  # 折线 1 x 2 y 3 color
    # plt.plot(x , y , 'g' , lw=10)  # 4 line w
    # # 折线 饼状 柱状
    # x = np.array([ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ])
    # y = np.array([ 13 , 25 , 17 , 36 , 21 , 16 , 10 , 15 ])
    # plt.bar(x , y , 0.2 , alpha=1 , color='b')  # 5 color 4 透明度 3 0.9
    plt.show()

#可以对包含元组对列表进行去重！！！太棒了
def tiqu():
    # t=('22',22,33,44)
    # t1 = ('22' , 22 , 33 , 44)
    # t2 = ('22' , 22 , 33 , 44)
    # d = [t,t1,t2]
    # b=set(d)
    # print(list(b))
    t=()
    t1 = (22,)
    t2 = (33,)

    print(t+t1+t2)

# 用正则提取内容
def retest():
    import re

    with open('res/a.xml','r') as file:
        txt = file.read()

    p=re.compile(r'<row>((?:.|\n)*?)</row>') #提取row的列表
    # p=re.compile(r'<field name="%s">(.*?)</field>'%b)
    a = p.findall(txt)# 提取
    for i in a:
        b = 'from_client'
        e=re.findall(r'<field name="%s">(.*?)</field>'%b,i)

        print(e[0])
    test = '口碑佳作《驴得》水》被许多剧迷称作"神剧"'

    # _info = re.search('《[^》]+》', test, flags=0).group()
    print(re.findall('《.*》', test, flags=0))

#分类排序
def  ddggee():
    t=[3,6,9,13]
    listd= [(2,3),(1,45),(22,3),(7,34),(9,3)]
    # listd.sort()
    # print(listd)
    d1=[]
    d2=[]
    d3=[]
    d4=[]

    a = 0
    for i in listd:
        if i[0]>t[a]:
            a +=1
        




    print(sorted(listd))

if __name__ == '__main__':
    ddggee()
