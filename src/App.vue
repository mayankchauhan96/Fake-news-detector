<template>
  <div id="app">
    <div>
      <label>Enter Text:</label>
      <input type="text" v-model="text" />
      <button @click="submitText()">Submit</button>
    </div>

  </div>
</template>

<script>
import {textRef} from './firebase';

export default {
  name: 'App',
  components: {

  },
  data(){
    return{
      text: "fake news "

    }
  },
  methods: {
    submitText(){
      textRef.push({
        text: this.text
      })

    }
  }
}
</script>

<style>

</style>
