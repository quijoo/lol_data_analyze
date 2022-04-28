import sqlite3
import csv
db = sqlite3.connect(database="C:/Users/herrn/Documents/PythonScripts/Scrapy/LoLAnalysis/LOL/data.db")
cursor = db.cursor()
sql = "SELECT * FROM items;"
li = cursor.execute(sql).fetchall()

f = open('data.csv','w', encoding="UTF-8")
writer = csv.writer(f)
for item in li:
    writer.writerow(item)
f.close()
db.close()