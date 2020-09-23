<template>
  <v-card class="overflow-hidden">
    <v-app-bar
      absolute
      color="transparent"
      elevate-on-scroll
      scroll-target="#scrolling-techniques-7"
      style="z-index:100;"
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

      <v-spacer style="text-align:center;"><router-link to="/"><img src="../assets/title.png" height="50px"></router-link></v-spacer>

    </v-app-bar>
    <v-sheet
      id="scrolling-techniques-7"
      class="overflow-y-auto"
      :min-width="frameSize.x"
      :max-height="frameSize.y"
      style="z-index:0; "
    >
      <div class="background" v-if="$route.name=='Home' || $route.name=='ToHandLanChoice'" style="padding-top:64px;" :style="{width:frameSize.x+'px', height:frameSize.y+'px'}">
        <router-view></router-view>
      </div>
      <div class="background" v-if="$route.name !='Home'&& $route.name!='ToHandLanChoice'" style=" padding-top:64px;" :style="{width:frameSize.x+'px', height:frameSize.y+'px'}">
        <div style="width:90%; height:90%; background-color:white; margin-left:5%;     border-radius: 30px;
    box-shadow: 0px 0px 27px -4px #00000026;" :style="{'margin-top':(frameSize.y-46-(frameSize.y*0.9))/2+'px'}">
        <router-view></router-view>
        </div>
      </div>
    </v-sheet>

    <v-navigation-drawer
      v-model="drawer"
      absolute
      bottom
      temporary
      style="z-index:101;"
    >
      <v-list
        nav
        dense
      >
        <v-list-item-group
          v-model="group"
          active-class="deep-purple--text text--accent-4"
        >
        <router-link to="/toHandLan">
          <v-list-item>
            <v-list-item-title>수어로 번역하기</v-list-item-title>
          </v-list-item>
        </router-link>

        <router-link to="/fromHandLan">
          <v-list-item>
            <v-list-item-title>수어를 번역하기</v-list-item-title>
          </v-list-item>
          </router-link>

        <router-link to="/board">
          <v-list-item>
            <v-list-item-title>게시판</v-list-item-title>
          </v-list-item>
        </router-link>

        <router-link to="/video">
          <v-list-item>
            <v-list-item-title>비디오</v-list-item-title>
          </v-list-item>
        </router-link>
        
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      frameSize:{
        x:0,
        y:0,
      },
      drawer: false,
      group: null,
    }
  },
  methods: {
    onResize(){
        this.frameSize = {x:window.innerWidth, y:window.innerHeight};      
    },
  },
  mounted(){
    this.onResize();
      window.onresize=()=>{
          this.onResize();
        }
      },
  watch:{
     group () {
        this.drawer = false
      },
  }
}
</script>

<style>
.background{
  background:url('../assets/background.png') no-repeat;
  background-size: cover;
}
</style>