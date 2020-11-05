<template>
  <div id="app">
    <div class="up">
      <van-overlay class="up" :show="Boolean(g._showLoading)">
        <div class="loading_wrapper up" @click.stop>
          <van-loading size="50px" text-size="16px" vertical
            >加载中...</van-loading
          >
        </div>
      </van-overlay>
      <van-notice-bar
        v-show="Boolean(g._showTips)"
        style="text-align:center; z-index: 10000; position: fixed; top: 0; left: 0; width: 100vw"
      >
        长按保存图片
      </van-notice-bar>
    </div>

    <router-view> </router-view>
  </div>
</template>

<script>
import wx from 'weixin-js-sdk';
import { Dialog, Toast } from 'vant';
import { apis } from './api/apis';
import { g, title, link, imgUrl } from './config';
import { preload } from './preload';

export default {
  name: 'App',
  data: () => {
    return { g };
  },
  async mounted() {
    await preload();
    apis.getUserInfo();
    if (this.$route.name == 'index' && this.$route.query.uid) {
      let user_id = this.$route.query.uid;
      Dialog.confirm({
        message: '是否要为你的好友助力',
        beforeClose: (action, done) => {
          if (action === 'confirm') {
            // 助力
            apis
              .helpFriend(user_id)
              .then((res) => {
                Toast.success({ message: res.data.message });
              })
              .catch((err) => {
                Toast.fail({
                  message:
                    err.response.data.message || `未知错误${err.response.data}`,
                });
              })
              .finally(() => {
                done();
              });
          } else {
            done();
          }
        },
      })
        .then(() => {})
        .catch(() => {});
    } else {
      if (this.$route.name == null) {
        this.$router.push({
          path: '/index',
        });
      }
    }

    // 获取jssdk需要的配置信息

    apis.wxconfig().then((res) => {
      wx.ready(() => {
        wx.checkJsApi({
          jsApiList: [
            'updateTimelineShareData',
            'updateAppMessageShareData',
            'startRecord',
            'stopRecord',
          ],
          success: () => {
            console.log('接口可用');
          },
        });

        wx.onMenuShareTimeline({
          title, // 分享标题
          link, // 分享链接，该链接域名必须与当前企业的可信域名一致
          imgUrl, // 分享图标
          success: function() {
            // 用户确认分享后执行的回调函数
          },
          cancel: function() {
            // 用户取消分享后执行的回调函数
          },
        });
        wx.onMenuShareAppMessage({
          title, // 分享标题
          desc: '', // 分享描述
          link, // 分享链接，该链接域名必须与当前企业的可信域名一致
          imgUrl, // 分享图标
          type: 'link', // 分享类型,music、video或link，不填默认为link
          success: function() {
            // 用户确认分享后执行的回调函数
          },
          cancel: function() {
            // 用户取消分享后执行的回调函数
          },
        });
        wx.updateTimelineShareData({
          title,
          link, // 分享链接，该链接域名或路径必须与当前页面对应的公众号JS安全域名一致
          imgUrl,
          success: function() {
            console.log('success');
            // 设置成功
          },
        });

        wx.updateAppMessageShareData({
          title, // 分享标题
          desc: '', // 分享描述
          link, // 分享链接，该链接域名或路径必须与当前页面对应的公众号JS安全域名一致
          imgUrl,
          success: function() {
            console.log('success');
            // 设置成功
          },
        });
      });
      wx.config({
        debug: false,
        appId: res.data.appid,
        timestamp: res.data.timestamp,
        nonceStr: res.data.noncestr,
        signature: res.data.signature,
        jsApiList: [
          'updateTimelineShareData',
          'updateAppMessageShareData',
          'startRecord',
          'stopRecord',
        ],
      });
    });
  },
};
</script>

<style>
body {
  margin: 0;
  padding: 0;
  min-height: 100vh;
  min-width: 100vw;
}
.up {
  z-index: 10000;
}
.page {
  min-height: 100vh;
  min-width: 100vw;
}
.bg1::before {
  background-image: url('./assets/bg1.png');
  content: ' ';
  background-size: 100vw 100vh;
  background-repeat: no-repeat;
  position: fixed;
  z-index: -1;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}
.bg2::before {
  background-image: url('./assets/bg2.png');
  content: ' ';
  background-size: 100vw 100vh;
  background-repeat: no-repeat;
  position: fixed;
  z-index: -1;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}
.loading_wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}
</style>
