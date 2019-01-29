# -*- coding: UTF-8 -*-
'''
关于用户帖子的各种统计工具
'''
# 公共库
import math
import jieba.analyse
import re
import nltk
from datetime import datetime

# 私有库
from tm51.tool import get_mini,new_folder,action_to_cn,make_pie,dde

# 文本地址
path_thread = 'forum_thread'
path_diary = 'forum_diary'


# 提取用户帖子文档
class count_theme:
    # useful_key = ['from_client','client_version','app_version','action_type','uid','device_id','info','remote_ip','created_at']  # 全字段
    # path_thread_key = ['id','plate_id','uid','subject','message','views','views_virtual','replies','hots','geo_id','remote_ip','from_client','style','anonymous','cover','status','is_blacklist','is_sync','last_post','auto_check_at','created_at','updated_at'] # 全字段
    path_thread_key = ['id','subject','message','views','replies','style','status','is_blacklist','created_at']  # 简版字段
    # path_thread_key = ['id','plate_id','created_at']  # 用于统计发帖类型

    # path_diary_key = ['id','uid','message','weather_id','bg_id','geo_id','remote_ip','from_client','views','views_virtual','replies','hots','style','is_secret','status','is_blacklist','diary_time','last_post','created_at','updated_at']  # 简版字段
    path_diary_key = ['id','message','views','replies','style','status','is_blacklist','created_at']  # 简版字段

    file_thread_key = []
    file_diary_key = []

    # 生成txt文件，然后将一个帖子做成一个文件，
    def _make_file_thread(self):
        self.file_thread_key = get_mini(path_thread,self.path_thread_key)  # 获取帖子列表

    def _make_file_diary(self):
        self.file_diary_key = get_mini(path_diary,self.path_diary_key)  # 获取日记列表

    # 按浏览次数生成文件夹
    def get_diary_by_views(self):
        self._make_file_diary()  # 生成数据

        # #载入自定义词库
        jieba.load_userdict("res/user_dict.txt")

        # 过滤停用词
        with open('res/stop_words.txt','r',encoding='utf-8') as file:
            stop_words = file.read()

        stop_word = re.compile('[a-zA-Z0-9]+')  # 过滤掉纯数字和字母传

        # 遍历统计词频，并排除停用词.如果单词没在停用词list中，则计数
        counts = []
        for _txt in self.file_diary_key:
            _message = _txt[1]  # 提取文本
            _list_word = jieba.cut(_message)  # 分词

            # 过滤停用词，并添加到数组中
            for i in _list_word:
                _bool = stop_word.match(i)
                if i not in stop_words and not _bool:
                    counts.append(i)
            # break

        de={}
        for i in counts:
            de[i] = de.get(i ,0)+1
        print(de)
        # de1 = sorted(list(de),key=lambda x:x[1],reverse=True)  # 排序
        # print(de1)

        fd = nltk.FreqDist(counts).items()#统计出现数
        fdd = sorted(fd,key=lambda x:x[1],reverse=True)# 排序
        print(fdd)

        # den= 0
        # with open('res/ddddd.txt','w') as file:
        #     for i in self.file_diary_key:
        #         if int(i[-5]) > 50 : # 筛选出回复数大于50的帖子
        #             # 载入自定义词库
        #             # jieba.load_userdict("user_dict.tnagesixt")
        #
        #
        #             _txt = jieba.lcut(i[1])                    #简单分词
        #             # # 载入停用语料库
        #             # jieba.analyse.set_stop_words("res/stop_words.txt")
        #             # a = jieba.analyse.extract_tags(i[1],topK=20,withWeight=True,allowPOS=())
        #
        #             # print(a)
        #             # total=0
        #             # for ti in a:
        #             #     total += ti[1]
        #             # file.write(r'综合得分:%s,帖子ID:%s,访问：%s,回复：%s，分词结果：%s'%(total,i[0],i[2],i[3],str(_txt)))
        #
        #             fd =nltk.FreqDist(_txt)
        #             file.write(str(fd.items()))
        #             file.write('\r\n')
        #             file.write('\r\n')
        #             den+=1
        #         break
        # print(den)

        # words = []  # 搜集分词结果
        # for i in self.file_diary_key:
        #     if int(i[-5]) > 10:  # 筛选出高回复数的帖子
        #         word = jieba.cut(i[1],cut_all=False,HMM=False)
        #         word = list(set(word))  # 去重，这样保证每个词都只有一个
        #         words += word
        #
        # # print(len(words))
        # # print(words)
        #
        # # 统计每个词在所有文章中的出现次数
        # counts = {}
        # for word in words:
        #     dd = an.match(word)
        #     if word not in stopwords and not dd:
        #         # if word not in stopwords:
        #         counts[word] = counts.get(word,0) + 1
        #
        # # print(len(counts))
        # # print(counts)
        #
        # # 排序
        # _list = list(counts.items())
        # _list.sort(key=lambda x:x[1],reverse=True)
        #
        # # print(len(_list))
        # # print(_list)
        #
        # nums_diary = len(self.file_diary_key)  # 文章总数
        #
        # # 生成IDF
        # totals = {}
        # for i in _list:
        #     # print(i[1],nums_diary,i[0])
        #     p = '%.10f' % (math.log10((nums_diary+1) / (i[1] + 1)+1))
        #     totals[i[0]] = p
        #     # break
        # print(len(totals))
        # print(totals)
        #
        # # 测试某个文章
        # for i in self.file_diary_key:
        #
        #     if int(i[-5]) > 1000:  # 筛选出高回复数的帖子
        #         print(i[0])
        #         word = jieba.lcut(i[1],cut_all=False,HMM=False)
        #         tdga = len(word)  # 总词数
        #         cdd = {}  # 词计数
        #         for i in word:
        #             cdd[i] = cdd.get(i,0) + 1
        #
        #         # 生成带有idf的数
        #         gggd = {}
        #         for key,value in cdd.items():
        #             if key in totals:
        #                 print(key)
        #                 print(value)
        #                 print(tdga)
        #                 print(totals[key])
        #                 gggd[key] = (value/tdga) * float(totals[key])
        #
        #         _1list = list(gggd.items())  # 统计包含此词的文档数
        #         _1list.sort(key=lambda x:x[1],reverse=True)
        #         print(_1list)
        #         break

    # 按回复次数生成文件夹
    def get_list_by_replies(self):
        pass

    def test(self):
        self._make_file_diary()  # 生成数据

        counts = {}
        for i in self.file_diary_key:
            if int(i[-5]) > 100:
                words = jieba.lcut(i[2],cut_all=False,HMM=False)  # 分析

                #
                list_words = []
                for word in words:
                    if word not in list_words:
                        list_words.append(word)

                print(i[0])


# 每日发帖的类型统计
def type_counts():
    with open('res/forum_thread/forum_thread.txt','r') as fild:
        ade = eval(fild.read())

    counts = {}
    for i in ade:
        # print(i)
        _date = str(datetime.strptime(i[2],"%Y-%m-%d %H:%M:%S").date())
        if _date not in counts:
            counts[_date] = [0,0,0,0,0,0,0,0,0,0,0,0]

        counts[_date][int(i[1])] += 1

    for key,value in counts.items():
        print(key,end='')
        for i in value:
            print('\t',i,end='')
        print('')


if __name__ == '__main__':
    # 构建实例
    a = count_theme()

    a.get_diary_by_views()

    # 每日发帖的类型统计
    # type_counts()

    # a.get_diary_by_views()
    # d=a.file_diary_key
    # print(len(d))
