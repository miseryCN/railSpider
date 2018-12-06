"""
邮件模块
"""

from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import settings,smtplib
from time import sleep


class Mails():
    def __init__(self):
        self.setting = settings.Settings()


    def format_address(self,word):
        name,address = parseaddr(word)
        return formataddr((Header(name, 'utf-8').encode(), address))

    def sendMail(self,myNickName,header,content):
        msg = MIMEText(content,"html","utf-8")
        msg["From"] = self.format_address(myNickName+"<%s>"%self.setting.mailUser)
        msg["To"] = self.format_address(self.setting.recvNickName+"<%s>"%self.setting.recvUser)
        msg["Subject"] = Header(header,"utf-8").encode()
        error_count = 0
        while True:
            try:
                server = smtplib.SMTP(self.setting.smtpServer,self.setting.smtpPort)
                server.login(self.setting.mailUser,self.setting.mailPass)
                server.sendmail(self.setting.mailUser,[self.setting.recvUser],msg.as_string())
                server.quit()
                break
            except:
                error_count += 1
                if error_count >10:
                    return
                sleep(10)
