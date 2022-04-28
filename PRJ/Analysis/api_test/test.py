# import requests
# import json

# import time
# def get(url):
#     header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.58",
#     "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
#     "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
#     "Origin": "https://developer.riotgames.com",
#     "X-Riot-Token": "RGAPI-f08ec09c-7583-4591-8b68-60f377517d30"
# }
#     res = requests.get(url = url, headers = header)
#     if res.status_code == 200:
#         return json.loads(res.text)
#     else:
#         return -1

# s = time.time()
# name = "Hide on bush"
# url_1 = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}".format(name)
# data_1 = get(url_1)
# if data_1 != -1:
#     account_id = data_1["accountId"]

# url_2 = "https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/{}?endIndex=10".format(account_id)
# data_2 = get(url_2)
# # print(item)
# if data_2 != -1:
#     sums = 0
#     for item in data_2['matches']:
#         data_tmp = get("https://kr.api.riotgames.com/lol/match/v4/matches/{}".format(item["gameId"]))
#         print(item["gameId"])
#         if data_tmp != -1:
#             for user in data_tmp["participants"]:
#                 if "highestAchievedSeasonTier" in user:
#                     sums += 1

#     print(sums)
# print(time.time()-s)

import json
from prettyprinter import pprint
filename = "C:/Users/herrn/Documents/Tencent Files/1085036164/FileRecv/ChampName.json"
f = open(filename, 'r')
data = json.loads(f.read())
li = list(data['data'].keys())
dic = data['data']
res  = {
    "name-cid":{},
    "cid-name":{}
}
for name in li:
    cid = dic[name]['key']
    res["name-cid"][name] = cid
    res["cid-name"][cid] = name
with open("C:/Users/herrn/Documents/Tencent Files/1085036164/FileRecv/name-cid.json", 'w') as f:
    f.write(json.dumps(res))
