from app.extensions import db, Model


class Info(Model):
    __tablename__ = 'infos'

    info_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    name = db.Column(db.String(255))
    tel = db.Column(db.String(255), unique=True)
    campus = db.Column(db.String(255))
