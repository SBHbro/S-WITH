<template>
  <div>
      <div>
          <div>
              <!-- <input :onclick="responsiveVoice.speak(transResult)" type='button' value='???? Play' /> -->
              <!-- <div><vue2-tts v-model="transResult"><button class="btn btn-primary btn-sm" type="button" @click="test">Test</button></vue2-tts></div> -->
              <div>{{transResult}}</div>
              <v-btn color="rgb(232, 107, 94)"><v-icon color="white">mdi-alert-circle</v-icon>구급 메세지 보내기<v-icon color="white">mdi-email</v-icon></v-btn>
              <router-link to="/fromHandLan"><v-btn color="rgb(54, 214, 123)"><v-icon color="white">mdi-refresh</v-icon>다시하기</v-btn></router-link>
                <router-link to="/"><v-btn color="rgb(228, 184, 244)"><v-icon color="white">mdi-home</v-icon>홈으로</v-btn></router-link>
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
            transResult:'화상을 입었어요',
            responsiveVoice:''
        }
    },
    beforeCreate(){
        // axios.get('http://code.responsivevoice.org/responsivevoice.js')
        // .then(response=>{
        //     console.log(response)
        // })
        // .catch(e=>{
        //     console.log('error:',e)
        // })
    },
    methods:{
        test() {
                // code
            }
    }
}
</script>

<style>

</style>