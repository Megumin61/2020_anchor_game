import typing

from app.extensions import db, Model


class Card(Model):
    __tablename__ = 'cards'

    card_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    first = db.Column(db.Boolean, default=True)

    card1 = db.Column(db.Integer, default=0)
    card2 = db.Column(db.Integer, default=0)
    card3 = db.Column(db.Integer, default=0)
    card4 = db.Column(db.Integer, default=0)
    card5 = db.Column(db.Integer, default=0)
    card6 = db.Column(db.Integer, default=0)
    card7 = db.Column(db.Integer, default=0)
    card8 = db.Column(db.Integer, default=0)

    def to_list(self) -> typing.List[dict]:
        return [
            {
                "collected": getattr(self, f'card{i}') == 3,
                "progress": getattr(self, f'card{i}')
            }
            for i in range(1, 9)
        ]

    def get_not_collected(self) -> typing.List[dict]:
        d = []
        for i in range(1, 9):
            if getattr(self, f'card{i}') < 3:
                d.append({'progress': getattr(self, f'card{i}'), 'index': i})
        return d
