"""
主文件
"""

import settings
from bs4 import BeautifulSoup
from header import Header
from time import sleep
import requests
from mails import Mails
import toHtml

class MainSpider():

    def __init__(self):
        self.setting = settings.Settings()
        self.websiteList = self.setting.get_url_list()
        self.updateDict = {}
        self.mail = Mails()


    def get_mainPage(self,url):
        header = Header()
        flag = True
        try_count = 0
        while flag:
            try:
                r = requests.get(url,headers=header,timeout=10)
                flag = False
            except:
                try_count += 1
                print("网络错误，重试... *"+str(try_count))
                if try_count >10:
                    return "error network",1
                sleep(10)
        html = BeautifulSoup(r.text,"html.parser")
        posts = html.select('div[class="ListInfoFrame"] table[class="listInfoTable"] tr td a')
        return posts[0].get("href"),posts[0].get_text().strip()


    def compare(self):
        for url in self.websiteList:
            order = self.websiteList.index(url)
            result = self.get_mainPage(url)
            postUrl,title = result
            webUrl,railName = self.setting.attributeDict[order]
            print(railName,title,webUrl+postUrl)
            if not postUrl == "error network":
                if order in self.updateDict.keys():
                    if not self.updateDict[order] == result:
                        print("发现更新!")
                        content = toHtml.Tohtml(webUrl+postUrl)
                        self.mail.sendMail(railName,title,content)
                else:
                    self.updateDict[order] = result
                    content = toHtml.Tohtml(webUrl + postUrl)
                    self.mail.sendMail(railName, title, content)
                    print("第一次操作！")
        sleep(30)
