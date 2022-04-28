# import requests
# from lxml import etree


# gameId = "1982187393"
# url = "https://br1.api.riotgames.com/lol/match/v4/matches/{}?".format(gameId)
token = "RGAPI-f1c6d16a-683d-457f-8695-2bcec1569d05"
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.56",
#     "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
#     "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
#     "Origin": "https://developer.riotgames.com",
#     "X-Riot-Token": token
# }

# response = requests.get(url, headers = header)
# print(response.text)



import random

import cassiopeia as cass

cass.set_riot_api_key(token)  # This overrides the value set in your configuration/settings.
cass.set_default_region("NA")

# summoner = cass.get_summoner(name="Kalturi")
# print("{name} is a level {level} summoner on the {region} server.".format(name=summoner.name,
#                                                                           level=summoner.level,
#                                                                           region=summoner.region))

# champions = cass.get_champions()
# random_champion = random.choice(champions)
# print("He enjoys playing champions such as {name}.".format(name=random_champion.name))

# challenger_league = cass.get_challenger_league(queue=cass.Queue.ranked_solo_fives)
# best_na = challenger_league[0].summoner
# print("He's not as good as {name} at League, but probably a better python programmer!".format(name=best_na.name))
res = cass.get_summoner()
print(res)