<template>
  <div style="width:100%; height:100%; padding-top:50px;">
      <div id="search" :style="{'margin-left':(frameSize.x*0.9-searchSize)/2+'px'}">
        <v-icon size="30" style="float:left;margin-right:20px;">mdi-magnify</v-icon>
        <input v-bind="translateSearch" placeholder="검색할 단어를 입력해주세요." type="text" style="height:100%; overflow:hidden;float:left;" :style="{width:searchSize-150+'px'}">
        
        <v-dialog v-model="dialog" scrollable max-width="300px">
      <template v-slot:activator="{ on, attrs }">
        <v-btn
        style="float:right; text-align:center;width:30px; height:30px; background-color:white; border-radius:15px;"
          v-bind="attrs"
          v-on="on"
          @click="transButton"
        >
          <v-icon>mdi-arrow-right</v-icon>
        </v-btn>
      </template>
      
      <v-card
      :style="{width:frameSize.x*0.8+'px'}"
      >
    <v-img
      src="../../assets/HandLan/result.png"
      height="200px"
    ></v-img>

    <v-card-title>
      <div style="margin:10px 0px; font-weight:bold; font-size:larger;">{{translateSearch}}에 대한 수어</div>
    </v-card-title>

    <v-card-subtitle>
      왼쪽 검지와 오른쪽 검지를 뻗는다.<br>
      두 손가락을 마주보게하고 오른쪽 손이 위로 오게 한다.
    </v-card-subtitle>
      

  </v-card>
    </v-dialog>
      </div>
      <camera id="camera" style="width:60%; height:80%; max-width:500px; max-height:800px;" :style="{'margin-left':(frameSize.x*0.9-cameraWidth)/2+'px','margin-top':(frameSize.y*0.9-cameraHeight)/2+'px'}"></camera>
      
  </div>
</template>

<script>
import Camera from '../../components/Camera.vue'

export default {
  components:{Camera},
  data() {
    return {
      translateSearch:'',
      frameSize:{
        x:0,
        y:0,
      },
      searchSize : 550,
      cameraWidth:500,
      cameraHeight:800,
    }
  },
  methods: {
    onResize(){
        this.frameSize = {x:window.innerWidth, y:window.innerHeight};
    },
  },
  beforeMount() {
    this.onResize();
     window.onresize=()=>{
      this.onResize();
      this.frameSize = {x:window.innerWidth, y:window.innerHeight};
      console.log(document.getElementById('search'));
      this.searchSize = document.getElementById('search').offsetWidth;      
      this.cameraWidth = document.getElementById('camera').offsetWidth;
      this.cameraHeight = document.getElementById('camera').offsetHeight;
      console.log(this.cameraWidth);
      console.log(this.searchSize);
        }
  },
  beforeUpdated(){
    this.searchSize = document.getElementById('search').offsetWidth;      
      this.cameraWidth = document.getElementById('camera').offsetWidth;
      this.cameraHeight = document.getElementById('camera').offsetHeight;
  },
  mounted(){
        this.onResize();
    window.onresize=()=>{
      this.onResize();
      this.frameSize = {x:window.innerWidth, y:window.innerHeight};
      console.log(document.getElementById('search'));
      this.searchSize = document.getElementById('search').offsetWidth;      
      this.cameraWidth = document.getElementById('camera').offsetWidth;
      this.cameraHeight = document.getElementById('camera').offsetHeight;
      console.log(this.cameraWidth);
      console.log(this.searchSize);
        }
  },
}
</script>

<style>
#search{
width: 80%; 
height: 50px; 
max-width:550px; 
background-color: rgb(243, 242, 242); border-radius: 45px; 
padding:10px 10px 10px 30px;
}
</style>