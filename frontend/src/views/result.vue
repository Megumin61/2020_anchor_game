<template>
  <div class="result page bg2">
    <van-image
      :class="this.$route.params.type == 'card' ? card : debris"
      :src="require('../assets/cards/' + imgName)"
    >
      <template v-slot:loading>
        <van-loading type="spinner" size="20" />
      </template>
    </van-image>

    <div class="result_tip_wrap">
      <img class="result_yellow" src="../assets/yellow.png" />
      <div class="result_tip">{{ tip }}</div>
    </div>
    <img
      class="result_signup result_btn"
      src="../assets/signup.png"
      @click="signup()"
    />

    <img class="result_help result_btn" src="../assets/share.png" />
    <img
      class="result_back result_btn"
      src="../assets/back.png"
      @click="back()"
    />
  </div>
</template>

<script>
export default {
  name: 'result',
  data: () => {
    return {
      card: 'result_card',
      debris: 'result_debris',
    };
  },
  methods: {
    signup() {
      window.location.href = 'http://hemc.100steps.net/2020/anchor';
    },
    back() {
      this.$router.push({ path: '/game' });
    },
  },
  computed: {
    imgName: function() {
      if (this.$route.params.type == 'card') {
        return `${this.$route.params.card_id}.jpg`;
      } else if (this.$route.params.type == 'debris') {
        return `${this.$route.params.card_id}${this.$route.params.card_id}.png`;
      }
      return '';
    },
    tip: function() {
      if (this.$route.params.type == 'card') {
        return '获得新卡牌！';
      } else if (this.$route.params.type == 'debris') {
        return '获得卡牌碎片';
      }
      return '';
    },
  },
};
</script>

<style scoped>
.result {
  display: flex;
  display: -webkit-flex;
  align-items: center;
  flex-direction: column;
}
.result_card {
  margin-top: 10.6vh;
  width: 47.8vw;
}
.result_debris {
  margin-top: 15vh;
  width: 58.8vw;
  height: auto;
}
.result_tip_wrap {
  position: relative;
  margin-top: 2.7vh;
  width: 100vw;
  display: flex;
  height: 5rem;
  display: -webkit-flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}
.result_yellow {
  position: absolute;
  top: 0;
  left: 15vw;
  height: 5rem;
  width: 70vw;
  z-index: 0;
  /* margin: auto; */
}
.result_tip {
  z-index: 10;
  color: #eeeeee;
  font-family: 'STHupo';
  text-shadow: 1px 1px 2px gray;
}
.result_signup {
  margin-top: 2.7vh;
}
.result_help {
  margin-top: 0.42vh;
}
.result_back {
  margin-top: 0.42vh;
  margin-bottom: 2vh;
}
.result_btn {
  width: 50vw;
}
</style>
