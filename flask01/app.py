import requests
from flask import Flask, request, render_template, jsonify, url_for, session, make_response, redirect
from flask_sqlalchemy import SQLAlchemy
import json
import random
from config import db
from dbmodel.Recommend import Recommend
from dbmodel.PersonalAbility import PersonalAbility
from dbmodel.Counter import Counter
from dbmodel.role import dbrole
from dbmodel.Match import Match
from dbmodel.Champdata import Champdata
from dbmodel.Kill import Kill
from riotwatcher import LolWatcher, ApiError
from scipy.stats import norm

# 主页额外的库
from riotwatcher import LolWatcher, ApiError
from werkzeug.utils import secure_filename
import pymysql

app = Flask(__name__)
app.secret_key = 'djstla'
app.config['DEBUG'] = True

# 全局变量

global result

# 周免英雄id
freeChampionIds = []

# 周免英雄 key、name、tag，
ChampIdAndAndNameAndTag = []

faker = []

f = open("./static/json/test.json", 'r')
data = f.read()
cidName = json.loads(data)['cid-name']
nameCid = json.loads(data)['name-cid']
f.close()

f1 = open("./static/json/ChampName.json", 'r')
#E:\Spring\flask01\flask01\static\ChampName.json   "data"
nameInfo = json.loads(f1.read())['data']
f1.close()


@app.route("/")
def index0():
    return render_template("/html/moban/index.html")


@app.route("/index")
def gotoindex():
    return render_template("/html/moban/index.html")


@app.route("/tables")
def gototables():
    return render_template("/html/moban/tables.html")


@app.route("/charts")
def gotocharts():
    return render_template("/html/moban/charts.html")


@app.route("/forms")
def gotoforms():
    dic = {}
    lanes = ["BOTTOM", "TOPSOLO", "MIDDLE", "JUNGLE", "SUPPORT"]
    for lane in lanes:
        tmp = db.session.query(dbrole).filter(dbrole.role == lane)
        for item in map(lambda x: {"cid": x.cid, "cname": cidName[x.cid], "appear": float(x.appear), "role": x.role},
                        tmp):
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

    Tname0 = res["TOPSOLO"][0]["cname"]
    Tname1 = res["TOPSOLO"][1]["cname"]
    Tname2 = res["TOPSOLO"][2]["cname"]
    Tname3 = res["TOPSOLO"][3]["cname"]

    return render_template("/html/moban/forms.html", clist=res, Tname0=Tname0, Tname1=Tname1, Tname2=Tname2,
                           Tname3=Tname3)


@app.route("/conter", methods=["GET", "POST"])
def gotoconter():
    dic = {}
    lanes = ["BOTTOM", "TOPSOLO", "MIDDLE", "JUNGLE", "SUPPORT"]
    for lane in lanes:
        tmp = db.session.query(dbrole).filter(dbrole.role == lane)
        for item in map(lambda x: {"cid": x.cid, "cname": cidName[x.cid], "appear": float(x.appear), "role": x.role},
                        tmp):
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
    id = request.args.get("id")

    versusList = res[dic[id]['role']]
    versusList.remove(dic[id])
    tmp1 = db.session.query(Counter).filter(Counter.cid == id).filter(Counter.versusid == versusList[0]["cid"])
    tmp2 = db.session.query(Counter).filter(Counter.cid == versusList[0]["cid"]).filter(Counter.versusid == id)
    counter = list(tmp1)[0]
    counter2 = list(tmp2)[0]
    return render_template("/html/moban/conter.html", versuslist=versusList, current=dic[id],
                           versus={
                               "cid": counter.cid,
                               "kill": round(float(counter.killcounter), 2),
                               "killed": round(float(counter.killedcounter), 2),
                               "cs": round(float(counter.csdiffer), 2),
                               "cwin": round(float(counter.cwin), 2),
                               "kdr": round(float(counter.killcounter) / (
                                       float(counter.killcounter) + float(counter.killedcounter)), 2)},
                           versus2={
                               "cid": counter2.cid,
                               "kill": round(float(counter2.killcounter), 2),
                               "killed": round(float(counter2.killedcounter), 2),
                               "cs": round(float(counter2.csdiffer), 2),
                               "cwin": round(float(counter2.cwin), 2),
                               "kdr": round(float(counter2.killcounter) / (
                                       float(counter2.killcounter) + float(counter2.killedcounter)), 2)}
                           )


