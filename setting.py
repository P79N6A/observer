from worker.leid import get_show_list


class execute():
    def __init__(self):
        self.url = {
            '大麦':['https://search.damai.cn/searchajax.html']
        }
    def toDo(self):
        a = get_show_list.Spider(self.url['大麦'])
        a.todo()