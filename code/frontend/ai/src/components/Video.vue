<template>
  <div>
      <button class="record" @click="record()" id="btn-start-recording">녹화</button>
      <button class="stop" @click="stop()" id="btn-stop-recording">멈춤</button>
<hr>
<video id="my-preview" controls autoplay></video>
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
    // Store a reference of the preview video element and a global reference to the recorder instance
         video : '',
         recorder : '',
         videoPlayer:'',
        }
    },
     methods: {
      record(){
        // Request access to the media devices
        
        // console.log(document.getElementById('my-preview'))
        navigator.mediaDevices.getUserMedia({
            audio: true, 
            video: true,
        }).then((stream) => {
            // Display a live preview on the video element of the page
            // setSrcObject(stream, video);
            this.video = document.querySelector("video");
            console.log(this.videoPlayer)
            this.video.srcObject = stream;
            this.video.play();
            video.muted = true;

            // Initialize the recorder
            this.recorder = new RecordRTCPromisesHandler(stream, {
                mimeType: 'video/webm',
                bitsPerSecond: 128000
            });
            console.log(this.recorder)
        });
            //         // Start recording the video
            // this.recorder.startRecording().then(function() {
            //     console.info('Recording video ...');
            // }).catch(function(error) {
            //     console.error('Cannot start video recording: ', error);
            // });

            // // release stream on stopRecording
            // this.recorder.stream = stream;
      },

      stop(){
         recorder.stopRecording().then(function() {
            console.info('stopRecording success');

            // Retrieve recorded video as blob and display in the preview element
            var videoBlob = recorder.getBlob();
            video.src = URL.createObjectURL(videoBlob);
            video.play();

            // Unmute video on preview
            video.muted = false;

            // Stop the device streaming
            recorder.stream.stop();
         })}
      }, 

    //   init() {
    //   if (
    //     "mediaDevices" in navigator &&
    //     "getUserMedia" in navigator.mediaDevices
    //   ) {
    //     let constraints = {
    //       video: {
    //         width: {
    //           min: 640,
    //           ideal: 1280,
    //           max: 1920,
    //         },
    //         height: {
    //           min: 360,
    //           ideal: 720,
    //           max: 1080,
    //         },
    //       },
    //     };
    //     navigator.mediaDevices.getUserMedia(constraints).then((stream) => {
    //       this.videoPlayer = document.querySelector("video");
    //       this.videoPlayer.srcObject = stream;
    //       this.videoPlayer.play();
    //     });
    //   } else {
    //     alert("Cannot get Media Devices");
    //   }

    // },
       
    mounted() {
        // this.init();
        this.videoPlayer = document.querySelector('video');
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