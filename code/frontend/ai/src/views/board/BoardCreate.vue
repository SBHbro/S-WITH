<template>
 <div style="width:100%; height:100%;">
    <v-row style="width: 100%; height: 100%; padding: 0px 2%; margin: 0px; " justify="center">
      <v-col cols="30" sm="20" md="10" lg="20">
        <!-- <v-card ref="form" cols="12" sm="10" md="8" lg="6"> -->
          <!-- <v-card-text> -->
            <div style="height:5%;" align="center">
              <router-link to="/board"><div style="float: left; color: rgb(0 0 0 / 60%); font-weight: bold; font-size: large;">
                <v-icon size="35px">mdi-chevron-left</v-icon>뒤로가기
              </div></router-link>
            </div>

    <table style="width:100%; height:85%;">
      <tr>
            <v-text-field
            style="margin:12px;"
              v-model="subject"
              :counter="20"
              label="제목을 입력해주세요"
              required
              id="subject"
              ref="subject"
            ></v-text-field>
  </tr>
  <tr width ="500" height="200">
            <v-textarea
              style= "width:100%; height:70%;"
              no-resize
              v-model="content"
              solo
              :counter="500"
              label=""
              placeholder="요청사항을 작성해주세요."
              required
              type="textarea"
              id="content"
              ref="content"
            ></v-textarea>
  </tr>
  <tr>
    <input style="width:50%; margin-left:0%; margin-top:0%; " type="file" @change="onChange($event)">
    <!-- <video style="width:50%; height:50%;" autoplay :src="image" /> -->
    <!-- <v-btn @click="uploadImage">Upload video</v-btn> -->
    <v-btn @click="removeImage">Remove video</v-btn>
  </tr>
          <!-- </v-card-text> -->
        </table>        
          <div style="height:10%;" class="form-group" align="center">
            <v-btn 
            align = "left"
            type="button" 
            color="rgb(46 179 103)"
            style=" color: white; width: 150px; height: 90%; font-size: large; font-weight: bold; text-shadow:#343a40d4 1px 1px 4px;"
    
            @click="checkHandler">등록하기</v-btn>

            <!-- <v-btn @click="clear">초기화</v-btn> -->
          </div>
        <!-- </v-card> -->
      </v-col>
    </v-row>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "boardcreate",
  data: () => ({
    items: ['naver.com', 'gmail.com', 'nate.com', 'daum.net','kakao.com'],
    notice: [],
    subject: "",
    content: "",
    email: "",
    emailDomain:"",
    image: '',
  }),

  methods: {
    checkHandler() {
      let err = true;
      let msg = "";
      err &&
        !this.subject &&
        ((msg = "제목 입력해주세요"),
        (err = false),
        this.$refs.subject.focus());
      err &&
        !this.content &&
        ((msg = "내용 입력해주세요"),
        (err = false),
        this.$refs.content.focus());
      err &&
        !this.email &&
        ((msg = "이메일을 입력해주세요"),
        (err = false),
        this.$refs.email.focus());

      if (!err) alert(msg);
      else this.createHandler();
    },
    createHandler() {
      console.log(this.email+'@'+this.emailDomain);
      axios
        .post(`https://j3b105.p.ssafy.io/api/notices/notice/create`, {
          subject: this.subject,
          content: this.content,
          email: this.email+'@'+this.emailDomain,
        })
        .then(() => {
          alert("등록이 완료되었습니다.");
          this.moveList();
        });
    },
    moveList() {
      this.$router.push("/board");
    },
    clear() {
      this.$refs.form.reset();
    },    
    removeImage: function () {
      this.image = '';
    },
    uploadImage(){
      var reader = new FileReader();
      reader.readAsDataURL(this.fileData);
      reader.onloadend = function() {
          var base64data = reader.result;
          console.log(base64data);
          axios.post(`http://localhost:8000/api/notices/upload`,{data : reader.result}).then(response=>{
              console.log(response);
            }).catch(e=>{
              console.log(e)
              // this.task = true
          })
      }
    },
    onChange(e) {
      const file = e.target.files[0];
      //   this.item.imageUrl = URL.createObjectURL(file);
      this.image = URL.createObjectURL(file);
      // this.$set(this.items[index], "file", file);
    }
  }
};
</script>

<style>
.v-text-field.v-text-field--solo:not(.v-text-field--solo-flat) > .v-input__control > .v-input__slot {
    min-height: 200px;
    box-shadow: 0px 3px 1px -2px rgba(0, 0, 0, 0.2) inset, 0px 2px 2px 0px rgba(0, 0, 0, 0.14) inset, 0px 1px 5px 0px rgba(0, 0, 0, 0.12) inset;
}
</style>