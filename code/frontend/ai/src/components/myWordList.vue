<template>
  <div class="note_container" style="width:100%; padding-top:150px;">
        <div style="width:100%;height:470px; position:relative;">
            <div v-for="(word,index) in paginatedData" :key="index" style="position:relative;height:50px; width:100%; margin-bottom:10px;">
        <v-row justify="center" style="width:100%; ">
            <div style="width:100%; max-width:400px; padding-left:20px; border-bottom: 1px solid #8080803b;">
                <div style="float:left; width:150px;; overflow:hidden;height:100%; padding:10px 0px;">{{word.word}}</div>
                <div style="float:right;width:200px;;">
                <div style="float:right"><v-btn color="#e06363" style="margin:0px 10px; font-weight: bold; color: white; text-shadow: 1px 1px 10px #00000059;" @click="deleteVoca(word.id)">삭제</v-btn></div>
                <div style="float:right"><v-btn color="#5ece5a" style="font-weight: bold; color: white; text-shadow: rgb(0 0 0 / 60%) 1px 1px 6px;" @click="showHandLan(word.id)">수화보기</v-btn></div>
                </div>
            </div>
        </v-row>
                </div>
            </div>

      <v-row justify="center">
      <button :disabled="pageNum === 0" @click="prevPage" class="page-btn" style="cursor:pointer;">
        <v-icon size="40px">mdi-arrow-left-drop-circle</v-icon>
      </button>
          <span style=" font-weight: bold;" class="page-count">{{ pageNum + 1 }} / {{ pageCount }}</span>
      <button :disabled="pageNum >= pageCount - 1" @click="nextPage" class="page-btn" style="cursor:pointer;">
        <v-icon size="40px">mdi-arrow-right-drop-circle</v-icon>
      </button>
      </v-row>
  </div>
</template>

<script>
export default {
data () {
    return {
       frameSize : {x:window.innerHeight*0.5625, y:window.innerHeight,per:1},
      pageNum: 0,
    //    NowClassNum:1,
        // intoFood:'egg',
        Nowgra:'',
    }
  },
  props: {
    listArray: {
      type: Array,
      required: true
    },
    pageSize: {
      type: Number,
      required: false,
      default: 7
    },
    
  },
  mounted(){
 this.onResize();

  },
  methods: {
      onResize(){
      if(window.innerHeight*0.5625 <=window.innerWidth){
        this.frameSize = {x:window.innerHeight*0.5625, y:window.innerHeight,per:innerHeight/640};
      }else{
        this.frameSize = {x:window.innerWidth, y:window.innerWidth*1.77,per:innerWidth/360};
        }
    },
    nextPage () {
      this.pageNum += 1;
    },
    prevPage () {
      this.pageNum -= 1;
    },
  },
  computed: {
    pageCount () {
      let listLeng = this.listArray.length,
          listSize = this.pageSize,
          page = Math.floor(listLeng / listSize);
      if (listLeng % listSize > 0) page += 1;
      
      /*
      아니면 page = Math.floor((listLeng - 1) / listSize) + 1;
      이런식으로 if 문 없이 고칠 수도 있다!
      */
      return page;
    },
    paginatedData () {
      const start = this.pageNum * this.pageSize,
            end = start + this.pageSize;
      return this.listArray.slice(start, end);
    }
  }
}
</script>

<style>
.note_container{
    position:relative;
    background-image: url("../assets/note.png");
    background-position: center;
    background-size: contain;
}
</style>