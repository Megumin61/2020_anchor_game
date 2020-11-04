<template>
  <div class="detail page bg2">
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
import { g } from '../config';
export default {
  name: 'detail',
  methods: {
    back() {
      this.$router.push({ path: '/map' });
    },
    showShareImage() {
      apis
        .getQRCode(this.$route.params.card_id)
        .then((res) => {
          // 返回base64编码的图片
          g.showTips();
          ImagePreview({
            images: [res.data.data],
            showIndex: false,
            onClose() {
              g.hideTips();
            },
          });
        })
        .catch((err) => {
          Toast.fail({
            message:
              err.response.data.message || `未知错误${err.response.data}`,
          });
        });
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
