<template>
  <v-card class="overflow-hidden">
    <v-app-bar
      absolute
      color="#ffffff73"
      elevate-on-scroll
      scroll-target="#scrolling-techniques-7"
      style="z-index:100;"
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

      <v-spacer style="text-align:center;"><router-link to="/"><div>홈으로</div></router-link></v-spacer>

    </v-app-bar>
    <v-sheet
      id="scrolling-techniques-7"
      class="overflow-y-auto"
      :min-width="frameSize.x"
      :max-height="frameSize.y"
      style="z-index:0;"
    >
      <div v-if="$route.name=='Home'" style="background-color:#fdebf6; padding-top:64px;" :style="{width:frameSize.x+'px', height:frameSize.y+'px'}">
        <router-view></router-view>
      </div>
      <div v-if="$route.name !='Home'" style="background-color:#fdebf6; padding-top:64px;" :style="{width:frameSize.x+'px', height:frameSize.y+'px'}">
        <div style="width:90%; height:90%; background-color:white; margin-left:5%;" :style="{'margin-top':(frameSize.y-46-(frameSize.y*0.9))/2+'px'}">
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
          <v-list-item>
            <v-list-item-title>Foo</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>Bar</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>Fizz</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title>Buzz</v-list-item-title>
          </v-list-item>

        <router-link to="/board">
          <v-list-item>
            <v-list-item-title>게시판</v-list-item-title>
          </v-list-item>
        </router-link>

        <router-link to="/camera">
          <v-list-item>
            <v-list-item-title>카메라</v-list-item-title>
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
  },
  watch:{
     group () {
        this.drawer = false
      },
  }
}
</script>

<style>

</style>