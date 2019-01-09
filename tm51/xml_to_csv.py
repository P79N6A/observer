# coding=utf-8
# 转换内容 ，并提取数据
import os
from datetime import datetime

from requests import RequestException

from bs4 import BeautifulSoup as bs
import time

# 自己人的账号
name = [ '我是威猛先生' , '不想讲' , '潶_佰' , '一个好名字' , '我是用户名' , '婵娟' , '幸福圈圈绕' , '青春水花' , '菠萝味蔡蔡' , '沈佳欣' , '程钰' , '杳杳' ,
         '天衣无缝' , '亚美尼亚' , '活泼雪儿'
    , '拉不拉洗' , '王昭君' , '拿一颗红豆泡茶' , '浮话' , 'YGPZ' , '金木小天使' , '小猪佩奇' , '吱吱吱吱吱' , 'linney丫' , '童梦妈妈123' , '慧lin' ,
         '慧琳lin' , '慧琳4921' , '慧琳琳' 'only one' , '微笑天使' , '米老鼠' , '飘渺。' , '心照不宣' , '小鲸鱼哎' , 'Elizabes' , '拾荒逝去的时光'
    , '秀秀、' , '大嘴巴' , '天赋选手' , '蓝透清澈的天' , '南极的鹅' , '美丽的明天01' , '菠萝味蔡蔡' , '期待自己宝宝'
    , '最美不过那过眼云烟丶' , '童梦妈妈_218a98' , '小叶子未来的妈妈。' , '姐姐的小脚丫' , '咚咚Every day'
    , '宝宝你要坚强' , '老公棒棒哒99' , '我1猪宝宝' , '李小华' , '丽水小楼听雀跃' , '北海爱上蓝海' ]

# 自己人的账号
com_name = [ (6058022 , 'Elizabes') , (6056829 , 'YGPZ') , (6029171 , '一个好名字') , (6056865 , '不想讲') ,
             (6061157 , '丽水小楼听雀跃') , (6059088 , '北海爱上蓝海') , (6039788 , '南极的鹅') , (6057331 , '吱吱吱吱吱') ,
             (6057114 , '咚咚Every day') , (56776 , '大嘴巴') , (6045024 , '天衣无缝') , (6044291 , '天赋选手') ,
             (6055976 , '姐姐的小脚丫') , (666 , '婵娟') , (6060994 , '宝宝你要坚强') , (6057333 , '小猪佩奇') , (6057369 , '小鲸鱼哎') ,
             (5463909 , '幸福圈圈绕') , (6057319 , '微笑天使') , (6057033 , '心照不宣') , (6057007 , '慧lin') , (6057020 , '慧琳4921') ,
             (6057009 , '慧琳lin') , (6061022 , '我1猪宝宝') , (6057323 , '我是威猛先生') , (6057316 , '我是用户名') ,
             (5476833 , '拾荒逝去的时光') , (6055977 , '拿一颗红豆泡茶') , (6044649 , '最美不过那过眼云烟丶') , (6035009 , '期待自己宝宝') ,
             (6044597 , '杳杳') , (6044318 , '沈佳欣') , (6044320 , '活泼雪儿') , (6053272 , '浮话') , (6035397 , '潶_佰') ,
             (6056059 , '王昭君') , (5827467 , '秀秀、') , (6044511 , '程钰') , (6056069 , '童梦妈妈123') ,
             (6057326 , '童梦妈妈_218a98') , (6057344 , '米老鼠') , (5802265 , '美丽的明天01') , (6061014 , '老公棒棒哒99') ,
             (5560866 , '菠萝味蔡蔡') , (6042978 , '蓝透清澈的天') , (6057332 , '金木小天使') , (6044550 , '青春水花') , (6057314 , '飘渺。') ,
             (6034906 , '小叶子未来的妈妈。') , (1 , 'admin') , (56776 , '大嘴巴') ]

