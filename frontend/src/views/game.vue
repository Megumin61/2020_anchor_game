<template>
  <div class="game page bg2">
    <div class="game_pic_wrap">
      <img class="game_pic" src="../assets/pic.png" @click="to_map()" />
    </div>
    <div class="game_text_wrap">
      <div class="game_text_tips">不知道说些什么就试试这句话吧</div>
      <div class="game_text">{{ text }}</div>
    </div>
    <div class="game_wrap">
      <div class="game_remain">剩余抽卡次数：{{ remain }} 次</div>
      <img class="game_speak" src="../assets/speak.png" />
      <div class="game_tips">ps.录音时间要大于1秒哦</div>
    </div>
  </div>
</template>

<script>
// import card1 from '../assets/cards/1.png';
// import card2 from '../assets/cards/2.png';
// import card3 from '../assets/cards/3.png';
// import card4 from '../assets/cards/4.png';
// import card5 from '../assets/cards/5.png';
// import card6 from '../assets/cards/6.png';
// import card7 from '../assets/cards/7.png';
// import card8 from '../assets/cards/8.png';
// import cardback1 from '../assets/cardback1.png';

export default {
  name: 'game',
  data: () => {
    return {
      text: '生活就像海洋，只有意志坚强的人才能到彼岸',
      remain: 3,
      //   imgs: [card1, card2, card3, card4, card5, card6, card7, card8, cardback1],
    };
  },
  methods: {
    to_map() {
      this.$router.push({ path: '/map' });
    },
    // perload(){
    //     for (let i = 0; i < this.imgs.length; i++) {
    //     let img = new Image();
    //     img.onload = () => {
    //       this.count++;
    //       if (this.count == this.imgs.length + 1) {
    //         loading.close();
    //       }
    //     };
    //     img.src = this.imgs[i];
    //   }
    // }
  },
  async mount() {},
};
</script>

<style scoped>
.game {
  display: flex;
  flex-direction: column;
}
.game_pic_wrap {
  width: 100vw;
  display: flex;
  display: -webkit-flex;
  flex-direction: row;
  justify-content: flex-end;
  margin-top: 7vh;
}
.game_pic {
  /* position: absolute; */

  width: 25vw;
  margin-right: 3vw;
}
.game_text_wrap {
  background-image: url('../assets/kuang1.png');
  background-size: 78.6vw 8rem;
  background-repeat: no-repeat;
  width: 78.6vw;
  min-height: 8rem;
  margin-left: 10.7vw;
  margin-top: 5vh;
}
.game_text_tips {
  padding-left: 7vw;
  padding-top: 1.5vh;
  padding-right: 4vw;
}
.game_text {
  font-size: 1.2em;
  padding-left: 10vw;
  padding-right: 7vw;
  margin-top: 1.5vh;
  padding-bottom: 1.5vh;
  line-height: 1.5em;
}
.game_wrap {
  display: flex;
  display: -webkit-flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
.game_remain {
  margin-top: 10vh;
}
.game_speak {
  margin-top: 0.5vh;
  width: 60vw;
}
.game_tips {
  margin-top: 0.5vh;
}
</style>
