"""
开启2个线程，一个爬取，一个监视
"""

import mainSpider
import threading
from time import sleep


class Main():
    def __init__(self):
        self.spider = mainSpider.MainSpider()

    def alive_check(self):
        while True:
            if not self.thread.isAlive():
                self.thread = threading.Thread(target=self.compare_thread)
                self.thread.start()
            sleep(10)


    def compare_thread(self):
        while True:
            self.spider.compare()


    def threads(self):
        self.thread = threading.Thread(target=self.compare_thread)
        self.thread.start()
        threading.Thread(target=self.alive_check).start()


if __name__ == '__main__':
    main = Main()
    main.threads()