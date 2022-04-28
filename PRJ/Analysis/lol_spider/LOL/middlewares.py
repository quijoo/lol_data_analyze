# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from LOL.tools.tokenDict import TokenPool
import time
import traceback


tokenPool = TokenPool([
    "RGAPI-3e84561a-88f2-4f23-81ef-b4ca8061b9d0",
    "RGAPI-13d97586-1dde-46e1-8d71-00eacd01ef99",
    "RGAPI-6836bfaa-ea16-48a4-8f78-fc6b0ad9d2b1",
    "RGAPI-461ef4a6-5586-45c6-a5b1-25a17378960b",
    "RGAPI-a0b8245e-fc6d-4181-a2f8-b25eddbeca11",
    "RGAPI-d0074b22-5eb0-40c1-8789-f35218938aae",
    "RGAPI-746cbd87-1f1a-4bfc-85a0-6d2c35bba017",
    "RGAPI-24136e4f-8208-46c3-bbd8-4be9c6e8059e",
    "RGAPI-24136e4f-8208-46c3-bbd8-4be9c6e8059e",
    "RGAPI-d0c9efa4-bb41-4a17-b87b-a8bd91adde54",
    "RGAPI-862e68ad-b3a2-489b-9342-763c1ed12b87",
    "RGAPI-0d8eb8c3-81bb-4bf0-af00-b2f8873a9e4e",
    "RGAPI-7264f074-ed06-41df-aec2-01b6b41dfbd1",
    "RGAPI-3317398d-79f3-4f9b-a79a-406785525dfb",
    "RGAPI-b7bd83c0-fe16-43fd-b38d-33e4c3b1cd56",])


from LOL.tools.tools import tokenGameMap

tokentmp = tokenGameMap()
def custom_log( response):
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        p_name = traceback.extract_stack()[-2][2]
        c_name = ""
        stat = c_name + '.' + p_name 
        out = "{0} [{1}] INFO: REQUEST: <{2}>".format(t, stat, response.url)
        print(out)
class LolSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.
    
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class LolDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.
        # print("Downloader: {}   Token:{}".format(request.url.split('/')[-1]))
        # print("Downloader: {}".format(request.url.split('/')[-1]))
        # 标志着爬取 useid
        custom_log(request)
        if  'index' in request.headers:
            token = tokenPool.getToken_1(int(request.headers['index']))
            request.headers['X-Riot-Token']= token
        else:
            request.headers['X-Riot-Token'], index = tokenPool.getToken()
            gameid = request.url.split('/')[-1]
            tokentmp.add(gameid, index)
        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.
        gameid = response.url.split('/')[-1]
        # if response.url.split('/')[-4] == "match": 
        #     print("-"*40)
        response.headers['index'] = tokentmp.getIndex(gameid)
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
