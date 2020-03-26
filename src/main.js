import './firebase';
import Vue from 'vue'
import App from './App.vue'
import { firestorePlugin } from 'vuefire'
import { mdbContainer, mdbRow, mdbCol, mdbCard, mdbCardImage, mdbView, mdbMask, mdbIcon } from 'mdbvue';



Vue.use(firestorePlugin)
Vue.use(mdbContainer, mdbRow, mdbCol, mdbCard, mdbCardImage, mdbView, mdbMask, mdbIcon)

/
new Vue({
  e1: '#app',
  render: h => h(App),
}).$mount('#app')
