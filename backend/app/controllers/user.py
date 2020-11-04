from flask import Blueprint, session, request

from app.services import database
from app.extends.error import HttpError

user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('')
def get_user_info():
    """
    获取用户信息
    :return:
    """

    return database.get_user_info(session.get('openid'))


@user_bp.route('/info', methods=['post'])
def save_user_info():
    """
    集齐后收集个人信息
    :return:
    """

    data: dict = request.get_json(force=True)

    name: str = data.get('name')
    if name is None:
        raise HttpError(400, '请填写姓名')
    tel: str = data.get('tel')
    if tel is None or not str(tel).isdigit() or len(str(tel)) != 11 or str(tel)[0] != '1':
        raise HttpError(400, '手机号填写错误')
    campus: str = data.get('campus')
    if campus is None:
        raise HttpError(400, '请填写校区')

    return database.save_user_info(session.get('openid'), name, tel, campus)


@user_bp.route('/qrcode/<int:card_id>')
def get_qrcode(card_id: int):
    """
    获取二维码

    :param card_id: 卡牌id
    :return:
    """

    pass
