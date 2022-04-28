from flask import Flask, redirect, url_for, request, render_template, make_response, session
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import json
from config import db
from dbmodel.Champion_id import  Champion_id
app = Flask(__name__)
app.secret_key = 'djstla'
app.config['DEBUG'] = True
import numpy as np

def test_3():
    id_list = []    #英雄id列表
    role_list = []  #英雄定位
    winrate_list=[] #英雄胜率
    apperate_list=[]#英雄登场率
    id = []
    data = db.session.query(Champion_id.cid).filter().all()
    for i in data:
        id.append(i.cid)
    a = np.unique(id)  #英雄id列表

    for idlist in a:
        data = db.session.query(Champion_id).filter(Champion_id.cid == idlist)
        ll = list(map(lambda x: x.appear, data))
        max_index = ll.index(max(ll))  # 索引 #l[max_index]最大值
        for id in data:
            if (id.appear == ll[max_index]):
                id_list.append(id.cid)
                role_list.append(id.role)
                winrate_list.append(id.win)
                apperate_list.append(id.appear)

        #对应英雄id 名字
    data = ''
    with open('C:/Users/myffa/Desktop/flask01/static/test.json', 'r', encoding='utf-8') as fp:
        data = json.loads(fp.read())
    cidAsKey = data['cid-name']
    nameAsKey = data['name-cid']
    idlist_json=[]
    namelist_json=[]
    for k in cidAsKey:
        namelist_json.append(cidAsKey[k])
    for k in nameAsKey:
        idlist_json.append(nameAsKey[k])
    # print(idlist_json)
    # print(namelist_json)
    #找出上单英雄id、胜率列表
    topid_list=[]
    topwinrate_list=[]
    topappear_list =[]
    for temp in range(len(role_list)):
        if(role_list[temp]=="TOPSOLO"):
            topid_list.append(id_list[temp])
            topwinrate_list.append(winrate_list[temp])
            topappear_list.append(apperate_list[temp])

    #上单英雄id、名字 按胜率排名
    topid_order =[]  #按胜率top的id排名
    topwin_order =[] #top胜率排名
    topname_order =[] #对应id排名的名字

    print("-------------按胜率的英雄排名------------------")
    for temp1 in range(len(topwinrate_list)):
        topwin_order.append(topwinrate_list[temp1])
    topwin_order.sort(reverse=True)

    for temp1 in range(len(topwinrate_list)):
            topid_order.append(topid_list[topwinrate_list.index(topwin_order[temp1])])
    print(topid_order)
    for temp1 in range(len(topid_order)):
        topname_order.append(namelist_json[idlist_json.index(topid_order[temp1])])
    print(topname_order)

    print("-------------按出场率的英雄排名------------------")
    #上单英雄id、名字 按出场率排名
    topid_order1 =[]  #按胜率top的id排名
    topappear_order1 =[] #top胜率排名
    topname_order1 =[] #对应id排名的名字

    for temp2 in range(len(topappear_list)):
        topappear_order1.append(topappear_list[temp2])

    topappear_order1.sort(reverse=True)
    for temp2 in range(len(topappear_list)):
            topid_order1.append(topid_list[topappear_list.index(topappear_order1[temp2])])
    print(topid_order1)
    for temp2 in range(len(topid_order1)):
        topname_order1.append(namelist_json[idlist_json.index(topid_order1[temp2])])
    print(topname_order1)
    dict_top = {"topid_order":topid_order1,"topname_order":topname_order1}
    print(dict_top)

    print(topwinrate_list[topid_list.index("114")]) #查询胜率
    print(role_list[id_list.index("236")]) #查询定位




import time
from prettyprinter import pprint
f = open("C:/Users/myffa/Desktop/flask01/static/test.json", 'r')
cidName = json.loads(f.read())['cid-name']

f.close()

def fuc4():
    print(cidName['105'])

lanes = ["BOTTOM","TOPSOLO","MIDDLE", "JUNGLE", "SUPPORT"]
# def test():
#     resList = {}
#     for lane in lanes:
#         tmp = db.session.query(Champion_id.cid).filter(Champion_id.role == lane).order_by(Champion_id.appear.desc())
#         resList[lane] = list(map(lambda x:{"cid":x.cid, "cname":cidName[x.cid]}, tmp))
#
#     pprint(resList['BOTTOM'][0])


def test_2():
    dic = {}
    for lane in lanes:
        tmp = db.session.query(Champion_id).filter(Champion_id.role == lane)
        for item in map(lambda x:{"cid":x.cid, "cname":cidName[x.cid], "appear":float(x.appear), "role":x.role}, tmp):
            if item["cid"] in dic:
                if dic[item["cid"]]["appear"] < item['appear']:
                    dic[item["cid"]] = item
                else:
                    pass
            else:
                dic[item["cid"]] = item
    res = {}
    for cid in dic.keys():
        role = dic[cid]['role']
        if role in res:
            res[role].append(dic[cid])
        else:
            res[role] = [dic[cid]]
    for line in res.keys():
        res[line] = sorted(res[line], key=lambda x: x["appear"], reverse=True)

    pprint(res)
    for champion in res["TOPSOLO"]:
        pprint(champion["cid"])

def test_3():
    list =[]
    list=["11","22"]
    print(list)
if __name__ == '__main__':

    start_1 = time.time()
    test_3()
    print(time.time() - start_1)