# -*- coding: utf-8 -*-
import scrapy
import json

from LOL.items import LolItem
from LOL.items import timeLineItem
from LOL.tools.tools import getOpp
import time
import sys
import traceback
from functools import wraps
nums = 0
class TestspiderSpider(scrapy.Spider):
    name = 'testSpider'
    handle_httpstatus_list = [400, 401,402,403,404,405,415,429,502,503,504,505,506,406,407, 500]
    # allowed_domains = ['https://br1.api.riotgames.com']
    start_id = 4296118515
    # start_urls = map(lambda x:"https://kr.api.riotgames.com/lol/match/v4/matches/{}?".format(x), [4457500654+t for t in range(0, 10000)])
    start_urls = [
        # "https://kr.api.riotgames.com/lol/match/v4/matches/{}?".format(4457500654),
        
        "https://kr.api.riotgames.com/lol/match/v4/matches/{}?".format(4484206415),
        "https://kr.api.riotgames.com/lol/match/v4/matches/{}?".format(3983268669),
    ]
    NUM = 0
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
            participants = data['participants']
            
            # player List TimeLine Data 
            playerList = []
            for i in range(0, len(participants)):
                playerList.append([participants[i]['timeline']['lane'],
                                   participants[i]['timeline']['role']])
            
            oppPlayerList = []
            for i in range(0, len(participants)):
                item = LolItem()

                item['oppgid'] = getOpp(i+1, playerList)
                oppPlayerList.append(item['oppgid'])
                try:
                    item['pname']=identities[i]['player']['summonerName']
                except:
                    item['name']=''
                try:
                    item['gameVersion']=data['gameVersion']
                except:
                    item['gameVersion']=''
                
                try:
                    item['pid']=i+1
                except:
                    item['pid']=0
                try:
                    item['cid']= participants[i]['championId']
                    playerList[i].append(item['cid'])
                except:
                    item['cid']=0
                    playerList[i].append(0)
                try:
                    # print("-"*40)
                    item['uid']=identities[i]['player']['accountId']
                except:
                    item['uid']=''
                try:
                    item['gid']=data['gameId']
                except:
                    item['gid']=''
                try:
                    item['lane']=participants[i]['timeline']['lane']
                except:
                    item['lane']=''
                try:
                    item['role']=participants[i]['timeline']['role']
                except:
                    item['role']=''
                try:
                    item['win']=participants[i]['stats']['win']
                except:
                    item['win']=''
                try:
                    item['season']=data['seasonId']
                except:
                    item['season']=''
                try:

                    item['rank'] = participants[i]['highestAchievedSeasonTier']
                except:
                    item['rank']=''
                try:
                    item['totalkil']=participants[i]['stats']['kills']
                except:
                    item['totalkil']=''
                try:
                    item['totalkilled']=participants[i]['stats']['deaths']
                except:
                    item['totalkilled']=''
                try:
                    item['totalsupport']=participants[i]['stats']['assists']
                except:
                    item['totalsupport']=''
                try:
                    item['damagetaken']= participants[i]['stats']['totalDamageTaken']
                except:
                    item['damagetaken']=''
                try:
                    item['damage']=participants[i]['stats']['totalDamageDealt']
                except:
                    item['damage']= ''
                try:
                    item['heal']=participants[i]['stats']['totalHeal']
                except:
                    item['heal'] = ''
                try:
                    item['csdiffer']=participants[i]['timeline']['csDiffPerMinDeltas']['0-10']
                except:
                    item['csdiffer'] = ''
                yield item
                self.NUM+=100
                if self.NUM <= 2000000:
                    yield scrapy.Request(url="https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/{}?endIndex=100".format(item['uid']),headers= headers,callback=self.parse_3)
            yield scrapy.Request(url=response.url.replace("matches", "timelines/by-match").replace("?", ''), callback=self.parse_2, meta = {'oppPlayerList':oppPlayerList, 'playerList':playerList})

       
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
            

    def parse_3(self, response):
        self.custom_log(response)
        if response.status == 200:
            data = json.loads(response.text)
            for item in data['matches']:
                gameid = item['gameId']
                if gameid in self.gameIdDict:
                    continue
                else:
                    yield scrapy.Request(url="https://kr.api.riotgames.com/lol/match/v4/matches/{}?".format(gameid), callback=self.parse)
                    self.gameIdDict[gameid] = 1
            return
