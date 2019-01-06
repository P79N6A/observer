# -*- coding: UTF-8 -*-
# 阅读者，专门找信息，专门爬取大麦网的演出活动地址，并保存为：get_url.csv


import requests  # 加载解析地址库
import json  # 解析json的库
import user_agent  # 随机生成user_agent
import re  # 用于提取剧名

from bs4 import BeautifulSoup as BS  # 加载解析HTML库


# 从大麦中获取列表信息
class get_post:
    def __init__(self, URL, DATA, COOKIE,REFERER):
        self.url = URL  # 接受POST请求的地址
        self.headers = {
            "User-Agent": user_agent.generate_user_agent(),  # 随机生成的,
            "cookie": COOKIE,
            "referer": REFERER
        }
        self.data = DATA  # 请求内容
        self.proxy_dict = {
            # "http": "180.118.86.4:9000/",
            # "https": "180.118.86.4:9000/"
        }  # 这里需要制造代理

    def todo(self):
        try:  # 如果被反扒，则解析json时会出错
            _response = requests.post(url=self.url, headers=self.headers, proxies=self.proxy_dict, data=self.data,
                                      verify=True)  # verify是否验证服务器的SSL证书)
            # print(_response.status_code,_response.text)


            _dict_data = json.loads(_response.text) # 将字符串数据转换成字典数据，
            _get_post = _dict_data["pageData"]["resultData"]    # 将需要的爬取的字典数据存储在变量中
            # print('成功获取json:',_dict_data)
            print('成功获取json')

            print('完成提取数据的任务')
            return _get_post    # 返回数组
        except:
            # 这部分还没有完善
            print('被墙了')
            return None




# 从大麦中获取更详细的信息
class get_info:
    def __init__(self, URL):
        self.url = URL
        self.headers = {
            "User-Agent": user_agent.generate_user_agent(),  # 随机生成的,
            # "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.2 Safari/605.1.15",
            "cookie": 'isg=BHt7CsD7o6lJ0Zr3paFHjq_HCFnl0I_S7utToG04GnqRzJqu9aEeIgFK4uyCd-fK; l=aB8neGmpyhCp3AEmBMa4dstiNxrxygBPznZWxMaL8iYGdP8ZuXKbBk-oWMzLI_XhizcgPwvUoUu2.; x5sec=7b226d65632d67756964652d7765623b32223a226535383534306265306134666163626536373439373135326465346364623432434c4c61724f454645504b73724a32746a2b616a48673d3d227d; _uab_collina=154633349240746853818272; UM_distinctid=15aa9009428293-0103a30182f46e8-1a441228-13c680-15aa9009429337; cn_7415364c9dab5n09ff68_dplus=%7B%22distinct_id%22%3A%20%2215aa9009428293-0103a30182f46e8-1a441228-13c680-15aa9009429337%22%2C%22initial_view_time%22%3A%20%221488889067%22%2C%22initial_referrer%22%3A%20%22http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzA4NjMyMzIyMA%3D%3D%26mid%3D2654063564%26idx%3D1%26sn%3Db2c9e26ab4628436e9dc1ff38f8e05d5%26scene%3D0%22%2C%22initial_referrer_domain%22%3A%20%22mp.weixin.qq.com%22%2C%22sp%22%3A%20%7B%22%24recent_outside_referrer%22%3A%20%22%24direct%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201544849099%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201544849099%7D%7D; destCity=%u6B66%u6C49; cporder=ordervalue=hXialdQTaYMrjQ2dGzNNg5abtukROzhyEqSw33D8xpfk%2bo9Buk44WtX3qla2ZmvSd9%2bi%2f9PbRXHEcxdJLs37AvV1w76nfyy6%2fo9Xq9J1GA8bG4cRszJps3H%2fzy9ESIl6e9a%2bHjmAAV0%3d; cporderV2=hXialdQTaYMrjQ2dGzNNg5abtukROzhyEqSw33D8xpfk%2bo9Buk44WtX3qla2ZmvSd9%2bi%2f9PbRXHEcxdJLs37AvV1w76nfyy6%2fo9Xq9J1GA8bG4cRszJps3H%2fzy9ESIl6e9a%2bHjmAAV0%3d; cna=W5Y0EQTl42YCARsRRUVaKCov; damai.cn_email="wapu@qq.com"; damai.cn_nickName=%E4%B9%9F%E9%97%A8%E7%9A%84%E9%97%A8; PHPStat_Return_Count_10000001=1; PHPStat_Return_Time_10000001=1492404093845; PHPStat_Cookie_Global_User_Id=_ck17040701013914617714059138794; PHPStat_First_Time_10000001=1491498099371',
            "referer": "https://search.damai.cn/search.htm"
        }

        self.proxy_dict = {
            # "http": "180.118.86.4:9000/",
            # "https": "180.118.86.4:9000/"
        }

    def todo(self):

        self.sampling(self.visit())

    # 获取页面内容
    def visit(self):
        try:
            # 获取get数据包,verify是否验证服务器的SSL证书
            response = requests.get(url=self.url, headers=self.headers, proxies=self.proxy_dict, verify=True, timeout=1)

            if response.status_code == 200:

                response.encoding = 'UTF-8'  # 自行转码

                page_source = BS(response.text, 'html.parser')  # 解析内容

                print(response.text)
                return page_source
            else:
                print('页面请求状态码：', response.status_code)
                return None
        except:
            # 向工作日志中写入内容
            return None

    # 提炼页面内容，返回列表内容
    def sampling(self, _info):
        pass


if __name__ == '__main__':
    url = 'https://piao.damai.cn/164857.html'

    test = get_info(url)
    test.todo()
