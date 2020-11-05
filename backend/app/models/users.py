import datetime

from app.extensions import db, Model


class User(Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    openid = db.Column(db.String(255), unique=True, nullable=False)
    remain = db.Column(db.Integer, default=3, comment='每日剩余抽奖次数')
    extra_remain = db.Column(db.Integer, default=0, comment='好友助力获得的')
    update_day = db.Column(db.Date, default=datetime.date.today())
    finish_time = db.Column(db.DateTime, default=None)
    info = db.Column(db.Boolean, default=False, comment='是否填写信息')

    @property
    def total_remain(self):
        return self.remain + self.extra_remain

    def reduce_remain(self):
        if self.remain > 0:
            self.remain = self.remain - 1
        else:
            self.extra_remain = self.extra_remain - 1
