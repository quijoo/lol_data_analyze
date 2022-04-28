from config import db

class Match(db.Model):
    __table_args__ = {'extend_existing': True}
    __bind_key__ = 'two'
    __tablename__ = 'items'

    # 玩家id和游戏id
    gid = db.Column(db.String(32), primary_key=True)
    pid = db.Column(db.String(32), primary_key=True)

    # 英雄ID
    cid = db.Column(db.String(32))

    # 位置
    lane = db.Column(db.String(32))