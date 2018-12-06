"""
网页转成邮件格式
"""

from requests import get
from bs4 import BeautifulSoup
import header
from time import sleep



def Tohtml(url):
    flag = True
    error_count = 0
    while flag:
        try:
            r = get(url,headers=header.Header())
            flag = False
        except:
            error_count += 1
            if error_count >10:
                return "error network"
            sleep(10)

    html = BeautifulSoup(r.text,"html.parser")
    title = html.select('div[class="topTlt"] p[class="title"]')[0].get_text()
    postInfo = html.select('div[class="topTlt"] span')
    contents = html.select('div[class="divAbs"]')
    postTime,postFrom = postInfo[1].get_text(),postInfo[3].get_text()
    text = open("module.html", "r").read()
    text = text.format(title=title,postTime=postTime,postFrom=postFrom,link=url)


    return text+str(contents[0])

