<template>
  <v-card class="overflow-hidden">
    <div style="width:100%; height:100%; background-color:#0000005c; position:fixed; z-index:2;" :style="{display:openLogin}" @click="closeLogin"></div>
    <v-app-bar
      absolute
      color="transparent"
      elevate-on-scroll
      scroll-target="#scrolling-techniques-7"
      style="z-index:100;"
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

      <v-spacer style="text-align:center;"><router-link to="/"><img src="../assets/title.png" height="50px"></router-link></v-spacer>

    </v-app-bar>
    <v-sheet
      id="scrolling-techniques-7"
      class="overflow-y-auto"
      :min-width="frameSize.x"
      :max-height="frameSize.y"
      style="z-index:0; "
    >

      <div class="background" v-if="$route.name=='Home' || $route.name=='ToHandLanChoice'" style="padding-top:64px;" :style="{width:frameSize.x+'px', height:frameSize.y+'px'}">
        <router-view></router-view>
        <!-- <v-card style="position: fixed;
    width: 800px;
    height: 200px;
    display: block;
    margin-top: -800px; z-index:3;
    margin-left: 586px;" :style="{display:openLogin}">
    <div style="width:65%; height:100%; margin-top:30px; padding-left:30px; float:left;">
      <input v-model="id" class="loginInput" placeholder="id">
      <input type="password" v-model="password" class="loginInput" placeholder="password">
    </div>  
    <div style="width:35%; height:100%; float:left; padding: 30px;">
      <v-btn style="float:left; width:100%; height:100%;">login</v-btn>
    </div>
    </v-card> -->
      </div>
      <div class="background" v-if="$route.name !='Home'&& $route.name!='ToHandLanChoice'" style=" padding-top:64px;" :style="{width:frameSize.x+'px', height:frameSize.y+'px'}">
        <div style="width:90%; height:90%; background-color:white; margin-left:5%;     border-radius: 30px;
    box-shadow: 0px 0px 27px -4openLoginpx #00000026;" :style="{'margin-top':(frameSize.y-46-(frameSize.y*0.9))/2+'px'}">
        <router-view></router-view>
        </div>
      </div>
    </v-sheet>

    <v-navigation-drawer
      v-model="drawer"
      absolute
      bottom
      temporary
      style="z-index:101;"
    >
      <v-list
        nav
        dense
      >
        <v-list-item-group
          v-model="group"
          active-class="deep-purple--text text--accent-4"
        >
        <router-link to="/toHandLan">
          <v-list-item>
            <v-list-item-title>수어로 번역하기</v-list-item-title>
          </v-list-item>
        </router-link>

        <router-link to="/fromHandLan">
          <v-list-item>
            <v-list-item-title>수어를 번역하기</v-list-item-title>
          </v-list-item>
          </router-link>

        <router-link to="/board">
          <v-list-item>
            <v-list-item-title>게시판</v-list-item-title>
          </v-list-item>
        </router-link>

        <router-link to="/upload">
          <v-list-item>
            <v-list-item-title>파일 업로드</v-list-item-title>
          </v-list-item>
        </router-link>

          <v-list-item @click="kakaoLogin">
            <v-list-item-title>로그인</v-list-item-title>
          </v-list-item>

          <v-list-item @click="kakaoLogout">
            <v-list-item-title>로그아웃</v-list-item-title>
          </v-list-item>

          <router-link to="/myNote">
          <v-list-item>
            <v-list-item-title>내 단어장</v-list-item-title>
          </v-list-item>
          </router-link>

        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </v-card>
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
      drawer: false,
      group: null,
      openLogin:'none',
      id:'',
      password:''
    }
  },
  methods: {
    onResize(){
        this.frameSize = {x:window.innerWidth, y:window.innerHeight};      
    },
    login(){
      this.openLogin = 'block';
    },
    closeLogin(){
      this.openLogin = 'none';
    },
    kakaoLogout() {
      window.Kakao.API.request({
        url: "/v1/user/unlink",
        success: res => {
          console.log("logout", res);
        }
      });
    },
    kakaoLogin() {
      // console.log(window.Kakao);
      window.Kakao.Auth.login({
        success: this.GetMe
      });
    },
    GetMe(authObj) {
      console.log("authObj", authObj);
      // 토큰 확인: 사용자의 id값 뽑아낼 때 쓰면 될듯
      window.Kakao.API.request({
        url: "/v2/user/me",
        success: res => {
          console.log("body", res);
          const kakao_account = res.kakao_account;
          console.log("카", kakao_account);
          const userInfo = {
            id: res.id,
            nickname: kakao_account.profile.nickname,
            email: kakao_account.email,
            gender: kakao_account.gender,
            birthday: kakao_account.birthday,
            age_range: kakao_account.age_range
          };

          axios
            .post(`https://j3b105.p.ssafy.io/api/users/user`, {
              id: userInfo.id,
              nickname: userInfo.nickname,
              email: userInfo.email,
              gender: userInfo.gender,
              birthday: userInfo.birthday,
              age_range: userInfo.age_range
            })
            .then(res => {
              console.log(res);
              console.log("로그인 성공");
              alert("로그인 성공!");
              console.log(res.data);
            })
            .catch(err => {
              console.log(err);
              console.log("로그인 실패");
            });

          console.log(userInfo);
          this.$bvModal.hide("bv-modal-example");
        },
        fail: error => {
          this.$router.push("/errorPage");
          console.log(error);
        }
      });
    }
  },
  mounted(){
    this.onResize();
      window.onresize=()=>{
          this.onResize();
        }
      },
  watch:{
     group () {
        this.drawer = false
      },
  }
}
</script>

<style>
.background{
  background:url('../assets/background.png') no-repeat;
  background-size: cover;
}
.loginInput{
      height: 59px;
    width: 100%;
    border-radius: 40px;
    padding: 0px 30px;
    box-shadow: 1px 1px 10px #e0e0e0 inset;
    margin-bottom:10px;
}
.loginInput:focus{
    height: 59px;
    width: 100%;
    border-radius: 40px;
    padding: 0px 30px;
    box-shadow: 1px 1px 10px #e0e0e0 inset;
    margin-bottom:10px;
}
</style>