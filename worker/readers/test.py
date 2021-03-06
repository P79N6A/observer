# -*- coding: UTF-8 -*-
# 通过从阅读者那里获取内容，并对内容进行解析，同时生成爬虫报告

# # 加载header信息
# import re
# import time
# from lxml import etree
# import pandas as pd
#
# from worker.url_info import URL_Info
#
# 加载解析地址库
import requests
from requests import RequestException
#
# import json
# import csv
#
# # 加载解析HTML库
# from bs4 import BeautifulSoup as BS
#
# # 导入获取地址的库
# # from worker.writers import save_list as Save
# from worker.agency import get_post
#
#
# class Spider(object):
#     # 构造请求头等
#     def __init__(self):
#         # 大麦网接受POST请求的地址
#         self.post_url = 'https://search.damai.cn/searchajax.html'
#
#         # 以后要试图用别到方法获取
#         self.Cookie = 'isg=BKys-EXc3E7Cn82CThRo44Q6f4zeZVAPNQZk9QbtuNf6EUwbLnUgn6KiNVmpgohn; l=aB8neGmpyhCp3pDBtManBsRP-xrxygBP2j0yxMazZiYGdP8ZuXKbBjno-Vw6d_qC55oy_X-iI; x5sec=7b226d65632d67756964652d7765623b32223a226330353961323833626333396639623439346663663365343461633235313234434d4341782b4546454a617937346a353176585946673d3d227d; UM_distinctid=15aa9009428293-0103a30182f46e8-1a441228-13c680-15aa9009429337; cn_7415364c9dab5n09ff68_dplus=%7B%22distinct_id%22%3A%20%2215aa9009428293-0103a30182f46e8-1a441228-13c680-15aa9009429337%22%2C%22initial_view_time%22%3A%20%221488889067%22%2C%22initial_referrer%22%3A%20%22http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzA4NjMyMzIyMA%3D%3D%26mid%3D2654063564%26idx%3D1%26sn%3Db2c9e26ab4628436e9dc1ff38f8e05d5%26scene%3D0%22%2C%22initial_referrer_domain%22%3A%20%22mp.weixin.qq.com%22%2C%22sp%22%3A%20%7B%22%24recent_outside_referrer%22%3A%20%22%24direct%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201546617582%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201546617582%7D%7D; x_hm_tuid=PGrpHppNc7p6qeO6rXzlt1Xkss1FsDkItpzuBytBQ5KWbMnMwqH0Nz0UiMR82FQq; _uab_collina=154633349240746853818272; destCity=%u6B66%u6C49; cna=W5Y0EQTl42YCARsRRUVaKCov; damai.cn_email="wapu@qq.com"; damai.cn_nickName=%E4%B9%9F%E9%97%A8%E7%9A%84%E9%97%A8; PHPStat_Return_Count_10000001=1; PHPStat_Return_Time_10000001=1492404093845; PHPStat_Cookie_Global_User_Id=_ck17040701013914617714059138794; PHPStat_First_Time_10000001=1491498099371'
#
#         # 请求内容
#         self.data = {
#             "cty": "武汉",
#             "ctl": "话剧歌剧",
#             "tsg": "0",
#             "order": "0"
#         }
#
#         # 上级页面
#         self.Referer = 'https://search.damai.cn/search.htm'
#
#         # 默认地址头
#         self._url_header = 'https://piao.damai.cn/'
#
#         self.listName = 'info_drama.csv'  # 第一次抓去之后，就可以放到这个里面了
#         # print(self.url)
#
#         self.re = 'https://search.damai.cn/searchajax.html'  # 抓去的大麦地址
#
#         #步骤参数
#         self.steps = 0
#
#         # 设置返回值
#         self._value=[]
#
#     # 主函数
#     def _do(self):
#
#         # 解析演出列表页面，返回包含演出基本信息的数组
#         _get_post = get_post(URL=self.post_url, DATA=self.data, COOKIE=self.Cookie, REFERER=self.Referer).todo()
#         print('获取页面信息成功\n')
#
#         # 获取有用信息
#         for j in range(len(_get_post)):
#             # 为了让代码更简洁，做了一个赋值
#             _info = _get_post[j]
#
#             # 获取有用的信息,属性
#             _j = {'标题': _info['name'],
#                   '副标题': _info['subhead'],
#                   '地点城市': _info['venuecity'],
#                   '演出场所': _info['venue'],
#                   '演出时间': _info['showtime'],
#                   '演出状态': _info['showstatus'],
#                   '演出类型': _info['subcategoryname'],
#                   'projectid': _info['projectid'],
#                   'imgurl': _info['imgurl'],
#                   '最低票价': _info['price'],
#                   '最高票价': _info['pricehigh'],
#                   '信息属性': self.steps
#                   }
#
#             # 添加剧名
#             if bool(re.search('《[^》]+》', _info['name'], flags=0)):  # 如果搜得到《》，则赋值到'剧名'
#                 _j['剧名'] = re.search('《[^》]+》', _info['name'], flags=0).group()
#             else:  # 如果提取不到《》，则写入日志
#                 # 之后在分析是，如果是空值，则不处理
#                 _j['剧名'] = None

