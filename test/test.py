import json

# model={'fav': '总冠军', 'age': 31} #数据
# with open("test.json",'w',encoding='utf-8') as json_file:
#         json.dump(model,json_file,ensure_ascii=False)


with open("test.json",'r',encoding='utf-8') as json_file:
    model=json.load(json_file)
    print(model['fav'])




db_name = {'剧目':'plans'}

def