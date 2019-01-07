import pandas as pd
# 加载解析HTML库
from bs4 import BeautifulSoup as BS
import jieba.analyse

info = BS(open('query_result.xml','r',encoding='utf-8'), 'html.parser')
fog = info.find_all('row')

inpu=[]
sirtl={}
for i in fog:
    n =i.find_all('field')
    ondu={}
    ondu['id']=i.find('field',class_='id').get_text()
    ondu['subject'] = n[3].get_text()
    ondu['message'] = n[4].get_text()
    ondu['views'] = n[5].get_text()
    ondu['replies'] = n[6].get_text()
    ondu['hots'] = n[7].get_text()

    # _fenci = jieba.lcut(ondu['message'])
    _fenci= jieba.analyse.extract_tags(ondu['message'],topK=20,withWeight=False)

    # print(ondu)
    #分词内容
    counts = {}

    for word in _fenci:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1

    for i in   counts:
        if i in sirtl:
            sirtl[i] = sirtl[i]+counts[i]
        else:
            sirtl[i] = counts[i]

    ondu['fenci'] = counts
    inpu.append(ondu)
    # print(ondu)
    # break

#停用词
ddd=[]
stopd = open('tingyongci.txt','r',encoding='utf-8').readlines()
for i in stopd:
    ddd.append(i)

_deg=[]
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