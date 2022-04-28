from config import db

class Champdata(db.Model):

    __table_args__ = {'extend_existing': True}
    __bind_key__ = 'two'
    __tablename__ = "table_rate"

    cid = db.Column(db.String(255), primary_key=True)

    rank = db.Column(db.String(255), primary_key=True)

    winrate = db.Column(db.String(255))

    appearancerate = db.Column(db.String(255))