<template>
  <div style="width:100%; height:100%;">
    <div style="width:100%; height:20%;">
    <div style="width:100%; height:50%"></div>
      <div id="search" :style="{'margin-left':searchMargin+'px'}" style="width: 100%; 
height: 50px; 
max-width:550px; 
background-color: rgb(243, 242, 242); border-radius: 45px; 
padding:10px 10px 10px 30px;">
        <v-icon size="30" style="float:left;margin-right:20px;">mdi-magnify</v-icon>
        <input v-model="attr" placeholder="수어로 번역할 한글을 입력해주세요." type="text" style="height:100%; overflow:hidden;float:left;" :style="{width:'50%'}">
        
        <v-btn
        style="float:right; text-align:center;width:30px; height:30px; background-color:white; border-radius:15px;"
          @click="transButton"
        >
          <v-icon>mdi-arrow-right</v-icon>
        </v-btn>
      </div>
  </div>
  <div style="width:100%;height:80%;">
    <v-row  style="width:100%; height:100%; margin:0px;" justify="center">
    <div  style="height:100%; width:100%; padding-top:1%;">
      <v-row :style="{display:isopened,width:frameSize.x*0.9+'px'}" style="margin-left:0px; margin-top:65px;;height:5%; min-height:500px; min-width:300px; position: fixed; z-index:2;" justify="center">
      <div  style=" height:100%; width:100%;">
        <video :src="`/video/${videoSrc}`" style="width:100%; height:50%; background-size: contain;" autoplay></video>
        <!-- <v-img
      src="../../assets/HandLan/result.png"
      width="100%"
      height="50%"
      style="background-size: contain;"
    ></v-img> -->
    <div style="width:100%; height:50%;">
      <div style="margin:10px 0px; font-weight:bold; font-size:larger; text-align:center;">{{attr}}에 대한 수어</div>

    <v-card-subtitle style="overflow:auto; text-align:center;     height: 117px; ">
      왼쪽 검지와 오른쪽 검지를 뻗는다.<br>
      두 손가락을 마주보게하고 오른쪽 손이 위로 오게 한다.
    </v-card-subtitle>
    <div style="width:100%; height: 50px; text-align: center;">
      <v-btn @click="addVoca"  color="rgb(57 181 111)" style="color:white; height:50px; font-size:45px; font-weight:bold; font-size:large"><v-icon>mdi-plus</v-icon>내 노트에 추가하기</v-btn>
    </div>
    </div>
      </div>
      </v-row>
      <v-row style="height:100%;" justify="center">
      <img style="height:100%;z-index:0;" :src="require('../../assets/dictionary_'+this.search+'.png')">
      </v-row>
    </div>
  </v-row>
  </div>
    <!-- <camera id="camera" style="height:80%; max-width:500px; max-height:800px; display:fixed; max-width:550px;" :style="{'margin-left':searchMargin+'px','margin-top':(frameSize.y*0.9-cameraHeight)/2+'px'}"></camera> -->
  </div>
</template>

<script>
import axios from 'axios'
// import Camera from '../../components/Camera.vue'
export default {
  // components:{Camera},
  data() {
    return {
      translateSearch:'',
      frameSize:{
        x:0,
        y:0,
      },
      searchSize : 0,
      cameraWidth:500,
      cameraHeight:800,
      attr:'',
      showSearchResult:'none',
      searchMargin:0,
      search:'close',
      isopened : 'none',
      videoSrc : ''
    }
  },
  methods: {
    onResize(){
        this.frameSize = {x:window.innerWidth, y:window.innerHeight};
    },
    transButton(){
      if(this.attr ==''){
        alert('검색할 단어를 입력해주세요');
      }else{
        this.showSearchResult = 'block';
        this.search = 'open';
        this.isopened = 'block';

        axios.get(`http://localhost:8000/api/ai/word`,{ params : {text : this.attr}}).then(res=>{
          console.log(res)
          this.videoSrc = res.data;
        });

      }
    },
    closeSearchResult(){
      this.showSearchResult = 'none';
    },
    addVoca() {
      var user_id;
      window.Kakao.API.request({
        url: "/v1/user/access_token_info",
        success: res => {
          user_id = res.id;
          console.log("token", user_id);
          axios
            .post(`https://j3b105.p.ssafy.io/api/users/voca`, {
              user_id: res.id,
              word: this.attr,
              video: "test"
            })
            .then(res => {
              console.log(res);
              console.log("단어 등록 완료");
              alert("내 단어장에 추가가 완료되었습니다. 내 단어장에서 확인해주세요.")
            });
        }
      });
    },
  },
  beforeMount() {
    this.onResize();
     window.onresize=()=>{
      this.onResize();
      this.frameSize = {x:window.innerWidth, y:window.innerHeight};
      console.log(document.getElementById('search'));
      this.cameraWidth = document.getElementById('camera').offsetWidth;
      this.cameraHeight = document.getElementById('camera').offsetHeight;
      this.searchMargin = document.getElementById('search').offsetWidth;
      console.log(this.cameraWidth);
      console.log(this.searchSize);
        }
  },
  
  mounted(){
      this.onResize();
      this.searchMargin = (this.frameSize.x*0.9-this.serachMargin)/2;
      if(this.frameSize.x>550){
        this.searchSize = 550;   

      }else{
        this.searchSize = this.frameSize.x*0.9;
      }
      this.searchMargin = (this.frameSize.x*0.9-this.searchSize)/2;
      console.log(this.searchMargin+" "+this.searchSize);
    window.onresize=()=>{
      this.onResize();
      this.frameSize = {x:window.innerWidth, y:window.innerHeight};
      console.log(document.getElementById('search'));
      if(this.frameSize.x>550){
        this.searchSize = 550;   
      }else{
        this.searchSize = this.frameSize.x*0.9;
      }     
      this.searchMargin = (this.frameSize.x*0.9-this.searchSize)/2; 
      this.cameraWidth = document.getElementById('camera').offsetWidth;
      this.cameraHeight = document.getElementById('camera').offsetHeight;
      console.log(this.cameraWidth);
      console.log(this.searchSserachMarginize);
      console.log(this.frameSize.x+"곱하기"+this.serachMargin+" "+this.serachMargin);
        }
  },
}
</script>

<style>
#searchResult{
  width:100%;
}
.v-image__image--cover {
    background-size: contain;
}
</style>