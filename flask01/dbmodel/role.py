from config import db

class dbrole (db.Model):
    __tablename__ = "table_5"
    cid = db.Column(db.String(32), primary_key=True)
    win = db.Column(db.String(32))
    appear = db.Column(db.String(32))
    role = db.Column(db.String(32), primary_key=True)
    kills = db.Column(db.String(32))
    killed = db.Column(db.String(32))
    damage = db.Column(db.String(32))
    damaged = db.Column(db.String(32))
    assist = db.Column(db.String(32))
    heal = db.Column(db.String(32))

