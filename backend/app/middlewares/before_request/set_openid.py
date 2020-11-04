"""
仅供测试
"""
from flask import session
import uuid


def set_openid():
    if session.get('openid') is None:
        session['openid'] = str(uuid.uuid4())
