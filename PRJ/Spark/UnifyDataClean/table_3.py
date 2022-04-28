# 取所有的英雄数据
import json
data = ''
with open("C:/Users/herrn/Documents/PythonScripts/Scrapy/LoLAnalysis/name-cid.json") as f:
    data = f.read()
data = json.loads(data)
cid_cname = data['cid-name']

from UnifyDataClean.tools import getReadDB, getWriteDB, roleDefine
def map_1(row):
    cid = row["cid"]

    kill = int(row['totalkill'])
    killed = int(row['totalkilled'])
    heal =int(row['heal'])
    damage = int(row['damage'])
    damaged = int(row['damagetaken'])
    assist = int(row['totalsupport'])
    cname = cid_cname[cid]
    if cid == '':
        cid = 0
    return (cid , (cname, kill, killed, heal, damage, damaged, assist, 1))

def dataClean(rdd0):

    rdd1 = rdd0.map(map_1)
    rdd2 = rdd1.reduceByKey(lambda x, y:(x[0], x[1]+y[1], x[2]+y[2], x[3]+y[3], x[4]+y[4], x[5]+y[5], x[6] + y[6], x[7]+y[7]))
    l1  =  rdd2.collect()

    return l1

def write(l, db, cursor):
    for i in range(len(list(l))):
        row = l[i]
        cursor.execute("INSERT INTO table_3 (cid, cname, kills, killed, heal, damage, damaged, assist) \
                        VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(
                        row[0], row[1][0], row[1][1]/row[1][7], row[1][2]/row[1][7], row[1][3]/row[1][7], row[1][4]/row[1][7], row[1][5]/row[1][7], row[1][6]/row[1][7]))
    db.commit()
    db.close()
def app():
    db, cursor = getWriteDB()
    rdd = getReadDB()
    l = dataClean(rdd)
    write(l, db, cursor)
if __name__ == '__main__':
    app()