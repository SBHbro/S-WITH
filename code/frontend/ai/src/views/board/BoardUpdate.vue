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
  <tr width ="500" height="300">
            <v-textarea
              style= "width:100%; height:100%;"
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
  <tr style="width:80%; margin-left:10%;">
            <v-text-field
            style="width:38%;float:left"
              v-model="email"
              :counter="20"
              label="아이디를 적어주세요."
              required
              id="email"
              ref="email"
            ></v-text-field><div style="float: left; width: 4%; font-size: xx-large; font-weight: 700; color: #00000078;">@</div>
            <v-col class="d-flex" cols="12" sm="6">
        <v-select
        style="width:58%;float:left; margin:0px; padding:0px;"
          :items="items"
          v-model="emailDomain"
          label="이메일을 선택해주세요."
          Standard
        ></v-select>
      </v-col>
          </tr>
          <!-- </v-card-text> -->
        </table>        
          <div style="height:10%;" class="form-group" align="center">
            <v-btn 
            align = "left"
            type="button" 
            color="rgb(54, 214, 123)"
            style=" color: white; width: 150px; height: 90%; font-size: large; font-weight: bold; text-shadow:#343a40d4 1px 1px 4px;"
    
            @click="checkHandler">수정하기</v-btn>

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
  name: "boardupdate",
  data: () => ({
    board: [],
    id: "",
    subject: "",
    content: "",
    email: "",
    image: '',
    date: "",
    reply:[],
    thisReply:""
  }),

  created() {
    var id = this.$route.params.id;
    axios
      .get(
        `https://j3b105.p.ssafy.io/api/notices/notice/${id}`)
      .then(({ data }) => {
        console.log(data);
        this.id = data.id;
        this.subject = data.subject;
        this.content = data.content;
        this.email = data.email;
          var dateBefore = data.date;
          var date = dateBefore.split("T")[0];
          date = date + " ";
          date = date + dateBefore.split("T")[1].split(".")[0];
        this.date = date;
      });
  },

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
      else this.updateHandler();
    },

    updateHandler() {
      var id = this.$route.params.id;
      axios
        .put(`https://j3b105.p.ssafy.io/api/notices/notice/${id}`, {
          subject: this.subject,
          content: this.content,
          email: this.email
        })
        .then(() => {
          alert("수정이 완료되었습니다.");
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
      // var reader = new FileReader();
      // reader.readAsDataURL(superBuffer); 
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

</style>