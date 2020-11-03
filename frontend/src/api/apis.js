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
};