@app.route("/counter/refresh", methods=["POST", "GET"])
def gcounter_refresh():
    cid = request.values.get("cid")
    versusid = request.values.get("versusid")
    # print(cid, versusid)
    info_1 = list(db.session.query(Counter).filter(Counter.cid == cid).filter(Counter.versusid == versusid))[0]
    info_2 = list(db.session.query(Counter).filter(Counter.cid == versusid).filter(Counter.versusid == cid))[0]
    data = {
        "current": {
            "cid": info_1.cid,
            "cwin": round(float(info_1.cwin), 2),
            "kill": round(float(info_1.killcounter), 2),
            "killed": round(float(info_1.killedcounter), 2),
            "cs": round(float(info_1.csdiffer), 2),
            "kdr": round(float(info_1.killcounter, ) / (float(info_1.killcounter) + float(info_1.killedcounter)), 2)
        },
        "versus": {
            "cname": cidName[info_2.cid],
            "cid": info_2.cid,
            "cwin": round(float(info_2.cwin), 2),
            "kill": round(float(info_2.killcounter), 2),
            "killed": round(float(info_2.killedcounter), 2),
            "cs": round(float(info_2.csdiffer), 2),
            "kdr": round(float(info_2.killcounter, ) / (float(info_2.killcounter) + float(info_2.killedcounter)), 2)
        },
    }
    return jsonify(data)


@app.route("/search", methods={"GET", "POST"})
def gotosearch():
    # 获取玩家昵称
    name = request.form.get("search") if request.args.get("search") == None else request.args.get("search")
    # 判断数据库里是否有该玩家
    data = db.session.query(PersonalAbility).filter(PersonalAbility.name == name)
    # 总场数
    num = len(list(data))
    if num == 0:
        return jsonify("no user")
    # 初始化
    a, b, c, d, e, f = 0, 0, 0, 0, 0, 0
    # 正态分布算能力图，均值和方差
    avg = [6.212772507904809, 91120.66245631552, 20685.11359349864, 9.492011982026959, 5222.794727353415,
           6.234986409274977]
    dif = [5.193065862482734, 63840.320019869854, 11659.338050001978, 7.8115649483243, 5963.011507339207,
           3.825938906129348]
    # 算出个人均值
    for item in data:
        a = a + int(item.totalkill)
        b = b + int(item.damage)
        c = c + int(item.damagetaken)
        d = d + int(item.totalsupport)
        e = e + int(item.heal)
        f = f + int(item.totalkilled)
    a = a / num
    b = b / num
    c = c / num
    d = d / num
    e = e / num
    f = f / num
    # 计算正太分布比例
    a1 = norm.cdf((a - avg[0]) / dif[0]) * 100
    b1 = norm.cdf((b - avg[1]) / dif[1]) * 100
    c1 = norm.cdf((c - avg[2]) / dif[2]) * 100
    d1 = norm.cdf((d - avg[3]) / dif[3]) * 100
    e1 = norm.cdf((e - avg[4]) / dif[4]) * 100
    f1 = 100 - (norm.cdf((f - avg[5]) / dif[5]) * 100)

    cdata = db.session.query(Recommend).all()
    sum = []
    a2, b2, c2, d2, e2, f2 = 0, 0, 0, 0, 0, 0
    j = 0
    dict = {}
    for i in cdata:
        a2 = norm.cdf(float(i.kills)) * 100

        b2 = norm.cdf(float(i.damage)) * 100
        c2 = norm.cdf(float(i.damaged)) * 100
        d2 = norm.cdf(float(i.assist)) * 100
        e2 = norm.cdf(float(i.heal)) * 100
        f2 = 100-norm.cdf(float(i.killed)) * 100
        sum.append(abs(a2 - a1) + abs(b2 - b1) + abs(c2 - c1) + abs(d2 - d1) + abs(e2 - e1) + abs(f2 - f1))
        dict[i.cname] = sum[j]

        j = j + 1
    key1 = sorted(dict, key=dict.get, reverse=True)[147]
    key2 = sorted(dict, key=dict.get, reverse=True)[146]
    key3 = sorted(dict, key=dict.get, reverse=True)[0]
    data2 = db.session.query(Recommend).filter(Recommend.cname == key1)
    lis2 = []
    for i in data2:
        lis2 = [norm.cdf(float(i.kills)) * 100, norm.cdf(float(i.damage)) * 100, norm.cdf(float(i.damaged)) * 100, \
                norm.cdf(float(i.assist)) * 100, norm.cdf(float(i.heal)) * 100, 100-norm.cdf(float(i.killed)) * 100]

    data3 = db.session.query(Recommend).filter(Recommend.cname == key2)
    lis3 = []
    for i in data3:
        lis3 = [norm.cdf(float(i.kills)) * 100, norm.cdf(float(i.damage)) * 100, norm.cdf(float(i.damaged)) * 100, \
                norm.cdf(float(i.assist)) * 100, norm.cdf(float(i.heal)) * 100, 100-norm.cdf(float(i.killed)) * 100]

    data4 = db.session.query(Recommend).filter(Recommend.cname == key3)
    lis4 = []
    for i in data4:
        lis4 = [norm.cdf(float(i.kills)) * 100, norm.cdf(float(i.damage)) * 100, norm.cdf(float(i.damaged)) * 100, \
                norm.cdf(float(i.assist)) * 100, norm.cdf(float(i.heal)) * 100, 100-norm.cdf(float(i.killed)) * 100]
    # 传递参数列表，名字
    return render_template("/html/moban/search.html", lis=[a1, b1, c1, d1, e1, f1], sname=name, cname1=key1, lis2=lis2,
                           cname2=key2, lis3=lis3, cname3=key3, lis4=lis4)


