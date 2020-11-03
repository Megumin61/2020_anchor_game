<template>
  <div class="map page bg2">
    <div style="visibility: hidden;height:0;">placeholder</div>
    <van-row class="map_row map_row1" gutter="20">
      <van-col span="8">
        <CollectedCard :i="1" v-if="cards[0].collected"></CollectedCard>
        <NotCollectedCard
          :progress="cards[0].progress"
          v-if="!cards[0].collected"
        ></NotCollectedCard>
      </van-col>
      <van-col span="8">
        <CollectedCard :i="2" v-if="cards[1].collected"></CollectedCard>
        <NotCollectedCard
          :progress="cards[1].progress"
          v-if="!cards[1].collected"
        ></NotCollectedCard>
      </van-col>
      <van-col span="8">
        <CollectedCard :i="3" v-if="cards[2].collected"></CollectedCard>
        <NotCollectedCard
          :progress="cards[2].progress"
          v-if="!cards[2].collected"
        ></NotCollectedCard>
      </van-col>
    </van-row>
    <van-row class="map_row map_row2" gutter="20">
      <van-col span="8">
        <CollectedCard :i="4" v-if="cards[3].collected"></CollectedCard>
        <NotCollectedCard
          :progress="cards[3].progress"
          v-if="!cards[3].collected"
        ></NotCollectedCard>
      </van-col>
      <van-col span="8">
        <CollectedCard :i="5" v-if="cards[4].collected"></CollectedCard>
        <NotCollectedCard
          :progress="cards[4].progress"
          v-if="!cards[4].collected"
        ></NotCollectedCard>
      </van-col>
      <van-col span="8">
        <CollectedCard :i="6" v-if="cards[5].collected"></CollectedCard>
        <NotCollectedCard
          :progress="cards[5].progress"
          v-if="!cards[5].collected"
        ></NotCollectedCard>
      </van-col>
    </van-row>
    <van-row class="map_row map_row2" gutter="20">
      <van-col span="8">
        <CollectedCard :i="7" v-if="cards[6].collected"></CollectedCard>
        <NotCollectedCard
          :progress="cards[6].progress"
          v-if="!cards[6].collected"
        ></NotCollectedCard>
      </van-col>
      <van-col span="8">
        <CollectedCard :i="8" v-if="cards[7].collected"></CollectedCard>
        <NotCollectedCard
          :progress="cards[7].progress"
          v-if="!cards[7].collected"
        ></NotCollectedCard>
      </van-col>
      <van-col span="8">
        <div style="visibility: hidden;">
          placeholder
        </div>
      </van-col>
    </van-row>
    <img class="map_back" src="../assets/back.png" @click="back()" />
  </div>
</template>

<script>
import CollectedCard from '../components/CollectedCard';
import NotCollectedCard from '../components/NotCollectedCard';
export default {
  name: 'map',
  components: {
    CollectedCard,
    NotCollectedCard,
  },
  data: () => {
    return {
      img_path: '../assets/cards/',
      cards: [
        {
          collected: true,
          progress: 3,
        },
        {
          collected: false,
          progress: 1,
        },
        {
          collected: true,
          progress: 1,
        },
        {
          collected: false,
          progress: 1,
        },
        {
          collected: false,
          progress: 2,
        },
        {
          collected: true,
          progress: 1,
        },
        {
          collected: false,
          progress: 1,
        },
        {
          collected: false,
          progress: 1,
        },
      ],
    };
  },
  methods: {
    back() {
      this.$router.push({ path: '/game' });
    },
  },
};
</script>

<style scoped>
.map {
  display: flex;
  display: -webkit-flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
.map_wrap {
  display: flex;
  display: -webkit-flex;
  justify-content: center;
  align-items: center;
  flex-direction: row;
  flex-wrap: wrap;
}
.map_img {
  width: 24vw;
  height: auto;
}

.map_row {
  margin-left: 7.9vw;
  margin-right: 7.9vw;
}

.map_row1 {
  /* margin-top: 10.8vh; */
}

.map_row2 {
  margin-top: 2.2vh;
}
.map_back {
  margin-top: 10vh;
  width: 50vw;
}
</style>
