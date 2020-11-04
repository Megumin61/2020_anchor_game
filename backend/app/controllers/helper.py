from flask import Blueprint, session, request

from app.services import database
from app.extends.error import HttpError

helper_bp = Blueprint('helper', __name__, url_prefix='/helper')


@helper_bp.route('', methods=['put'])
def help_friend():
    """
    助力
    :return:
    """

    user_id = request.get_json(force=True).get('user_id')

    if user_id is None:
        raise HttpError(400, '获取user_id失败，请重新扫码进入')

    return database.help_friend(user_id=user_id, openid=session.get('openid'))
