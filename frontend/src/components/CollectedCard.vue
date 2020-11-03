<template>
  <div class="collected_card">
    <van-image
      class="collected_card_img"
      :src="require('../assets/cards/' + i + '.jpg')"
    >
      <template v-slot:loading>
        <van-loading type="spinner" size="20" />
      </template>
    </van-image>
    <div class="collected_card_show_wrap">
      <img
        class="collected_card_show"
        src="../assets/big.png"
        @click="to_detail()"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: 'CollectedCard',
  props: {
    i: Number,
  },
  data: () => {
    return {};
  },
  methods: {
    to_detail() {
      this.$router.push({ path: '/detail/' + this.i });
    },
  },
};
</script>

<style scoped>
.collected_card {
  position: relative;
}
.collected_card_img {
  width: 100%;
  height: auto;
  /* width: 10vw; */
  /* width: 24vw;
  height: auto; */
  /* height: auto; */
}
.collected_card_show_wrap {
  position: absolute;
  display: flex;
  display: -webkit-flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-color: rgba(0, 0, 0, 0.38);
  top: 0;
  right: 0;
  width: 7vw;
  height: 7vw;
}
.collected_card_show {
  width: 4.5vw;
  height: 4.5vw;
  margin: auto;
}
</style>
