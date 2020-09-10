<template>
  <div style="width:100%;height:100%;">
      <v-card style="width:50%;height:100%; display:inline-block; float:left;">
        <router-link to="/toHandLan"><v-btn style="position: absolute;
    margin: 5px; height:60px; width:60px; text-align:center;"><v-icon size="50px">mdi-replay</v-icon></v-btn></router-link>
        <img src="../../assets/photoresult.jpg" style="width:100%; height:100%;">
      </v-card>
      <v-card style="width:50%; height:100%; display:inline-block;">
      <v-tabs
          v-model="tabs"
          fixed-tabs
        >
          <v-tabs-slider></v-tabs-slider>
          <v-tab
            href="#mobile-tabs-5-1"
            class="primary--text"
          >
            <v-icon>mdi-vector-rectangle</v-icon>물체
          </v-tab>

          <v-tab
            href="#mobile-tabs-5-2"
            class="primary--text"
          >
            <v-icon>mdi-pencil</v-icon> 글씨
          </v-tab>
        </v-tabs>
      <v-tabs-items v-model="tabs">
      <v-tab-item
        v-for="i in 2"
        :key="i"
        :value="'mobile-tabs-5-' + i"
      >
        <v-card flat>
          <v-card-text></v-card-text>
        </v-card>
      </v-tab-item>
    </v-tabs-items>
      </v-card>
  </div>
</template>

<script>


export default {
  data() {
        return {
            transResultIMG:'../assets/photoresult.jpg',
            responsiveVoice:'',
            tabs: null,
            text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        }
    },
}
</script>

<style>
.v-toolbar__content{
  height:0px;
}
</style>