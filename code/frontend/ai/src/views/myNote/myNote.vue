<template>
  <div style="width:100%; height:100%;">
    <v-row justify="center" style="width:100%; height:10%;  margin:0px;">
    <h2>내 단어장</h2>
    </v-row>
    <v-row justify="center" style="width:100%; height:90%; margin:0px;">
      <div style="height:100%; width:100%; position:relative;"><my-word-list style="height:100%;width:100%;" :list-array="mywords"></my-word-list></div>
    </v-row>
      
  </div>
</template>

<script>
import axios from 'axios'
import MyWordList from '../../components/myWordList.vue'

export default {
  components:{MyWordList},
data() {
    return {
      frameSize:{
        x:0,
        y:0,
      },
      mywords:[]
    }
  },
  methods: {
    onResize(){
        this.frameSize = {x:window.innerWidth, y:window.innerHeight};
    },
selectVocaList() {
      window.Kakao.API.request({
        url: "/v1/user/access_token_info",
        success: res => {
          axios
            .get(`https://j3b105.p.ssafy.io/api/users/user/voca/${res.id}`)
            .then(response => {
              console.log(response);
              this.mywords = response.data;
              console.log("유저의 단어 전부 가져오기 완료");
            });
        }
      });
    },
    deleteVoca(voca_id) {
      window.Kakao.API.request({
        url: "/v1/user/access_token_info",
        success: () => {
          axios
            .delete(`https://j3b105.p.ssafy.io/api/users/voca/${voca_id}`)
            .then(res => {
              console.log(res);
              console.log("단어 삭제 완료");
              this.selectVocaList();
            });
        }
      });
    },
  },
  mounted(){
    this.onResize();
  },
  created(){
    this.selectVocaList();
  }
}
</script>

<style>

</style>