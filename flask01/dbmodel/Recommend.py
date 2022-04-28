from config import db

class Recommend(db.Model):
    __tablename__ = "table_4"
    cid = db.Column(db.String(32), primary_key=True)
    cname = db.Column(db.String(32))
    #击杀
    kills = db.Column(db.String(32))
    #输出
    damage = db.Column(db.String(32))
    #坦度（承伤）
    damaged = db.Column(db.String(32))
    #助攻
    assist = db.Column(db.String(32))
    #治疗
    heal = db.Column(db.String(32))
    #生存（被杀）
    killed= db.Column(db.String(32))