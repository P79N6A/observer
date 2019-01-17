#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author: Frank
@contact: frank.chang@shoufuyou.com
@file: test_duration_time.py
@time: 2018/8/26 下午5:23

讨论列表去重的方法

"""
import random

from tools import fn_timer
import numpy as np
import pandas  as pd

Count = 10_0000

l = [random.randint(-5, 5) for i in range(Count)]


# print(l)


@fn_timer
def fun_set(l):
    return list(set(l))


@fn_timer
def fun_comprehension(l):
    """
    用列表推导式
    :param l:
    :return:
    """
    ret = []

    [ret.append(i) for i in l if i not in ret]

    return ret


@fn_timer
def fun_dict_fromkeys(l):
    l2 = dict.fromkeys(l).keys()

    return list(l2)


@fn_timer
def fun_dict_comprehension(l):
    l2 = dict.fromkeys(l)

    return [key for key in l2]




@fn_timer
def fun_series(l):
    s = pd.Series(l)
    s.drop_duplicates(inplace=True)
    return s.tolist()


def test_duration_time():
    ret1 = fun_set(l)
    ret2 = fun_comprehension(l)
    ret3 = fun_dict_fromkeys(l)

    ret4 = fun_dict_comprehension(l)

    ret5 = fun_series(l)

    print(ret1)
    print(ret2)
    print(ret3)
    print(ret4)
    print(ret5)


if __name__ == '__main__':
    test_duration_time()
---------------------
作者：阿常呓语
来源：CSDN
原文：https://blog.csdn.net/u010339879/article/details/82291878
版权声明：本文为博主原创文章，转载请附上博文链接！