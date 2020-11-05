from .check_wechat_login import check_wechat_login
from .is_ongoing import is_ongoing

# from .set_openid import set_openid

def before_request():
    # set_openid()
    is_ongoing()
    check_wechat_login()
