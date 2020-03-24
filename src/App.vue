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
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 20px;
}
</style>
