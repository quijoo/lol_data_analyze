from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark import SparkConf,SparkContext
import json


import pymysql

# 输出数据的数据库
def getWriteDB():
    db = pymysql.connect("localhost", "root", "123123123", "lol")
    cursor = db.cursor()
    return db, cursor


def getReadDB(table="table_dirty"):
    sc = SparkContext(appName='championCapility')
    ctx = SQLContext(sc)
    jdbcDf=ctx.read.format("jdbc").options(url="jdbc:mysql://localhost:3306/lol",
                                           driver="com.mysql.jdbc.Driver",
                                           dbtable="(SELECT * FROM {}) tmp".format(table),
                                           user="root",
                                           password="123123123").load()
    return jdbcDf.rdd


def roleDefine(role, lane):
    res = "-1"
    if role == "SOLO" and (lane == "BOTTOM" or lane == "TOP"):
        res = "TOPSOLO"
    elif role == "DUO_CARRY":
        res = "BOTTOM"
    elif role == "DUO_SUPPORT":
        res = "SUPPORT"
    elif lane == "JUNGLE":
        res = "JUNGLE"
    elif lane == "MIDDLE":
        res = "MIDDLE"
    else:
        res = "-1"
    return res

def getMap():
    data = ''
    with open("C:/Users/herrn/Desktop/PRJ/JSON/name-cid.json") as f:
        data = f.read()
    data = json.loads(data)
    cid_cname = data['cid-name']
    return cid_cname


