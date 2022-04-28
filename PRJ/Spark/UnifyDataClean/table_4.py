# 取所有的英雄数据
import json
import math
from UnifyDataClean.tools import getReadDB, getWriteDB, roleDefine, getMap
cid_cname = getMap()


def map_4_1(row):
    cid = row["cid"]

    kill = (float(row['kills']))
    killed = float(row['killed'])
    heal =float(row['heal'])
    damage = float(row['damage'])
    damaged = float(row['damaged'])
    assist = float(row['assist'])
    cname = row["cname"]
    if cid == '':
        cid = 0
    return (cid , (cname, kill, killed, heal, damage, damaged, assist))

def map_4_2(row):
    return ("" , (row[1][1],row[1][2],row[1][3],row[1][4],row[1][5],row[1][6]))

def dataClean(rdd4_0):
    rdd4_1 = rdd4_0.map(map_4_1)
    rdd4_2 = rdd4_1.map(map_4_2)
    rdd4_3 = rdd4_2.reduceByKey(lambda x,y:(x[0]+y[0], x[1]+y[1], x[2]+y[2], x[3]+y[3], x[4]+y[4], x[5]+y[5]))
    l = list(rdd4_3.collect())[0][1]
    l = list(map(lambda x:x/148, l))
    rdd4_4 = rdd4_1.map(lambda x: ("", ((x[1][1] - l[0])**2,(x[1][2] - l[1])**2,(x[1][3] - l[2])**2,(x[1][4] - l[3])**2,(x[1][5] - l[4])**2,(x[1][6] - l[5])**2)))
    rdd4_5 = rdd4_4.reduceByKey(lambda x, y: (x[0]+y[0], x[1]+y[1], x[2]+y[2], x[3]+y[3], x[4]+y[4], x[5]+y[5]))
    rdd4_6 = rdd4_5.map(lambda x:tuple(map(lambda y:math.sqrt(y/148), x[1])))
    l2 = rdd4_6.collect()[0]

    print(l)
    print(l2)
    # 计算方差
    rdd4_7 = rdd4_1.map(lambda x: (x[0],(
                                    x[1][0],
                                    (x[1][1]-l[0])/l2[0],
                                    (x[1][2]-l[1])/l2[1],
                                    (x[1][3]-l[2])/l2[2],
                                    (x[1][4]-l[3])/l2[3],
                                    (x[1][5]-l[4])/l2[4],
                                    (x[1][6]-l[5])/l2[5],
                                )))
    ln = rdd4_7.collect()
    print(ln)
    return list(ln)

def write(l, db, cursor):
    for i in range(len(list(l))):
        row = l[i]
        print(row[0], row[1][0], row[1][1], row[1][2], row[1][3], row[1][4], row[1][5], row[1][6])
        cursor.execute("INSERT INTO table_4 (cid, cname, kills, killed, heal, damage, damaged, assist) \
                        VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(
                        row[0], row[1][0], row[1][1], row[1][2], row[1][3], row[1][4], row[1][5], row[1][6]))
    db.commit()
    db.close()
def app():
    db, cursor = getWriteDB()
    rdd = getReadDB("table_3")
    l = dataClean(rdd)
    write(l, db, cursor)
if __name__ == '__main__':
    app()