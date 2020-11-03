<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
  async mounted() {
    this.$router.push({
      // path: '/result/card/1',
      path: '/index',
    });
  },
};
</script>

<style>
body {
  margin: 0;
  padding: 0;
  min-height: 100vh;
  min-width: 100vw;
}
.page {
  background-size: 100vw 100vh;
  min-height: 100vh;
  min-width: 100vw;
  background-attachment: fixed;
  background-repeat: no-repeat;
}
.bg1 {
  background-image: url('./assets/bg1.png');
}
.bg2 {
  background-image: url('./assets/bg2.png');
}
</style>
