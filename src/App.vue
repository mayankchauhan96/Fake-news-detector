<template>
  <div id="app">
    <div>
      <label>Enter Text:</label>
      <input type="text" v-model="text" />
      <button @click="submitText()">Submit</button>
    </div>

    <div>
      <ul>
        <li v-for="singlenews of listofnews"
        v-bind:key="singlenews['.key']"> 
          <p>{{singlenews.text}}</p>
          <button @click="deletenews(singlenews['.key'])
          ">Delete</button>
         </li>
      </ul>
    </div>
  </div>
</template>

<script>
import {textRef} from './firebase';

export default {
  data(){
    return{
      text: ""

    }
  },
  firebase: {
    listofnews: textRef
    
  },
  methods: {
    submitText(){
      textRef.push({
        text: this.text
      });
      this.text = '';

    },
    deletenews(key){
      textRef.child(key).remove();

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

li {
  margin: 0 10px;
}
</style>
