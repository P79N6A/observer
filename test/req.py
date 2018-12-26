# 用requests下载图片

import requests
from requests import RequestException

from other import url_info as _config
from bs4 import BeautifulSoup as bs


# 主函数
def main():
    page_info = {}
    # 设置地址
    page_info['url'] = _config.url

    # 设置请求头
    page_info['headers'] = _config.headers

    # 设置代理
    page_info['proxies'] = _config.proxies

    html = get_one_page(page_info)
    parse_one_page(html)


def get_one_page(info):
    try:
        response = requests.get(info['url'], headers=info['headers'], proxies=info['proxies'], timeout=1)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):

    #解析内容
    soup = bs(html, 'html.parser')



    #获取信息主题
    df = soup.find('div', class_='article')

    #获取演出信息列表
    gd = df.find('ul',class_='events-list')

    #获取页码信息
    page_number= df.find('span',class_='next')
    page_number_href= page_number.find('a').get('href')

    #在这里，我们需要把所有的页码都获取到，然后在分析每个页面有多少活动，最后再完成每个页面都信息获取
    print(page_number_href)

    dge= gd.find_all("div",class_="title")
    for ge in dge:

        #给每个链接地址赋值
        ge=ge.find('a').get('href')
        print(ge)




def get_info(fd):
    print(fd.find('a').get('href'))


if __name__ == '__main__':
    main()
