<template>
  <div style="width:100%; height:100%;" :style="{'padding-top':(frameSize.y-64-(frameSize.x*0.3))/2+'px'}">
    <div>
      <router-link to="/fromHandLan"><div class="serviceButton" :style="{'margin-left':frameSize.x*0.15+'px',height:frameSize.x*0.3+'px'}"><div>수어를<br>번역하기</div></div></router-link>
      <router-link to="/toHandLan"><div class="serviceButton" :style="{'margin-left':frameSize.x*0.15+'px',height:frameSize.x*0.3+'px'}"><div>수어로<br>번역하기</div></div></router-link>
    </div>
    
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  data() {
    return {
      frameSize:{
        x:0,
        y:0,
      }
    }
  },
  methods: {
    onResize(){
        this.frameSize = {x:window.innerWidth, y:window.innerHeight};
    },
  },
  mounted(){
    this.onResize();
  }
}
</script>

<style scoped>
.serviceButton{
  width:30%;
  background-color:white;
  display: block;
  border-radius: 18px;
  box-shadow: 0px 6px 17px 0px #00000012;
  text-align: center;
  float: left;
  min-width: 300px;
  min-height: 300px;
}
</style>