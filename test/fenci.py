import jieba
#无法运行

# 创建停用词列表
def stopwordslist():
    stopwords = [line.strip() for line in open('res/stoptxt.txt',encoding='UTF-8').readlines()]
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
filename = "res/test.txt"
outfilename = "res/out.txt"
inputs = open(filename, 'r', encoding='UTF-8')
outputs = open(outfilename, 'w+', encoding='UTF-8')

# 将输出结果写入ou.txt中

outputs.write(seg_depart(inputs))
print("-------------------正在分词和去停用词-----------")
outputs.close()
inputs.close()
print("删除停用词和分词成功！！！")







# 获取每个目录下所有的文件
for mydir in catelist:
    class_path = corpus_path + mydir + "/"  # 拼出分类子目录的路径
    # print(class_path)
    seg_dir = seg_path + mydir + "/"  # 拼出分词后语料分类目录
    if not os.path.exists(seg_dir):  # 是否存在目录，如果没有创建
        os.makedirs(seg_dir)
    # print(seg_dir)
    file_list = os.listdir(class_path)  # 获取class_path下的所有文件
    for file_path in file_list:  # 遍历类别目录下文件
        fullname = class_path + file_path  # 拼出文件名全路径
        # print(fullname)
        content = readfile(fullname).strip()  # 读取文件内容
        content = content.replace("\r\n".encode(encoding="utf-8"),"".encode(encoding="utf-8"))  # 删除换行和多余的空格
        content = content.replace(" ".encode(encoding="utf-8"),"".encode(encoding="utf-8"))
        content_seg = jieba.cut(content.strip())  # 为文件内容分词
        stopwords = stopwordslist('./stopwords1.txt')
        outstr = []

        for word in content_seg:
            if word not in stopwords:
                if word != '\t' and word != '\n':
                    # outstr.append(word)
                    outstr.append(word)
        for word in outstr:
            if ' ' in outstr:
                outstr.remove(' ')
        temp_dict = {}
        total += 1
        for word in outstr:
            # print(word)
            temp_dict[word] = 1
            # print(temp_dict)
        for key in temp_dict:
            num = all_dict.get(key,0)
            all_dict[key] = num + 1
        # savefile(seg_dir+file_path,"".join(outstr))  # 将处理后的文件保存到分词后语料目录



# idf_dict字典就是生成的IDF语料库
idf_dict = {}
for key in all_dict:
    # print(all_dict[key])
    w = key
    p = '%.10f' % (math.log10(total / (all_dict[key] + 1)))
    if w > u'\u4e00' and w <= u'\u9fa5':
        idf_dict[w] = p
print('IDF字典构造结束')
fw = open('wdic.txt','w',encoding='utf-8')

for k in idf_dict:
    if k != '\n':
        print(k)
        fw.write(k + ' ' + idf_dict[k] + '\n')
fw.close()

