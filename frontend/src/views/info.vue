<template>
  <div class="info page bg2">
    <div class="info_title">恭喜你集齐卡牌</div>
    <div class="info_line"></div>
    <div class="info_tips_wrap">
      <div class="info_tips">我们会以短信的方式通知你领取神秘礼物</div>
      <div class="info_tips">请填写一下信息</div>
    </div>
    <div class="info_form_wrap">
      <div class="info_input">
        <span>姓名</span>
        <input id="name" type="text" v-model="name" />
      </div>
      <div class="info_input">
        <span>校区</span>
        <input
          id="name"
          class="select"
          type="text"
          v-model="campus"
          readonly
          @click="showPicker = true"
        />
      </div>
      <div class="info_input">
        <span>电话</span>
        <input id="name" type="tel" maxlength="11" v-model="tel" />
      </div>
    </div>
    <img class="info_submit" @click="onSubmit()" src="../assets/submit.png" />

    <van-popup v-model="showPicker" round position="bottom">
      <van-picker
        show-toolbar
        :columns="columns"
        @cancel="showPicker = false"
        @confirm="onConfirm"
      />
    </van-popup>
  </div>
</template>

<script>
import { Toast } from 'vant';
import { apis } from '../api/apis';

export default {
  name: 'info',
  data: () => {
    return {
      name: '',
      campus: '',
      tel: '',
      showPicker: false,
      columns: ['大学城校区', '五山校区', '国际校区'],
    };
  },
  methods: {
    onSubmit() {
      // 检验手机号
      if (
        isNaN(Number(this.tel)) ||
        this.tel.length != 11 ||
        this.tel[0] != '1'
      ) {
        Toast.fail({ message: '手机号错误' });
        this.tel = '';
        return;
      }
      apis
        .saveUserInfo(this.name, this.tel, this.campus)
        .then((res) => {
          Toast({ message: res.data.message });
        })
        .catch((err) => {
          Toast.fail({
            message:
              err.response.data.message || `未知错误${err.response.data}`,
          });
        });
    },
    onConfirm(val) {
      this.campus = val;
      this.showPicker = false;
    },
  },
};
</script>

<style scoped>
.info {
  display: flex;
  display: -webkit-flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
.info_line {
  border: 0.5px solid black;
  margin-top: 0.7em;
  margin-bottom: 0.7em;
  width: 90vw;
}
.info_title {
  font-size: 1.5em;
}
.info_tips_wrap {
  margin: 0 15vw;
}
.info_tips {
  font-size: 1em;
}

input {
  outline: none;
  background-color: transparent;
  border: 1px solid black;
  margin-left: 4vw;
  width: 54.8vw;
  border-radius: 4px;
  line-height: 1.5em;
  box-sizing: border-box;
  padding: 0 0.15em;
}

.info_input {
  line-height: 1.5em;
  font-size: 1.2em;
  margin-top: 7vw;
}
.info_submit {
  margin-top: 7vw;
  width: 50vw;
}

.select {
  background-image: url('../assets/arrow.png');
  background-size: auto 70%;
  background-repeat: no-repeat;
  background-position: right 2vw center;
}
</style>
