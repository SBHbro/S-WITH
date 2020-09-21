<template>
 <div>
    <v-row justify="center">
      <v-col cols="30" sm="20" md="10" lg="20">
        <!-- <v-card ref="form" cols="12" sm="10" md="8" lg="6"> -->
          <!-- <v-card-text> -->

            <div align="center">
              <h2>새 글 등록하기</h2>
            </div>

            <v-divider class="mt-20"></v-divider>

<table>
  <tr>
            <v-text-field
              v-model="subject"
              :counter="20"
              label="제목"
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
              outlined
              :counter="500"
              label=""
              placeholder="내용을 작성해주세요."
              required
              type="textarea"
              id="content"
              ref="content"
            ></v-textarea>
  </tr>
  <tr>
            <v-text-field
              v-model="email"
              :counter="20"
              label="이메일"
              required
              id="email"
              ref="email"
            ></v-text-field>
</tr>
          <!-- </v-card-text> -->
</table>        
          <v-divider class="mt-20"></v-divider>

          <div class="form-group" align="center">
            <v-btn 
            align = "left"
            type="button" 
            @click="checkHandler">등록</v-btn>

            <v-btn @click="clear">초기화</v-btn>
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
    notice: [],
    subject: "",
    content: "",
    email: "",
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
      axios
        .post(`http://j3b105.p.ssafy.io/api/notices/notice/create`, {
          subject: this.subject,
          content: this.content,
          email: this.email,
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
    }
  }
};
</script>

<style>

</style>