# 主页---------------------------------------------------------------------------------------------------------


@app.route("/getSummoner", methods=["GET", "POST"])
def getSummoner():
    with open('./static/json/rank.json', 'r') as temp_file:
        result = json.load(temp_file)
    return json.dumps(result)


@app.route("/getfromSQL", methods=["GET", "POST"])
def getfromSQL():
    if request.method == 'POST':
        return request.form['name']


# 计算哪些位置场均击杀最高
@app.route("/killrate")
def killrate():
    getresult = Kill.query.all()
    count = {'TOP': 0, 'JUNGLE': 182435, 'MIDDLE': 0, 'BOTTOM_CARRY': 0, 'BOTTOM_SUPPORT': 0}
    for item in getresult:
        if item.lane == 'TOP':
            count['TOP'] = count['TOP'] + int(item.kills)
        elif item.lane == 'JUNGLE':
            count['JUNGLE'] = count['JUNGLE'] + int(item.kills)
        elif item.lane == 'MIDDLE':
            count['MIDDLE'] = count['MIDDLE'] + int(item.kills)
        elif item.lane == 'BOTTOM' and item.role == 'DUO_CARRY':
            count['BOTTOM_CARRY'] = count['BOTTOM_CARRY'] + int(item.kills)
        elif item.lane == 'BOTTOM' and item.role == 'DUO_SUPPORT':
            count['BOTTOM_SUPPORT'] = count['BOTTOM_SUPPORT'] + int(item.kills)
        else:
            print("error")
    return jsonify(count)


# 返回周免英雄
@app.route("/championFree")
def championFree():
    global ChampIdAndAndNameAndTag
    with open('./static/json/free.json', 'r') as temp_file:
        ChampIdAndAndNameAndTag = json.load(temp_file)
    return json.dumps(ChampIdAndAndNameAndTag)


