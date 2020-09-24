<template>
  <div style="width:100%; height:100%;">
    <div @click="closeSearchResult" style="width: 100%;
    height: 100%;
    position: fixed;
    background-color: #0000008c;
    display: block;
    z-index: 1;" :style="{display:showSearchResult,'margin-left':'-'+frameSize.x*0.05+'px'}"></div>
    <div style="width:100%; height:10%"></div>
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
      
      <v-card id="searchResult" style="z-index:2; width:100%; position:relative;"
      :style="{height:frameSize.y*0.6+'px',display:showSearchResult}"
      >
    <v-img
      src="../../assets/HandLan/result.png"
      width="100%"
      height="50%"
      style="background-size: contain;"
    ></v-img>
    <div style="width:100%; height:50%;">
    <v-card-title>
      <div style="margin:10px 0px; font-weight:bold; font-size:larger;">{{attr}}에 대한 수어</div>
    </v-card-title>

    <v-card-subtitle style="overflow:auto;">
      왼쪽 검지와 오른쪽 검지를 뻗는다.<br>
      두 손가락을 마주보게하고 오른쪽 손이 위로 오게 한다.
    </v-card-subtitle>
    <div style="width:100%; height: 50px; position:absolute; bottom:0; float:right;">
      <v-btn @click="closeSearchResult">닫기</v-btn>
    </div>
    </div>
  </v-card>
    <!-- <camera id="camera" style="height:80%; max-width:500px; max-height:800px; display:fixed; max-width:550px;" :style="{'margin-left':searchMargin+'px','margin-top':(frameSize.y*0.9-cameraHeight)/2+'px'}"></camera> -->
  </div>
</template>

<script>
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
      }
    },
    closeSearchResult(){
      this.showSearchResult = 'none';
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