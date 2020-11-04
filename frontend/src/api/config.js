import axios from 'axios';
import { g } from '../config';
import { Toast } from 'vant';

const baseURL = 'http://localhost:5000';
// const baseURL = 'https://zekaio.cn/2020/anchor/game/api'
const wechatBaseURL = 'https://hemc.100steps.net/2020/wechat';

// axios配置
export const instance = axios.create({
  baseURL,
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: true,
});

export const wxInstance = axios.create({
  baseURL: wechatBaseURL,
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: true,
});

function defaultSuccFunc(res) {
  return Promise.resolve(res);
}

function defaultFailFunc(err) {
  if (!err.response) {
    Toast.fail({
      message: '服务器无法响应，请稍后再试',
    });
  } else {
    // err.response.data
    switch (err.response.status) {
      // 未登录
      case 401:
        console.log(encodeURIComponent(window.location.href));
        // window.location.href = `${wechatBaseURL}/auth?state=${encodeURIComponent(
        //   window.location.href
        // )}`;
        Toast.fail({
          message: '请先登录',
        });
        break;
      // 不在活动时间
      case 410:
        Toast.fail({
          message: err.response.data.message,
        });
        break;
      // 服务器错误
      case 500:
        Toast.fail({
          message: '服务器错误，请稍后再试',
        });
        break;
      default:
        return Promise.reject(err);
    }
  }
  return new Promise(() => {});
}

function succFunc(res) {
  g.hideLoading();
  return defaultSuccFunc(res);
}

function failFunc(err) {
  g.hideLoading();
  return defaultFailFunc(err);
}

instance.interceptors.response.use(succFunc, failFunc);
wxInstance.interceptors.response.use(defaultSuccFunc, defaultFailFunc);

instance.interceptors.request.use(
  (config) => {
    g.showLoading();
    if (/get/i.test(config.method)) {
      config.params = config.params || {};
      config.params.timestamp = new Date().getTime();
    }
    return config;
  },
  (err) => {
    return Promise.reject(err);
  }
);
