<template>
  <div class="game page bg2">
    <div class="game_pic_wrap">
      <img class="game_pic" src="../assets/pic.png" @click="to_map()" />
    </div>
    <div class="game_text_wrap">
      <img class="game_kuang" src="../assets/kuang.png" />
      <div class="game_text_tips not_selected">
        不知道说些什么就试试这句话吧
      </div>
      <div class="game_text not_selected">{{ text }}</div>
    </div>
    <div class="game_wrap">
      <div class="game_remain not_selected">剩余抽卡次数：{{ remain }} 次</div>

      <div class="record">
        <div
          :class="recording ? 'record_on' : 'record_off'"
          id="record_anim1"
        ></div>
        <div
          id="record_btn"
          @touchstart="touchstart($event)"
          @touchend="touchend($event)"
          @touchcancel="touchend($event)"
        ></div>
        <div
          :class="recording ? 'record_on' : 'record_off'"
          id="record_anim2"
        ></div>
      </div>

      <div class="game_tips not_selected">ps.录音时间要大于1秒哦</div>

      <div class="card_container not_selected">
        <img class="game_light" src="../assets/light.png" />
        <img
          class="game_card"
          :class="recordFinished ? 'cards_on' : 'cards_off'"
          id="anim_card1"
          src="../assets/cardback2.png"
        />
        <img
          class="game_card cards_off"
          :class="recordFinished ? 'cards_on' : 'cards_off'"
          id="anim_card2"
          src="../assets/cardback2.png"
        />
        <img
          class="game_card cards_off"
          :class="[
            recordFinished ? 'cards_on' : 'cards_off',
            cardFly ? 'cards_fly' : '',
          ]"
          id="anim_card3"
          src="../assets/cardback2.png"
        />
      </div>
    </div>
  </div>
</template>

<script>
// import wx from 'weixin-js-sdk';
import { apis } from '../api/apis';
import { Toast } from 'vant';
export default {
  name: 'game',
  data: () => {
    return {
      text: '生活就像海洋，只有意志坚强的人才能到彼岸',
      remain: 3,
      recording: false,
      recordFinished: false,
      cardFly: false,
      goodRecord: false,
    };
  },
  methods: {
    to_map() {
      this.$router.push({ path: '/map' });
    },
    touchstart(e) {
      e.preventDefault();
      if (this.remain) {
        this.recording = true;
        this.goodRecord = false;
        setTimeout(() => {
          this.goodRecord = true;
        }, 1000);
      }
    },
    touchend(e) {
      e.preventDefault();
      if (this.remain) {
        this.recording = false;
        if (this.goodRecord) {
          apis
            .drawCard()
            .then((res) => {
              // 录音完毕，卡牌旋转
              this.recordFinished = true;
              setTimeout(() => {
                this.recordFinished = false;
                this.cardFly = true;
                setTimeout(() => {
                  this.cardFly = false;
                  // 进入新页面
                  this.$router.push({
                    path: `/result/${res.data.card ? 'card' : 'debris'}/${
                      res.data.index
                    }`,
                    query: {
                      finish: res.data.finish,
                      winner: res.data.winner,
                      info: res.data.info,
                      count: res.data.count,
                    },
                  });
                }, 1820);
              }, 2000);
            })
            .catch((err) => {
              Toast.fail({
                message:
                  err.response.data.message || `未知错误${err.response.data}`,
              });
            });
        } else {
          Toast.fail({ message: '录音时间必须要大于一秒' });
        }
      }
    },
  },
  async mounted() {
    // 获取jssdk需要的配置信息

    // apis.wxconfig().then(res => {
    //   wx.config({
    //     debug: false,
    //     appId: res.appid,
    //     timestamp: res.timestamp,
    //     nonceStr: res.noncestr,
    //     signature: res.signature,
    //     jsApiList: ['startRecord', 'stopRecord'],
    //   });
    // });

    apis
      .getUserInfo()
      .then((res) => {
        console.log('获取用户信息');
        this.remain = res.data.remain;
      })
      .catch((err) => {
        console.log(err);
      });

    // let record_btn = document.getElementById('record_btn');
    // console.log(record_btn);
    // record_btn.addEventListener('touchstart', e => {
    //   e.preventDefault();
    //   // alert('touchstart');
    // });
    // record_btn.addEventListener('touchend', e => {
    //   e.preventDefault();
    //   alert('touchend');
    // });
  },
};
</script>

<style scoped>
.game {
  display: flex;
  display: -webkit-flex;
  flex-direction: column;
  justify-content: center;
}
.not_selected {
  user-select: none;
  -moz-user-select: none;
  -webkit-user-select: none;
}
.game_pic_wrap {
  width: 100vw;
  display: flex;
  display: -webkit-flex;
  flex-direction: row;
  justify-content: flex-end;
  margin-top: 3vh;
}
.game_pic {
  /* position: absolute; */

  width: 25vw;
  margin-right: 3vw;
}
.game_text_wrap {
  /* background-image: url('../assets/kuang1.png');
  background-size: 78.6vw 8rem;
  background-repeat: no-repeat; */
  position: relative;
  width: 78.6vw;
  height: fit-content;
  /* min-height: 8rem; */
  margin-left: 10.7vw;
  margin-top: 5vh;
}
.game_kuang {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
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
  /* margin-top: 0.5vh; */
  width: 60vw;
}
.game_tips {
  margin-top: 0.5vh;
}

