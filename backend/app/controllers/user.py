from flask import Blueprint, session, request
import qrcode
from PIL import Image, PngImagePlugin, JpegImagePlugin
import io
import base64

from app.services import database
from app.extends.error import HttpError
from app.config import BaseConfig

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


@user_bp.route('/qrcode')
def get_qrcode():
    """
    获取二维码
    :return:
    """
    card_id: str = request.args.get('card_id')
    if card_id is None or card_id not in ['1', '2', '3', '4', '5', '6', '7', '8']:
        raise HttpError(400, 'card_id错误')

    bg: PngImagePlugin.PngImageFile = Image.open('./assets/bg.png')
    card: JpegImagePlugin.JpegImageFile = Image.open(f'./assets/cards/{card_id}.jpg')

    new_card = card.resize((1501, 2171), Image.ANTIALIAS)

    bg.paste(new_card, (518, 921))

    qr = qrcode.QRCode(border=1)

    user = database._get_user_by_openid(session.get('openid'))

    qr.add_data(BaseConfig.frontend_baseurl + '?uid=' + str(user.user_id))
    qr.make(fit=True)

    img_qr = qr.make_image(fill_color="#3f454b", back_color="#ffffff").resize((656, 656), Image.ANTIALIAS)
    bg.paste(img_qr, (1433, 3202))

    jpg_bg = bg.convert('RGB')

    buffered = io.BytesIO()
    jpg_bg.save(buffered, format='JPEG')

    img = base64.b64encode(buffered.getvalue())
    buffered.close()

    return {
        'data': 'data:image/jpeg;base64,' + str(img, encoding='utf-8')
    }