# 返回周免英雄胜率
@app.route("/getWeekWinRate", methods=['GET', 'POST'])
def getWeekWinRate():
    getNumber = []

    temp = Champdata.query.all()
    temp2 = request.form.get('data')
    mylist = json.loads(temp2)

    temp3 = []
    for y in mylist:
        temp3.append(y["Champid"])

    # print(temp3)

    countnum = 0
    for i in temp3:
        win = 0
        appear = 0
        cname = ''
        winrate = 0
        for item in temp:
            if int(item.cid) == i:
                win = win + int(item.winrate)
                appear = appear + int(item.appearancerate)
        # print(ChampIdAndAndNameAndTag)
        winrate = win * 100 / appear
        cname = ChampIdAndAndNameAndTag[countnum]['Champname']
        getNumber.append({'cid': i, 'cname': cname, 'winrate': winrate})
        countnum = countnum + 1
    return json.dumps(getNumber)


# 改变服务器
@app.route("/getchangeFWQ", methods=['POST', 'GET'])
def getchangeFWQ():
    if request.form['fwq'] == 'kr':
        with open('./static/json/rank.json', 'r') as temp_file:
            result = json.load(temp_file)
        return json.dumps(result)
    elif request.form['fwq'] == 'eun1':
        with open('./static/json/eun1.json', 'r') as temp_file:
            result = json.load(temp_file)
        return json.dumps(result)
    elif request.form['fwq'] == 'jp1':
        with open('./static/json/jp1.json', 'r') as temp_file:
            result = json.load(temp_file)
        return json.dumps(result)
    else:
        return "error"


# 排名写入json文件
@app.route("/writejson", methods=["GET", "POST"])
def writejson():
    token = "RGAPI-bbeb7be1-050c-42d3-b6b2-4ed010e19c40"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.58",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com",
        "X-Riot-Token": token
    }
    url = "https://jp1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/CHALLENGER/I?page=1"
    res = requests.get(url=url, headers=headers)
    result = json.loads(res.text)[:12]
    for item in result:
        item.pop("veteran")
        item.pop("inactive")
        item.pop("freshBlood")
        item.pop("hotStreak")

    # print(result)
    temp = json.dumps(result)
    with open('./static/json/jp1.json', 'w') as json_file:
        json_file.write(temp)

    return "success"


@app.route("/getSumWinRate", methods=["GET", "POST"])
def getSumWinRate():
    with open('./static/json/sumwinrate.json', 'r') as temp:
        temp2 = json.load(temp)

    return json.dumps(temp2)


# 将周免英雄信息写入json
@app.route("/getfreeSumfromAPI")
def getgetfreeSumfromAPI():
    lol_watcher=LolWatcher("RGAPI-aa31eeb0-5d39-4441-8e57-5e96c7fe46b7")
    # 区域
    region = 'KR'

    championFreeResult = lol_watcher.champion.rotations(region=region)

    freeChampionIds = championFreeResult['freeChampionIds']

    with open('./static/json/ChampName.json', 'r') as fp:
        ChampName = json.load(fp)

    temp1 = ChampName['data']

    # 找出周免英雄的名字和定位
    for i in freeChampionIds:
        for j in temp1:
            if int(temp1[j]['key']) == i:
                ChampIdAndAndNameAndTag.append(
                    {'Champid': i, 'Champname': temp1[j]['name'], 'Champtag': temp1[j]['tags'][0]})

    with open('./static/json/free.json', 'w') as file_free:
        file_free.write(json.dumps(ChampIdAndAndNameAndTag))

    return render_template("html/moban/index.html", result="suucess")


# 主页---------------------------------------------------------------------------------------------------------


# 英雄排名------------------------------------------------------------------------------------------------------



