import Vue from 'vue';
import VueRouter from 'vue-router';

import index from './views/index.vue';
import game from './views/game.vue';
import map from './views/map.vue';
import result from './views/result.vue';
import detail from './views/detail.vue';

Vue.use(VueRouter);

const routerPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
  return routerPush.call(this, location).catch(error => error);
};

const routes = [
  {
    path: '/index',
    component: index,
  },
  {
    path: '/game',
    component: game,
  },
  {
    path: '/map',
    component: map,
  },
  {
    path: '/result/:type/:card_id',
    component: result,
  },
  {
    path: '/detail/:card_id',
    component: detail,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
