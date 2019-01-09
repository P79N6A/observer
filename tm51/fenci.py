import jieba

# 创建停用词列表
def stopwordslist():
    stopwords = [line.strip() for line in open('stoptxt.txt',encoding='UTF-8').readlines()]
    return stopwords

# 对句子进行中文分词
def seg_depart(sentence):
    # 对文档中的每一行进行中文分词
    print("正在分词")
    sentence_depart = jieba.lcut(sentence)
    # 创建一个停用词列表
    stopwords = stopwordslist()
    # 输出结果为outstr
    outstr = ''
    # 去停用词
    for word in sentence_depart:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr

# 给出文档路径
filename = "Init.txt"
outfilename = "out.txt"
inputs = open(filename, 'r', encoding='UTF-8')
outputs = open(outfilename, 'w+', encoding='UTF-8')

# 将输出结果写入ou.txt中

outputs.write(seg_depart(inputs))
print("-------------------正在分词和去停用词-----------")
outputs.close()
inputs.close()
print("删除停用词和分词成功！！！")