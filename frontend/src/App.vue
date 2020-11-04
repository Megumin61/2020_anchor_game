<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import { Dialog, Toast } from 'vant';
import { apis } from './api/apis';
export default {
  name: 'App',
  async mounted() {
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
</style>