@app.route("/Test",methods = ["POST", "GET"])
def refresh_appear():
    data = request.form.get("data")
    # str = [ win,appear,role,kills,killed,heal,damage,damaged ,assist]
    print(data)
    if data=="win":
        l = dbrole.query.order_by(dbrole.win.desc()).limit(10).all()
    if data=="appear":
        l = dbrole.query.order_by(dbrole.appear.desc()).limit(10).all()
    if data=="kills":
        l = dbrole.query.order_by(dbrole.kills.desc()).limit(10).all()
    if data=="killed":
        l = dbrole.query.order_by(dbrole.killed.desc()).limit(10).all()
    if data=="heal":
        l = dbrole.query.order_by(dbrole.heal.desc()).limit(10).all()
    if data=="damage":
        l = dbrole.query.order_by(dbrole.damage.desc()).limit(10).all()
    if data=="damaged":
        l = dbrole.query.order_by(dbrole.damaged.desc()).limit(10).all()
    if data=="assist":
        l = dbrole.query.order_by(dbrole.assist.desc()).limit(10).all()
    data_id =list(map(lambda x:x.cid,l))
    name = list(map(lambda x:cidName[x], data_id))
    print(name[0])
    #name_top = name[0]
    name_alldata = nameInfo[name[0]]
    name_story = name_alldata['blurb']
    name_value = name_alldata['info']
    #{'attack': 6, 'defense': 2, 'magic': 6, 'difficulty': 9}
    name_attack = name_value['attack']
    name_defense = name_value['defense']
    name_magic = name_value['magic']
    name_difficulty = name_value['difficulty']
    data_appear = list(map(lambda x:x.appear,l))
    data_appear = list(map(float, data_appear))
    data_appear = ['{:.4f}'.format(i) for i in data_appear]
    data_win = list(map(lambda x:x.win,l))
    data_win = list(map(float, data_win))
    data_win = ['{:.4f}'.format(i) for i in data_win]
    data_kills = list(map(lambda x: x.kills, l))
    data_kills = list(map(float, data_kills))
    data_kills = ['{:.2f}'.format(i) for i in data_kills]
    data_killed = list(map(lambda x: x.killed, l))
    data_killed = list(map(float, data_killed))
    data_killed = ['{:.2f}'.format(i) for i in data_killed]
    data_heal = list(map(lambda x: x.heal, l))
    data_heal = list(map(float, data_heal))
    data_heal = ['{:.2f}'.format(i) for i in data_heal]
    data_damage = list(map(lambda x: x.damage, l))
    data_damage = list(map(float, data_damage))
    data_damage = ['{:.2f}'.format(i) for i in data_damage]
    data_damaged = list(map(lambda x: x.damaged, l))
    data_damaged = list(map(float, data_damaged))
    data_damaged = ['{:.2f}'.format(i) for i in data_damaged]
    data_assist = list(map(lambda x: x.assist, l))
    data_assist = list(map(float, data_assist))
    data_assist = ['{:.2f}'.format(i) for i in data_assist]
    data_role = list(map(lambda x:x.role,l))
    print(data_id)
    return jsonify({"sort_by": data,"cids":data_id,"name": name ,"a":data_appear,"win": data_win,"kills": data_kills,"killed": data_killed,
                    "heal": data_heal,"damage": data_damage,"damaged": data_damaged,"assist": data_assist,"r":data_role,
                    "stroy":name_story,"attack":name_attack,"defense":name_defense,"magic":name_magic,"difficulty":name_difficulty,})

# 英雄排名------------------------------------------------------------------------------------------------------
@app.route("/test_post", methods={"GET", "POST"})
# @app.route("/test_post/nn", methods={"GET", "POST"})
def search():
    # sql
    # 获取 search 的值
    cname = request.form.get("search")
    if cname == "":
        return redirect(url_for("gotocharts"))
    # 通过 cname 查找 cid ， 再通过cid搜索
    try:
        cid = nameCid[cname]
    except:
        return redirect(url_for("gotocharts"))
    data = db.session.query(Recommend).filter(Recommend.cid == cid).all()
    if len(data) == 0:
        return redirect(url_for("gotocharts"))
    data = [data[0].kills, data[0].killed, data[0].damage, data[0].damaged, data[0].heal, data[0].assist]
    data = list(map(lambda x:round(norm.cdf(float(x))*100), data))
    data.append(int(cid))
    return render_template("html/moban/charts.html", lis=data,cname=request.form.get("search"))

if __name__ == '__main__':
    app.debug = True
    app.run()
