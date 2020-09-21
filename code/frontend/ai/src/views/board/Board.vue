<template>
    <div class="container" align="center">
      <div>
        <h2>게시판</h2>



      <div align="right">
          <v-btn 
            align = "left"
            type="button"
            id="mvWriteBtn"
            class="btn btn-sm btn-primary"
            data-backdrop="static"
            @click="movePage"
            >새글쓰기</v-btn>

        <v-spacer></v-spacer>
        <v-col cols="12" sm="6">
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="제목, 내용을 검색해주세요"
            single-line
            filled
          ></v-text-field>
        </v-col>
      </div>

        <v-data-table
          v-model="selected"
          :headers="headers"
          :items="boards"
          :search="search"
          :items-per-page="5"
          item-key="id"
          @click:row="moveRead"
        ></v-data-table>

      </div>
    </div>
</template>

<script>
import axios from "axios";
export default {
  name: "boardlist",
  data() {
    return {
      search: "",
      headers: [
        { text: "NO.", value: "id" },
        { text: "제 목", value: "subject" },       
        { text: "작 성 자", value: "email" },
        { text: "작 성 일", value: "date" }
      ],
      boards: [],
      selected: []
    };
  },
  created() {
    axios
      .get(`http://j3b105.p.ssafy.io/api/notices/notice`)
      .then(({ data }) => {
        console.log(data)
        this.boards = data;
      });
  },
  computed: {
    numberOfPages() {
      return Math.ceil(this.boards.length / this.itemsPerPage);
    }
  },
  methods: {
    movePage() {
      this.$router.push("/board/create");
    },
    moveRead(value) {
      // console.log(value.id);
      this.$router.push("/board/detail/" + value.id);
    },
    nextPage() {
      if (this.page + 1 <= this.numberOfPages) this.page += 1;
    },
    formerPage() {
      if (this.page - 1 >= 1) this.page -= 1;
    },
    updateItemsPerPage(number) {
      this.itemsPerPage = number;
    }
  }
};
</script>

<style>
table {
  width: 100%;
  border-collapse: collapse;
}
table th {
  font-size: 1.2rem;
}
table tr {
  height: 2rem;
  text-align: center;
  border-bottom: 1px solid #505050;
}
table tr:first-of-type {
  border-top: 2px solid #404040;
}
table tr td {
  padding: 1rem 0;
  font-size: 1.1rem;
}
container{
  border-bottom: 1px solid #505050;
}
.btn-cover {
  margin-top: 1.5rem;
  text-align: center;
}
.btn-cover .page-btn {
  width: 5rem;
  height: 2rem;
  letter-spacing: 0.5px;
}
.btn-cover .page-count {
  padding: 0 1rem;
}
.btn btn-sm btn-primary{
  margin-left: 250px;
}
</style>