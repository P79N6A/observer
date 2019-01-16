# coding=utf-8

# 公共库
import os  # 转换内容 ，并提取数据
from datetime import datetime
import matplotlib.pyplot as plt

# 私有库
from tm51.tool import get_mini , new_folder , action_to_cn

key_list =['id','type','target_id','phase_id','phase_time','created_at']
name='phase_relation'


#生成user的文件
class c():
    data =get_mini(name,key_list)

    #得出用户的阶段组成关系
    def to_mini(self):
        user_list =[]
        d_dict = {1:"我在备孕",7:"准备试管",8:"前期检查",9:"降调",10:"促排",11:"取卵移植",12:"黄体支持",3:"我怀孕啦",4:"宝宝生啦"}

        _dict =[] #做一个空数组，便于统计
        for i in range(9):
            _dict.append(0)
        print(_dict)

        #筛选出用户数据
        for i in self.data:
            # print(type(i[1]))
            if i[1] ==str(3) : #如果是用户
                _i =int(i[3])

                a=0
                for d in d_dict:
                    if _i==d:
                        _dict[a] +=1
                        break
                    a +=1
        print(_dict)

        labels = "我在备孕","准备试管","前期检查","降调","促排","取卵移植","黄体支持","我怀孕啦","宝宝生啦"
        explode = [ 0.05 , 0 , 0 , 0,0,0,0,0,0]  # 0.1 凸出这部分，
        plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
        # autopct ，show percet
        plt.pie(x=_dict , labels=labels , explode=explode , autopct='%3.1f %%' ,
                shadow=True , labeldistance=1.1 , startangle=90 , pctdistance=0.6

                )
        # from matplotlib.font_manager import FontProperties
        # font = FontProperties(fname='/Library/Fonts/Hanzipen.ttc' , size=10)
        # plt.rc('font',family=font)

        plt.show()



if __name__ == '__main__':
    a =c()
    a.to_mini()