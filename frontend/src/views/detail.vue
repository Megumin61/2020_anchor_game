<template>
  <div class="detail page bg2">
    <div style="visibility: hidden;height:0;">placeholder</div>

    <van-image
      class="detail_img"
      :src="require('../assets/cards/' + $route.params.card_id + '.jpg')"
    >
      <template v-slot:loading>
        <van-loading type="spinner" size="20" />
      </template>
    </van-image>
    <img class="detail_help detail_btn" src="../assets/share.png" />
    <img
      class="detail_back detail_btn"
      src="../assets/back.png"
      @click="back()"
    />
  </div>
</template>

<script>
export default {
  name: 'detail',
  data: () => {
    return {};
  },
  methods: {
    back() {
      this.$router.push({ path: '/map' });
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
</style>
