<template>
  <div style="width:100%; height:100%;">
    <v-row justify="center" style="width:100%; height:10%;">
    <h2>내 단어장</h2>
    </v-row>
    <div style="width:100%; height:90%;">
      <img src="../../assets/dictionary_open.png">

    </div>
      <v-card style="height:50px;" v-for="(word,index) in mywords" :key="index">
          {{word.word}}
          <div style="float:right"><v-btn @click="deleteVoca(word.id)"><v-icon color="red">mdi-minus</v-icon></v-btn></div>
      </v-card>
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