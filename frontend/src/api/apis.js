import { instance, wxInstance } from './config';
instance;
export let apis = {
  // 获取jssdk配置信息
  wxconfig: () => {
    return wxInstance({
      url: '/offiaccount/jssdk',
      method: 'post',
      data: { url: window.location.href.split('#')[0] },
    });
  },

  /**
   * 获取用户信息
   * GET /user
   *
   * @returns {Number} remain 剩余抽奖次数
   * @returns {Object[]} cards 每个卡牌的信息
   * @returns {Boolean} card.collected 是否集齐
   * @returns {Number} card.progress 进度
   */
  getUserInfo: () => {
    return instance({
      url: '/user',
      method: 'get',
    });
  },

  /**
   * 集齐后收集用户信息
   * POST /user/info
   *
   * @param name 姓名
   * @param tel 手机号
   * @param campus 校区
   *
   * @throws 400 信息填写错误
   * @throws 403 还未集齐
   * @throws 405 已有五个人集齐
   * @throws 406 已填写过信息
   */
  saveUserInfo: (name, tel, campus) => {
    return instance({
      url: '/user/info',
      method: 'post',
      data: { name, tel, campus },
    });
  },
  /**
   * 获取二维码
   * GET /user/qrcode?card_id={card_id}
   *
   * @returns {String} data base64编码的图片
   *
   * @throws 400 card_id无效
   */
  getQRCode: (card_id) => {
    return instance({
      url: `/user/qrcode?card_id=${card_id}`,
      method: 'get',
    });
  },

  /**
   * 抽卡
   * PUT /card
   *
   * @returns {Boolean} card 是否是卡牌
   * @returns {Number} index 卡牌编号
   * @returns {Boolean} finish 是否已完成
   * @returns {Boolean} winner 是否是前五个集齐的
   * @returns {Boolean} info 是否填写了信息
   *
   * @throws 406 抽奖次数已用完
   */
  drawCard: () => {
    return instance({
      url: '/card',
      method: 'put',
    });
  },

  /**
   * 助力
   * PUT /helper
   *
   * @param user_id 用户id
   *
   * @throws 400 user_id无效
   * @throws 403 无法给自己助力
   * @throws 404 用户不存在
   * @throws 406 今日已为该用户助力
   */
  helpFriend: (user_id) => {
    return instance({
      url: '/helper',
      method: 'put',
      data: { user_id },
    });
  },
};
