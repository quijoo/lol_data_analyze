import json
import requests
import time
f = open("champ.json", 'r', encoding='UTF-8');
data = f.read()
f.close()
data = json.loads(data)
li = list(data['data'].keys())
dic = data['data']
print()
url = 'https://opgg-static.akamaized.net/images/lol/champion/{}.png'
# for i in li:
# item = "Aatrox"
headers = headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.58",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        }
for item in li:
    name = dic[item]['key']
    res = requests.get(url.format(item), headers=headers)
    with open('champImg/{}.png'.format(name), 'wb') as f:
        f.write(res.content)
    f.close()
    print("[INFO] {}, <{}>".format(item, res.status_code))
    time.sleep(2)
