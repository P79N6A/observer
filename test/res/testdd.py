import os


def get_path():
    # 获得当前路径的上级路径
    curPath2 = os.path.dirname(os.getcwd())
    print(curPath2)
    # 获得项目的路径
    curPath = os.path.abspath(__file__)
    print(curPath)
    # 获取当前文件的路径：

    from os import path
    d = path.dirname(__file__)  # 返回当前文件所在的目录
    # __file__ 为当前文件, 若果在ide中运行此行会报错,可改为  #d = path.dirname('.')
    # 获得某个路径的父级目录：

    parent_path = os.path.dirname(d)  # 获得d所在的目录,即d的父级目录
    parent_path = os.path.dirname(parent_path)  ##获得parent_path所在的目录即parent_path的父级目录
    # 获得规范的绝对路径：

    abspath = path.abspath(d)  # 返回d所在目录规范的绝对路径


if __name__ =='__main__':
    get_path()