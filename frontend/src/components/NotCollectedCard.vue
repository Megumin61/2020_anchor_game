<template>
  <div class="not_collected_card">
    <van-image
      class="not_collected_card_img"
      :src="require('../assets/cardback1.png')"
    >
      <template v-slot:loading>
        <van-loading type="spinner" size="20" />
      </template>
    </van-image>
    <div class="not_collected_card_progress_wrap">
      <div class="not_collected_card_progress">收集进度:{{ progress }}/3</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NotCollectedCard',
  props: {
    progress: Number,
  },
};
</script>

<style scoped>
.not_collected_card {
  position: relative;
}
.not_collected_card_img {
  width: 100%;
  height: auto;
}
.not_collected_card_progress_wrap {
  width: 100%;
  position: absolute;
  display: flex;
  display: -webkit-flex;
  justify-content: center;
  align-items: center;
  background-color: #607092;
  bottom: 10%;
}
.not_collected_card_progress {
  font-size: 10px;
  color: #e3e9f8;
  padding: 0.3em 0;
}
</style>
