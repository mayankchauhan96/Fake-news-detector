import './firebase';
import Vue from 'vue'
import App from './App.vue'
import vueFire from 'vuefire';

Vue.use(vueFire);

new Vue({
  render: h => h(App),
}).$mount('#app')
