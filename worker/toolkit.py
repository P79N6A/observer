# 工具包
import time


def _parse(self):  # get解析
    try:
        _response = requests.get(self.get_url, headers=self.headers, timeout=3)
        if _response.status_code == 200:
            # 自行转码
            _response.encoding = 'UTF-8'
            # 解析内容
            page_source = BS(_response.text, 'html.parser')

            # print(response.text)
            print('获取页面资源成功')
            return page_source
        else:
            print('解析代理网站时出现错误', _response.status_code)
            return None
    except RequestException:
        print('解析代理网站时出现错误', RequestException)
        return None


# 传入分词，和数据库中的内容做比较，如果没有相似的，就返回True，如果有相似度高的，就返回False
def whether_repeat(label):
    make_label(label)
    return make_label(label)


# 分词，输入文章，返回提交的关键词,注意这里如果返回的话，不能返回列表，不然会在数据库里面显示成list
def make_label(text):
    return ('关键词')

#记录器,记录日志
def input_log(*texts):
    import os
    _path='%s/res/temp_log'%os.path.dirname(__file__)#获取此方法的绝对地址
    # print('%s %s' % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), texts))
    with open('%s/res/temp_log'%os.path.dirname(__file__), 'a+') as file:
        file.write('%s\t'%time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        for i in texts:
            file.write('%s\t'%i)
        file.write('\n')


if __name__ == '__main__':
    a = input_log('d','d')
