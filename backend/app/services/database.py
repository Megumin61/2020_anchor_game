import datetime
import typing
import random

from app.models import *
from app.extensions import db
from app.extends.error import HttpError


def _check_remain_update(user: User):
    if not user:
        raise HttpError(401, '请先登录微信')
    if user.update_day < datetime.date.today():
        user.update_day = datetime.date.today()
        user.remain = 3
        db.session.add(user)
        db.session.commit()


def _get_user_by_openid(openid: str) -> User:
    user: User = (
        User
            .query
            .filter_by(openid=openid)
            .first()
    )

    if user is None:
        user: User = User(openid=openid)
        db.session.add(user)
        db.session.flush()

        card: Card = Card(user_id=user.user_id)
        db.session.add(card)
        db.session.commit()
    else:
        _check_remain_update(user)

    return user


def _get_card_by_user_id(user_id: int) -> Card:
    return (
        Card
            .query
            .filter_by(user_id=user_id)
            .first()
    )


def _check_info() -> bool:
    return (
               Info
                   .query
                   .count()
           ) < 5


def _draw_card_return(index: int = random.randint(1, 8), card: bool = random.randint(1, 10) <= 6, finish: bool = False,
                      winner: bool = False,
                      info: bool = False) -> dict:
    return {
        'index': index,
        'card': card,
        'finish': finish,
        'winner': winner,
        'info': info
    }


def get_user_info(openid: str):
    user: User = _get_user_by_openid(openid)

    card: Card = _get_card_by_user_id(user.user_id)

    return {
        'remain': user.total_remain,
        'cards': card.to_list()
    }


def draw_card(openid: str):
    """
    抽卡
        1. 判断是否集齐 是->1.1 否->2
            1.1 是否已填写信息 是->finish = true, winner = true, info = true 否->1.1.1
                1.1.1 是否已有五人填写信息 是->finish = true, winner = false, info = false 否->finish = true, winner = true, info = false

        2. 是否是第一抽 是 ->3.1，修改first为false 否->3

        3 随机数判断是卡牌还是碎片 卡牌->3.1 碎片->3.2
            3.1 随机将一个未集齐的卡牌的碎片数改为3，抽完后判断是否集齐->1->集齐修改finish_time
            3.2 随机将一个未集齐的卡牌的碎片数加1，判断是否集齐->1->集齐修改finish_time

    """
    user: User = _get_user_by_openid(openid)

    if user.finish_time is not None:  # 已经集齐
        if user.info:  # 已经填写信息
            return _draw_card_return(finish=True, winner=True, info=True)
        else:
            if _check_info():  # 如果填写信息少于五人
                return _draw_card_return(finish=True, winner=True)
            else:  # 已有五人填写信息
                return _draw_card_return(finish=True)

    if user.total_remain == 0:
        raise HttpError(406, '抽卡次数已用完')

    card: Card = _get_card_by_user_id(user.user_id)

    if card.first:  # 第一抽
        card_id = random.randint(1, 8)
        is_card = True
        card.first = False
    else:
        not_collected: typing.List[dict] = card.get_not_collected()  # 还没集齐的卡牌
        card_id = not_collected[random.randint(0, len(not_collected) - 1)].get('index')  # 抽到的卡牌的index
        is_card = random.randint(1, 10) <= 6  # 是否抽到卡牌

    if is_card:  # 随机抽一张卡牌
        setattr(card, f'card{card_id}', 3)
    else:
        setattr(card, f'card{card_id}', getattr(card, f'card{card_id}') + 1)

    user.reduce_remain()

    db.session.commit()
    if len(card.get_not_collected()) == 0:  # 集齐了
        user.finish_time = datetime.datetime.now()
        db.session.commit()
        if _check_info():  # 如果填写信息少于五人
            return _draw_card_return(index=card_id, card=is_card, finish=True, winner=True)
        else:  # 已有五人填写信息
            return _draw_card_return(index=card_id, card=is_card, finish=True)
    else:
        return _draw_card_return(index=card_id, card=is_card)


def help_friend(user_id: int, openid: str):
    current_user: User = _get_user_by_openid(openid)
    be_helper: User = User.query.get(user_id)

    if current_user.user_id == be_helper.user_id:
        raise HttpError(403, '无法给自己助力')

    if be_helper is None:
        raise HttpError(404, '用户不存在')

    helper: Helper = (
        Helper
            .query
            .filter_by(helper_user_id=current_user.user_id, be_helper_user_id=be_helper.user_id,
                       date=datetime.date.today())
            .first()
    )
    if helper is not None:
        raise HttpError(406, '今日已帮助过该用户')

    be_helper.extra_remain = be_helper.extra_remain + 1
    helper: Helper = Helper(helper_user_id=current_user.user_id, be_helper_user_id=be_helper.user_id,
                            date=datetime.date.today())

    db.session.add(helper)
    db.session.commit()

    return {'message': '助力成功'}


def save_user_info(openid: str, name: str, tel: str, campus: str):
    user: User = _get_user_by_openid(openid)

    if user.finish_time is None:
        raise HttpError(403, '还未集齐卡牌')

    if user.info:
        raise HttpError(406, '已填写过信息')

    if not _check_info():
        raise HttpError(405, '已有五人集齐并填写信息')

    info: Info = (
        Info
            .query
            .filter_by(tel=tel)
            .first()
    )

    if info:
        raise HttpError(406, '该手机号已填写过信息')

    info: Info = Info(user_id=user.user_id, name=name, tel=tel, campus=campus)
    user.info = True
    db.session.add(info)
    db.session.commit()
    return {'message': '填写信息成功'}
