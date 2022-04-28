import requests
import json
from prettyprinter import pprint
def getTopTen():
    token = "RGAPI-f08ec09c-7583-4591-8b68-60f377517d30"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.58",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://developer.riotgames.com",
        "X-Riot-Token": token
    }
    url = "https://kr.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/CHALLENGER/I?page=1"
    res = requests.get(url = url, headers = headers)
    data = json.loads(res.text)[:10]
    for item in data:
        item.pop("veteran")
        item.pop("inactive")
        item.pop("freshBlood")
        item.pop("hotStreak")
    pprint(data)


if __name__ == "__main__":
    getTopTen()