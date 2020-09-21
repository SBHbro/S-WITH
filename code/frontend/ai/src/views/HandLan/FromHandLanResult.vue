<template>
  <div style="width:100%; height:100%;">
        <div id="textbox" style="text-align:center;" :style="{'padding-top':(frameSize.y*0.9-textHeight-80)/2+'px'}">
            <div style="font-size:57px; font-weight: bold;     margin-bottom: 50px"><button @click="textToSound"><v-icon size="57px" id="speaker" v-text="speaker" :color="spaekerColor"></v-icon></button>{{transResult}}</div>
            <div style="width:100%;">
                <v-btn class="btnText" style="width:50%; height: 46px; margin:10px 0px; max-width:500px; font-size: large; min-width: 250px; color:white;" color="rgb(232, 107, 94)"><v-icon color="white">mdi-alert-circle</v-icon>구급 메세지 보내기<v-icon color="white">mdi-email</v-icon></v-btn>
            </div>
            <div style="width:100%;">
                <router-link to="/fromHandLan"><v-btn class="btnText" style="width:24.5%;height: 46px; font-weight: bold; font-size: large; color:white; margin-right:1%; max-width:250px; min-width: 124px;" color="rgb(54, 214, 123)"><v-icon color="white">mdi-refresh</v-icon>다시하기</v-btn></router-link>
                <router-link to="/"><v-btn class="btnText" style="width:24.5%; font-weight: bold; height: 46px; font-size: large; max-width:250px; color:white; min-width: 124px;" color="rgb(228, 184, 244)"><v-icon color="white">mdi-home</v-icon>홈으로</v-btn></router-link>
            </div>
        </div> 
  </div>
</template>

<script>
// import Vue2Tts from 'vue2-tts'
// import axios from 'axios'

export default {
    components: {
        // 'vue2-tts': Vue2Tts
    },
    data() {
        return {
            transResult:'화상을 입었어요.',
            responsiveVoice:'',
            speaker:'mdi-volume-medium',
            spaekerColor:'gray',
            textWidth:0,
            textHeight:0,
            frameSize:{
                    x:0,
                    y:0,
            }
        }
    },
    beforeCreate(){
        const textToSpeech = require('@google-cloud/text-to-speech');

        // Import other required libraries
        const fs = require('fs');
        const util = require('util');
        // Creates a client
        const client = new textToSpeech.TextToSpeechClient();
        this.quickStart(fs,util,client); 

    },
    beforeUpdate(){
        this.textWidth = document.getElementById('textbox').offsetWidth;
        this.textHeight = document.getElementById('textbox').offsetHeight;
        console.log(this.textHeight);
    },
    mounted(){
    this.onResize();
      window.onresize=()=>{
          this.onResize();
        }
      },
    methods:{
        textToSound(){
            this.speaker = 'mdi-volume-high';
            this.spaekerColor = 'blue';
            this.quickStart()
        },
        test() {
                // code
        },
        onResize(){
            this.frameSize = {x:window.innerWidth, y:window.innerHeight};
        },
        async quickStart(fs,util,client) {
        // The text to synthesize
        const text = 'hello, world!';

        // Construct the request
        const request = {
            input: {text: text},
            // Select the language and SSML voice gender (optional)
            voice: {languageCode: 'en-US', ssmlGender: 'NEUTRAL'},
            // select the type of audio encoding
            audioConfig: {audioEncoding: 'MP3'},
        };

        // Performs the text-to-speech request
        const [response] = await client.synthesizeSpeech(request);
        // Write the binary audio content to a local file
        const writeFile = util.promisify(fs.writeFile);
        await writeFile('output.mp3', response.audioContent, 'binary');
        console.log('Audio content written to file: output.mp3');
        }
    }
}
</script>

<style>
.btnText{
    color: white;
    font-weight: bold;
    font-size: large;
    text-shadow: 1px 1px 2px #00000063;
}
</style>