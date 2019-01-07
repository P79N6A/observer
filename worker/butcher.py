#屠夫用于分词
import jieba.analyse

# 定义文件地址，并读取文件为 string
path = './bookcase/book.txt'
text= open(path,'r',encoding='UTF-8').read()

kets=jieba.analyse.extract_tags(text,topK=1000,withWeight=False,allowPOS=())
print(kets)