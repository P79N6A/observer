# coding:utf-8
import json
import requests
from wxpy import *
import re  # 正则表达式
from datetime import datetime  # 日期处理
import schedule  # 定时任务
import time  # 计时
import threading  # 多县城


# bot = Bot()
# bot.file_helper.send_image('ParticleSmoke.png')

# 回复 my_friend 发送的消息
# @bot.register(my_friend)
# def reply_my_friend(msg):
#    return 'received: {} ({})'.format(msg.text, msg.type)

# 回复发送给自己的消息，可以使用这个方法来进行测试机器人而不影响到他人
# @bot.register(bot.self, except_self=False)
# def reply_self(msg):
#   return 'received: {} ({})'.format(msg.text, msg.type)

# 打印出所有群聊中@自己的文本消息，并自动回复相同内容
# 这条注册消息是我们构建群聊机器人的基础
# @bot.register(Group, TEXT)
# def print_group_msg(msg):
#    if msg.is_at:
#        print(msg)
#        msg.reply(meg.text)

def auto_ai(text):
    url = "http://www.tuling123.com/openapi/api"
    api_key = "6217a0a8599240dabd313665983ed0bd"
    payload = {
        "key": api_key,
        "info": text,
        "userid": "666"
    }
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.content)
    if ('url' in result.keys()):

        return "[九日AI]  " + result["text"] + result["url"]
    else:
        return "[九日AI]  " + result["text"]


bot = Bot(cache_path=True, console_qr=True, qr_path='res/wxpy.pkl')  # 保留缓存自动登录。可用
"""
cache_path –
设置当前会话的缓存路径，并开启缓存功能；为 None (默认) 则不开启缓存功能。
开启缓存后可在短时间内避免重复扫码，缓存失效时会重新要求登陆。
设为 True 时，使用默认的缓存路径 ‘wxpy.pkl’。
console_qr –
在终端中显示登陆二维码，需要安装 pillow 模块 (pip3 install pillow)。
可为整数(int)，表示二维码单元格的宽度，通常为 2 (当被设为 True 时，也将在内部当作 2)。
也可为负数，表示以反色显示二维码，适用于浅底深字的命令行界面。
例如: 在大部分 Linux 系统中可设为 True 或 2，而在 macOS Terminal 的默认白底配色中，应设为 -2。
qr_path – 保存二维码的路径
qr_callback – 获得二维码后的回调，可以用来定义二维码的处理方式，接收参数: uuid, status, qrcode
login_callback – 登陆成功后的回调，若不指定，将进行清屏操作，并删除二维码文件
logout_callback – 登出时的回调
"""
_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
bot.file_helper.send('登录时间：%s' % _now)
print('微信助手已经启动')

# 定义各种类型
my_friend = ensure_one(bot.friends().search('小元'))
my_love = ensure_one(bot.friends().search('晴牵一线'))
my_test = ensure_one(bot.groups().search('test'))
my_u = ensure_one(bot.groups().search('猪年都要做自己'))

"""
chats – 消息所在的聊天对象：单个或列表形式的多个聊天对象或聊天类型，为空时匹配所有聊天对象
msg_types – 消息的类型：单个或列表形式的多个消息类型，为空时匹配所有消息类型 (SYSTEM 类消息除外)
except_self – 排除由自己发送的消息
run_async – 是否异步执行所配置的函数：可提高响应速度
enabled – 当前配置的默认开启状态，可事后动态开启或关闭
"""


@bot.register(chats=[my_u], except_self=False)
def group_message(msg):
    print('[接收]' + str(msg))

    _re = re.search(r'我', str(msg)).group()
    if _re:
        ret = '我……'
        print('搜到内容：%s' % ret)
        time.sleep(3)
        # return ret

    # if (msg.type == 'Picture'):  # 如果是图片
    #     ret = '[奸笑][奸笑]'
    # elif (msg.type == 'Text'):
    #     ret = '一切都会好起来的'
    #     # ret = auto_ai(msg.text)
    # print('[发送]' + str(ret))


@bot.register(my_test)
def group_message(msg):
    print('[接收]' + str(msg))

    # 如果发现内容中有关键词，则发送对应的内容
    re
    # 定期每间隔一个时间，发送一个内容
    if (msg.type != 'Text'):
        ret = '[奸笑][奸笑]'
    else:
        ret = auto_ai(msg.text)
    print('[发送]' + str(ret))
    return ret


@bot.register(chats=[Friend])#好友的
def forward_message(msg):
    print('[接收]' + str(msg))

    # if (msg.type != 'Text'):
    #     ret = '[奸笑][奸笑]'
    # else:
    #     ret = auto_ai(msg.text)

    # print('[发送]' + str(ret))
    # return ret


embed()