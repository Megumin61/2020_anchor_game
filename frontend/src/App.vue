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
import { Dialog, Toast } from 'vant';
import { apis } from './api/apis';
import { g } from './config';
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
              .then(res => {
                Toast.success({ message: res.data.message });
              })
              .catch(err => {
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
  background-size: 100vw 100vh;
  min-height: 100vh;
  min-width: 100vw;
  background-attachment: fixed;
  background-repeat: no-repeat;
}
.bg1 {
  background-image: url('./assets/bg1.png');
}
.bg2 {
  background-image: url('./assets/bg2.png');
}
.loading_wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}
</style>
