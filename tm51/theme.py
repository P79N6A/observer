# -*- coding: UTF-8 -*-

# 文本地址
path_thread = 'res/forum_thread.xml'
path_diary = 'res/forum_diary.xml'


class count_theme:
    # useful_key = ['from_client','client_version','app_version','action_type','uid','device_id','info','remote_ip','created_at']  # 全字段
    # path_thread_key = ['id','plate_id','uid','subject','message','views','views_virtual','replies','hots','geo_id','remote_ip','from_client','style','anonymous','cover','status','is_blacklist','is_sync','last_post','auto_check_at','created_at','updated_at'] # 全字段
    # path_diary_key = ['id','uid','message','weather_id','bg_id','geo_id','remote_ip','from_client','views','views_virtual','replies','hots','style','is_secret','status','is_blacklist','diary_time','last_post','created_at','updated_at']  # 简版字段

    path_thread_key = ['id','subject','message','views','replies','style','status','is_blacklist','created_at']  # 简版字段
    path_diary_key = ['id','message','views','replies','style','status','is_blacklist','created_at']  # 简版字段

    #生成txt文件，然后将一个帖子做成一个文件，


if __name__ == '__main__':
    count_theme()