#
#             self._value.append(_j)
#
#     @property
#     def get_value(self):
#         self._do()
#         return self._value
#
#         # 去重之后放到ListName这个文件中,是第一次获取数据，并返回去重后到数据
#         # _useful_url = Save(_get_url, self.listName)
#
#         # 和_list中的 showslist.csv 做比较，如果列表中已经有了，就删除，返回没有添加的DataFrame
#         # _clean_list = self.clean()
#
#         # 逐个地址获取演出的详细信息，将详细的信息添加进来，返回完整的DataFrame
#         # _good_info = self.get_info()
#
#     # 获取需要爬去的演出列表地址，并保存为：get_url.csv
#     def get_list(self):
#         # 获取post数据包
#         response = requests.post(url=self.url['url'], headers=self.url['headers'], data=self.url['data'])
#         # print(response)
#
#         # 将字符串数据转换成字典数据
#         dict_data = json.loads(response.text)
#         # print(dict_data)
#
#         # 将需要的爬取的字典数据存储在变量中
#         need_spider_data = dict_data["pageData"]["resultData"]
#         # print(need_spider_data)
#
#         # clean数据
#         _clean_list = []
#
#         # 提取内容那
#         for j in range(len(need_spider_data)):
#             _j = {'标题': need_spider_data[j]['name'],
#                   '副标题': need_spider_data[j]['subhead'],
#                   '地点城市': need_spider_data[j]['venuecity'],
#                   '演出场所': need_spider_data[j]['venue'],
#                   '演出时间': need_spider_data[j]['showtime'],
#                   '演出状态': need_spider_data[j]['showstatus'],
#                   '演出类型': need_spider_data[j]['subcategoryname'],
#                   'projectid': need_spider_data[j]['projectid'],
#                   'imgurl': need_spider_data[j]['imgurl'],
#                   '最低票价': need_spider_data[j]['price'],
#                   '最高票价': need_spider_data[j]['pricehigh'],
#                   '剧名': re.search('《[^》]+》', _j['标题'], flags=0).group()
#                   }
#
#             _clean_list.append(_j)
#
#         # 测试字典数据是否能解析出来
#         print(_clean_list)
#
#         # 保存内容到
#
#         return _clean_list
#
#     # 获取列表中每条页面的有用信息,并保存在原来的文件中，并保存到
#     def get_info(self):
#         _data = pd.DataFrame(
#             pd.read_csv('/Users/tama1/Documents/ob/worker/readers/get_url.csv', header=0, encoding='UTF-8'))
#
#         # # 增加是否抓取详情的列
#         _data['蜘蛛状态'] = False
#         # print(test)
#
#         # 建立容器
#         gat_info_list = []
#
#         # 遍历列表
#         for i in _data.iterrows():
#
#             # 如果本条数据没有被爬取，则爬取
#             if i[1]['蜘蛛状态'] == False:
#                 # 拼接地址
#                 _url = self._url_header + str(i[1]['projectid']) + '.html'
#                 # print(_url)
#
#                 # 打包出请求表头
#                 _url_info = URL_Info(_url).damai()
#
#                 # 解析页面
#                 # _html = pares(_url_info)
#                 # print(_html)
#
#                 # 测试用
#                 _test = """<!DOCTYPE html>
#                 #
#                 # <html xmlns="http://www.w3.org/1999/xhtml">
#                 # <head>
#                 # <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
#                 # <meta content="a2o6e" name="spm-id"/>
#                 # <meta content="webkit" name="renderer"/>
#                 # <meta content="webkit" name="force-rendering"/>
#                 # <meta content="IE=edge,chrome=1" http-equiv="X-UA-Compatible">
#                 # <meta content="no-cache" http-equiv="pragma"/>
#                 # <meta content="no-cache,must-revalidate" http-equiv="cache-control"/>
#                 # <meta content="0" http-equiv="expires"/>
#                 # <title>武汉话剧歌剧 黑色喜剧《驴得水》武汉站【网上订票】– 大麦网</title>
#                 # <meta content="2018-12-28 00:31:49" name="create-time">
#                 # <meta content="武汉话剧歌剧,黑色喜剧《驴得水》武汉站,大麦网" name="keywords">
#                 # <meta content="大麦网（Damai.cn）武汉话剧歌剧 黑色喜剧《驴得水》武汉站将于2019-01-06在武汉琴台大剧院上演，大麦网为武汉琴台大剧院话剧歌剧 黑色喜剧《驴得水》武汉站门票代理，更多门票价格及订票详情请咨询大麦网武汉站." name="description">
#                 # <meta content="0.5" name="aplus-auto-exp-visible"/>
#                 # <meta content="500" name="aplus-auto-exp-duration"/>
#                 # <meta content='[{"logkey":"/damai_pc.default.project_qr_purchase","tag":"div","filter":"data-spm-auto","props":["item_id"]}]' name="aplus-auto-exp"/>
#                 # <link href="//dui.dmcdn.cn/??dm_2015/goods/css/style.css?v5.28.0,damai_v2/login_register3.0/css/style.css?v5.28.0" rel="stylesheet" type="text/css"/>
#                 # <link href="//g.alicdn.com/??damai/pc-wx/0.1.0/index.css" rel="stylesheet" type="text/css"/>
#                 # <style type="text/css">
#                 # .chat-view-xiaoneng-version{opacity:0;}
#                 # .m-choose .tt { padding-top: 10px; }
#                 # .m-cart .tt { padding-top: 16px; }
#                 # .m-choose .lst .s_manjian { height: 71px; }
#                 # .jiathis_style  .jtico{text-align:left;overflow:hidden;display:block!important;height:16px!important;line-height:16px!important;padding-left:20px!important;cursor:pointer;}
#                 # .jiathis_style  .jtico:hover{opacity:0.8;}
#                 # .jiathis_style .jiathis_txt {float: left;font-size: 12px;line-height: 18px !important;text-decoration: none;}
#                 # </style>
#                 # <script type="text/javascript">
#                 # var projectInfo = {"ProjectID":171739,"CityID":586,"Name":"黑色喜剧《驴得水》武汉站","ShowTime":"2019-01-06","Price":80.00,"SiteStatus":3,"VenueName":"武汉琴台大剧院","IsOnlyXuanZuo":true,"QuestionPass":false,"TicketValidateType":0,"htmlName":null,"Tabcontrol":0,"IsShowStartTime":false,"StartTicketTime":"\/Date(1545113426000)\/","SellStartTime":"\/Date(1545113403000)\/","OptimizationTicket":0};
#                 # var hostName = "wuhan", itemDomain = "piao.damai.cn", categoryId = 3, is_show_perform_calendar = 0;
#                 # is_show_perform_calendar = 1;
#                 # var PrivelegePId=108944;
#                 #
#                 # var is_show_qr_code = 0;
#                 # </script>
#                 # </meta></meta></meta></meta></head>
#                 # <body data-spm="project">
#                 # <script exparams="clog=o&amp;aplus&amp;sidx=aplusSidex&amp;ckx=aplusCkx" id="beacon-aplus" src="//g.alicdn.com/alilog/mlog/aplus_v2.js" type="text/javascript"></script>
#                 # <div class="g-hd" style="position:static;">
#                 # <div class="g-hdc">
#                 # <input id="Hidden1" type="hidden" value="%e9%bb%91%e8%89%b2%e5%96%9c%e5%89%a7%e3%80%8a%e9%a9%b4%e5%be%97%e6%b0%b4%e3%80%8b%e6%ad%a6%e6%b1%89%e7%ab%99"/>
#                 # <input id="Title" type="hidden" value="我在@大麦网 『www.damai.cn』发现了一个非常不错的演出:『黑色喜剧《驴得水》武汉站』,时间是2019-01-06，场馆在,强烈推荐！分享一下&gt;&gt;&gt;&gt;&gt;&gt;"/>
#                 # <input id="NameCN" type="hidden" value="%ba%da%c9%ab%cf%b2%be%e7%a1%b6%c2%bf%b5%c3%cb%ae%a1%b7%ce%e4%ba%ba%d5%be"/>
#                 # <input id="LinkCN" type="hidden" value="https%3a%2f%2fpiao.damai.cn%2f171739.html"/>
#                 # <input id="cityId" type="hidden" value="586"/>
#                 # <input id="cityName" type="hidden" value="武汉"/>
#                 # <input id="CategoryID" type="hidden" value="3"/>
#                 # <input id="ChildCategoryID" type="hidden" value="3"/>
#                 # <input id="epconfig" type="hidden" value="120"/>
#                 # <!-- logo begin -->
#                 # <h1 class="m-logo"><a href="//www.damai.cn/" title="大麦网">大麦</a></h1>
#                 # <!-- logo end -->
#                 # <!-- 城市切换 begin -->
#                 # <div class="m-citys">
#                 # <span class="tt">武汉站</span>
#                 # </div>
#                 # <!-- 城市切换 end -->
#                 # <!-- 顶部栏 begin -->
#                 # <ul class="m-topbar">
#                 # <li class="itm first">
#                 # <!-- 搜索 begin -->
#                 # <div class="m-sch">
#                 # <input class="ipt" id="txtSearchText" placeholder="请输入演出、赛事、艺人、场馆名称..." type="text"/>
#                 # <a class="btn" href="javascript:;" id="btnSearch">搜索</a>
#                 # <div class="m-suggest" id="rlist_txtSearchText">
#                 # </div>
#                 # </div>
#                 # <!-- 搜索 end -->
#                 # </li>
#                 # <li class="itm">
#                 # <!-- 用户登录 begin -->
#                 # <div class="m-sign m-sign-log">
#                 # <label id="userLoginInfo">
#                 # <a class="user" href="javascript:;"><img original="//dui.dmcdn.cn/dm_2015/goods/images/user.png"/></a>
#                 # <span class="sign"><a href="//www.damai.cn/redirect.aspx?type=login">登录</a> | <a href="//www.damai.cn/redirect.aspx?type=reg">注册</a></span>
#                 # </label>
#                 # <div class="menu" my="menu" style="display:none;">
#                 # <a class="first" href="//my.damai.cn/account/myinfo.aspx" target="_blank">个人信息</a>
#                 # <a href="//order.damai.cn/index.aspx" target="_blank">订单管理</a>
#                 # <a href="https://coupon.damai.cn/coupon-web-damai/mycoupon/myCoupon" target="_blank">我的优惠券</a>
#                 # <a class="exit" href="//www.damai.cn/redirect.aspx?type=loginout">退出</a>
#                 # </div>
#                 # </div>
#                 # <!-- 用户登录 end -->
#                 # </li>
#                 # </ul>
#                 # <!-- 顶部栏 end -->
#                 # </div>
#                 # </div>
#                 # <div class="g-bd" data-color="" data-image="">
#                 # <div class="g-bdc">
#                 # <div class="g-mn">
#                 # <!-- 终极页项目信息 begin -->
#                 # <div class="m-box m-box-col2 m-box-goods" id="projectInfo">
#                 # <div class="hd">
#                 # <!-- 面包屑 begin -->
#                 # <p class="m-crm">
#                 # <strong>黑色喜剧《驴得水》武汉站</strong>
#                 # </p>
#                 # <!-- 面包屑 end -->
#                 # </div>
#                 # <div class="mn">
#                 # <!-- 项目海报 begin -->
#                 # <div class="m-poster">
#                 # <!-- 项目图 begin -->
#                 # <div class="m-picbox">
#                 # <img alt="黑色喜剧《驴得水》武汉站" height="373" original="//pimg.dmcdn.cn/perform/project/1717/171739_n.jpg" title="黑色喜剧《驴得水》武汉站" width="277"/>
#                 # </div>
#                 # <!-- 项目图 end -->
#                 # <!-- 分享 begin -->
#                 # <div class="m-share" data-spm="click">
#                 # <span class="txt">分享到：</span>
#                 # <!-- JiaThis Button BEGIN -->
#                 # <div class="jiathis_style">
#                 # <a class="jiathis_button_tsina" data-spm-click="gostr=/damai_pc.default.click;localid=share_0;dclicktitle=微博&amp;ditem_id=171739" href="http://service.weibo.com/share/share.php?title=我在@大麦网 『www.damai.cn』发现了一个非常不错的演出:『黑色喜剧《驴得水》武汉站』,时间是2019-01-06，场馆在,强烈推荐！分享一下&gt;&gt;&gt;&gt;&gt;&gt;&amp;url=https%3a%2f%2fpiao.damai.cn%2f171739.html&amp;source=bookmark&amp;appkey=3588246140&amp;pic=https%3A%2F%2Fpimg.dmcdn.cn%2Fperform%2Fproject%2F1717%2F171739_n.jpg&amp;ralateUid=1722647874" target="_blank" title="分享到微博"><span class="jiathis_txt jtico jtico_tsina"></span></a>
#                 # <a class="jiathis_button_weixin" data-spm-click="gostr=/damai_pc.default.click;localid=share_1;dclicktitle=微信&amp;ditem_id=171739" title="分享到微信"><span class="jiathis_txt jtico jtico_weixin"></span></a>
#                 # <a class="jiathis_button_qzone" data-spm-click="gostr=/damai_pc.default.click;localid=share_2;dclicktitle=QQ空间&amp;ditem_id=171739" href="http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url=https%3A%2F%2Fpiao.damai.cn%2F171739.html&amp;title=我在@大麦网 『www.damai.cn』发现了一个非常不错的演出:『黑色喜剧《驴得水》武汉站』,时间是2019-01-06，场馆在,强烈推荐！分享一下&gt;&gt;&gt;&gt;&gt;&gt;&amp;pics=http%3A%2F%2Fpimg.dmcdn.cn%2Fperform%2Fproject%2F1717%2F171739_n.jpg&amp;summary=" target="_blank" title="分享到QQ空间"><span class="jiathis_txt jtico jtico_qzone"></span></a>
#                 # </div>
#                 # <!-- JiaThis Button END -->
#                 # </div>
#                 # <!-- 分享 end -->
#                 # </div>
#                 # <!-- 项目海报 end -->
#                 # <!-- 项目模块 begin -->
#                 # <div class="m-goods">
#                 # <h2 class="tt" data-spm="click">
#                 # <span class="txt">黑色喜剧《驴得水》武汉站</span>
#                 # </h2>
#                 # <h3 class="stt">
#                 # <span class="quotl"></span>
#                 # <span class="txt">驴得水</span>
#                 # <span class="quotr"></span>
#                 # </h3>
#                 # <!-- 时间轴 begin -->
#                 # <div class="m-timeline m-timeline-3" id="projectAxis">
#                 # <div class="wrap">
#                 # <div class="box">
#                 # <div class="bar"><div class="line" style="width:290px"></div></div>
#                 # <div class="itm itm-1 " style="width:145px"><h3 class="txt">项目待定</h3><div class="ico"></div><p class="date"></p></div>
#                 # <div class="itm itm-2 " style="width:145px"><h3 class="txt">预售/预订</h3><div class="ico"></div><p class="date"></p></div>
#                 # <div class="itm itm-3 itm-crt" style="width:145px"><h3 class="txt">售票中</h3><div class="ico"></div><p class="date"></p></div>
#                 # <div class="itm itm-4 " style="width:145px"><h3 class="txt">演出开始</h3><div class="ico"></div><p class="date"></p></div>
#                 # </div>
#                 # </div>
#                 # </div>
#                 # <!-- 时间轴 end -->
#                 # <!-- 产品模块 begin -->
#                 # <div class="m-product m-product-2 -m-product-1 j_goodsDetails">
#                 # <div class="m-goodstips m-goodstips-2" id="projectStatusDescn" style="display:none;">
#                 # <div class="hd">
#                 # <i class="ico"></i>
#                 # <span class="txt txt-status" data-status="售票中">
#                 # 						售票中						</span>
#                 # </div>
#                 # <div class="bd">
#                 # <div class="tips">
#                 # <div class="box z-hide"><p class="itm">
#                 # </p></div>
#                 # <div class="ops"><span class="btnsel"></span></div>
#                 # </div>
#                 # </div>
#                 # <div class="mark" id="jinpaiMark" style="display:none;"></div>
#                 # </div>
#                 # <div class="m-countdown" data-init="false" id="toBeAboutTo" style="display:none;">
#                 # <div class="ct"></div>
#                 # <div class="tips"><i class="ico"></i><span class="txt j_endtime"></span></div>
#                 # </div>
#                 # <!-- 促销信息模块 begin -->
#                 # <div class="" data-col="1" data-row="4" id="yhcx"></div>
#                 # <div class="m-load z-hide" id="getInfoFail"><p class="txt"><i></i>加载失败</p></div>
#                 # <!-- 促销信息模块 end -->
#                 # <!-- 选择日历模块 begin -->
#                 # <div class="m-choose m-choose-picker" data-col="4" data-row="3" style="display:none">
#                 # <h3 class="tt" style="padding-top: 6px;">选择时间：</h3>
#                 # <div class="ct">
#                 # <div class="m-datepicker">
#                 # <div class="weekbox">
#                 # <div class="box"></div>
#                 # </div>
#                 # <div class="datebox">
#                 # <div class="box"></div>
#                 # </div>
#                 # </div>
#                 # </div>
#                 # </div>
#                 # <!-- 选择日历模块 end -->
#                 # <!-- 选择日期模块 begin -->
#                 # <div class="m-choose m-choose-date " data-col="4" data-spm="clicktime" id="performList">
#                 # <h3 class="tt">
#                 # 								演出时间：</h3>
#                 # <div class="ct">
#                 # <ul class="lst lst-dis">
#                 # <li class="loading" style="line-height:32px;padding-left:10px"><span>加载中，请稍后...</span></li>
#                 # </ul>
#                 # </div>
#                 # </div>
#                 # <!-- 选择日期模块 end -->
#                 # <!-- 选择票价模块 begin -->
#                 # <div class="m-choose m-choose-price " data-col="4" data-spm="clickprice" id="priceList">
#                 # <h3 class="tt">选择票价：</h3>
#                 # <div class="ct">
#                 # <ul class="lst lst-dis">
#                 # <li class="loading" style="line-height:32px;padding-left:10px"><span>加载中，请稍后...</span></li>
#                 # </ul>
#                 # <div class="tips-warn z-hide" id="warnXiangou"><span class="txt"></span></div>
#                 # <div class="tips tips-oos"><span class="ico"></span><span class="txt">暂时无货，登录试试运气~</span></div>
#                 # </div>
#                 # </div>
#                 # <!-- 选择票价模块 end -->
#                 # <!-- 购物车模块 begin -->
#                 # <div class="m-cart " data-spm="click" id="cartList" style="display:none;">
#                 # <h3 class="tt" style="display:none;">您选择了：</h3>
#                 # <div class="ct" style="display:none;">
#                 # <ul class="lst"></ul>
#                 # </div>
#                 # <div class="ops">
#                 # <a class="u-btn u-btn-c1 u-btn-choose" data-spm-click="gostr=/damai_pc.default.click;localid=buyselectseatbtn;ditem_id=171739" href="javascript:;" id="btnXuanzuo" style="display:none;">选座购买</a>
#                 # </div>
#                 # </div>
#                 # <!-- 购物车模块 end -->
#                 # <div class="m-probox m-remine" id="kaishoutixingLayer" style="display:none;">
#                 # <input class="u-ipt u-ipt-md" id="kaishoutixingPhone" placeholder="请输入接收信息的手机号" type="text"/>
#                 # <a class="u-btn u-btn-md u-btn-remind" href="javascript:kaishoutixing;" id="btnKaishoutixing"><i class="ico"></i><span class="txt">开售提醒</span></a>
#                 # </div>
#                 # <div class="m-countdown" data-init="false" id="jinpaiCounter" style="display:none;">
#                 # <div class="ct"><span class="lab">距抢座开始：</span>
#                 # <span class="num num-0">0</span><span class="num num-0">0</span><span class="txt">小时</span>
#                 # <span class="num num-0">0</span><span class="num num-0">0</span><span class="txt">分</span>
#                 # <span class="num num-0">0</span><span class="num num-0">0</span><span class="txt">秒</span></div>
#                 # <div class="tips"><i class="ico"></i><span class="txt"></span></div>
#                 # </div>
#                 # <div class="m-goodstab" id="jinpaiTabs" style="display:none;">
#                 # <div class="hd">
#                 # <ul class="tab">
#                 # <li class="itm itm-tab j_tabOrders f-dn">我的抢座</li>
#                 # <li class="itm itm-tab z-crt j_tabLives">抢座实况</li>
#                 # <li class="itm itm-tab j_tabGroups f-dn">查看分组说明</li>
#                 # </ul>
#                 # <div class="sort" id="jinpaiMyRanking" style="margin-right:8px;">我的排名：<strong>-</strong></div>
#                 # </div>
#                 # <div class="bd">
#                 # <div class="itm itm-tab f-dn" id="jinpaiOrders">
#                 # <table class="m-table" rules="rows">
#                 # <thead>
#                 # <tr>
#                 # <th class="cola">订单号</th>
#                 # <th class="colb">票价（数量）</th>
#                 # <th class="cola">排名</th>
#                 # <th class="cola">分组</th>
#                 # <th class="colc">进场时间</th>
#                 # <th>操作</th>
#                 # </tr>
#                 # </thead>
#                 # <tbody></tbody>
#                 # </table>
#                 # </div>
#                 # <div class="itm itm-tab z-show" id="jinpaiLives">
#                 # <!-- 抢座实况 begin -->
#                 # <div class="m-grablive">
#                 # <div class="inner">
#                 # <ul class="lst" id="jinpaiLiveList"></ul>
#                 # </div>
#                 # </div>
#                 # <!-- 抢座实况 end -->
#                 # </div>
#                 # <div class="itm itm-tab f-dn" id="jinpaiGroupList">
#                 # <!-- 查看分组说明 begin -->
#                 # <div class="m-groupshow">
#                 # <div class="inner">
#                 # <ul class="lst"></ul>
#                 # </div>
#                 # </div>
#                 # <!-- 查看分组说明 end -->
#                 # </div>
#                 # </div>
#                 # </div>
#                 # <a id="privilegeAnchor" name="projectPrivilege"></a>
#                 # <div class="m-qrcode"><!-- 大麦网客户端二维码 -->
#                 # <h3 class="tt"><span id="ErWeiMaTips">手机扫一扫<br/>下单更快捷</span></h3>
#                 # <p class="ct"><img alt="大麦网客户端" height="108" original="//static.dmcdn.cn/Erweima/1717/171739.jpg" width="109"/></p>
#                 # </div>
#                 # <div class="m_heighlight_tip"></div>
#                 # </div>
#                 # <!-- 产品模块 end -->
#                 # </div>
#                 # <!-- 项目模块 end -->
#                 # </div>
#                 # <!-- 侧栏 begin -->
#                 # <div class="sd">
#                 # <div class="m-sdbox m-showtime">
#                 # <h2 class="tt">演出时间</h2>
#                 # <div class="ct">
#                 # <span class="txt">2019-01-06</span>
#                 # <a class="u-btn u-btn-cal" href="javascript:;" id="rili" onclick="showcalendar(event, this); return false;" onfocus="showcalendar(event, this);"><i>日历</i></a>
#                 # </div>
#                 # </div>
#                 # <!-- 演出场馆 begin -->
#                 # <div class="m-sdbox m-venue">
#                 # <h2 class="tt">演出场馆</h2>
#                 # <div class="ct">
#                 # <p class="txt"> 武汉琴台大剧院 </p>
#                 # </div>
#                 # </div>
#                 # <!-- 演出场馆 end -->
#                 # <!-- 票品支持 begin -->
#                 # <div class="m-sdbox m-support">
#                 # <h2 class="tt">票品支持</h2>
#                 # <div class="ct">
#                 # <ul class="m-mantab">
#                 # <li class="itm"><a class="u-btn u-btn-choose" href="javascript:;"><i></i>选座</a>
#                 # <div class="layer">
#                 # <div class="hd"><a class="btn-close" href="javascript:;">关闭</a></div>
#                 # <div class="bd">
#                 # <p>本项目支持自助选座。</p><p>1. 选择演出时间，并点击"选座购买"进入选座页面。</p><p>2. 选座后，在15分钟内支付成功，选座生效。</p>
#                 # </div>
#                 # <div class="ft">
#                 # <a class="btn btn-close" href="javascript:;">关闭</a>
#                 # </div>
#                 # </div>
#                 # </li>
#                 # <li class="itm"><a class="u-btn u-btn-super" href="javascript:;"><i></i>超级票</a>
#                 # <div class="layer">
#                 # <div class="hd"><a class="btn-close" href="javascript:;">关闭</a></div>
#                 # <div class="bd">
#                 # <p>1.本项目支持使用【电子钱包-超级票账户】消费，支付时优先扣减超级票余额。</p><p>2.超级票成功充值电子钱包后，享受全网通兑、分次消费、无有效期限制、无使用张数限制、秒杀、抢票等服务。</p>
#                 # </div>
#                 # <div class="ft">
#                 # <a class="btn btn-close" href="javascript:;">关闭</a>
#                 # </div>
#                 # </div>
#                 # </li>
#                 # <li class="itm"><a class="u-btn u-btn-wallet" href="javascript:;"><i></i>电子钱包</a>
#                 # <div class="layer">
#                 # <div class="hd"><a class="btn-close" href="javascript:;">关闭</a></div>
#                 # <div class="bd">
#                 # <p>本项目支持电子钱包。</p>
#                 # <p>1. 电子钱包是由大麦网自主研发的第三方支付平台</p>
#                 # <p>2. 为每一个用户在购票过程中提供"简单、安全、快速"的在线支付解决方案</p>
#                 # </div>
#                 # <div class="ft">
#                 # <a class="btn btn-close" href="javascript:;">关闭</a>
#                 # </div>
#                 # </div>
#                 # </li>
#                 # <li class="itm"><a class="u-btn u-btn-credit" href="javascript:;"><i></i>返积分</a>
#                 # <div class="layer">
#                 # <div class="hd"><a class="btn-close" href="javascript:;">关闭</a></div>
#                 # <div class="bd">
#                 # <p>【会员多倍积分】 大麦会员按不同等级可分别获得消费金额×50%到100%比例的积分返还</p>
#                 # <p>您可以在积分商城兑换明星周边、演出票品、优惠卡券等商品，也可以参与抽奖活动，赢取幸运大礼。</p>
#                 # </div>
#                 # <div class="ft">
#                 # <a class="btn btn-close" href="javascript:;">关闭</a>
#                 # </div>
#                 # </div>
#                 # </li>
#                 # <!-- -->
#                 # <li class="itm"><a class="u-btn u-btn-express" href="javascript:;"><i></i>快递</a></li>
#                 # </ul>
#                 # </div>
#                 # </div>
#                 # <!-- 票品支持 end -->
#                 # <!-- 实票配送 begin -->
#                 # <div class="m-sdbox m-entity" id="freight">
#                 # <h2 class="tt"> 实票配送</h2>
#                 # <div class="ct">
#                 # <div class="u-sel u-sel-c1 u-sel-entity">
#                 # <div class="hd">
#                 # <span class="txt">北京</span>
#                 # <span class="ico"></span>
#                 # </div>
#                 # <div class="menu">
#                 # <ul class="lst"></ul>
#                 # </div>
#                 # </div>
#                 # <p class="tips">加载中...</p>
#                 # </div>
#                 # </div>
#                 # <!-- 实票配送 end -->
#                 # </div>
#                 # <!-- 侧栏 end -->
#                 # </div>
#                 # <!-- 终极页项目信息 end -->
#                 # <!-- 终极页项目详情 begin -->
#                 # <div class="m-box m-box-col2">
#                 # <div class="mn">
#                 # <!-- 项目详情 begin -->
#                 # <div class="m-detail">
#                 # <!-- 项目详情选项卡 begin -->
#                 # <div class="m-infonav" id="m-infonav">
#                 # <div class="hd">
#                 # <div class="nav">
#                 # <ul class="tab">
#                 # <li><a class="itm itm-tab first z-crt" data-href="#m-infonav" data-idx="0" data-show="1,2" href="javascript:;" id="tabProjectDescn"><i></i><span class="txt">演出信息</span></a></li>
#                 # <li><a class="itm itm-tab" data-href="#m-infonav" data-idx="3" href="javascript:;"><i></i><span class="txt">购买说明</span></a></li>
#                 # <li><a class="itm itm-tab" data-href="#m-infonav" data-idx="4" href="javascript:;"><i></i><span class="txt">付款方式</span></a></li>
#                 # </ul>
#                 # <div class="buy" id="buyButtonC" style="display:none;">
#                 # <a class="u-btn u-btn-buy " href="javascript:;" id="btnXuanzuo2" style="display:none;"><i class="ico"></i><span class="txt">选座购买</span></a>
#                 # </div>
#                 # </div>
#                 # </div>
#                 # <div class="bd">
#                 # <div class="itm-tab z-show" rel="0">
#                 # <!-- 演出信息 begin -->
#                 # <div class="m-infobase m-liveinfo">
#                 # <dl class="infoitm">
#                 # <dt class="tt"><span class="txt">基本信息</span></dt>
#                 # <dd class="ct">
#                 # <div class="table-info">
#                 # <table class="m-table2">
#                 # <tbody>
#                 # <tr>
#                 # <td class="bg" width="90">演出时间</td><td>2019-01-06</td> <td class="bg" width="90">演出场馆</td><td width="200">武汉琴台大剧院</td> </tr><tr> <td class="bg" width="90">演出时长</td><td>约70分钟</td> <td class="bg" width="90">入场时间</td><td width="200">演出前约30分钟</td> </tr><tr> </tr><tr> </tr><tr> </tr><tr> <td class="bg">限购</td><td>选座购买每单限6张</td> <td class="bg">儿童入场提示</td><td>不建议14岁以下儿童观看<br/></td> </tr><tr> <td class="bg">禁止携带物品</td>
#                 # <td>由于安保和版权的原因，大多数演出、展览及比赛场所禁止携带食品、饮料、专业摄录设备、打火机等物品，请您注意现场工作人员和广播的提示，予以配合</td>
#                 # <td class="bg">付款时效提醒</td>
#                 # <td>购票下单成功后需在15分钟内完成支付，未支付成功的订单，将在下单15分钟后系统自动取消，所选价位将自动释放后重新点亮，大家可及时刷新购票页面进行购买。</td>
#                 # </tr> <tr> <td class="bg">缺货登记提醒</td>
#                 # <td>所需票价若为灰色，说明已经售完。您可以在当前页面进行缺货登记，后期如果有票会以短信形式及时通知。</td>
#                 # <td class="bg">发票说明</td>
#                 # <td>发票由现场提供，演出当天请持门票到演出场馆开具</td>
#                 # </tr> <tr> <td class="bg">座位类型</td>
#                 # <td>请按门票对应位置，有序对号入座</td>
#                 # <td class="bg">物品寄存</td>
#                 # <td>无寄存处，请自行保管携带物品</td>
#                 # </tr> <tr> <td class="bg">有无中文字幕</td>
#                 # <td>演出现场无字幕</td>
#                 # <td class="bg">演出语言</td>
#                 # <td>普通话</td>
#                 # </tr> <tr> <td class="bg">主演演员（团体）</td>
#                 # <td>周申，刘露<br/></td>
#                 # <td class="bg">大麦网首次开售时全场可售门票总张数</td>
#                 # <td>300张</td>
#                 # </tr> <tr> <td class="bg">退换说明</td>
#                 # <td>票品不支持退换。如无法正常观看，还请自行处理，给您带来不便敬请谅解</td>
#                 # <td class="bg"></td><td></td></tr>
#                 # </tbody>
#                 # </table>
#                 # </div>
#                 # </dd>
#                 # </dl>
#                 # <dl class="infoitm">
#                 # <dt class="tt"><span class="txt">项目介绍</span></dt>
#                 # <dd class="ct">
#                 # <div class="pre"><h4>
#                 # 	演出介绍
#                 # </h4>
#                 # 　　民国时期的一个乡村学校，由于严重缺水，校长将一头驴虚报成英语  老师，来为学校挑水。面临上级的检查，大家决定让一个铁匠来冒充  这个叫"驴得水"的英语老师。但是上级却对这位"驴"老师刨根问  底。眼看事情要败露，大家只能用更多的谎言去弥补。于是，事件的发展越来越超乎校长和老师们的预料……<br/>
#                 # <strong>　　导演/编剧 周申： </strong><br/>
#                 # 　　2006年独立指导小剧场话剧《朱丽小姐》联合导演话剧《三姊妹》  2007年（商业展示）自编自导小型音乐短剧《浪漫夜晚》  联合导演小剧场话剧《秃头歌女》  2008年编剧并联合导演音乐浪漫喜剧《如果，我不是我》<br/>
#                 # <strong>　　导演/编剧 刘露：</strong><br/>
#                 # 　　中央戏剧学院  导演系本科、导演系研究生  代表作：  《三姊妹》《秃头歌女》《如果我不是我》</div>
#                 # </dd>
#                 # </dl>
#                 # <dl class="infoitm">
#                 # <dt class="tt"><span class="txt">温馨提示</span></dt>
#                 # <dd class="ct">
#                 # <div class="table-info">
#                 # <table class="m-table2">
#                 # <tbody>
#                 # <tr>
#                 # <td class="bg">发票说明</td><td>发票由现场提供，演出当天请持门票到演出场馆开具</td>
#                 # </tr>
#                 # </tbody>
#                 # </table>
#                 # </div>
#                 # </dd>
#                 # </dl>
#                 # </div>
#                 # <!-- 演出信息 end -->
#                 # </div>
#                 # <!-- 1 -->
#                 # <div class="itm-tab" rel="3">
#                 # <!-- 购票说明 begin -->
#                 # <div class="m-infobase m-buydesc">
#                 # <dl class="infoitm">
#                 # <dt class="tt"><span class="txt">特别提示</span></dt>
#                 # <dd>
#                 # <h3 class="stt">售前提示</h3>
#                 # <p>1.为避免快递配送不能及时送达，演出距开场时间少于3天时不提供【快递配送】服务，请您谅解！您可以选择电子票或在线支付后上门自取纸质票。 <a href="//help.damai.cn/damai/contents/277/5966.html" target="_blank" title="点击查看上门取票地址">点击查看上门取票地址&gt;&gt;</a></p></dd>
#                 # <dd>
#                 # <p>2.凡演出票类商品，开票时间一般为演出前二到四周，正式开票后会第一时间短信通知您，请注意接收。</p>
#                 # </dd>
#                 # <dd>
#                 # <p>3.如您不是通过“选座购买”通道进行的票品购买，最终票品数量视项目主办方及场馆情况而定，正式开票后大麦网将根据用户付款先后顺序依次配票，可能存在票品不足不能为您配票的风险，如最终未能配票，大麦网承诺全额退款，但不承担其他损失。</p>
#                 # </dd>
#                 # <dd>
#                 # <h3 class="stt">支付方式</h3>
#                 # <p>网上银行（招商银行等） 支付平台（支付宝等） 转账汇款(招商银行等)　<a href="//help.damai.cn/damai/contents/281/5740.html" target="_blank" title="查看详情">查看详情&gt;&gt;</a></p>
#                 # </dd>
#                 # <dd>
#                 # <h3 class="stt">退/换货说明</h3>
#                 # <p>针对不可抗力和非不可抗力的退/换票情况和处理，请点击查阅<a href="//help.damai.cn/damai/contents/299/2228.html" target="_blank" title="大麦网退换货说明">大麦网退换货说明&gt;&gt;</a></p>
#                 # </dd>
#                 # </dl>
#                 # <dl class="infoitm">
#                 # <dt class="tt"><span class="txt">无线端购票</span></dt>
#                 # <dd>
#                 # <p>1.  使用智能设备用户在各应用商店中搜索"大麦"下载安装客户端，购票体验更流畅</p>
#                 # <p>2.  非智能设备用户可浏览器访问m.damai.cn进行演出查询，随时购票</p>
#                 # </dd>
#                 # <dd class="appdown">
#                 # <div class="applnk">
#                 # <a class="iphone" href="//mapi.damai.cn/href.aspx?id=1" target="_blank">iphone版</a>
#                 # <a class="ipad" href="//mapi.damai.cn/href.aspx?id=2" target="_blank">ipad版</a>
#                 # <a class="android" href="//mapi.damai.cn/href.aspx?id=5" target="_blank">android版</a>
#                 # </div>
#                 # </dd>
#                 # </dl>
#                 # <dl class="infoitm">
#                 # <dt class="tt"><span class="txt">网上订购</span></dt>
#                 # <dd><img -src="//dui.dmcdn.cn/dm_2015/goods/img/process.jpg" original="//dui.dmcdn.cn/dm_2015/goods/images/process.jpg"/></dd>
#                 # </dl>
#                 # <dl class="infoitm" id="orderOnCompany">
#                 # <dt class="tt"><span class="txt">上门订购</span></dt>
#                 # <dd>
#                 # <p>大麦网武汉分部</p>
#                 # <p>办公地址：武汉市武昌区临江大道96号武汉万达中心写字楼611-612 （积玉桥万达威斯汀酒店旁） <a class="c7" href="//map.damai.cn/Traffic/goThere.aspx?endCity=%e6%ad%a6%e6%b1%89&amp;to=1&amp;end_x_y=114.308719,30.564207&amp;end=%e5%a4%a7%e9%ba%a6%e7%bd%91%e6%ad%a6%e6%b1%89%e5%88%86%e9%83%a8" target="_blank" title="点击查看如何到达">点击查看如何到达</a></p>
#                 # <p>营业时间：周一至周六 9:00-18:00</p>
#                 # <p>支付说明：上门支持现金支付和刷卡支付 <a class="c7" href="//map.damai.cn/traffic/circumjacent.aspx?action=search&amp;cityName=%e6%ad%a6%e6%b1%89&amp;cityId=586&amp;Keyword=%e5%a4%a7%e9%ba%a6%e7%bd%91%e6%ad%a6%e6%b1%89%e5%88%86%e9%83%a8&amp;option=bank&amp;CenterLngLat=114.308719,30.564207" target="_blank" title="点击查看周边提款">点击查看周边提款</a></p>
#                 # </dd>
#                 # </dl>
#                 # </div>
#                 # <!-- 购票说明 end -->
#                 # </div>
#                 # <div class="itm-tab" rel="4">
#                 # <!-- 付款方式 begin -->
#                 # <div class="m-infobase m-paymode" style="display: block;">
#                 # <dl class="infoitm">
#                 # <dt class="tt"><span class="txt">在线支付</span></dt>
#                 # <dd><p>支持多家网上银行、支付平台（支付宝、快钱、银联、微信支付等）在线支付，<a href="//help.damai.cn/damai/channels/281.html" target="_blank">查看详情&gt;&gt;</a></p></dd>
#                 # <dd>
#                 # <h3 class="stt">支付平台：</h3>
#                 # <ul class="lst">
#                 # <li><img alt="支付宝" original="//static.dmcdn.cn/PayLogo/2.jpg" style="display: inline;"/></li>
#                 # <li><img alt="微信扫码支付" original="//static.dmcdn.cn/PayLogo/57.jpg" style="display: inline;"/></li>
#                 # </ul>
#                 # </dd>
#                 # <dd>
#                 # <h3 class="stt">网上银行：</h3>
#                 # <ul class="lst">
#                 # <li><img alt="招商银行" original="//static.dmcdn.cn/PayLogo/10.jpg" style="display: inline;"/></li>
#                 # <li><img alt="中国建设银行" original="//static.dmcdn.cn/PayLogo/11.jpg" style="display: inline;"/></li>
#                 # <li><img alt="中国工商银行" original="//static.dmcdn.cn/PayLogo/12.jpg" style="display: inline;"/></li>
#                 # <li><img alt="交通银行" original="//static.dmcdn.cn/PayLogo/13.jpg" style="display: inline;"/></li>
#                 # <li><img alt="中国农业银行" original="//static.dmcdn.cn/PayLogo/14.jpg" style="display: inline;"/></li>
#                 # <li><img alt="广东发展银行" original="//static.dmcdn.cn/PayLogo/15.jpg" style="display: inline;"/></li>
#                 # <li><img alt="中国银行" original="//static.dmcdn.cn/PayLogo/17.jpg" style="display: inline;"/></li>
#                 # <li><img alt="上海浦东发展银行" original="//static.dmcdn.cn/PayLogo/23.jpg" style="display: inline;"/></li>
#                 # </ul>
#                 # </dd>
#                 # </dl>
#                 # <dl class="infoitm">
#                 # <dt class="tt"><span class="txt">柜台付款</span></dt>
#                 # <dd><p>您也可以选择就近的公司网点，到柜台直接付款购买，<a href="//help.damai.cn/damai/channels/284.html" target="_blank">查看分公司上门地址&gt;&gt;</a></p></dd>
#                 # </dl>
#                 # </div>
#                 # <!-- 付款方式 end -->
#                 # </div>
#                 # <div class="itm-tab" rel="5">
#                 # <!-- 先付先抢 begin -->
#                 # <div class="m-infobase m-payrob">
#                 # <div class="infoitm">
#                 # <dt class="tt"><span class="txt">详情介绍</span></dt>
#                 # <dd>
#                 # <p>1.“先付先抢”是大麦网为广大用户推出的一项全新“特权”服务。凡是标有“先付先抢”活动图标的项目，只要在预售阶段付款成功，都将在正式开票前的2-24小时，获得优先于其他用户自主选座的权利。</p>
#                 # <p>2.付款成功后，您将在付款成功页面得到一个系统分配的排号，您也可以登录订单详情页面查看该号码。排号是完全按照付款成功的先后顺序分配，不区分票价。抢座开始前，会发送短信告知抢座时间，并对所有的排号进行分组，排号越靠前，被分入提前选座分组的机会越大，最大程度确保先付款用户的利益，所以，不要犹豫哦，马上占领先机！</p>
#                 # <p>3.大麦网提供所有可售座位进行抢座，由用户自行选择；相对于传统预售配票，更加透明化，保证公平、公正、公开！</p>
#                 # <p>4.如果因为时间关系或其他原因，未能及时参与抢座，您也无需担心。抢座结束后，大麦网工作人员会按照付款先后顺序依次挑选座位进行配票。</p>
#                 # <p><a href="//help.damai.cn/damai/contents/292/5706.html" target="_blank"><img alt="" original="//dui.dmcdn.cn/damai_v2/goods/img/grab-pic02.jpg"/></a></p>
#                 # </dd>
#                 # </div>
#                 # <div class="infoitm">
#                 # <dt class="tt"><span class="txt">无线端先付先抢详情</span></dt>
#                 # <dd>
#                 # <p>为方便用户随时随地抢票，大麦客户端同样支持先付先抢功能，且比网站更快更流畅的购买成功。</p>
#                 # <p>请您按照如下提示下载大麦客户端：</p>
#                 # <ul class="tab-ul-txt">
#                 # <li>iPhone、iPad、Android、Windows Phone等智能设备用户可在各应用市场（如App Store、安卓市场等）搜索"大麦"进行下载安装</li>
#                 # <li>无法安装客户端的用户可浏览器访问m.damai.cn进行购票。</li>
#                 # </ul>
#                 # </dd>
#                 # </div>
#                 # <div class="infoitm">
#                 # <dt class="tt"><span class="txt">温馨提示</span></dt>
#                 # <dd>
#                 # <p>1.现金支付、转账汇款、第三方渠道购买和上门付款的订单不支持本次抢座活动，付款成功后您将获得系统分配的排号，请您留意支付成功页面，或登录网站“订单管理-订单详情”查看排号；</p>
#                 # <p>2.正式抢座从可以入场开始，直到抢座结束，期间任何时候都能进行抢座；</p>
#                 # <p>3.部分手机或软件存在短信屏蔽功能，可能导致您收不到大麦网发送的短信提醒。</p>
#                 # <div class="tab-grab-map-tis clear">
#                 # <a class="mtn fl" href="//mobile.damai.cn/" target="_blank"><img original="//dui.dmcdn.cn/damai_v2/goods/img/grab-pic03.png" style="display:inline;"/></a>
#                 # <a class="fr" href="//news.damai.cn/trends/a/20120528/1365.shtml" target="_blank"><img original="//dui.dmcdn.cn/damai_v2/goods/img/grab-pic04.png" style="display: inline;"/></a>
#                 # </div>
#                 # </dd>
#                 # </div>
#                 # </div>
#                 # <!-- 先付先抢 end -->
#                 # </div>
#                 # </div>
#                 # </div>
#                 # <!-- 项目详情选项卡 end -->
#                 # </div>
#                 # <!-- 项目详情 end -->
#                 # </div>
#                 # <div class="sd">
#                 # <div class="subitem">
#                 # <ul>
#                 # <li class="s-ion1">
#                 # <a>
#                 # <p class="s-t1">大麦客户端</p><p class="s-t2">抢票神器！随时随地尊享优惠</p>
#                 # <span class="s-ewm" style="display: none;"><img src="//dui.dmcdn.cn/dm_2015/goods/img/kehuduan.png"/><strong class="f14">比PC更迅猛</strong><br/><strong>提前开抢</strong></span>
#                 # </a>
#                 # </li>
#                 # </ul>
#                 # </div>
#                 # <!-- 热门推荐 begin -->
#                 # <div class="m-sdbox2-first" id="hotProjects"></div>
#                 # <!-- 热门推荐 end-->
#                 # <!-- 抢票速度榜 begin -->
#                 # <!-- 抢票速度榜 end -->
#                 # <!-- 浏览历史 begin -->
#                 # <div class="m-sdbox2 m-sdbox2-first m-history" id="lishiurl" style="display:none;">
#                 # <div class="hd">
#                 # <h2 class="tt">浏览历史</h2>
#                 # </div>
#                 # <div class="bd">
#                 # <ul class="m-sdlst"></ul>
#                 # </div>
#                 # </div>
#                 # <!-- 浏览历史 end -->
#                 # <!-- 大麦微博 begin -->
#                 # <div class="m-sdbox2 m-weibo">
#                 # <div class="hd">
#                 # <h2 class="tt">大麦微博</h2>
#                 # </div>
#                 # <div class="bd">
#                 # <div class="player" id="weibo_con_"></div>
#                 # </div>
#                 # </div>
#                 # <!-- 大麦微博 end -->
#                 # </div>
#                 # </div>
#                 # <!-- 终极页项目详情 end -->
#                 # </div>
#                 # </div>
#                 # </div>
#                 # <div class="g-ft">
#                 # <div class="m-ft1">
#                 # <div class="bd">
#                 # <!-- 底部链接 begin -->
#                 # <div class="m-lnks">
#                 # <a href="https://help.damai.cn/helpPage.htm" target="_blank">帮助中心</a>
#                 #                                 |<a href="https://help.damai.cn/helpPage.htm?pageId=69" target="_blank">公司介绍</a>
#                 #                                 |<a href="https://help.damai.cn/helpPage.htm?pageId=70" target="_blank">品牌识别</a>
#                 #                                 |<a href="https://help.damai.cn/helpPage.htm?pageId=72" target="_blank">大麦大事记</a>
#                 #                                 |<a href="https://help.damai.cn/helpPage.htm?pageId=40" target="_blank">隐私权专项政策</a>
#                 #                                 |<a href="https://jubao.alibaba.com/internet/readme.htm" target="_blank">廉正举报</a>
#                 #                                 |<a href="https://help.damai.cn/helpPage.htm?pageId=58" target="_blank">联系合作</a>
#                 #                                 |<a href="https://job.alibaba.com/zhaopin/positionList.htm" target="_blank">招聘信息</a>
#                 #                                 |<a href="https://x.damai.cn/markets/special/fangzhapian" target="_blank">防骗秘籍</a>
#                 # </div>
#                 # <!-- 底部链接 end -->
#                 # </div>
#                 # </div>
#                 # <div class="m-ft2">
#                 # <div class="bd">
#                 # <!-- 版权信息 begin -->
#                 # <div class="m-cprt">
#                 # <p>
#                 # <a href="http://www.miitbeian.gov.cn" target="_blank">京ICP证031057号</a><span>|</span>
#                 # <a href="http://www.miitbeian.gov.cn" target="_blank">京ICP备11043884号</a><span>|</span>
#                 # <a href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010102000430" target="_blank">
#                 # <img class="vm" src="//dui.dmcdn.cn/dm_2014/common/img/police.png">京公网安备11010102000430号
#                 # 			</img></a>
#                 # <a href="//dui.dmcdn.cn/dm_2014/common/img/logo/gbdsjm.jpg" target="_blank">广播电视节目制作经营许可证 (京)字第02253号</a>
#                 # <br/>
#                 # <a href="//dui.dmcdn.cn/dm_2014/common/img/logo/wlwhjy.jpg?v2016" target="_blank">网络文化经营许可证 京网文[2016]3438-413号</a><span>|</span>
#                 # <a href="//dui.dmcdn.cn/dm_2014/common/img/logo/yyxyc.jpg" target="_blank">营业性演出许可证 京市演587号</a>
#                 # </p>
#                 # <p>北京红马传媒文化发展有限公司 版权所有 大麦网 Copyright 2003-2018 All Rights Reserved</p>
#                 # <p>
#                 # <a href="//www.damai.cn/" rel="nofollow" target="_blank" title="中国票务在线"><img alt="" class="mr10" original="//dui.dmcdn.cn/dm_2014/common/img/logo/piao.png"/></a>
#                 # <a href="//dui.dmcdn.cn/dm_2014/common/img/logo/dzyyzz.jpg" rel="nofollow" target="_blank" title="电子营业执照"><img alt="" class="mr10" original="//dui.dmcdn.cn/dm_2014/common/img/logo/dzyy.png" src="//dui.dmcdn.cn/dm_2014/common/img/logo/dzyy.png" style="display: inline;"/></a>
#                 # <span id="siteseal">
#                 # <script async="" type="text/javascript">
#                 # 	function verifySeal() {
#                 # 		var bgHeight = "null";
#                 # 		var bgWidth = "593";
#                 # 		var url = "https:\/\/seal.godaddy.com\/verifySeal?sealID=LU6rXPgk5BZ67ZEYpYS2JcN3AyCJOs6aD3HBo4dwA3iGeqp6csKFmqgB0zLL";
#                 # 		window.open(url,'SealVerfication','menubar=no,toolbar=no,personalbar=no,location=yes,status=no,resizable=yes,fullscreen=no,scrollbars=no,width=' + bgWidth + ',height=' + bgHeight);
#                 # 	}
#                 # </script>
#                 # <img alt="SSL site seal - click to verify" onclick="verifySeal();" src="//www.damai.cn/dm2015/images/siteseal_gd_3_h_l_m.gif" style="cursor:pointer;cursor:hand"/> </span>
#                 # <a href="https://www.pcisecuritystandards.org/" rel="nofollow" target="_blank"><img class="mr10" original="//dui.dmcdn.cn/dm_2014/common/img/logo/pci.png"/></a>
#                 # <a href="http://www.itrust.org.cn/home/index/itrust_certifi/wm/1756737221" rel="nofollow" target="_blank"><img class="mr10" original="//dui.dmcdn.cn/dm_2014/common/img/logo/xin.png"/></a>
#                 # <a href="https://search.szfw.org/cert/l/CX20130327002367002885" id="___szfw_logo___" target="_blank"><img original="//www.damai.cn/images/chengxin.png"/></a>
#                 # </p>
#                 # </div>
#                 # <!-- 版权信息 end -->
#                 # </div>
#                 # </div>
#                 # </div>
#                 # <!-- 蒙版 begin -->
#                 # <div class="m-mask z-hide"></div>
#                 # <!-- 蒙版 end -->
#                 # <!-- 缺货登记弹层 begin -->
#                 # <div class="m-layer m-layer-oos z-hide -m-hu" id="layerQuehuodengji">
#                 # <form>
#                 # <div class="hd">
#                 # <h2 class="tt">缺货登记</h2>
#                 # <a class="u-btn u-btn-close" href="javascript:;"><span class="ico"></span></a>
#                 # </div>
#                 # <div class="bd">
#                 # <!-- 缺货登记模块 begin -->
#                 # <div class="m-oos">
#                 # <div class="desc">
#                 # <p>此价格票品暂时缺货，您可以进行缺货登记。</p>
#                 # <p>为了方便有票时能够按照登记顺序通知您，我们将记录您的相关信息；若始终缺货，将不做另行通知。</p>
#                 # </div>
#                 # <ul class="fm">
#                 # <li class="fmitm">
#                 # <label class="lab">数    量：</label>
#                 # <div class="ipt">
#                 # <!-- <div class="u-sel"> -->
#                 # <div class="u-sel" data-context=".fmitm">
#                 # <div class="hd">
#                 # <span class="txt">1</span>
#                 # <span class="btnsel"></span>
#                 # </div>
#                 # <div class="menu">
#                 # <ul class="lst j_count">
#                 # <li><a class="itm z-crt" href="javascript:;">1</a></li>
#                 # <script type="text/javascript">
#                 # 					for(var i = 2; i <= 20; i++) {
#                 # 						document.write('<li><a class="itm" href="javascript:;">' + i + '</a></li>');
#                 # 					}
#                 # 				  </script>
#                 # </ul>
#                 # <input name="count" type="hidden" value="1">
#                 # </input></div>
#                 # </div>
#                 # </div>
#                 # </li>
#                 # <li class="fmitm">
#                 # <label class="lab">手机号码：</label>
#                 # <div class="ipt">
#                 # <input class="u-ipt u-ipt-sm" name="mobilePhone" type="text" value=""/>
#                 # <span class="c1">*</span>
#                 # </div>
#                 # </li>
#                 # <li class="fmitm">
#                 # <label class="lab">留    言：</label>
#                 # <div class="ipt">
#                 # <textarea class="u-ipt u-ipt-lg" name="notes"></textarea>
#                 # </div>
#                 # </li>
#                 # <li class="fmitm fmitm-1">
#                 # <div class="ipt"><a class="u-btn" href="javascript:;" id="btnQuehuodengji">提交</a></div>
#                 # </li>
#                 # </ul>
#                 # </div>
#                 # <!-- 缺货登记模块 end -->
#                 # </div>
#                 # <input name="performId" type="hidden" value=""/>
#                 # <input name="performName" type="hidden" value=""/>
#                 # <input name="performTime" type="hidden" value=""/>
#                 # <input name="priceId" type="hidden" value=""/>
#                 # <input name="price" type="hidden" value=""/>
#                 # <input name="pricename" type="hidden" value=""/>
#                 # <input name="enStr" type="hidden" value=""/>
#                 # </form>
#                 # </div>
#                 # <!-- 缺货登记弹层 end -->
#                 # <!-- 手机客户端下载弹层 begin -->
#                 # <div class="m-layer m-layer-appdown z-hide" id="appDownLayer">
#                 # <div class="hd">
#                 # <h2 class="tt">手机客户端下载</h2>
#                 # <a class="u-btn u-btn-close" href="javascript:;"><span class="ico"></span></a>
#                 # </div>
#                 # <div class="bd">
#                 # <div class="m-appdown">
#                 # <div class="qrcode">
#                 # <div class="code"></div>
#                 # <p class="txt">手机扫描快速下载</p>
#                 # </div>
#                 # <ul class="lst">
#                 # <li class="itm iphone"><a href="http://itunes.apple.com/cn/app/da-mai/id513829338?mt=8" target="_blank">iPhone版</a></li>
#                 # <li class="itm android"><a href="//mapi.damai.cn/href.aspx?id=11" target="_blank">Android版</a></li>
#                 # <li class="itm ipad"><a href="http://itunes.apple.com/cn/app//id481947980?mt=8" target="_blank">iPad版</a></li>
#                 # </ul>
#                 # </div>
#                 # </div>
#                 # </div>
#                 # <!-- 手机客户端下载弹层 end -->
#                 # <!-- 开售提醒弹层 begin -->
#                 # <div class="m-layer m-layer-remind z-hide" id="layerRemind">
#                 # <div class="hd">
#                 # <h2 class="tt">提示</h2>
#                 # <a class="u-btn u-btn-close" href="javascript:;"><span class="ico"></span></a>
#                 # </div>
#                 # <div class="bd">
#                 # <!-- 开售提醒模块 begin -->
#                 # <div class="m-remind">
#                 # <p class="tips"><i class="ico ico-succ"></i><span class="txt">成功设置项目开售提醒！</span></p>
#                 # <p class="desc">我们将在项目开售前以短信的方式通知您</p>
#                 # <!-- 开售提醒模块 end -->
#                 # </div>
#                 # </div>
#                 # </div>
#                 # <!-- 开售提醒弹层 end -->
#                 # <!--您输入的特权码无效，请重试 begin-->
#                 # <div class="m-layer m-layer-error z-hide" id="privilege_error">
#                 # <div class="hd">
#                 # <a class="u-btn u-btn-close" href="javascript:;"><span class="ico"></span></a>
#                 # </div>
#                 # <div class="bd">
#                 # <div class="m-error">
#                 # <p class="tips"><i class="ico-tips"></i><span class="txt" id="privilegeErrorMsg">您输入的特权码无效，请重试</span></p>
#                 # <div class="ops">
#                 # <a class="u-btn j_btnOk" href="javascript:;">确定</a>
#                 # </div>
#                 # </div>
#                 # </div>
#                 # </div>
#                 # <!--您输入的特权码无效，请重试 end-->
#                 # <!--您的操作过于频繁，请稍后重试 begin-->
#                 # <div class="m-layer m-layer-error z-hide" id="privilege_error_307">
#                 # <div class="hd">
#                 # <a class="u-btn u-btn-close" href="javascript:;"><span class="ico"></span></a>
#                 # </div>
#                 # <div class="bd">
#                 # <div class="m-error">
#                 # <p class="tips"><i class="ico-tips"></i><span class="txt">您的操作过于频繁，请稍后重试</span></p>
#                 # <div class="ops">
#                 # <a class="u-btn" href="javascript:;">确定</a>
#                 # </div>
#                 # </div>
#                 # </div>
#                 # </div>
#                 # <!--您的操作过于频繁，请稍后重试 end-->
#                 # <!--本项目需M3、M4 会员等级用户才可购买 begin-->
#                 # <div class="m-layer m-layer-error z-hide">
#                 # <div class="hd">
#                 # <a class="u-btn u-btn-close" href="javascript:;"><span class="ico"></span></a>
#                 # </div>
#                 # <div class="bd">
#                 # <div class="m-error">
#                 # <p class="tips"><i class="ico-tips"></i><span class="txt">本项目需M3、M4 <br>会员等级用户才可购买</br></span></p>
#                 # <div class="ops">
#                 # <a class="u-btn" href="javascript:;">查看等级</a>
#                 # <a class="u-btn u-btn-c2" href="javascript:;">取消</a>
#                 # </div>
#                 # </div>
#                 # </div>
#                 # </div>
#                 # <!--本项目需M3、M4 会员等级用户才可购买 end-->
#                 # <!--您的账户未完成实名认证 begin-->
#                 # <div class="m-layer m-layer-error z-hide">
#                 # <div class="hd">
#                 # <a class="u-btn u-btn-close" href="javascript:;"><span class="ico"></span></a>
#                 # </div>
#                 # <div class="bd">
#                 # <div class="m-error">
#                 # <p class="tips"><i class="ico-tips"></i><span class="txt">您的账户未完成实名认证</span></p>
#                 # <div class="ops">
#                 # <a class="u-btn" href="javascript:;">去认证</a>
#                 # <a class="u-btn u-btn-c2" href="javascript:;">取消</a>
#                 # </div>
#                 # </div>
#                 # </div>
#                 # </div>
#                 # <!--您的账户未完成实名认证 end-->
#                 # <!--请输入特权码 begin-->
#                 # <div class="m-layer m-layer-code z-hide" id="privilege_error_404">
#                 # <div class="bd">
#                 # <div class="m-error">
#                 # <p class="tips"><i class="ico-tips"></i><span class="txt">请输入用户特权码</span></p>
#                 # <div class="ops">
#                 # <a class="u-btn" href="javascript:;">确定</a>
#                 # </div>
#                 # </div>
#                 # </div>
#                 # </div>
#                 # <!--请输入特权码 end-->
#                 # <div class="m-layer z-hide" id="layerWeiShare">
#                 # <div class="hd">
#                 # <h2 class="tt" style="font-size:12px;">分享到微信朋友圈</h2>
#                 # <a class="u-btn u-btn-close" href="javascript:;"><span class="ico"></span></a>
#                 # </div>
#                 # <div class="bd">
#                 # <div class="m-viewseat" style="background:#fff url(img/loading.gif) no-repeat center center;">
#                 # <div class="seat" style="padding:20px 60px;width:220px; height: 220px;"><img alt="" lazy-src="//piao.damai.cn/ShowBarcode.aspx?content=https%3A%2F%2Fpiao.damai.cn%2F171739.html" style="width:220px; height: 220px; display:none;"/></div>
#                 # </div>
#                 # </div>
#                 # <div style="background:#fff;border-top:1px solid #e6e6e6; padding:8px 0px 8px 20px">
#                 # <p>打开微信，点击底部的“发现”，使用 “扫一扫”<br>即可将网页分享到我的朋友圈。</br></p>
#                 # </div>
#                 # </div>
#                 # <!-- 选择商品弹层 begin -->
#                 # <div class="m-layer m-layer-choosegoods z-hide" id="chooseGoodsLayer">
#                 # <div class="hd">
#                 # <h2 class="tt">请选择您要的商品信息</h2>
#                 # <a class="u-btn u-btn-close" href="javascript:;"><span class="ico"></span></a>
#                 # </div>
#                 # <div class="bd">
#                 # <div class="m-choosegoods j_goodsDetails">
#                 # <!-- 选择日期模块 begin -->
#                 # <div class="m-choose m-choose-date " data-col="4" data-row="2">
#                 # <h3 class="tt">选择时间：</h3>
#                 # <div class="ct">
#                 # <ul class="lst"></ul>
#                 # </div>
#                 # </div>
#                 # <!-- 选择日期模块 end -->
#                 # <!-- 选择票价模块 begin -->
#                 # <div class="m-choose m-choose-price" data-col="4" data-row="3">
#                 # <h3 class="tt">选择票价：</h3>
#                 # <div class="ct">
#                 # <ul class="lst"></ul>
#                 # <div class="tips tips-oos"><span class="ico"></span><span class="txt">暂时无货，登录试试运气~</span></div>
#                 # </div>
#                 # </div>
#                 # <!-- 选择票价模块 end -->
#                 # <!-- 购物车模块 begin -->
#                 # <div class="m-cart">
#                 # <h3 class="tt" style="display:none;">您选择了：</h3>
#                 # <div class="ct" style="display:none;">
#                 # <ul class="lst"></ul>
#                 # </div>
#                 # <div class="ops">
#                 # <a class="u-btn u-btn-c1 u-btn-choose" href="javascript:;" id="btnXuanzuo3" style="display:none;">选座购买</a>
#                 # </div>
#                 # </div>
#                 # <!-- 购物车模块 end -->
#                 # </div>
#                 # </div>
#                 # </div>
#                 # <!-- 选择商品弹层 end -->
#                 # <!-- 固定侧栏 begin -->
#                 # <div class="m-sdfix">
#                 # <span class="itm weixin xiaonengService" style="cursor:pointer;">在线<br/>客服</span>
#                 # <a class="itm resch" href="//www.wenjuan.com/s/QV7vm2/" target="_blank">
#                 # <i class="ico"></i>
#                 # <span class="txt">调查问卷</span>
#                 # </a>
#                 # <a class="itm weixin" href="javascript:;" id="siteWeixinQR" style="display:none;">
#                 # <i class="ico"></i>
#                 # <span class="code"><img alt="大麦网" original="img/qrcode.png"/></span>
#                 # </a>
#                 # <a class="itm totop" href="javascript:;" id="gotop">
#                 # <i class="ico"></i>
#                 # <span class="txt">返回顶部</span>
#                 # </a>
#                 # </div>
#                 # <!-- 固定侧栏 end -->
#                 # <script src="//dui.dmcdn.cn/dm_2015/goods/js/jquery-1.8.2.min.js" type="text/javascript"></script>
#                 # <script type="text/javascript">
#                 #         var performCount = 2;
#                 #     </script>
#                 # <iframe border="0" frameborder="no" id="mapview" name="mapview" scrolling="no" style="display:none;"></iframe>
#                 # <script type="text/javascript">
#                 # var showCalendar = 0;
#                 # </script>
#                 # <!-- 日历插件 begin -->
#                 # <div class="m-calendar">
#                 # <div class="hd"></div>
#                 # <div class="bd"></div>
#                 # </div>
#                 # <!-- 日历插件 end -->
#                 # <script type="text/javascript">
#                 # var projectDates={};
#                 #  jQuery("#rili").attr("data-value", '2019.01.06'); projectDates['D20190106']=true;
#                 # projectDates['D20190106']=true;
#                 # showCalendar = 1;
#                 # </script>
#                 # <script src="//dui.dmcdn.cn/??dm_2015/goods/site/js/common-min.js?v5.28.0,dm_2015/goods/site/js/search-min.js?v5.28.0,dm_2015/goods/site/js/widgetUIDs-min.js?v5.28.0,dm_2015/goods/site/js/calendarSettings-min.js,dm_2015/goods/site/js/calendar-min.js,dm_2015/goods/site/js/weixin-min.js,dm_2015/goods/site/js/json2-min.js,dm_2015/goods/site/js/datepicker-min.js,dm_2015/goods/site/js/app-min.js?v5.28.0" type="text/javascript"></script>
#                 # <script src="/js/min/item-min.js?v5.28.0" type="text/javascript"></script>
#                 # <script src="/js/min/qa-min.js?v5.28.0" type="text/javascript"></script>
#                 # <script src="//www.damai.cn/staticfile/Announcement/Announcement.js?937492837" type="text/javascript"></script>
#                 # <script type="text/javascript">
#                 #     var title = $("#Title").val();
#                 # 	var ShowSpeedList=0,ShowTotalMoney=0;
#                 # 		ShowSpeedList=0;
#                 # 			ShowTotalMoney=0;
#                 # 		(function () {
#                 # 		$('#showVenueMap').on('click', function() {
#                 # 			$('#mapview').on('load', dm_mapview.show).attr("src", jQuery(this).attr("map-src")).show();
#                 # 			return false;
#                 # 		});
#                 # 	})();
#                 # </script>
#                 # <script async="async" src="https://secure.damai.cn/static/jquery.playalert3.js?0001" type="text/javascript"></script>
#                 # <script async="async" src="//cp.damai.cn/js/Service51La/SeoFlowStatistics.js?45" type="text/javascript"></script>
#                 # <script async="async" src="//dui.dmcdn.cn/dm_2015/goods/site/map/js/mapview.js" type="text/javascript"></script>
#                 # <script type="text/javascript">
#                 # $(document).on("click", ".xiaonengService", function() {
#                 # 	 window.open("https://online.damai.cn/alime/toalime?from=damai_itemdetail&page=" + encodeURIComponent(location.href));
#                 # });
#                 # </script>
#                 # <!-- start Dplus --><script type="text/javascript">!function(a,b){if(!b.__SV){var c,d,e,f;window.dplus=b,b._i=[],b.init=function(a,c,d){function g(a,b){var c=b.split(".");2==c.length&&(a=a[c[0]],b=c[1]),a[b]=function(){a.push([b].concat(Array.prototype.slice.call(arguments,0)))}}var h=b;for("undefined"!=typeof d?h=b[d]=[]:d="dplus",h.people=h.people||[],h.toString=function(a){var b="dplus";return"dplus"!==d&&(b+="."+d),a||(b+=" (stub)"),b},h.people.toString=function(){return h.toString(1)+".people (stub)"},e="disable track track_links track_forms register unregister get_property identify clear set_config get_config get_distinct_id track_pageview register_once track_with_tag time_event people.set people.unset people.delete_user".split(" "),f=0;f<e.length;f++)g(h,e[f]);b._i.push([a,c,d])},b.__SV=1.1,c=a.createElement("script"),c.type="text/javascript",c.charset="utf-8",c.async=!0,c.src="//w.cnzz.com/dplus.php?token=7415364c9dab5n09ff68",d=a.getElementsByTagName("script")[0],d.parentNode.insertBefore(c,d)}}(document,window.dplus||[]),dplus.init("7415364c9dab5n09ff68");</script><!-- end Dplus -->
#                 # <!-- start Dplus Define -->
#                 # <script type="text/javascript">!function(a,b){var c,d;window.__dplusDefineCacheQueue=[],b.define=function(){window.__dplusDefineCacheQueue.push(Array.prototype.slice.call(arguments))},c=a.createElement("script"),c.type="text/javascript",c.charset="utf-8",c.async=!0,c.src="//w.cnzz.com/dplus.define.php",d=a.getElementsByTagName("script")[0],d.parentNode.insertBefore(c,d)}(document,window.dplus);</script>
#                 # <!-- end Dplus Define -->
#                 # <script type="text/javascript">
#                 # 	(function() {
#                 # 		dplus.define('page', function(page){
#                 # 			page.init("7415364c9dab5n09ff68", {
#                 # 				'page_duration': true, //默认不跟踪页面停留时间
#                 # 				'clean_url': true //默认是clean url
#                 # 			});
#                 # 		});
#                 # 		dplus.define('page', function(page){
#                 # 			page.setType('project');//设置页面类型
#                 # 			page.setTitle("黑色喜剧《驴得水》武汉站");//设置页面标题,不填默认取document.title，建议填演出名
#                 # 			page.setCategory(['话剧歌剧', '话剧歌剧']);//该演出对应的三级类目
#                 # 			page.setTags([]);//该演出的其他TAG
#                 # 			page.view({
#                 # 				'$avn':"武汉琴台大剧院",
#                 # 				'$alr':"",
#                 # 				'$aad': "武汉"
#                 # 			});
#                 # 		});
#                 # 	})();
#                 # 	$(document)
#                 # 	.on("click", "#gexhTuijian li a", function() {
#                 # 		var $this = $(this);
#                 # 		dplus.track('recclick',{
#                 # 			'$tti':'project',
#                 # 			'$tul':location.href,
#                 # 			'$tna':'热门推荐',
#                 # 			'$tdx':$this.closest("li").index() - 0 + 1,
#                 # 			'$pid':$this.attr("data-projectId"),
#                 # 			'tag':$this.attr('id'),
#                 # 			'$na':$this.attr('title')
#                 # 		});//
#                 # 	}).on("click", "#dysbmit:not(.u-btn-dis)", function() {
#                 # 		jQuery.getJSON("/ajax/GetUserInfo.html", { projectId: projectInfo.ProjectID, t: Math.random() }, function(rsp) {
#                 # 			abc(rsp.Data.userInfo.code);
#                 # 		});
#                 # 		function abc(code) {
#                 # 			var params = { "$tti": "project", "$pid": projectInfo.ProjectID + "", "$userid": code + "" };
#                 # 			dplus.track('rssclick',params);
#                 # 		}
#                 # 	});
#                 # 	$(document).ready(function() {
#                 # 	    var cityid = projectInfo.CityID;
#                 # 	    if (cityid != "" && cityid == "2279") {
#                 # 	        cityid = "2148";
#                 # 	    }
#                 # 	    var uid = getwidgetUID(cityid);
#                 # 	    if (location.protocol == "http:" && uid) {
#                 # 			$("#weibo_con_").html("<iframe width=\"100%\" height=\"550\" class=\"share_self\"  frameborder=\"0\" scrolling=\"no\" src=\"http://service.t.sina.com.cn/widget/WeiboShow.php?width=0&height=550&fansRow=2&ptype=1&speed=0&skin=5&isTitle=0&noborder=0&isWeibo=1&isFans=0&uid=" + uid + "\"></iframe>");
#                 # 			$("div.m-weibo").show();
#                 # 			var uuid = uid.split('&')[0];
#                 # 			$("#wbFollowIframe_").attr("src", "http://widget.weibo.com/relationship/followbutton.php?btn=light&style=2&uid={0}&width=136&height=24&language=zh_cn".format(uuid));
#                 # 	    } else if (location.protocol == "https:" && uid) {
#                 # 	        var uuid = uid.split('&')[0];
#                 # 	        $("#wbFollowIframe_").attr("src", "//www.damai.cn/WeiboAgent.aspx?uid={0}".format(uuid));
#                 # 	        $("#weibo_con_").parent().parent().remove();
#                 # 	    } else {
#                 # 	        $("#wbFollowIframe_").parent().remove();
#                 # 	        $("#weibo_con_").parent().parent().remove();
#                 # 	    }
#                 # 	});
#                 # 	</script>
#                 # <script src="//g.alicdn.com/mtb/lib-mtop/2.3.16/mtop.js"></script>
#                 # <script src="//g.alicdn.com/??damai/pc-wx/0.1.4/index.js"></script>
#                 # </body>
#                 # </html>"""
#                 _html = BS(_test, 'html.parser')
#                 dd = etree.HTML(_test)
#
#                 # 建立信息字典，单条信息是字典
#
#                 # 获取有用信息
#                 i[1]['演出时长'] = _html.find('div', class_='m-infobase').findAll('tr')[1].findAll('td')[1].text
#                 i[1]['演出语言'] = _html.find('div', class_='m-infobase').findAll('tr')[9].findAll('td')[3].text
#                 i[1]['演出字幕'] = _html.find('div', class_='m-infobase').findAll('tr')[9].findAll('td')[1].text
#                 i[1]['主要演员'] = _html.find('div', class_='m-infobase').findAll('tr')[10].findAll('td')[1].text
#                 i[1]['演出介绍'] = _html.find('div', class_='m-infobase').find('div', class_='pre').contents  # 显示子节点
#                 i[1]['剧名']: re.search('《[^》]+》', i[1]['标题'], flags=0).group()
#                 # gat_info_list.append(_info)
#                 i[1]['蜘蛛状态'] = True
#                 print(i[1])
#
#             break
#             time.sleep(5)
#
#         # 保存到
#         Save(gat_info_list, 'info_list.csv')
#
#         return gat_info_list
#
#
# # 解析页面
# def pares(Info):
#     try:
#         response = requests.get(Info['url'], headers=Info['headers'], proxies=Info['proxies'], timeout=1)
#         if response.status_code == 200:
#             # 自行转码
#             response.encoding = 'UTF-8'
#
#             # 解析内容
#             page_source = BS(response.text, 'html.parser')
#
#             # print(response.text)
#             return page_source
#         else:
#             print('页面请求状态码：', response.status_code)
#             return None
#     except RequestException:
#         # 向工作日志中写入内容
#         return None
#
#
# # 保存为CSV数据
# def save(self):
#     # 构建属性列表
#     # list = ['actors', 'categoryname', 'cityname', 'description', 'price', 'pricehigh', 'showstatus', 'showtime', 'subcategoryname', 'venue', 'venuecity', 'verticalPic']
#     list = self.data_key
#
#     # 此处出现保存，报错为缺少字段，因此追加一个字段
#     list.append('favourable')
#     # 测试list
#     # print(list)
#
#     # 数据
#     my_data = self.parse()
#     # 测试
#     # print(my_data)
#
#     with open("damaiwang" + ".csv", "w", newline="", encoding='utf8') as f:
#         # 传入头数据，即第一行数据
#         writer = csv.DictWriter(f, list)
#         writer.writeheader()
#         for row in my_data:
#             writer.writerow(row)
#
#
# # def get_list0(self, n):
# #     url = "https://piao.damai.cn/" + str(n) + ".html"
# #     response = requests.get(url)
# #     response.encoding = "utf-8"
# #     html = BS(response.text, 'html.parser')
# #
# #
# #
# #
# # # # 保存为字典数据
# # # def save_dict(self):
# # #     with open("damaiwang", 'w', encoding='utf8') as f:
# # #         f.write(str(self.parse()))
# #
# #
# # # 返回页面的源代码,会因为反爬虫，所以需要额外做判断，之后要把这部分单独做出来
# # def get_parse(info):
# #     try:
# #         response = requests.get(info['url'], headers=info['headers'], proxies=info['proxies'], timeout=1)
# #         if response.status_code == 200:
# #             # 解析内容
# #             page_source = BS(response.text, 'html.parser')
# #
# #             # print(response.text)
# #             return page_source
# #         else:
# #             print(response.status_code)
# #             return None
# #     except RequestException:
# #         # 向工作日志中写入内容
# #         return None
#
#
# #
# # # 请求url获取响应
# # def post_parse(url):
# #     response = requests.post(url=url['url'], headers=url['headers'], data=url['data'])
# #
# #     # 将字符串数据转换成字典数据
# #     dict_data = json.loads(response.text)
# #
# #     # 将需要的爬取的字典数据存储在变量中
# #     need_spider_data = dict_data["pageData"]["resultData"]
# #
# #     # 测试字典数据是否能解析出来
# #     # print(dict_data["pageData"]["resultData"])
# #     return need_spider_data


if __name__ == '__main__':
    a=Crawler()
    a.getCookie()


