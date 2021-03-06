# -* - coding: UTF-8 -* -
#这里要做一个获取config的库，这样可以直接通过函数，将参数变成字典，调用出来
from configparser import ConfigParser


# #以列表形式返回所有的section
# sections = conf.sections()
# print('sections:', sections) #sections: ['sec_b', 'sec_a']
# # 得到指定section的所有option
# options = conf.options("sec_a")
# print('options:', options )#options: ['a_key1', 'a_key2']
# # #得到指定section的所有键值对
# # kvs = conf.items("sec_a")
# # print 'sec_a:', kvs #sec_a: [('a_key1', '20'), ('a_key2', '10')]
# # #指定section,option读取值
# # str_val = conf.get("sec_a", "a_key1")
# # int_val = conf.getint("sec_a", "a_key2")print "value for sec_a's a_key1:", str_val #value for sec_a's a_key1: 20
# # print "value for sec_a's a_key2:", int_val #value for sec_a's a_key2: 10


def CONFIG(module):
    # 生成config对象
    conf = ConfigParser()

    # 用config对象读取配置文件
    conf.read("config.cfg",encoding='utf-8')

    # 得到指定section的所有option
    options = conf.items(module)
    print(options[1])


if __name__=='__main__':
    CONFIG('get_show_list')