from config import db

class Kill(db.Model):
    __table_args__ = {'extend_existing': True}
    __bind_key__ = 'two'
    __tablename__ = 'table_lx_1'

    lane = db.Column(db.String(255), primary_key=True)

    role = db.Column(db.String(255), primary_key=True)

    kills = db.Column(db.String(255))