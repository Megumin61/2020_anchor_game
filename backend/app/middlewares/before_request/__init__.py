from .check_wechat_login import check_wechat_login
from .is_ongoing import is_ongoing


def before_request():
    is_ongoing()
    check_wechat_login()
