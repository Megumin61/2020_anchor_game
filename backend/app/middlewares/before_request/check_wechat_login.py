from flask import session, request, current_app
import requests
import json
import traceback

from app.extends.error import HttpError


def check_wechat_login():
    if not session.get('openid'):
        resp = requests.get('https://hemc.100steps.net/2020/wechat/auth/user/openid', cookies=request.cookies)
        try:
            data = json.loads(resp.content)
            if 'openid' in data:
                session['openid'] = data.get('openid')
        except:
            current_app.logger.error(traceback.format_exc())
    if not session.get('openid'):
        raise HttpError(401, '请先登录微信')
