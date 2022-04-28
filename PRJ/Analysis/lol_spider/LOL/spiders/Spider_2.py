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
    name = 'Spider_2'
    handle_httpstatus_list = [400, 401,402,403,404,405,415,429,502,503,504,505,506,406,407, 500]
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.58",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://developer.riotgames.com",
            "X-Riot-Token":"",
        }
    def start_requests(self):
        print("*"*50)
        print("启动爬虫！")
        print("*"*50)
        conn =pymysql.connect(host="localhost", port=3306, db="lol", user="root", passwd="123123123", charset='utf8')
        cur = conn.cursor()
        cur.execute("select * from table_gameid;")
        res = cur.fetchall()
        for url in map(lambda x: "https://kr.api.riotgames.com/lol/match/v4/matches/{}?".format(x[0]), res):    
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)
    def custom_log(self, response):
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        p_name = traceback.extract_stack()[-2][2]
        c_name = self.__class__.__name__
        stat = c_name + '.' + p_name 
        out = "{0} [{1}] INFO: STAT: <{2}>, <{3}>".format(t, stat, response.status, response.url)
        print(out)
    def parse(self, response):
        self.custom_log(response)
        if response.status!=200:
            return
        else:
            data = json.loads(response.text)
            identities = data['participantIdentities']
            participants = data['participants']
            playerList = []
            for i in range(0, len(participants)):
                playerList.append([participants[i]['timeline']['lane'],
                                   participants[i]['timeline']['role']])
            for i in range(0, len(participants)):
                item = LolItem()
                item['oppgid'] = getOpp(i+1, playerList)
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