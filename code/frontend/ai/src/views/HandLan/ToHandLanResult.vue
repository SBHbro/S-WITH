<template>
  <div style="width:100%;height:100%;">
      <v-card style="width:50%;height:100%; display:inline-block; float:left;">
        <router-link to="/toHandLan"><v-btn style="position: absolute;
    margin: 5px; height:60px; width:60px; text-align:center;"><v-icon size="50px">mdi-replay</v-icon></v-btn></router-link>
        <img :src="objectImage" style="width:100%; height:100%;" v-if="change">
        <img :src="textImage" style="width:100%; height:100%;" v-if="!change">
      </v-card>
      <v-card style="width:50%; height:100%; display:inline-block;">
      <v-tabs
          v-model="tabs"
          fixed-tabs
        >
          <v-tabs-slider></v-tabs-slider>
          <v-tab
            href="#mobile-tabs-5-1"
            class="primary--text"
            @click="tabChange(1)"
          >
            <v-icon>mdi-vector-rectangle</v-icon>물체
          </v-tab>

          <v-tab
            href="#mobile-tabs-5-2"
            class="primary--text"
            @click="tabChange(2)"
          >
            <v-icon>mdi-pencil</v-icon> 글씨
          </v-tab>
        </v-tabs>
      <v-tabs-items v-model="tabs">
      <v-tab-item
        v-for="i in 2"
        :key="i"
        :value="'mobile-tabs-5-' + i"
      >
        <v-card flat>
          <div v-if="i==1">
            <v-card v-for="(result,index) in objects" style="margin:10px; display:block;" :key="index">
              <img style="width:80px; height:80px; margin:5px; display:inline-block;" :src="result.src">
              <div style="display:inline-block;">{{result.transResultLetter}}</div>
              <v-dialog v-model="dialog" scrollable max-width="300px">
      <template v-slot:activator="{ on, attrs }">
        <v-btn
        style="float:right;"
          v-bind="attrs"
          v-on="on"
          @click="transButton(result)"
        >
          <v-icon>mdi-hand-pointing-right</v-icon>수화 보기<v-icon>mdi-hand-pointing-left</v-icon>
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
      <div style="margin:10px 0px; font-weight:bold; font-size:larger;">{{nowTransLate.transResultLetter}}에 대한 수어</div>   
    </v-card-title>

    <v-card-subtitle>
      왼쪽 검지와 오른쪽 검지를 뻗는다.<br>
      두 손가락을 마주보게하고 오른쪽 손이 위로 오게 한다.
    </v-card-subtitle>
      

  </v-card>
    </v-dialog>
            </v-card>
          </div>
          
          
          <div v-if="i==2" >
            <v-card v-for="(result,index) in letters" :key="index" style="height: 50px;
              margin: 5px 0px;
              padding:6px 8px;
              font-weight: bold;
              font-size: x-large;">
    <div style="float:left;width:80%;text-align:center;">
              {{result.transResultLetter}}
              </div>
              <v-btn
        style="float:right; width:20%;"
          v-bind="attrs"
          v-on="on"
          @click="transButton(result)"
        >
          <v-icon>mdi-hand-pointing-right</v-icon>수화 보기<v-icon>mdi-hand-pointing-left</v-icon>
        </v-btn>
            </v-card>
          </div>
        </v-card>
      </v-tab-item>
    </v-tabs-items>
  </v-card>
      
      <v-row justify="center">
    
  </v-row>
  </div>
</template>

<script>


export default {
  data() {
    return {
        transResultIMG:'../assets/photoresult.jpg',
        responsiveVoice:'',
          dialogm1: '',
          frameSize:{
          x:0,
          y:0,
        },
        nowTransLate:'',
        dialog: false,
        tabs: ['objects','letters'],
        objects:[
        ],
        letters:[
        ],
        objectImage : '',
        textImage : '',
        change : true,

    }
        
    },
    methods: {
      onResize(){
          this.frameSize = {x:window.innerWidth, y:window.innerHeight};
      },
      transButton(nowTrans){
        this.nowTransLate = nowTrans;
        console.log(nowTrans)
      },
      tabChange(type){
        if(type == 1){
          this.change = true;
        } else {
          this.change = false;
        }
        
      }
    },
    mounted(){
    window.onresize=()=>{
      this.onResize();
    }
    console.log(this.$route.params.oList);
    console.log(this.$route.params.tList);
    if(this.$route.params.tList){
      this.$route.params.oList.data.forEach(object => {
        // console.log(object);
        this.objects.push({src : 'data:image/jpeg;base64,'+object.src,transResultLetter: object.label})
      });
    } else {
      this.objects.push({src : '', transResultLetter : '물체를 찾을 수 없습니다.'})
    }
    if(this.$route.params.tList){
      this.$route.params.tList.data.forEach(letter => {
        console.log(letter);
        this.letters.push({transResultLetter: letter})
      });
    } else {
        this.letters.push({transResultLetter: '단어를 찾을 수 없습니다.'})
    }
    this.objectImage = this.$route.params.objectImage;
    this.textImage = this.$route.params.textImage;
  },
}
</script>

<style>
.v-toolbar__content{
  height:0px;
}
</style>