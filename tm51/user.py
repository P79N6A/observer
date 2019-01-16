# coding=utf-8

# 公共库
import os  # 转换内容 ，并提取数据
from datetime import datetime

# 私有库
from tm51.tool import get_mini , new_folder , action_to_cn

key_list =['id','username','sex','birth','geo_id','email','mobile','head_img','salt','from_client','status','is_virtual','is_freeze','last_login_ip','last_login_time','is_new','is_pop','alipay_account','created_at','updated_at','last_at']
name='user'


#生成user的文件
def to_mini():
    get_mini(name,key_list)



if __name__ == '__main__':
    to_mini()