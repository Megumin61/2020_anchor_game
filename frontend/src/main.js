import Vue from 'vue';
import App from './App.vue';
import router from './router';

import {
  Col,
  Row,
  Image as VanImage,
  Loading,
  Overlay,
  NoticeBar,
  Popup,
  Picker,
} from 'vant';

Vue.config.productionTip = false;

Vue.use(Col)
  .use(Row)
  .use(VanImage)
  .use(Loading)
  .use(Overlay)
  .use(NoticeBar)
  .use(Popup)
  .use(Picker);

Vue.prototype.$showLoading = true;
Vue.prototype.$showTips = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
