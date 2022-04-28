# -*- coding: utf-8 -*-
import scrapy
import json

from LOL.items import LolItem, timeLineItem
from LOL.tools.tools import getOpp
import time
import sys
import traceback
import pymysql

class TestspiderSpider(scrapy.Spider):
    name = 'Spider_3'
    handle_httpstatus_list = [400, 401,402,403,404,405,415,429,502,503,504,505,506,406,407, 500]
    # allowed_domains = ['https://br1.api.riotgames.com']
    start_id = 4296118515
    # start_urls = map(lambda x:"https://kr.api.riotgames.com/lol/match/v4/matches/{}?".format(x), [4457500654+t for t in range(0, 10000)])
    start_urls = [
        # "https://kr.api.riotgames.com/lol/match/v4/matches/{}?".format(4457500654),
        
        "https://kr.api.riotgames.com/lol/match/v4/matches/{}?".format(4484206415),
        "https://kr.api.riotgames.com/lol/match/v4/matches/{}?".format(3983268669),
    ]
    def start_requests(self):
        conn =pymysql.connect(host="localhost", port=3306, db="lol", user="root", passwd="123123123", charset='utf8')
        cur = conn.cursor()
        cur.execute("select * from table_gameid;")
        res = cur.fetchall()
        for url in map(lambda x: "https://kr.api.riotgames.com/lol/match/v4/timelines/by-match/{}".format(x[0]), res):    
            yield scrapy.Request(url=url, callback=self.parse_2)
            
    def custom_log(self, response):
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        p_name = traceback.extract_stack()[-2][2]
        c_name = self.__class__.__name__
        stat = c_name + '.' + p_name 
        out = "{0} [{1}] INFO: STAT: <{2}>, <{3}>".format(t, stat, response.status, response.url)
        print(out)
    def parse_2(self, response):
        self.custom_log(response)
        if response.status!=200:
            return
        else:
            oppPlayerList = response.meta['oppPlayerList']
            playerList = response.meta['playerList']
            data = json.loads(response.text)["frames"]
            d = {}
            towerList = []
            item = timeLineItem()
            towerKiller = {}
            towerTime = {
                'TOP_LANE':('', 0),
                'MID_LANE':('', 0),
                'BOT_LANE':('', 0),
            }
            for events in map(lambda x:x['events'] ,data):
                for event in events:
                    if event['type'] == 'CHAMPION_KILL':
                        kid = event['killerId']
                        vid = event['victimId']
                        # print(vid, oppPlayerList[kid-1])
                        if vid == oppPlayerList[kid-1]:
                            if kid in d:
                                d[kid] += 1
                            else:
                                d[kid] = 1
                    if event['type'] == 'BUILDING_KILL':
                        kid = event['killerId']
                        lane = event['laneType']
                        if kid in towerKiller:
                            towerKiller[kid] += 1
                        else:
                            towerKiller[kid]  = 1
                        towerTime[lane] = (event['timestamp'], kid) if towerTime[lane][0] == '' else towerTime[lane]
            for i in range(len(oppPlayerList)):
                item['pid'] = i+1
                item['gid'] = response.url.split('/')[-1]
                item['oppcid'] = playerList[oppPlayerList[i]-1][2] if oppPlayerList[i] != -1 else -1
                item['killcounter'] = d[i+1] if i+1 in d else 0
                item['killedcounter'] = d[oppPlayerList[i]] if oppPlayerList[i] in d else 0
                item['tower'] = towerKiller[i+1] if i+1 in towerKiller else 0
                if playerList[i][0][0:3] == "TOP":
                    item['firsttowertime'] = towerTime["TOP_LANE"][0] if (((i+1) <= 5 and towerTime["TOP_LANE"][1] <= 5) or ((i+1) > 5 and towerTime["TOP_LANE"][1] > 5)) and towerTime["TOP_LANE"][1]!=0 else 0
                elif playerList[i][0][0:3] == "MID":
                    item['firsttowertime'] = towerTime["MID_LANE"][0] if (((i+1) <= 5 and towerTime["MID_LANE"][1] <= 5) or ((i+1) > 5 and towerTime["MID_LANE"][1] > 5)) and towerTime["TOP_LANE"][1]!=0 else 0
                elif playerList[i][0][0:3] == "BOT":
                    item['firsttowertime'] = towerTime["BOT_LANE"][0] if (((i+1) <= 5 and towerTime["BOT_LANE"][1] <= 5) or ((i+1) > 5 and towerTime["BOT_LANE"][1] > 5)) and towerTime["TOP_LANE"][1]!=0 else 0
                else:
                    item['firsttowertime'] = 0
                yield item
            return