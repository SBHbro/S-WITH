<template>
<div id="app">
  <div v-if="!image">
    <h2>Upload video</h2>
    <input type="file" @change="onChange($event)">
  </div>
  <div v-else>
    <video autoplay :src="image" />
    <button @click="uploadImage">upload image</button>
    <button @click="removeImage">Remove image</button>
  </div>
</div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
      return{
          image: '',
          fileData:'',
      }
  },

  methods: {
//       var files = e.target.files || e.dataTransfer.files;
//       this.createImage(files[0]);
    
//     createImage(file) {
//       var image = new Image();
//       var reader = new FileReader();
//       var vm = this;

//       reader.onload = (e) => {
//         vm.image = e.target.result;
//       };
//       reader.readAsDataURL(file);
//     },
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
              // this.answer = response.data[0].answer
              // this.accuracy = response.data[0].accuracy
              // this.task = true
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
      this.fileData = file;
      // this.$set(this.items[index], "file", file);
    }

   }
}
</script>

<style lang="scss" scoped>
 #app {
  text-align: center;
}
.img {
  width: 30%;
  margin: auto;
  display: block;
  margin-bottom: 10px;
}
</style>