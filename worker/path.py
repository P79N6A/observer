import os  # 转换内容 ，并提取数据
import sys
print(os.getcwd())
print(os.path.dirname(os.getcwd()))
print(os.path.split(os.path.realpath(__file__)))
print(sys.path[0])