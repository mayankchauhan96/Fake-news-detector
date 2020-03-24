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
<!-- The core Firebase JS SDK is always required and must be listed first -->
<script src="/__/firebase/7.12.0/firebase-app.js"></script>

<!-- TODO: Add SDKs for Firebase products that you want to use
     https://firebase.google.com/docs/web/setup#available-libraries -->
<script src="/__/firebase/7.12.0/firebase-analytics.js"></script>

<!-- Initialize Firebase -->
<script src="/__/firebase/init.js"></script>
<style>

</style>
