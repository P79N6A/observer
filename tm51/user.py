# coding=utf-8
"""
统计用户ID表的数据的工具
"""

# 公共库
import os  # 转换内容 ，并提取数据
from datetime import datetime

# 私有库
from tm51.tool import get_mini,new_folder,action_to_cn,make_pie,dde

"""
['id'  # int(11) unsigned NOT NULL AUTO_INCREMENT,
 'username'  # varchar(64) CHARACTER SET utf8mb4 NOT NULL DEFAULT '' COMMENT '用户名',
 'password'  # varchar(128) NOT NULL DEFAULT '' COMMENT '密码',
 'sex'  # tinyint(4) NOT NULL DEFAULT '2' COMMENT '性别 0保密 1男 2女',
 'birth'  # date DEFAULT '1970-01-01' COMMENT '生日',
 'geo_id'  # int(11) DEFAULT '0' COMMENT '地域',
 'email'  # varchar(128) DEFAULT '' COMMENT '邮件',
 'mobile'  # varchar(11) DEFAULT '' COMMENT '手机号',
 'head_img'  # varchar(255) DEFAULT '' COMMENT '用户头像',
 'salt'  # varchar(12) NOT NULL DEFAULT '' COMMENT '加密盐值',
 'from_client'  # tinyint(4) DEFAULT '1' COMMENT '来源终端 1 pc 2 ios 3 android 4 wap',
 'status'  # tinyint(4) NOT NULL DEFAULT '0' COMMENT '用户状态 默认 0 有效',
 'is_virtual'  # tinyint(4) DEFAULT '0' COMMENT '0 真实用户； 1 虚拟用户',
 'is_freeze'  # tinyint(4) DEFAULT '0' COMMENT '默认0 未冻结；1冻结（不能体现)',
 'last_login_ip'  # varchar(64) DEFAULT '' COMMENT '最后登陆IP',
 'last_login_time'  # timestamp NULL DEFAULT '0000-00-00 00:00:00' COMMENT '最后登陆日期',
 'is_new'  # tinyint(4) DEFAULT '1' COMMENT '默认 0表示是不是新手 1是新手',
 'is_pop'  # tinyint(4) DEFAULT '1' COMMENT '是否弹出过（设置状态时）默认1没弹出过；0已弹过',
 'alipay_account'  # varchar(255) NOT NULL COMMENT '支付宝账号（姓名#支付宝账号）',
 'created_at'  # timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
 'updated_at'  # timestamp NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP COMMENT
 '更新时间']  # 全字段
"""
tops_num = 8  # 设置显示前几名的内容
_split_ = '\t'  # 统计报告的分隔符号
name = 'user'
path = new_folder('res/%s' % name)

useful_key = ['id','username','sex','birth','email','mobile','is_virtual','created_at']  # 简版字段


def make_txt():
    """
    如果没有txt文件，则生成txt文件，如果有文件，则返回此文件的内容
    :return: 返回整个数据表，
    """
    file_path = r'res/user.xml'  # 文件路径
    if os.path.exists(file_path):  # 如果没有文件，则生成文件
        return get_mini(name,useful_key)  # 转换数据，获取想要的字段
    else:
        print('没有xml文件')
        return


def make_file(data):
    """
    根据txt文件，按照用户的注册月份，同一个月份的用户放在一个文件夹中
    """


    stati = dict()  # 将用户信息按照年月分类
    for i in data:
        if i[-2] == '0':  # 屏蔽虚拟用户
            _i = i[-1].split("-")
            _date = r'%s-%s' % (_i[0],_i[1])  # 获取用户的年月信息
            stati[_date] = stati.get(_date,[]) + [i]
            # print(stati)

    path_txt = new_folder(r'%s/by_Date' % path)  # 创建文件夹，并创建文件
    for _key,_list in stati.items():  # 按年月放置用户信息
        delete_file(_key)  # 删除对应文件
        with open(r'%s/%s_%s.txt' % (path_txt,_key,len(_list)),'w') as file:  # 创建文件
            for i in _list:
                file.write(str(i))
                file.write('\r\n')

    with open(r'%s/make_file.txt' % path,'w') as file:
        file.write(str(stati))

    return stati


def make_chart():
    """
    制作每月用户注册人数的图标
    :rtype: object
    """
    file_path = (r'%s/make_file.txt' % path)  # 文件路径
    if not os.path.exists(file_path):  # 如果没有文件，则生成文件
        _file = make_file()
    else:
        with open(file_path,'r') as file:  # 获取文件内容
            _file = eval(file.read())

    import matplotlib.pyplot as plt

    x = list()
    y = list()
    for _key,_value in _file.items():  # 生成x、y轴数据
        if int(_key.split('-')[0]) == 2018:  # 只取2018年的数据
            x.append(r'%s月' % _key.split('-')[1])
            y.append(len(_value))

    plt.rcParams['font.family'] = ['Arial Unicode MS']  # 解决中文乱码

    plt.bar(x[:],y[:])  # 生成表格

    for _x,_y in zip(x,y):  # 显示刻度上的数字
        plt.text(_x,_y,_y,ha='center',va='bottom')

    plt.title('2018年每月注册用户数')  # 显示标题

    plt.savefig(r'%s/2018.jpg' % path)  # 保存图标
    plt.show()


def delete_file(key):
    """
    删除指定的文件
    :return:
    """

    file_list = os.listdir('%s/%s' % (path,'by_Date'))  # 获取文件夹的所有文件和目录

    for file in file_list:  # 查找需要的文件,并删除
        if file.split(".")[0]:  # 排除系统文件
            if file.split("(")[0] == key:  # 找到文件，并删除
                os.remove(r'%s/%s/%s' % (path,'by_Date',file))
                break


if __name__ == '__main__':
    # data=make_txt()  # 获取文件
    # make_file(data)  # 生成月份文件
    make_chart()  # 生成注册用户表格
