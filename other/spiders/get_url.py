# -*- coding: UTF-8 -*-
# 专门爬取大麦网的演出活动地址，并保存为：get_url.csv


import requests     # 加载解析地址库
import json         # 解析json的库
import user_agent   # 随机生成user_agent


class get_url:
    def __init__(self, URL):
        self.url = URL
        self.headers = {
            "User-Agent": user_agent.generate_user_agent(),  # 随机生成的,
            "cookie": 'sg=BODgXGSsqDAOKBHm8ihczxB-s-iy6cSznTkxsVrw9_uOVYF_AvhMQ9om6V1VfnyL; x5sec=7b226d65632d67756964652d7765623b32223a223533386566636634643032653865346532663864303563353039613161333766434975787a4f4146454b477531394767675a795a50413d3d227d; destCity=%u6B66%u6C49; UM_distinctid=15aa9009428293-0103a30182f46e8-1a441228-13c680-15aa9009429337; cn_7415364c9dab5n09ff68_dplus=%7B%22distinct_id%22%3A%20%2215aa9009428293-0103a30182f46e8-1a441228-13c680-15aa9009429337%22%2C%22initial_view_time%22%3A%20%221488889067%22%2C%22initial_referrer%22%3A%20%22http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzA4NjMyMzIyMA%3D%3D%26mid%3D2654063564%26idx%3D1%26sn%3Db2c9e26ab4628436e9dc1ff38f8e05d5%26scene%3D0%22%2C%22initial_referrer_domain%22%3A%20%22mp.weixin.qq.com%22%2C%22sp%22%3A%20%7B%22%24recent_outside_referrer%22%3A%20%22%24direct%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201544754020%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201544754020%7D%7D; cporder=ordervalue=hXialdQTaYMrjQ2dGzNNg5abtukROzhyEqSw33D8xpfk%2bo9Buk44WtX3qla2ZmvSd9%2bi%2f9PbRXHEcxdJLs37AvV1w76nfyy6%2fo9Xq9J1GA8bG4cRszJps3H%2fzy9ESIl6e9a%2bHjmAAV0%3d; cporderV2=hXialdQTaYMrjQ2dGzNNg5abtukROzhyEqSw33D8xpfk%2bo9Buk44WtX3qla2ZmvSd9%2bi%2f9PbRXHEcxdJLs37AvV1w76nfyy6%2fo9Xq9J1GA8bG4cRszJps3H%2fzy9ESIl6e9a%2bHjmAAV0%3d; x_hm_tuid=HX0R/4vuvZhQSFPrJHYzAaAK09/d6YuHHQTVt0Jh//2wFInEwUh5pONLiImkp6oQ; cna=W5Y0EQTl42YCARsRRUVaKCov; damai.cn_email="wapu@qq.com"; damai.cn_nickName=%E4%B9%9F%E9%97%A8%E7%9A%84%E9%97%A8; PHPStat_Return_Count_10000001=1; PHPStat_Return_Time_10000001=1492404093845; PHPStat_Cookie_Global_User_Id=_ck17040701013914617714059138794; PHPStat_First_Time_10000001=1491498099371',
            "referer": "https://search.damai.cn/search.htm?spm=a2oeg.home.category.ditem_1.5db723e1UDy41J&ctl=%E8%AF%9D%E5%89%A7%E6%AD%8C%E5%89%A7&order=1&cty=%E6%AD%A6%E6%B1%89"
        }
        self.data = {
            "cty": "武汉",
            "ctl": "话剧歌剧",
            "tsg": "0",
            "order": "1"
        }

    def todo(self):
        # 获取post数据包
        _response = requests.post(url=self.url, headers=self.headers, data=self.data)
        # print(response)

        # 将字符串数据转换成字典数据
        _dict_data = json.loads(_response.text)
        # print(dict_data)

        # 将需要的爬取的字典数据存储在变量中
        _need_spider_data = _dict_data["pageData"]["resultData"]
        # print(_need_spider_data)

        # clean数据，并提取内容
        _get_list = []
        for j in range(len(_need_spider_data)):
            #为了让代码更简洁，做了一个赋值
            _double =_need_spider_data[j]

            # 获取有用的信息
            _j = {'标题': _double['name'],
                  '副标题': _double['subhead'],
                  '地点城市': _double['venuecity'],
                  '演出场所': _double['venue'],
                  '演出时间': _double['showtime'],
                  '演出状态': _double['showstatus'],
                  '演出类型': _double['subcategoryname'],
                  'projectid': _double['projectid'],
                  'imgurl': _double['imgurl'],
                  '最低票价': _double['price'],
                  '最高票价': _double['pricehigh'],
                  '信息属性':0
                  }

            #添加到数组中
            _get_list.append(_j)

        #返回数组
        #print(_get_list)
        return _get_list

if __name__ == '__main__':
    url = 'https://search.damai.cn/searchajax.html'

    test = get_url(url)
    test.todo()
