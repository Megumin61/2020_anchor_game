import card1 from './assets/cards/1.jpg';
import card2 from './assets/cards/2.jpg';
import card3 from './assets/cards/3.jpg';
import card4 from './assets/cards/4.jpg';
import card5 from './assets/cards/5.jpg';
import card6 from './assets/cards/6.jpg';
import card7 from './assets/cards/7.jpg';
import card8 from './assets/cards/8.jpg';

import debris1 from './assets/cards/11.png';
import debris2 from './assets/cards/22.png';
import debris3 from './assets/cards/33.png';
import debris4 from './assets/cards/44.png';
import debris5 from './assets/cards/55.png';
import debris6 from './assets/cards/66.png';
import debris7 from './assets/cards/77.png';
import debris8 from './assets/cards/88.png';

import bg1 from './assets/bg1.png';
import bg2 from './assets/bg2.png';

import again from './assets/again.png';
import arrow from './assets/arrow.png';
import back from './assets/back.png';
import big from './assets/big.png';
import cardback1 from './assets/cardback1.png';
import cardback2 from './assets/cardback2.png';
import go from './assets/go.png';
import kuang from './assets/kuang.png';
import light from './assets/light.png';
import logo2 from './assets/logo2.png';
import pic from './assets/pic.png';
import share from './assets/share.png';
import signup from './assets/signup.png';
import speak from './assets/speak.png';
import submit from './assets/submit.png';
import wave1 from './assets/wave1.png';
import wave2 from './assets/wave2.png';
import wave3 from './assets/wave3.png';
import yellow from './assets/yellow.png';

let imgs = [
  bg1,
  bg2,

  card1,
  card2,
  card3,
  card4,
  card5,
  card6,
  card7,
  card8,

  debris1,
  debris2,
  debris3,
  debris4,
  debris5,
  debris6,
  debris7,
  debris8,

  again,
  arrow,
  back,
  big,
  cardback1,
  cardback2,
  go,
  kuang,
  light,
  logo2,
  pic,
  share,
  submit,
  signup,
  speak,
  wave1,
  wave2,
  wave3,
  yellow,
];

import { g } from './config';

export async function preload() {
  console.log('start preload');
  g.showLoading();
  let timeout = setTimeout(() => {
    g.hideLoading();
  }, 3000);

  let count = 0;

  for (let i = 0; i < imgs.length; i++) {
    let img = new Image();
    img.onload = () => {
      count++;
      if (count == imgs.length) {
        g.hideLoading();
        clearTimeout(timeout);
      }
    };
    img.src = imgs[i];
  }
}
