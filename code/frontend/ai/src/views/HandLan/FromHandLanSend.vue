<template>
  <div id="video" style="width:100%; height:100%;">
    <a :href="videoSrc" download="test.webm">gigi</a>
      <!-- <Video style="width:100%; height:100%;" :src="videoSrc"></Video> -->
      <video id="preview" controls autoplay :src="videoSrc"></video>
      
      <div id="send" style="margin-top:-80px" :style="{'margin-left':(frameSize.x*0.9-305)/2+'px'}">
        <router-link to="/FromHandLan"><v-btn class="sendBtn" color="rgb(232, 107, 94)" style="width:150px;color:white; margin-right:5px; height:50px; font-size:45px; font-weight:bold; font-size:large"><v-icon>mdi-backup-restore</v-icon>다시 하기</v-btn></router-link>
        <router-link to="/FromHandLanResult"><v-btn class="sendBtn" color="rgb(54, 214, 123)" style="width:150px;color:white; height:50px; font-size:45px; font-weight:bold; font-size:large"><v-icon>mdi-check</v-icon>번역 하기</v-btn></router-link>
      </div>
      

    </div>
</template>

<script>
// import Video from '../../components/Video.vue'
// import axios from 'axios'
export default {
    // components:{Video},

    data(){
      return{
        frameSize:{
          x:0,
          y:0,
        },
        sendWidth:0,
        buttonMargin:0,
        videoSrc : '',
      }
    },
    methods:{
      onResize(){
          this.frameSize = {x:window.innerWidth, y:window.innerHeight};
      },
    },
    mounted(){
      
      window.onresize=()=>{
        this.onResize();
        
      }
      this.videoSrc = this.$route.params.videoSrc;
    }
}
</script>

<style lang="scss" scoped>
.video {
  width: 100%;
  height: 100%;
  padding: 0px;
  box-sizing: border-box;

  .send{
    display: block;
    // position:fixed;
    width: 75px;
    height: 75px;
    border-radius: 50%;
    background-color: transparentize($color: #2493dd, $amount: 0.75);
    border: 1px solid color #171717;
    border-radius: 50%;
    outline: none;
    cursor: pointer;
    // margin-top: 530px;
    // margin-left: 900px;

    &:hover {
      background-color: #2493dd;
    }
    &:active {
      background-color: darken($color: #2493dd, $amount: 10);
    }
  }

  .redo{
    display: block;
    // position:fixed;
    width: 75px;
    height: 75px;
    border-radius: 50%;
    background-color: transparentize($color: #fd3015, $amount: 0.75);
    border: 1px solid color #171717;
    border-radius: 50%;
    outline: none;
    cursor: pointer;
    // margin-top: 530px;
    // margin-left: 1000px;

    &:hover {
      background-color: #fd3015;
    }
    &:active {
      background-color: darken($color: #fd3015, $amount: 10);
    }
  }

  .snap {
    display: block;
    // position:fixed;
    width: 75px;
    height: 75px;
    border-radius: 50%;
    background-color: transparentize($color: #ffce00, $amount: 0.75);
    border: 1px solid color #171717;
    border-radius: 50%;
    outline: none;
    cursor: pointer;
    // margin-top: 530px;
    // margin-left: 250px;

    &:hover {
      background-color: #ffce00;
    }
    &:active {
      background-color: darken($color: #ffce00, $amount: 10);
    }
  }
}
#btnStart{
  width: 100px;
  height:100px;
  border:0px solid transparent;
  border-radius: 50px;
  min-width:unset;
  padding:25px;
  position:fixed;
  margin-top:-130px;
}
#btnStartInner{
  background-color: #b72e2e;
    width: 50px;
    height: 50px;
    box-shadow: 0px 0px 10px #00000070;
    border-radius: 25px;
}
.sendBtn{
  height:100px;
  color:white;
}
#btnCapture{
  width: 100px;
  height:100px;
  border:0px solid transparent;
  border-radius: 50px;
  min-width:unset;
  padding:25px;
  position:fixed;
  margin-top:-130px;
}
</style>