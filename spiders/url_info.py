# 爬虫页面信息配置文件

class URL_Info():
    def __init__(self, url, data={}):
        self.url = url
        self.data = data
        self.data_key = None
        # 构造IP代理(按需求开启)
        self.proxies = {
            # "http": "http://47.93.56.0:3128",
            # "http": "http://39.135.24.12:80",
        }

    # 加载豆瓣的相关属性
    def douban(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
            "Cookie": "",
            "Referer": "https://www.douban.com/location/wuhan/events/future-all"
        }
        info = {'url': self.url, 'headers': headers, 'proxies': self.proxies}

        return info

    #加载大麦到内到
    def damai(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.1 Safari/605.1.15",
            "cookie": 'sg=BODgXGSsqDAOKBHm8ihczxB-s-iy6cSznTkxsVrw9_uOVYF_AvhMQ9om6V1VfnyL; x5sec=7b226d65632d67756964652d7765623b32223a223533386566636634643032653865346532663864303563353039613161333766434975787a4f4146454b477531394767675a795a50413d3d227d; destCity=%u6B66%u6C49; UM_distinctid=15aa9009428293-0103a30182f46e8-1a441228-13c680-15aa9009429337; cn_7415364c9dab5n09ff68_dplus=%7B%22distinct_id%22%3A%20%2215aa9009428293-0103a30182f46e8-1a441228-13c680-15aa9009429337%22%2C%22initial_view_time%22%3A%20%221488889067%22%2C%22initial_referrer%22%3A%20%22http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzA4NjMyMzIyMA%3D%3D%26mid%3D2654063564%26idx%3D1%26sn%3Db2c9e26ab4628436e9dc1ff38f8e05d5%26scene%3D0%22%2C%22initial_referrer_domain%22%3A%20%22mp.weixin.qq.com%22%2C%22sp%22%3A%20%7B%22%24recent_outside_referrer%22%3A%20%22%24direct%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201544754020%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201544754020%7D%7D; cporder=ordervalue=hXialdQTaYMrjQ2dGzNNg5abtukROzhyEqSw33D8xpfk%2bo9Buk44WtX3qla2ZmvSd9%2bi%2f9PbRXHEcxdJLs37AvV1w76nfyy6%2fo9Xq9J1GA8bG4cRszJps3H%2fzy9ESIl6e9a%2bHjmAAV0%3d; cporderV2=hXialdQTaYMrjQ2dGzNNg5abtukROzhyEqSw33D8xpfk%2bo9Buk44WtX3qla2ZmvSd9%2bi%2f9PbRXHEcxdJLs37AvV1w76nfyy6%2fo9Xq9J1GA8bG4cRszJps3H%2fzy9ESIl6e9a%2bHjmAAV0%3d; x_hm_tuid=HX0R/4vuvZhQSFPrJHYzAaAK09/d6YuHHQTVt0Jh//2wFInEwUh5pONLiImkp6oQ; cna=W5Y0EQTl42YCARsRRUVaKCov; damai.cn_email="wapu@qq.com"; damai.cn_nickName=%E4%B9%9F%E9%97%A8%E7%9A%84%E9%97%A8; PHPStat_Return_Count_10000001=1; PHPStat_Return_Time_10000001=1492404093845; PHPStat_Cookie_Global_User_Id=_ck17040701013914617714059138794; PHPStat_First_Time_10000001=1491498099371',
            "referer": "https://search.damai.cn/search.htm?spm=a2oeg.home.category.ditem_1.5db723e1UDy41J&ctl=%E8%AF%9D%E5%89%A7%E6%AD%8C%E5%89%A7&order=1&cty=%E6%AD%A6%E6%B1%89"
        }
        data = {
            "cty": "武汉",
            "ctl": "话剧歌剧",
            "tsg": "0",
            "order": "1"
        }

        info = {'url': self.url, 'headers': headers, 'data':data,'data_key':None,'proxies': self.proxies}
        return info

    def Agent(self):
        _list = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
                 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.1 Safari/605.1.15"]

