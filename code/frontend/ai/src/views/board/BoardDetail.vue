<template>
  <div style="width:100%; height:100%;">
    <v-row style="width:100%; height:100%;overflow-y:scroll; overflow-x:hidden;" justify="center">
      <v-col cols="30" sm="20" md="10" lg="10">
            <div style="height:10%; min-height:35px;" align="center">
              <router-link to="/board"><div style="float: left; color: rgb(0 0 0 / 60%); font-weight: bold; font-size: large;">
                <v-icon size="35px">mdi-chevron-left</v-icon>뒤로가기
              </div></router-link>
            </div>
            <div style="height:10%;border-bottom:1px solid rgba(0, 0, 0, 0.12);" align="center">
              <h3>{{subject}}</h3>
              <div v-if="$store.state.userinfo.id==this.id" style=" margin-top:-25px; float:right;">
               <div class="modify btn" style="" @click="moveUpdate">수정</div>
               <div class="delete btn" @click="Delete">삭제</div>
              </div>
            </div>
            <div style="height:8%; width:100%; border-bottom:1px solid rgba(0, 0, 0, 0.12);     padding: 8px 0px;">     
              <div style=" width:50%; float:left;">글쓴이 : {{email}}</div> 
              <div style="width:50%; float:right;text-align:right;">{{date}} 작성</div>              
            </div>
            <div style="width:100%; height:68%; padding:15px;">{{content}}</div>
           
            <div>
              
            </div>

            <div class="replyinput">
              <input v-model="thisReply" style="border:1px solid rgba(0, 0, 0, 0.12); height:45px; width:90%; background-color:white; float:left;" placeholder="댓글을 입력해주세요.">
              <v-btn @click="addReply"
            style="height:45px; width:9%;border-color: transparent; float: left; color: white; font-weight: bold; font-size: small; text-shadow: 1px 1px 5px #0000006b;"
            type="button"
            class="btn btn-sm"
            color="rgb(98 149 232)"
            >등록</v-btn>
            </div>
            <div class="reply" v-for="(re,index) in reply" :key="index">
              <div style="width:100%; height:40%;">
                <div style="float: left; width: 50%; padding: 2px 5px; font-weight: 500; color: #000000ad; font-size: 18px;">{{re.user_id}}</div>
                <div style="float: right; width: 50%; text-align: right; font-size: 12px; color: #00000082; padding: 6px 31px;"> {{re.date}}</div></div>
              <div style="width:100%; height:60%;"> {{re.content}} </div>
            </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import store from '../../store'
import axios from "axios";
export default {
  name: "boarddetail",
  data: () => ({
    board: [],
    id: "",
    subject: "",
    content: "",
    email:"",
    date: "",
    reply:[],
    thisReply:""
  }),

  created() {
    var id = this.$route.params.id;
    this.selectNoticeReply();
    axios
      .get(
        `https://j3b105.p.ssafy.io/api/notices/notice/${id}`)
      .then(({ data }) => {
        this.id = data.id;
        this.subject = data.subject;
        this.content = data.content;
        this.email = store.state.userinfo.email;
      });
  },

  methods: {
    moveList() {
      this.$router.push("/board");
    },
    moveUpdate() {
      this.$router.push("/board/update/" + this.id);
    },
    Delete() {
      // this.$router.push("/board/delete/" + this.id);
      var id = this.$route.params.id;
      axios
      .delete(
        `https://j3b105.p.ssafy.io/api/notices/notice/delete/${id}`
      )
      .then(() => {
        alert("게시글이 삭제되었습니다");
        this.$router.push("/board");
      });
    },
    addReply() {
      var notice_num = 8;
      window.Kakao.API.request({
        url: "/v1/user/access_token_info",
        success: res => {
          axios
            .post(`https://j3b105.p.ssafy.io/api/notices/reply`, {
              user_id: res.id,
              notice_id: notice_num,
              content: this.thisReply
            })
            .then(res => {
              console.log(res);
              console.log("댓글 등록 완료");
              this.selectNoticeReply();
            });
        }
      });
    },
    selectNoticeReply() {
      window.Kakao.API.request({
        url: "/v1/user/access_token_info",
        success: () => {
          axios
            .get(`https://j3b105.p.ssafy.io/api/notices/notice/reply/${this.id}`)
            .then(response => {
              console.log(response);
              this.reply = response.data;
              console.log(this.reply);
              console.log("한 게시글에 대한 댓글 가져오기 완료");
            });
        }
      });
    },
  }
};
</script>

<style scoped>
.btn{
  display:inline-block;
  margin:0px 4px;
  height:100%;
}
.delete{
  color:#b72626;
}
.modify{
  color:#148843;
}
.replyinput{
    width: 100%;
    height: 65px;
    background-color: #80808021;
    border-top: 1px solid rgba(0, 0, 0, 0.12);
    border-bottom: 1px solid rgba(0, 0, 0, 0.12);
    padding:10px;
}
.reply{
  height:80px;
  width:100%;
  border-bottom: 1px solid rgba(0, 0, 0, 0.10);
}
</style>