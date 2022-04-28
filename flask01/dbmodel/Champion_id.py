from config import db


class dbrole(db.Model):
    __tablename__ = "table_1"
    cid = db.Column(db.String(32), primary_key=True)
    win = db.Column(db.String(32))
    appear= db.Column(db.String(32))
    role= db.Column(db.String(32), primary_key=True)

