<template>
  <div>
      <button class="record" @click="record()" id="btn-start-recording">녹화</button>
      <button class="stop" @click="stop()" id="btn-stop-recording">멈춤</button>
<hr>
<video id="my-preview" autoplay></video>
<video id="preview" controls autoplay></video>
<!-- <video style="width:50%; height:90%;" autoplay ref="video" id="video" class="video"></video> -->
<!-- <video style="width:100%; height:100%;" controls autoplay ref="video" id="my-preview" class="video" v-if="ok"></video> -->
  </div>
</template>

<script src="https://cdn.webrtc-experiment.com/RecordRTC.js"></script>
<script src="https://webrtc.github.io/adapter/adapter-latest.js"></script>

<script>
export default {
    name: "video",

    data(){
        return{
          video : '',
          recorder : '',
          videoPlayer:'',
          recordedBlobs:[],
        }
    },
    methods: {
      record(){
        navigator.mediaDevices.getUserMedia({
            // audio: true, 
            video: true,
        }).then((stream) => {
            // Display a live preview on the video element of the page
            // setSrcObject(stream, video);
            // this.video = document.querySelector("video");

            // this.video = document.getElementById("my-preview");
            // // console.log(this.videoPlayer)
            // this.video.srcObject = stream;
            // this.video.play();
            // video.muted = true;

            // Initialize the recorder
            this.recorder = new MediaRecorder(stream, {
                mimeType: 'video/webm',
            });

            var recordArr = [];
            var recordedVideo = document.getElementById("preview");
            console.log(recordedVideo);
            this.recorder.onstop = function(e) {
              console.log("Recorder stopped: ");
              console.log(recordArr);
              var superBuffer = new Blob(recordArr, { type: "video/webm" });
              recordedVideo.src = window.URL.createObjectURL(superBuffer);
              recordedVideo.addEventListener("loadedmetadata", function () {
                if (recordedVideo.duration === Infinity) {
                  recordedVideo.currentTime = 1e101;
                  recordedVideo.ontimeupdate = function () {
                    recordedVideo.currentTime = 0;
                    recordedVideo.ontimeupdate = function () {
                      delete recordedVideo.ontimeupdate;
                      recordedVideo.play();
                    };
                  };
                }
              });
            };
            this.recorder.ondataavailable = function(e) {
              if (e.data && e.data.size > 0) {
                recordArr.push(e.data);
              }
            };
            this.recorder.start(10); // collect 10ms of data
            console.log("MediaRecorder started", this.recorder)
        });
      },
      stop(){
          this.recorder.stop();
         }
      },
      // init(){
      //   navigator.mediaDevices.getUserMedia({
      //       // audio: true, 
      //       video: true,
      //   }).then((stream) => {
      //     this.videoPlayer = document.getElementById("my-preview");
      //     this.videoPlayer.srcObject = stream;
      //     this.videoPlayer.play();
      //   });
      // },
      
    mounted() {
      // this.init();
      navigator.mediaDevices.getUserMedia({
            // audio: true, 
            video: true,
        }).then((stream) => {
          this.videoPlayer = document.getElementById("my-preview");
          this.videoPlayer.srcObject = stream;
          this.videoPlayer.play();
        });
        // this.videoPlayer = document.querySelector('video');
    },
};
</script>

<style lang="scss" scoped>

  .record {
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
    .stop{
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

</style>