actin_list = {'startAPP':'启动APP' , 'returnDesktop':'返回桌面' , 'returnAPP':'返回APP' , 'siteHome':'首页' ,
              'siteGroupHome':'社区首页' , 'siteAllForum':'全部版块' , 'siteForumIVF':'试管婴儿版块' , 'siteForumDiary':'妈妈日记版块' ,
              'siteForumGoods':'喜报版块' , 'siteForumMom':'童梦母婴版块' , 'siteForumInfertility':'不孕不育版块' ,
              'siteForumART':'人工授精版块' , 'siteForumMedical':'医疗信息版块' , 'siteForumServe':'社区服务版块' ,
              'siteForumActivity':'社区活动版块' , 'sitePostContent':'帖子详情' , 'siteNews':'消息页面' , 'siteShare':'分享帖子' ,
              'sitePostType':'选择发帖类型' , 'sitePostEditor':'帖子编辑页面' , 'siteSelectLabel':'选择标签' , 'siteSearch':'搜索页面' ,
              'siteSearchResults':'搜索结果' , 'sitePersonalCenter':'我的界面' , 'siteUserSettings':'用户设置' ,
              'siteChangePic':'修改头像' , 'siteChangeName':'修改昵称' , 'siteChangePassword':'修改密码' , 'siteAddMobile':'绑定手机' ,
              'siteChangeMobile':'更改手机' , 'siteAddEmail':'绑定邮箱' , 'siteChangeEmail':'更换邮箱' , 'siteFocus':'关注界面' ,
              'siteFan':'粉丝界面' , 'siteSet':'设置界面' , 'siteFeedback':'反馈界面' , 'siteAboutUs':'关于我们' , 'siteReport':'举报界面' ,
              'siteUserCard':'用户名片界面' , 'siteUserLogin':'手机登录/注册' , 'siteAccountLogin':'账号登陆' , 'siteForgot':'忘记密码' ,
              'siteAgreement':'用户协议' , 'popUp':'弹出框提示' , 'requestData':'请求数据时' , 'clickHomeSlideshow':'首页-轮播图' ,
              'clickHomeTopic':'首页-专题' , 'clickHomePost':'首页-推文' , 'clickHomeQuick':'首页-悬浮按钮' ,
              'clickGroupSearch':'社区-搜索按钮' , 'clickGroupNews':'社区-消息按钮' , 'clickGroupHotForum':'社区-热门版块' ,
              'clickGroupAllForum':'社区-全部版块' , 'clickGroupAdv':'社区-广告' , 'clickGroupAllChannel':'社区-全部页签' ,
              'clickGroupNewest':'社区-最新页签' , 'clickGroupBest':'社区-精华页签' , 'clickGroupHot':'社区-热门页签' ,
              'clickGroupPost':'社区-文章' , 'clickGroupPosting':'社区-发帖按钮' , 'clickAllForumBack':'全部版块-返回按钮' ,
              'clickAllForumIn':'全部版块-版块按钮' , 'clickForumAllChannel':'版块页面-全部按钮' , 'clickForumNewest':'版块页面-最新按钮' ,
              'clickForumBest':'版块页面-精华按钮' , 'clickForumHot':'版块页面-热门按钮' , 'clickForumTop':'版块页面-置顶贴' ,
              'clickForumPost':'版块页面-帖子' , 'clickForumPosting':'版块页面-发贴按钮' , 'clickPostContentBack':'帖子详情-返回按钮' ,
              'clickPostContentMenu':'帖子详情-功能按钮' , 'clickPostContentFocus':'帖子详情-关注/取关按钮' ,
              'clickPostContentReview':'帖子详情-评论按钮' , 'clickPostContentCollection':'帖子详情-收藏按钮' ,
              'clickPostContentLike':'帖子详情-点赞按钮' , 'clickPostContentShare':'帖子详情-分享按钮' ,
              'clickPostReviewReply':'帖子详情-评论区回复' , 'clickPostReviewLike':'帖子详情-评论区点赞' ,
              'clickPostContentPic':'帖子详情-点击图片' , 'clickPostContentDelete':'帖子详情-删除' , 'clickReviewReport':'评论界面-举报' ,
              'clickReviewLike':'评论界面-点赞' , 'clickReviewReply':'评论界面-回复' , 'clickReviewDelete':'评论界面-删除' ,
              'clickPostingAdd':'发帖界面-添加页签' , 'clickPosting':'发帖界面-发布按钮' , 'clickCenterPost':'个人中心-帖子' ,
              'clickCenterFocus':'个人中心-我的关注' , 'clickCenterFan':'个人中心-我的粉丝' , 'clickPostContentReply':'帖子详情-回复按钮'}


# 判断最近50个发日记的人的名单
def dd(self):
    _list = bs(self.text , 'lxml').find_all('row')

    # 排出内容人员的用户名
    _v = [ ]
    for i in com_name:
        _v.append(str(i[ 0 ]))

    # 排出内容人员
    value = [ ]
    for i in _list:
        if i.find_all('field')[ 1 ].text not in _v:
            _g = {'帖子id':i.find_all('field')[ 0 ].text , '用户ID':i.find_all('field')[ 1 ].text}
            value.append(i.find_all('field')[ 1 ].text)

    print('一共有 %d 个用户，用户ID为：%s' % (len(value) , value))


