# -*- coding: UTF-8 -*-
"""
微信机器人，负责在微信中和用户互动

作用：
启动后，用于和微信群中都用户互动

工作内容：
1. 相应群中出现都内容，触发特定任务
2. 包括：每日的打招呼、最新演出通告、群公告通告

目前到问题：
1.
"""
# 公共库
import itchat
from itchat.content import *

# 内部库
from worker.librarian import get_show  # 获取数据库信息
from worker.toolkit import whether_repeat  # 工具


def _itchat():
    itchat.auto_login(enableCmdQR=2, hotReload=True)
    # print(itchat.get_friends(True))
    itchat.send('Hello, filehelper', toUserName='filehelper')
    """
    hotReload=True:一定时间内重新开启也可以不用重新扫码
    enableCmdQR=True:可以在登陆的时候使用命令行显示二维码
    enableCmdQR=2:部分系统可能字幅宽度有出入，可以通过将enableCmdQR赋值为特定的倍数进行调整
    enableCmdQR=-1:默认控制台背景色为暗色（黑色），若背景色为浅色（白色），可以将enableCmdQR赋值为负值
    """

    @itchat.msg_register(TEXT, isFriendChat=True)
    def _FriendChat(msg):
        # equals to print(msg['FromUserName'])
        print(msg)
        get_show(7)
        return get_show(7)

    @itchat.msg_register(TEXT, isGroupChat=True)
    def _GroupChat(msg):
        print(msg.isAt)
        # equals to print(msg['FromUserName'])
        print(len(msg.user.memberList))
        # for key,value in :
        #     print(key)
        #     print(value)
        # return msg['MsgId']

    @itchat.msg_register(TEXT, isMpChat=True)
    def _GroupChat(msg):
        # equals to print(msg['FromUserName'])
        print(msg)
        # return msg['MsgId']

    print(len(itchat.get_friends()))
    itchat.run(True)


if __name__ == '__main__':
    _itchat()
