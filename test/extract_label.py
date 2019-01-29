# -*- coding: UTF-8 -*-

#公共库
import jieba.analyse #分词库



#做完语料库之后，就可以用这个来做判断了
def ddd(txt):
    # #载入自定义词库
    # jieba.load_userdict("user_dict.txt")

    #载入自定义语料库
    jieba.analyse.set_idf_path("./jieba-master/extra_dict/idf.txt.big")

    #载入停用语料库
    jieba.analyse.set_stop_words("./jieba-master/extra_dict/stop_words.txt")

    a =jieba.analyse.extract_tags(txt,topK=10,withWeight=True, allowPOS=())
    b = jieba.analyse.textrank(txt,topK=10,withWeight=True,allowPOS=('ns', 'n', 'vn', 'v'))


    print('extract_tags:%s'%a)
    print('textrank:%s' % b)



if __name__ == '__main__':
    with open('res/test.txt','r') as file:
        _file = file.read()


    ddd(_file)