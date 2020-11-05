export let g = {
  _showLoading: 0,
  _showTips: 0,
  showLoading() {
    this._showLoading++;
  },
  hideLoading() {
    if (this._showLoading > 0) {
      this._showLoading--;
    }
  },
  showTips() {
    this._showTips++;
  },
  hideTips() {
    if (this._showTips > 0) {
      this._showTips--;
    }
  },
};

export let sentences = [
  '顺生而行尽破朦胧，爱上天上人间',
  '力量本就存在无数表现形式，生命亦具有无限的可能',
  '舞台是一个什么样的地方？灯光、掌声、短暂但热烈的爱',
  '生活就像海洋，只有意志坚强的人才能到达彼岸',
];

// export const applicationFormURL = 'https://zekaio.cn/2020/anchor/form';
// export const baseURL = 'https://zekaio.cn/2020/anchor/game/api';
// export const wechatBaseURL = 'https://zekaio.cn/2020/wechat';

export const applicationFormURL = 'https://hemc.100steps.net/2020/anchor/form';
export const baseURL = 'https://hemc.100steps.net/2020/anchor/game/api';
export const wechatBaseURL = 'https://hemc.100steps.net/2020/wechat';

// export const baseURL = 'http://localhost:5000';
export const title = '寻声人';
export const link = 'https://hemc.100steps.net/2020/anchor/game';
export const imgUrl = 'https://hemc.100steps.net/2020/anchor/game/share.png';
