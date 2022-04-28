# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs,json
import pymysql
# import sqlite3
class LolPipeline(object):
    # def __init__(self, sqlite_file, sqlite_table):
        # self.sqlite_file = sqlite_file
        # self.sqlite_table = sqlite_table
        
    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls(
    #         sqlite_file = crawler.settings.get('SQLITE_FILE'), # 从 settings.py 提取
    #         sqlite_table = crawler.settings.get('SQLITE_TABLE', 'items')
    #     )
    num1 = 0
    num2 = 0
    def open_spider(self, spider):
        db = spider.settings.get('MYSQL_DB_NAME','lol')
        host = spider.settings.get('MYSQL_HOST', 'localhost')
        port = spider.settings.get('MYSQL_PORT', 3306)
        user = spider.settings.get('MYSQL_USER', 'root')
        passwd = spider.settings.get('MYSQL_PASSWORD', '123456')

        self.conn =pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset='utf8')
        self.cur = self.conn.cursor()

    # 关闭数据库
    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()
 
    def process_item(self, item, spider):
        # print(self.num1, self.num2)
        if item.name == 'item_1':
            item= dict(item)
            item['rank'] = '0' if item['rank'] == '' else item['rank']
            insert_sql = "INSERT INTO table_dirty_1 (version,name,cid,oppgid,uid,gid,pid,lane,role,win,season,ranks,totalkill,totalkilled,totalsupport,damagetaken,damage,heal,csdiffer) VALUES ('{}','{}', '{}', '{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(item['gameVersion'], item['pname'], item['cid'], str(item['oppgid']),str(item['uid']),str(item['gid']),str(item['pid']),str(item['lane']),str(item['role']),str(item['win']),str(item['season']),str(item['rank']),str(item['totalkil']),str(item['totalkilled']),str(item['totalsupport']), str(item['damagetaken']),str(item['damage']),str(item['heal']),str(item['csdiffer']))
            # print(insert_sql)
            # try:
            self.cur.execute(insert_sql)
            # except:
            #     # print('-'*40)
            #     # print(insert_sql)
            #     pass
            self.conn.commit()
            # self.num1+=1
        elif item.name == 'item_2':
            item= dict(item)
            insert_sql = "UPDATE table_dirty_1 SET oppcid = '{}', killcounter = '{}', killedcounter='{}',  tower='{}' , firsttowertime = '{}' WHERE pid = '{}' and gid = '{}';".format(item['oppcid'], item['killcounter'], item['killedcounter'], item['tower'], item['firsttowertime'], item['pid'], item['gid'])
            # print(insert_sql)
            self.cur.execute(insert_sql)
            self.conn.commit()
            # self.num2+=1
        elif item.name == 'item_3':
            item= dict(item)
            insert_sql = "INSERT INTO table_gameid (gameId) VALUES ('{}');".format(item["gameId"])

            self.cur.execute(insert_sql)
            self.conn.commit()
            # self.num2+=1
        else:
            pass
        
        return item
