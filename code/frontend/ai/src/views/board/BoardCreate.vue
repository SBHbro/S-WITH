<template>
<div>
  <table>
      <tr>
        <th>TITLE</th>
        <td><input placeholder="제목"></td>
      </tr>
      <tr>
        <th>CONTENT</th>
        <td><input placeholder="내용"></td>
      </tr>
      <tr>
        <th>EMAIL</th>
        <td><input placeholder="작성자 이메일"></td>
      </tr>
    </table>
    <div class="btn-cover">
      <button @click="movePage" class="page-btn">
        등록
      </button>
    </div>
</div>
</template>

<script>
export default {
    methods: 
    {
        movePage () {
            window.location.href = "http://localhost:8080/#/board";
        }
    }
}
</script>

<style>

</style>