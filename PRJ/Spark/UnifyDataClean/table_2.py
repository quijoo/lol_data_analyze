# name ：JY
# 需求 ： (cid, versusid) killcounter, killedcounter, firsttowertime
#                         cwinrate, kdr, kda

from UnifyDataClean.tools import getReadDB, getWriteDB, roleDefine




def map_1(row):
    cid = row["cid"]
    versusid = row['oppcid']

    killcounter = int(row['killcounter']) if row['killcounter'] != None else 0
    killedcounter = int(row['killedcounter']) if row['killedcounter'] != None else 0
    firsttowertime = 0 if (row['firsttowertime']== None or row['firsttowertime']=="") else int(row['firsttowertime'])

    cwin = 1 if row['win'] == "True" else 0
    csdiffer = float(row['csdiffer']) if row['csdiffer']!= '' else 0
    if versusid == "-1" or versusid == None or versusid == "None":
        versusid = ''
        cid=''
    return ((cid, versusid), (killcounter,1, killedcounter, firsttowertime, cwin,csdiffer))

def dataClean(rdd0):

    rdd1 = rdd0.map(map_1)
    rdd2 = rdd1.reduceByKey(lambda x, y:(x[0]+y[0], x[1]+y[1], x[2]+y[2], x[3]+y[3], x[4]+y[4], x[5]+y[5]))
    l1  =  rdd2.collect()

    return l1

def write(l, db, cursor):
    for i in range(len(list(l))):
        row = l[i]
        cursor.execute("INSERT INTO table_2 (cid, versusid, killcounter,nums, killedcounter, firsttowertime, cwin, csdiffer) \
                        VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(
                        row[0][0], row[0][1], row[1][0]/row[1][1], row[1][1], row[1][2]/row[1][1], row[1][3]/row[1][1], row[1][4]/row[1][1], row[1][5]/row[1][1]))
    db.commit()
    db.close()
def app():
    db, cursor = getWriteDB()
    rdd = getReadDB()
    l = dataClean(rdd)
    write(l, db, cursor)
if __name__ == '__main__':
    app()