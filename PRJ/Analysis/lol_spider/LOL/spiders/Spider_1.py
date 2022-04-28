# -*- coding: utf-8 -*-
import scrapy
import json

from LOL.items import LolItem, timeLineItem, gameIdItem
from LOL.tools.tools import getOpp
import time
import sys
import traceback


class TestspiderSpider(scrapy.Spider):
    name = 'Spider_1'
    handle_httpstatus_list = [400, 401,402,403,404,405,415,429,502,503,504,505,506,406,407, 500]
    # allowed_domains = ['https://br1.api.riotgames.com']
    # start_urls = map(lambda x:"https://kr.api.riotgames.com/lol/match/v4/matches/{}?".format(x), [4457500654+t for t in range(0, 10000)])
    start_urls = [
        # "https://kr.api.riotgames.com/lol/match/v4/matches/{}?".format(4457500654),
        
        "https://kr.api.riotgames.com/lol/match/v4/matches/{}?".format(4484206415),
        "https://kr.api.riotgames.com/lol/match/v4/matches/{}?".format(3983268669),
    ]
    NUM = 100000
    gameIdDict = {}    
    
    
    def custom_log(self, response):
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        p_name = traceback.extract_stack()[-2][2]
        c_name = self.__class__.__name__
        stat = c_name + '.' + p_name 
        out = "{0} [{1}] INFO: STAT: <{2}>, <{3}>".format(t, stat, response.status, response.url)
        print(out)




    def parse(self, response):
        self.custom_log(response)
        # print(tokenPool.getToken())
        # https://kr.api.riotgames.com/lol/match/v4/matches/{}?
        # https://kr.api.riotgames.com/lol/match/v4/timelines/by-match/4296118515
        
        index = response.headers['index']
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.58",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://developer.riotgames.com",
            "X-Riot-Token":"",
            "index":index
        }
        if response.status!=200:
            return
        else:
            data = json.loads(response.text)
            identities = data['participantIdentities']
            for i in range(0, len(identities)):
                uid=identities[i]['player']['accountId']
                if len(self.gameIdDict) <= self.NUM:
                    yield scrapy.Request(url="https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/{}?endIndex=100".format(uid),headers= headers,callback=self.parse_3)

        
    def parse_3(self, response):
        self.custom_log(response)
        print("-"*100)
        print("gameIdList.Length = {}".format(len(self.gameIdDict)))
        print("-"*100)
        if response.status == 200:
            data = json.loads(response.text)
            for item in data['matches']:
                gameid = item['gameId']
                if gameid in self.gameIdDict:
                    continue
                else:
                    if len(self.gameIdDict) <= self.NUM:
                        yield scrapy.Request(url="https://kr.api.riotgames.com/lol/match/v4/matches/{}?".format(gameid), callback=self.parse)
                        self.gameIdDict[gameid] = ''
                    # else:
                    item = gameIdItem()
                    item["gameId"] = gameid
                    yield item

