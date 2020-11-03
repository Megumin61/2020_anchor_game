import Vue from 'vue';
import App from './App.vue';
import router from './router';

import { Col, Row, Image as VanImage, Loading } from 'vant';

Vue.config.productionTip = false;

Vue.use(Col)
  .use(Row)
  .use(VanImage)
  .use(Loading);

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
