<template>
  <div class="detail page bg2">
    <van-overlay :show="showOverlay">
      <div class="detail_loading_wrapper" @click.stop>
        <van-loading size="50px" text-size="16px" vertical
          >加载中...</van-loading
        >
      </div>
    </van-overlay>
    <van-notice-bar
      v-show="showTips"
      style="text-align:center; z-index: 10000; position: fixed; top: 0; left: 0; width: 100vw"
    >
      长按保存图片
    </van-notice-bar>
    <van-image
      class="detail_img"
      :src="require('../assets/cards/' + $route.params.card_id + '.jpg')"
    >
      <template v-slot:loading>
        <van-loading type="spinner" size="20" />
      </template>
    </van-image>
    <img
      class="detail_help detail_btn"
      src="../assets/share.png"
      @click="showShareImage()"
    />
    <img
      class="detail_back detail_btn"
      src="../assets/back.png"
      @click="back()"
    />
  </div>
</template>

<script>
import { ImagePreview, Toast } from 'vant';
import { apis } from '../api/apis';
export default {
  name: 'detail',
  data: () => {
    return { showOverlay: false, showTips: false };
  },
  methods: {
    back() {
      this.$router.push({ path: '/map' });
    },
    showShareImage() {
      this.showOverlay = true;
      apis
        .getQRCode(this.$route.params.card_id)
        .then((res) => {
          // 返回base64编码的图片
          this.showTips = true;
          let that = this;
          ImagePreview({
            images: [res.data.data],
            showIndex: false,
            onClose() {
              console.log('close');
              that.showTips = false;
            },
          });
        })
        .catch((err) => {
          Toast.fail({
            message:
              err.response.data.message || `未知错误${err.response.data}`,
          });
        })
        .finally(() => {
          this.showOverlay = false;
        });
    },
  },
  watch: {
    showOverlay: function(value) {
      if (value) {
        let that = this;
        setTimeout(() => {
          that.showOverlay = false;
          that.showTips = false;
        }, 5000);
      }
    },
  },
};
</script>

<style scoped>
.detail {
  display: flex;
  display: -webkit-flex;
  align-items: center;
  flex-direction: column;
}
.detail_img {
  margin-top: 10.6vh;
  width: 47.8vw;
}
.detail_help {
  margin-top: 10vh;
}
.detail_back {
  margin-top: 0.42vh;
}
.detail_btn {
  width: 50vw;
}
.detail_loading_wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}
</style>
