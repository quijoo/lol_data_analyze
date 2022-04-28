import json
f = open("C:/Users/herrn/Documents/PythonScripts/Scrapy/LoLAnalysis/name-cid.json", 'r')
data = json.loads(f.read())
f.close()
print(data['name-cid']['Aatrox'])
print(data['cid-name']['32'])