from config import db


class PersonalAbility(db.Model):
    __tablename__ = "table_dirty"
    gid = db.Column(db.String(32), primary_key=True)
    pid = db.Column(db.String(32), primary_key=True)
    #玩家名
    name = db.Column(db.String(32))
    #击杀
    totalkill = db.Column(db.String(32))
    #输出
    damage = db.Column(db.String(32))
    #坦度（承伤）
    damagetaken = db.Column(db.String(32))
    #助攻
    totalsupport = db.Column(db.String(32))
    #治疗
    heal = db.Column(db.String(32))
    #生存（被杀）
    totalkilled= db.Column(db.String(32))
