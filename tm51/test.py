# 在用户操作表，但排出在发帖表、日记表、回复表中的用户，
def action():
    # 创建文件夹
    file_50 = Tool().new_flie(50)
    file_100 = Tool().new_flie(100)
    file_1000 = Tool().new_flie(1000)

    _v_forum_thread = get_value().forum_thread  # 今天发帖的记录
    _uid_forum_thread = Tool().get_uid(_v_forum_thread)  # 今天发帖用户的ID列表
    print('发帖人数：%d' % len(_uid_forum_thread))

    _uid_forum_thread = Tool().out_com(_uid_forum_thread)  # 排出自己人
    print('排出自己人后，发帖人数：%d' % len(_uid_forum_thread))

    # 今天操作用户的ID列表
    _v_user_action_report = get_value().user_action_report  # 今天操作记录
    _uid_user_action_report = Tool().get_uid(_v_user_action_report)  # 今天操作的用户列表
    print('活跃人数：%d' % len(_uid_user_action_report))

    _uid_user_action_report = Tool().out_com(_uid_user_action_report)  # 排出自己人
    print('排出自己人后，发帖人数：%d' % len(_uid_user_action_report))

    # 将今日发帖的用户从操作的用户中去除
    _out_list = [ ]
    for i in _uid_user_action_report:
        if i not in _uid_forum_thread:
            _out_list.append(i)

    # 提取用户在操作中的记录
    for _uid in _out_list:  # 逐个处理列表中的数据
        # 用于保存一个用户到所有操作
        _list = [ ]

        # 从操作列表中提取对用用户ID的行动
        for j in _v_user_action_report:

            if _uid == j[ 'uid' ]:  # 如果在操作记录中找到这个人到ID
                # 用于保存一条操作：时间和操作
                _v = [ ]

                # 时间
                _v.append(datetime.strptime(j[ 'created_at' ] , "%Y-%m-%d %H:%M:%S").time())

                # 动作
                if j[ 'action_type' ] in actin_list:
                    _v.append(actin_list[ j[ 'action_type' ] ])

                # 去重
                if _v not in _list:
                    _list.append(_v)

        # 根据用户操作到次数，分文件夹保存数据
        if len(_list) <= 50:
            # 创建文件
            _save = open('%s/%s.txt' % (file_50 , _uid) , 'w+' , encoding='utf-8')
            for i in _list:
                for j in range(len(i)):
                    _save.write(str(i[ j ]))
                    _save.write(' ')
                _save.write('\r\n')
            _save.close()
        elif len(_list) > 50 and len(_list) <= 100:
            # 创建文件
            _save = open('%s/%s.txt' % (file_100 , i) , 'w+' , encoding='utf-8')
            for i in _list:
                for j in range(len(i)):
                    _save.write(str(i[ j ]))
                    _save.write(' ')
                _save.write('\r\n')
            _save.close()
        else:
            # 创建文件
            _save = open('%s/%s.txt' % (file_1000 , i) , 'w+' , encoding='utf-8')
            for i in _list:
                for j in range(len(i)):
                    _save.write(str(i[ j ]))
                    _save.write(' ')
                _save.write('\r\n')
            _save.close()

        # 在这里做一个统计，用户进行了多少次操作
        print(str(_uid) + ',' + str(len(_list)) + '\n')
        # break

    print('50条操作的用户有：' + str(len(os.listdir(file_50))))
    print('100条操作的用户有：' + str(len(os.listdir(file_100))))
    print('50条操作的用户有：' + str(len(os.listdir(file_1000))))


# 传入文件名，得出用户的记录条数
def numbers(Path):
    file_path = './res/' + str(Path)  # 文件路径
    file_name = './res/file_' + str(Path)  # 文件名

    _file_list = os.listdir(file_path)  # 文件名列表



    # 所有操作进行计数
    _file_time = {}
    for i in _file_list:
        _file = open(file_path + '/' + i , 'r' , encoding='utf-8')
        _list = _file.readlines()

        for j in _list:
            _d = j.split(" ")
            if _d[ 1 ] not in _file_time:
                _file_time[ _d[ 1 ] ] = 1
            else:
                _file_time[ _d[ 1 ] ] += 1

        _file.close()

    # 打印数据
    _end = open(file_name + '.txt' , 'w' , encoding='utf-8')

    # 操作记录的总条数
    _times = 0

    _list_50 = [ ]
    for i in _file_time:
        # 计算总数
        _times += _file_time[ i ]

        # 写入到文件中
        _end.write(str(i) + ',' + str(_file_time[ i ]))
        _end.write('\r\n')

    _end.write('一共有：%s 个用户记录，总共有 %s 条操作记录' % (len(_file_list) , _times))

    _end.close()

