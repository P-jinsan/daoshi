# -*- coding: utf-8 -*-
import scrapy
import json
import queue
import threading
import re
from daoshi.items import DaoshiItem
class DaoshiDataSpider(scrapy.Spider):
    name = 'daoshi_data'
    #allowed_domains = ['https://daoshi.eol.cn/home']
    #start_urls = ['https://daoshi.eol.cn/home/getTutor?special_id=0&page=2&recommend=1']
    def start_requests(self):
        url = 'https://daoshi.eol.cn/home/getTutor?special_id=0&page=1&recommend=1'
        yield scrapy.FormRequest(url, method='GET', callback=self.parse, dont_filter=True)
        # url_list = ["https://daoshi.eol.cn/home/getTutor?special_id=0&page={}&recommend=1".format(page) for page in range(1, 5033)]
        # for i in range(0,5032):#5032
        #     yield scrapy.FormRequest(url_list[i],method = 'GET', callback=self.parse,dont_filter = True)
    url_list = ["https://daoshi.eol.cn/home/getTutor?special_id=0&page={}&recommend=1".format(page) for page in
                range(1, 5033)]
    def parse(self, response):
        item = DaoshiItem()
        mytext = json.loads(response.text)
        data = mytext["data"]
        url_page = re.search('page=(.*?)&recommend',response.url,re.S).group(1)
        page = int(url_page)
        # 单线程存
        for eachdata in data:
                # print(eachdata['name'])
                item['school_id'] = eachdata["school_id"]
                item['email'] = eachdata["email"]
                item['title'] = eachdata["title"]
                item['phone'] = eachdata["phone"]
                item['tutor_id'] = eachdata["tutor_id"]
                item['clicks'] = eachdata["clicks"]
                item['name'] = eachdata["name"]
                item['yes_rank'] = eachdata["yes_rank"]
                item['aspect'] = eachdata["aspect"]
                item['school'] = eachdata["school"]
                item['special'] = eachdata["special"]
                item['depart'] = eachdata["depart"]
                item['introduce'] = eachdata["introduce"]
                item['work'] = eachdata["work"]
                yield item
        if page < 5033:
            yield scrapy.FormRequest(self.url_list[page], method='GET', callback=self.parse, dont_filter=True)
        # 多线程存
        # exitFlag = 0
        # class myThread (threading.Thread):
        #     def __init__(self, threadID, name, q):
        #         threading.Thread.__init__(self)
        #         self.threadID = threadID
        #         self.name = name
        #         self.q = q
        #     def run(self):
        #         #print ("开启线程：" + self.name)
        #         process_data(self.name, self.q)
        #         #print ("退出线程：" + self.name)
        #
        # def process_data(threadName, q):
        #     item = DaoshiItem()
        #     while not exitFlag:
        #         queueLock.acquire()
        #         if not workQueue.empty():
        #             data = q.get()
        #             queueLock.release()
        #             # print(threadName+':'+data["name"])
        #             item['school_id'] = data["school_id"]
        #             item['email'] = data["email"]
        #             item['title'] = data["title"]
        #             item['phone'] = data["phone"]
        #             item['tutor_id'] = data["tutor_id"]
        #             item['clicks'] = data["clicks"]
        #             item['name'] = data["name"]
        #             item['yes_rank'] = data["yes_rank"]
        #             item['aspect'] = data["aspect"]
        #             item['school'] = data["school"]
        #             item['special'] = data["special"]
        #             item['depart'] = data["depart"]
        #             item['introduce'] = data["introduce"]
        #             item['work'] = data["work"]
        #         else:
        #             queueLock.release()
        #
        # threadList = ["Thread-1", "Thread-2", "Thread-3"]
        # queueLock = threading.Lock()
        # workQueue = queue.Queue(11)
        # threads = []
        # threadID = 1
        # # 创建新线程
        # for tName in threadList:
        #     thread = myThread(threadID, tName, workQueue)
        #     thread.start()
        #     threads.append(thread)
        #     threadID += 1
        # # 填充队列
        # queueLock.acquire()
        # for word in data:
        #     workQueue.put(word)
        # queueLock.release()
        # # 等待队列清空
        # while not workQueue.empty():
        #     pass
        # # 通知线程退出
        # exitFlag = 1
        # # 等待所有线程完成
        # for t in threads:
        #     t.join()