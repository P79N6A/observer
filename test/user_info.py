# coding=utf-8
#分词，排除禁用词，并提取词频

import jieba, math

import jieba.analyse
# jieba.cut主要有三种模式
# 随便对一个动物园的评论进行分析
str_text = open(u'res/test.txt', encoding='utf-8', errors='ignore').read()

paichu={}
# words = jieba.analyse.extract_tags(str_text,topK=3)

words = jieba.cut(str_text,cut_all=False,HMM=False)
counts ={}
for word in words:
    if len(word) == 1:
        counts
    else:
        counts[word] = counts.get(word,0)+1


fe  =''
_list = list(counts.items())
_list.sort(key=lambda x:x[1], reverse=True)

for w,i in  _list:
    fe =fe+w+' '+str(i)+'\n'
de= "".join(fe)

print(counts)
print(de)

#
#
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# # f = open(r'test.txt','r',encoding='utf-8').read()
# # print(f)
# wordcloud = WordCloud(font_path='res/simheittf.ttf',background_color="white",width=1000, height=860, margin=2).generate(de)
#
# # width,height,margin可以设置图片属性
# # generate 可以对全部文本进行自动分词,但是对中文支持不好
# # 可以设置font_path参数来设置字体集
# #background_color参数为设置背景颜色,默认颜色为黑色
#
# #
#
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.show()
# wordcloud.to_file('test.png')
# # 保存图片,但是在第三模块的例子中 图片大小将会按照 mask 保存