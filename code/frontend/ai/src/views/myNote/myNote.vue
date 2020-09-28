<template>
  <div style="width:100%; height:100%;">
    <v-row justify="center" style="width:100%; height:10%;">
    <h2>내 단어장</h2>
    </v-row>
    <v-row justify="center" style="width:100%; height:90%;">
      <img style="height:100%; width:auto; position:relative;" src="../../assets/dictionary_open.png">
      <div style="position: absolute; height: 50%; width: auto; margin: 116px;">
      <div style="position:relative;height:50px; width:350px;border-bottom: 1px solid #8080803b; margin-bottom:10px;" v-for="(word,index) in mywords" :key="index">
         <div style="float:left; width:150px;; overflow:hidden;height:100%; padding:10px 0px;">{{word.word}}</div>
        <div style="float:right;width:200px;;">
        <div style="float:right"><v-btn color="#e06363" style="margin:0px 10px; font-weight: bold; color: white; text-shadow: 1px 1px 10px #00000059;" @click="deleteVoca(word.id)">삭제</v-btn></div>
         <div style="float:right"><v-btn color="#5ece5a" style="font-weight: bold; color: white; text-shadow: rgb(0 0 0 / 60%) 1px 1px 6px;" @click="showHandLan(word.id)">수화보기</v-btn></div>
        </div>
        </div>
      </div>
    </v-row>
      
  </div>
</template>

<script>
import axios from 'axios'
export default {
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
  created(){
    this.selectVocaList();
  }
}
</script>

<style>

</style>