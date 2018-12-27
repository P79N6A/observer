from other.spiders import damai


class execute():
    def __init__(self):
        self.url = {
            '大麦':['https://search.damai.cn/searchajax.html']
        }
    def toDo(self):
        a = damai.Spider(self.url['大麦'])
        a.todo()