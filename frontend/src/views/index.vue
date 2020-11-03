<template>
  <div class="index page bg1">
    <img class="index_head" src="../assets/logo2.png" />
    <div class="index_text">录音可抽卡</div>
    <div class="index_text">初始抽卡机会为三次</div>
    <div class="index_text">邀请好友助力可以获得额外抽卡机会</div>
    <div class="index_text">每位好友一天只能助力一次哦</div>
    <div class="index_text">(ps.前五位集齐卡牌有神秘小礼物哟)</div>
    <img class="index_go" src="../assets/go.png" @click="go()" />
  </div>
</template>

<script>
export default {
  name: 'index',
  methods: {
    go() {
      this.$router.push({ path: '/game' });
    },
  },
};
</script>

<style scoped>
.index {
  display: flex;
  display: -webkit-flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
.index_head {
  width: 77vw;
  height: auto;
  margin-bottom: 6.25vh;
}

.index_text {
  font-size: 1.2em;
  line-height: 1.6em;
}

.index_go {
  width: 50vw;
  height: auto;
  margin-top: 6.25vh;
}
</style>