/* ========语音动画======== */
.record {
  /* 装按钮的容器 */
  height: fit-content;
  width: 100vw;
  /* margin-left: 5vw; */
  display: flex;
  /* align-items: center; */
  display: -webkit-flex;
  /* justify-content: center; */
  flex-wrap: nowrap;
  margin-top: 0.5vh;
}
#record_btn {
  background-image: url('../assets/speak.png');
  background-repeat: no-repeat;
  background-position: center;
  background-size: contain;
  width: 60vw;
  height: 25vw;
  /* height: auto; */
  /* margin-top: 5%; */
}
.record_off {
  /* 不说话时 没有声波动画 */
  margin-top: 5%;
  background-image: url('../assets/wave1.png');
  background-size: contain;
  background-position: center;
  background-repeat: no-repeat;
  height: 15vw;
  width: 20vw;
  opacity: 0;
}
.record_on {
  /* 声波动画 */
  margin-top: 5%;
  background-image: url('../assets/wave1.png');
  background-size: contain;
  background-position: center;
  background-repeat: no-repeat;
  height: 15vw;
  width: 20%;
  animation: change_wave 1s linear infinite;
}
#record_anim2 {
  transform: scaleX(-1);
}
@keyframes change_wave {
  0% {
    background-image: url('../assets/wave1.png');
    opacity: 0;
  }
  5% {
    background-image: url('../assets/wave1.png');
    opacity: 1;
  }
  50% {
    background-image: url('../assets/wave2.png');
    opacity: 1;
  }
  80% {
    background-image: url('../assets/wave3.png');
    opacity: 1;
  }
  100% {
    background-image: url('../assets/wave1.png');
    opacity: 0;
  }
}

/* ===========卡牌动画=========== */
.card_container {
  /*
    这个是不会动的时候
    装卡的容器 背景是light 
     */
  /* background-image: url('../assets/light.png');
  background-position: bottom;
  background-size: contain;
  background-repeat: no-repeat; */
  position: relative;
  height: 20vh;
  /* height: fit-content; */
  width: 90vw;
  margin-top: 16vh;
  /* margin-left: 5%; */
  /* position: absolute; */
  /* bottom: 2%; */
  /* margin-bottom: 5vh; */
}
.game_light {
  position: absolute;
  bottom: 0;
  width: 90vw;
  height: auto;
  margin: auto;
}

.game_card {
  height: 20vh;
}

/* .cards_off {
  /* height: 60%; */
/* transform: scale(0.9); */
/* } */

#anim_card1 {
  position: absolute;
  left: 10%;
  bottom: 30%;
  transform: translate3d(0, 0, 0);
}

#anim_card2 {
  position: absolute;
  right: 10%;
  z-index: 2;
  bottom: 30%;
  transform: translate3d(0, 0, 0);
}

#anim_card3 {
  position: absolute;
  bottom: 15%;
  /* text-align: center; */
  /* right: 35%;
  left: 35%; */
  left: 50%;
  /* margin: auto; */
  z-index: 3;
  transform: translate3d(-50%, 0, 0);
}
/* classname切换为 cards_on 播放转卡动画（三张卡都要换 */
.cards_on#anim_card1 {
  animation: roll_card1 2s infinite linear;
}

.cards_on#anim_card2 {
  animation: roll_card2 2s infinite linear;
}
.cards_on#anim_card3 {
  animation: roll_card3 2s infinite linear;
}

@keyframes roll_card1 {
  0% {
    z-index: 1;
    transform: translate3d(0, 0, 0);
  }

  30% {
    transform: translate3d(150%, 0, 0);
    z-index: 2;
  }

  60% {
    transform: translate3d(75%, 3vh, 0);
    z-index: 3;
  }
  100% {
    z-index: 1;
    transform: translate3d(0, 0, 0);
  }
}
@keyframes roll_card2 {
  0% {
    z-index: 2;
    transform: translate3d(0, 0, 0);
  }

  30% {
    transform: translate3d(-75%, 3vh, 0);
    z-index: 3;
  }

  60% {
    transform: translate3d(-150%, 0, 0);
    z-index: 1;
  }
  100% {
    z-index: 2;
    transform: translate3d(0, 0, 0);
  }
}
@keyframes roll_card3 {
  0% {
    z-index: 3;
    /* transform: translate3d(0, 0, 0); */
    transform: translate3d(-50%, 0, 0);
  }

  30% {
    z-index: 1;
    /* transform: translate3d(-75%, -100px, 0); */
    transform: translate3d(-125%, -3vh, 0);
  }

  60% {
    /* transform: translate3d(75%, -100px, 0); */
    transform: translate3d(25%, -3vh, 0);
    z-index: 2;
  }
  100% {
    z-index: 3;
    /* transform: translate3d(0, 0, 0); */
    transform: translate3d(-50%, 0, 0);
  }
}
/* 切换classname 为cards_fly 播放飞卡动画 需要配合路由动画切换页面 */
.cards_fly {
  /* 给anim_card3替换classname */
  /* animation：动画名称 持续时间 运动曲线(匀速linear) 何时开始 播放次数(无限infinite ) 是否反方向(逆播放alternate) 动画起始或者结束的状态(保持forwards/回到起始backwards); */
  animation: fly 1.8s ease-in-out forwards;
}
@keyframes fly {
  0% {
    z-index: 5;
    transform: translate3d(-50%, 0, 0);
    opacity: 1;
  }
  18% {
    transform: translate3d(-50%, 0%, 0) scale3d(2, 2, 1) rotateX(40deg);
  }
  40% {
    transform: translate3d(-50%, -500%, 0) scale3d(0.5, 0.5, 1) rotateX(80deg);
    opacity: 0;
  }
  70% {
    transform: translate3d(-50%, 100%, 0) scale3d(2, 2, 1) rotateX(40deg);
    opacity: 0;
  }
  100% {
    transform: translate3d(-50%, -150%, 0) scale3d(3, 3, 1) rotateX(0deg);
    opacity: 1;
  }
}
</style>
