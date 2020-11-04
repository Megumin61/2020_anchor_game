import datetime

from app.extensions import db, Model


class Helper(Model):
    __tablename__ = 'helpers'

    helper_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    helper_user_id = db.Column(db.Integer)
    be_helper_user_id = db.Column(db.Integer)
    date = db.Column(db.Date, default=datetime.date.today())
