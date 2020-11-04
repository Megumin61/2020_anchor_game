import Vue from 'vue';
import VueRouter from 'vue-router';

import index from './views/index.vue';
import game from './views/game.vue';
import map from './views/map.vue';
import result from './views/result.vue';
import detail from './views/detail.vue';
import info from './views/info.vue';

Vue.use(VueRouter);

const routerPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
  return routerPush.call(this, location).catch((error) => error);
};

const routes = [
  {
    name: 'index',
    path: '/index',
    component: index,
  },
  {
    name: 'game',
    path: '/game',
    component: game,
  },
  {
    name: 'map',
    path: '/map',
    component: map,
  },
  {
    name: 'result',
    path: '/result/:type/:card_id',
    component: result,
  },
  {
    name: 'detail',
    path: '/detail/:card_id',
    component: detail,
  },
  {
    name: 'info',
    path: '/info',
    component: info,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
