# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LolItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = "item_1"
    oppgid  = scrapy.Field()
    uid     = scrapy.Field()
    gid     = scrapy.Field()
    pid     = scrapy.Field()
    cid     = scrapy.Field()
    gameVersion = scrapy.Field()
    pname   = scrapy.Field()
    lane    = scrapy.Field()
    role    = scrapy.Field()
    win     = scrapy.Field()
    season  = scrapy.Field()
    rank    = scrapy.Field()
    totalkil= scrapy.Field()
    totalkilled     = scrapy.Field()
    totalsupport    = scrapy.Field()
    damagetaken     = scrapy.Field()
    damage          = scrapy.Field()
    heal            = scrapy.Field()
    csdiffer        = scrapy.Field()


class timeLineItem(scrapy.Item):
    name = "item_2"
    pid = scrapy.Field()
    gid = scrapy.Field()
    oppcid  = scrapy.Field()
    tower = scrapy.Field()
    killcounter = scrapy.Field()
    killedcounter = scrapy.Field()
    firsttowertime = scrapy.Field()

class gameIdItem(scrapy.Item):
    name = "item_3"
    gameId = scrapy.Field()