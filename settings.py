"""
配置文件
"""


class Settings():

    def __init__(self):
        self.project_code = "2000001"                                                            #销售-项目公告
        self.bidding_code = "2200001"                                                            #销售-中标公告
        self.websites = [
            "http://wz.lanzh.95306.cn/mainPageNoticeList.do?method=init&id={id}",     #兰州铁路局
            #"http://wz.cd-rail.com/mainPageNoticeList.do?method=init&id={id}",        #成都铁路局
            "http://wz.xian.95306.cn/mainPageNoticeList.do?method=init&id={id}",         #西安铁路局
            "http://wz.huhht.95306.cn/mainPageNoticeList.do?method=init&id={id}",         #呼和浩特铁路局
            "http://wz.qingz.95306.cn/mainPageNoticeList.do?method=init&id={id}",   #青藏铁路局
        ]
        self.attributeDict = {
            0 : ("http://wz.lanzh.95306.cn/","兰州铁路局"),
            1 : ("http://wz.lanzh.95306.cn/","兰州铁路局"),
            #2 : ("http://wz.cd-rail.com/","成都铁路局"),
            #3 : ("http://wz.cd-rail.com/","成都铁路局"),
            2 : ("http://wz.xian.95306.cn/","西安铁路局"),
            3 : ("http://wz.xian.95306.cn/","西安铁路局"),
            4 : ("http://wz.huhht.95306.cn/","呼和浩特铁路局"),
            5 : ("http://wz.huhht.95306.cn/","呼和浩特铁路局"),
            6 : ("http://wz.qingz.95306.cn/","青藏铁路局"),
            7 : ("http://wz.qingz.95306.cn/","青藏铁路局")
        }

        self.mailUser = "example@mxhichina.com"
        self.mailPass = "password"
        self.recvNickName = "xxx"
        self.recvUser = "recv@qq.com"
        self.smtpServer = "smtp.mxhichina.com"
        self.smtpPort = 25



    def get_url_list(self):
        websiteList = []
        for website in self.websites:
            websiteList.append(website.format(id=self.project_code))
            websiteList.append(website.format(id=self.bidding_code))
        return websiteList