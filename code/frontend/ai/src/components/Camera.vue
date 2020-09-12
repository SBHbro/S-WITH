<template>
  <div id="camera" class="camera" >
    <video autoplay class="feed"></video>
    <!-- <button class="snap" v-on:click="$emit('take-picture')">SNAP</button> -->
    <div v-if="$route.name =='FromHandLan'">
        <v-btn :style="{'margin-left':(frameSize.x*0.9-100)/2+'px'}" type="button" @click="startRecording()" v-bind:disabled="isStartRecording" id="btnStart">
          <div id="btnStartInner"></div>
        </v-btn>
        <!-- <router-link to="/fromHandLanResult"><v-btn type="button" class="btn btn-success" @click.prevent="submitVideo()" v-bind:disabled="isSaveDisabled" id="btnSave">{{ submitText }}</v-btn></router-link> -->
        <!-- <v-btn type="button" class="btn btn-primary" @click.prevent="retakeVideo()" v-bind:disabled="isRetakeDisabled" id="btnRetake">Retake</v-btn> -->
    </div>
    <div v-if="$route.name =='ToHandLan'">
      <router-link to="/ToHandLanResult"><v-btn :style="{'margin-left':buttonMargin+'px'}" id="btnCapture"><v-icon size="45px">mdi-camera</v-icon></v-btn></router-link>
    </div>
    <div id="send" style="margin-top:-80px" :style="{'margin-left':(frameSize.x*0.9-305)/2+'px'}" v-if="$route.name =='FromHandLanSend'">
      <router-link to="/FromHandLan"><v-btn class="sendBtn" color="rgb(232, 107, 94)" style="width:150px;color:white; margin-right:5px; height:50px; font-size:45px; font-weight:bold; font-size:large"><v-icon>mdi-backup-restore</v-icon>다시 하기</v-btn></router-link>
      <router-link to="/FromHandLanResult"><v-btn class="sendBtn" color="rgb(54, 214, 123)" style="width:150px;color:white; height:50px; font-size:45px; font-weight:bold; font-size:large"><v-icon>mdi-check</v-icon>번역 하기</v-btn></router-link>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'
export default {
  name: "camera",
  data() {
    return {
      frameSize:{
        x:0,
        y:0,
      },
      sendWidth:0,
      buttonMargin:0,
      videoPlayer:''
    }
  },
  methods: {
    onResize(){
        this.frameSize = {x:window.innerWidth, y:window.innerHeight};
    },
    startRecording(){
      if($('#btnStartInner').css('border-radius')=='25px'){
        $('#btnStartInner').css('border-radius','0px');
      }else{
       this.$router.push('/FromHandLanSend');
      }
    },
    init() {
      if (
        "mediaDevices" in navigator &&
        "getUserMedia" in navigator.mediaDevices
      ) {
        let constraints = {
          video: {
            width: {
              min: 640,
              ideal: 1280,
              max: 1920,
            },
            height: {
              min: 360,
              ideal: 720,
              max: 1080,
            },
          },
        };
        navigator.mediaDevices.getUserMedia(constraints).then((stream) => {
          this.videoPlayer = document.querySelector("video");
          this.videoPlayer.srcObject = stream;
          this.videoPlayer.play();
        });
      } else {
        alert("Cannot get Media Devices");
      }
    },
  },
  beforeMount() {
    this.init();
    this.onResize();
  },
  beforeUpdated(){
    this.sendWidth = document.getElementById('send').offsetWidth*2+5;
    this.buttonMargin = (document.getElementById('camera').offsetWidth -100)/2;
    console.log(this.buttonMargin);
    console.log(document.getElementById('camera').offsetWidth);
  },
  mounted(){
    window.onresize=()=>{
      this.onResize();
    }
  },
  destroy(){
    this.videoPlayer.stop();
  }
};
</script>

<style lang="scss" scoped>
.camera {
  width: 100%;
  height: 100%;
  padding: 0px;
  box-sizing: border-box;

  .feed {
    display: block;
    width: 100%;
    height:100%;
    background-color: #171717;
    box-shadow: 4px 4px 12px 0px rgba(0, 0, 0, 0.3);
    margin: 0 auto;
  }
  .snap {
    display: block;
    position:fixed;
    width: 75px;
    height: 75px;
    border-radius: 50%;
    background-color: transparentize($color: #ffce00, $amount: 0.75);
    border: 1px solid color #171717;
    border-radius: 50%;
    outline: none;
    cursor: pointer;
    margin: 25px auto;

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
