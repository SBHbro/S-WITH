<template>
  <div id="upload">
    <file-pond
      name="bin"
      ref="pond"
      allow-multiple="true"
      max-files="3"
      accepted-file-types="image/jpeg, image/png, video/mp4, video/webm"
      :server="server"
      v-bind:files="myFiles"
      v-on:init="handleFilePondInit"
      v-on:processfile="onload"
      />
  </div>
</template>

<script>
// Import Vue FilePond
import vueFilePond from 'vue-filepond'

// Import FilePond styles
import 'filepond/dist/filepond.min.css'

// Import FilePond plugins
// Please note that you need to install these plugins separately

// Import image preview plugin styles

// import 'filepond-plugin-image-preview/dist/filepond-plugin-image-preview.min.css'

// Import image preview and file type validation plugins
import FilePondPluginFileValidateType from 'filepond-plugin-file-validate-type'
import FilePondPluginImagePreview from 'filepond-plugin-image-preview'

// Create component
const FilePond = vueFilePond(FilePondPluginFileValidateType, FilePondPluginImagePreview)

export default {
  name: 'app',
  data () {
    return {
      myFiles: [],
      server: {
        url: `https://j3b105.p.ssafy.io/video/upload`,
        process: {
          headers: {
            Authorization: localStorage.getItem('token')
          }
        }
      }
    }
  },
  methods: {
    handleFilePondInit () {
      console.log('FilePond has initialized')
      // FilePond instance methods are available on `this.$refs.pond`
    },
    onload (e, r) {
      console.log(r)
    }
  },
  components: {
    FilePond
  }
}
</script>

<style lang="scss" scoped>
.upload {
  width: 50%;
  height: 50%;
  padding: 0px;
  box-sizing: border-box;
}
</style>