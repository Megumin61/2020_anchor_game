from flask import Blueprint, session

from app.services import database

card_bp = Blueprint('card', __name__, url_prefix='/card')


@card_bp.route('', methods=['put'])
def draw_card():
    """
    抽卡
    :return:
    """

    return database.draw_card(session.get('openid'))
