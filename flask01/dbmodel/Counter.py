from config import db


class Counter(db.Model):
    __tablename__ = "table_2"
    cid = db.Column(db.String(32), primary_key=True)
    killcounter =db.Column(db.String(32))
    killedcounter = db.Column(db.String(32))
    csdiffer =db.Column(db.String(32))
    cwin = db.Column(db.String(32))
    # appear= db.Column(db.String(32))
    versusid = db.Column(db.String(32), primary_key=True)