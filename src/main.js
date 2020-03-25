import './firebase';
import Vue from 'vue'
import App from './App.vue'
import { firestorePlugin } from 'vuefire'

Vue.use(firestorePlugin)

new Vue({
  e1: '#app',
  render: h => h(App),
}).$mount('#app')
