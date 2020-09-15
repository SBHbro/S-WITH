<template>
  <div id="camera" class="camera" >
   
    <video autoplay ref="video" id="video" class="video" v-if="ok"></video>
    <button class="snap" v-on:click="capture()">SNAP</button>
    <canvas ref="canvas" class="canvas" id="canvas" width="1000" height="800"></canvas>
    <button class="send" @click="objectDetection()">물체</button>
    <button class="redo" @click="textDetection()">글자</button>

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
import axios from 'axios'
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
      videoPlayer:'',
      canvas:'',
      video:'',
      ok : true,
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
    capture(){
      this.video = this.$refs.video;
      this.canvas = this.$refs.canvas;
      this.canvas.getContext("2d").drawImage(this.video, 0, 0, 640, 480);
      //this.ok = !this.ok;
      // 캡처한거 저장하는
      // this.captures.push(this.canvas.toDataURL("image/png"));
      //
      // this.ok = 'true';
      //
    },
     objectDetection(){
      // this.canvas;
      console.log(this.canvas.toDataURL());
      axios.get('http://localhost:8000/',this.canvas.toDataURL()).then(data=>{
        console.log(data);
      })
    },
    textDetection(){
      alert('글자')
    }
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
  },
};
</script>

<style lang="scss" scoped>
.camera {
  width: 100%;
  height: 100%;
  padding: 0px;
  box-sizing: border-box;

  .video{
    display: block;
    position:fixed;
    height: 500px;
    margin-top: 10px;
    margin-right: 900px;
  }

  .canvas{
    display: block;
    position:fixed;
    width: 1050px;
    height: 840px;
    margin-top: 10px;
    margin-left: 700px;
  }
  
  .send{
    display: block;
    position:fixed;
    width: 75px;
    height: 75px;
    border-radius: 50%;
    background-color: transparentize($color: #2493dd, $amount: 0.75);
    border: 1px solid color #171717;
    border-radius: 50%;
    outline: none;
    cursor: pointer;
    margin-top: 530px;
    margin-left: 900px;

    &:hover {
      background-color: #2493dd;
    }
    &:active {
      background-color: darken($color: #2493dd, $amount: 10);
    }
  }

  .redo{
    display: block;
    position:fixed;
    width: 75px;
    height: 75px;
    border-radius: 50%;
    background-color: transparentize($color: #fd3015, $amount: 0.75);
    border: 1px solid color #171717;
    border-radius: 50%;
    outline: none;
    cursor: pointer;
    margin-top: 530px;
    margin-left: 1000px;

    &:hover {
      background-color: #fd3015;
    }
    &:active {
      background-color: darken($color: #fd3015, $amount: 10);
    }
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
    margin-top: 530px;
    margin-left: 250px;

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