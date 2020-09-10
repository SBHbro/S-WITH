<template>
<div>
  <table>
      <tr>
        <th>NO</th>
        <td>{{ items.no }}</td>
      </tr>
      <tr>
        <th>TITLE</th>
        <td>{{ items.title }}</td>
      </tr>
      <tr>
        <th>CONTENT</th>
        <td>{{ items.content }}</td>
      </tr>
      <tr>
        <th>EMAIL</th>
        <td>{{ items.email }}</td>
      </tr>
      <tr>
        <th>DATE</th>
        <td>{{ items.date }}</td>
      </tr>
    </table>
    <div class="btn-cover">
      <button @click="moveUpdate" class="page-btn">
        수정
      </button>
      <button @click="Delete" class="page-btn">
        삭제
      </button>
          <button @click="moveList" class="page-btn">
        목록으로 돌아가기
      </button>
    </div>
</div>
</template>

<script>
export default {

    methods: 
    {
        moveUpdate () {
            window.location.href = "http://localhost:8080/#/board/update";
        },
        Delete () {
            window.location.href = "http://localhost:8080/#/board";
        },
        moveList () {
            window.location.href = "http://localhost:8080/#/board";
        }
    }

}
</script>

<style>

</style>