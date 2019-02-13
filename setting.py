from worker.readers import test


class execute():
    def __init__(self):
        self.url = {
            '大麦':['https://search.damai.cn/searchajax.html']
        }
    def toDo(self):
        a = test.Spider(self.url['大麦'])
        a.todo()