def od(self):
    j = [ ]
    n = [ ]
    for i in com_name:
        if i[ 1 ] in name:
            name.remove(i[ 1 ])
        else:
            pass

    print('没有查到的内容：%s' % name)
    print('查到的内容：%s' % j)


# 提取列表中的UID列表
class get_value:
    def __init__(self):
        self._forum_thread = '../res/forum_thread.xml'
        self._forum_thread_txt = '../res/forum_thread.txt'

        self._user_action_report = '../res/user_action_report.xml'
        self._user_action_report_txt = '../res/user_action_report.txt'

    def _get_value(self , Path):
        # 将内容格式化
        _text = open(Path , 'r' , encoding='utf-8').read()
        _switch = _text.replace('field name=' , 'field class=')
        _list = bs(_switch , 'lxml').find_all('row')

        # 格式化为列表
        _re = [ ]
        for i in _list:
            _j = {}
            for j in i.find_all('field'):
                _j[ j.get('class')[ 0 ] ] = j.text

            _re.append(_j)
            # print(_re)
        return _re

    @property  # 提取'../res/forum_thread.xml'中的内容
    def forum_thread(self):
        isExists = os.path.exists(self._forum_thread_txt)

        if isExists:  # 存在则读取内容
            _file = open(self._forum_thread_txt , 'r' , encoding='utf-8').read()
            _value = eval(str(_file))
            print('直接调用_forum_thread_txt')

        else:  # 不存在，则转换xml
            _value = self._get_value(self._forum_thread)

            # 并保存到txt
            _file = open(self._forum_thread_txt , 'w' , encoding='utf-8')
            _file.write(str(_value))
            _file.close()
            print('新建_forum_thread_txt')

        return _value

    @property
    def user_action_report(self):
        isExists = os.path.exists(self._user_action_report_txt)

        if isExists:  # 存在则读取内容
            _file = open(self._user_action_report_txt , 'r' , encoding='utf-8').read()
            _value = eval(str(_file))
            print('直接调用_user_action_report_txt')

        else:  # 不存在，则转换xml
            _value = self._get_value(self._user_action_report)

            # 并保存到txt
            _file = open(self._user_action_report_txt , 'w' , encoding='utf-8')
            _file.write(str(_value))
            _file.close()
            print('新建_user_action_report_txt')

        return _value


# 工具组件
class Tool:
    # 获取列表中的uid
    def get_uid(self , Data):  # 提取用户ID、并去除0
        _value = [ ]
        for i in Data:
            if i[ 'uid' ] not in _value:
                # print(type(i[ 'uid' ]))
                _value.append(i[ 'uid' ])

        if '0' in _value:
            _value.remove('0')

        return _value

    # 新建文件夹
    def new_flie(self , Name):
        path = "./res/" + str(Name)
        # 判断路径是否存在
        isExists = os.path.exists(path)

        # print(isExists)
        # 判断结果
        if not isExists:
            os.makedirs(path)

        return path

    def out_com(self , List):
        # 排出内容人员的用户名
        _v = [ ]
        for i in com_name:
            _v.append(str(i[ 0 ]))

        # 排出内容人员
        value = [ ]
        for i in List:
            if i not in _v:
                value.append(i)

        return value


# 查看没有发帖的用户在做什么，保存到了res文件夹
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
            _save = open(file_50 + '/%s.txt' % _uid , 'w+' , encoding='utf-8')
            for i in _list:
                for j in range(len(i)):
                    _save.write(str(i[ j ]))
                    _save.write(' ')
                _save.write('\r\n')
            _save.close()
        elif len(_list) > 50 and len(_list) <= 100:
            # 创建文件
            _save = open(file_100 + '/%s.txt' % i , 'w+' , encoding='utf-8')
            for i in _list:
                for j in range(len(i)):
                    _save.write(str(i[ j ]))
                    _save.write(' ')
                _save.write('\r\n')
            _save.close()
        else:
            # 创建文件
            _save = open(file_1000 + '/%s.txt' % i , 'w+' , encoding='utf-8')
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
    file_name = 'file_' + str(Path)  # 文件名

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


if __name__ == '__main__':
    action()
    numbers(50)
    numbers(100)
    numbers(1000)
