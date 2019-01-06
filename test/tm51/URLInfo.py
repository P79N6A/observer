#爬虫页面信息配置文件

#url = 'https://www.douban.com/location/wuhan/events/future-drama'
url = 'https://search.damai.cn/search.htm?spm=a2oeg.home.category.ditem_1.3bc023e1yp13wI&ctl=话剧歌剧&order=1&cty='

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; OPPO A57 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.10 (Baidu; P1 6.0.1)'
}

proxies ={
}

def load():
    info = {}
    # 设置地址
    info['url'] = url

    # 设置请求头
    info['headers'] = headers

    # 设置代理
    info['proxies'] = proxies

    return info

if __name__ == '__main__':
    print(load()['url'])
