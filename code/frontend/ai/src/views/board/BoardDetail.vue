<template>
  <div>
    <v-row justify="center">
      <v-col cols="30" sm="20" md="10" lg="10">
            <div align="center">
              <h2>글 상세보기</h2>
            </div>
            <v-divider class="mt-20"></v-divider>

            <div>
              <table>
               <tr>
                <td>        
                  <v-col cols="12" sm="10" md="8">
                     <v-text-field
                        label=""
                         filled
                         rounded
                         dense
                         readonly
                         v-model="subject"
                      ></v-text-field>
                   </v-col>
        </td>
                <td>                  
                  <v-col cols="12" sm="10" md="8">
          <v-text-field
            label=""
            filled
            rounded
            dense
            readonly
            v-model="email"
          ></v-text-field>
        </v-col></td>
                <td>                 
                   <v-col cols="12" sm="8" md="6">
          <v-text-field
            label=""
            filled
            rounded
            dense
            readonly
            v-model="date"
          ></v-text-field>
        </v-col></td>
              </tr>
              </table>
            </div>

            <v-divider class="mt-20"></v-divider>
          
          
            <v-textarea
            filled
          name="content"
          label="내용"
          readonly
          value=""
          v-model="content"
          id="content"
          ref="content"
        ></v-textarea>

          <div
            class="form-group"
            align="center"
          >
            <v-btn @click="moveList">목록</v-btn>
            <v-btn @click="moveUpdate">수정</v-btn>
            <v-btn @click="Delete">삭제</v-btn>
          </div>

          <div
            class="form-group"
            align="center"
          >
          </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>

import axios from "axios";
export default {
  name: "boarddetail",
  data: () => ({
    board: [],
    id: "",
    subject: "",
    content: "",
    email:"",
    date: ""
  }),

  created() {
    var id = this.$route.params.id;
    axios
      .get(
        `http://j3b105.p.ssafy.io/api/notices/notice/${id}`)
      .then(({ data }) => {
        this.id = data.id;
        this.subject = data.subject;
        this.content = data.content;
        this.email = data.email;
        this.date = data.date;
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
        `http://j3b105.p.ssafy.io/api/notices/notice/delete/${id}`
      )
      .then(() => {
        alert("게시글이 삭제되었습니다");
        this.$router.push("/board");
      });
    }
  }
};
</script>

<style>

</style>