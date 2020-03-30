<template>
  <div id="app">

    <div>
      <h3>Fake News Detector</h3>
      <mdb-container>
        <mdb-row>
          <mdb-col sm="4">
            <mdb-card dark>
              <mdb-view hover>
                <a href="#!">
                  <mdb-card-image src="https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20%28131%29.jpg" alt="Card image cap"></mdb-card-image>
                  <mdb-mask flex-center waves overlay="white-slight"></mdb-mask>
                </a>
              </mdb-view>
              <mdb-card-body color="elegant" class="white-text">
                <a class="activator mr-4"><mdb-icon icon="share-alt" /></a>
                <mdb-card-title>asked by: {{readtitle}}</mdb-card-title>
                <hr class="hr-light"/>
                <mdbCardText class="font-small mb-3">{{readnews}}</mdbCardText>
              </mdb-card-body>
            </mdb-card>
          </mdb-col>
        </mdb-row>
      </mdb-container>
      <ul>
      <button @click="markFake()">Fake news</button>
      </ul>
      <ul>
      <button @click="markReal()">Real news</button>
      </ul>
      <ul>
      <button @click="markIrr()">Irrelevant news</button>
      </ul>
      <ul>
      <button @click="markNs()">Not Sure</button>
      </ul>
      <ul>
      <button @click="markExpl()">Mark as expilicit</button>
      </ul>
      <label>Status:  </label>
      
      <label> {{readstatus}}</label>

    </div>

  </div>
</template>

<script>

import {db} from './firebase';
import { mdbContainer,mdbCardText,mdbCardTitle, mdbRow, mdbCardBody, mdbCol, mdbCard, mdbCardImage, mdbView, mdbMask, mdbIcon } from 'mdbvue';

export default {
  name: 'app',

components:{

    mdbContainer,
    mdbRow,
    mdbCol,
    mdbCard,
    mdbCardImage,
    // mdbCardHeader,
    mdbCardBody,
    mdbCardTitle,
    mdbCardText,
    // mdbCardFooter,
    // mdbCardUp,
    // mdbCardAvatar,
    // mdbCardGroup,
    // mdbBtn,
    mdbView,
    mdbMask,
    mdbIcon
  },

  methods:{
    markFake() {
      var updates = {};
      console.log("marked fake");
      updates['Incoming/-M3fAqVTTmCJSBzKchAD/status'] = "fake news";
      db.ref().update(
        updates
      )
    },
    
  },

  data: function () {
    return {
      // readtitle: '',
      readnews: '',
      readstatus: ''
    };
  },
  created() {
    db.ref('Incoming/-M3fAqVTTmCJSBzKchAD/userid').once('value', storedValue => this.readtitle = storedValue);
    db.ref('Incoming/-M3fAqVTTmCJSBzKchAD/news').once('value', storedValue => this.readnews = storedValue);
    db.ref('Incoming/-M3fAqVTTmCJSBzKchAD/status').once('value', storedValue => this.readstatus = storedValue);

  },
  
}
</script>

<style>
  * {
    box-sizing: border-box;
  }
  body, html {
    margin: 10px;
    padding: 5px;
    font-family: 'Nunito', sans-serif;
    font-weight: 600;
    color: #2F353E;
    background-color: rgb(226, 217, 217);
    text-align: center;

  }
  section {
    position: relative;
  }
  a {
    display: block;
    text-decoration: none;
    padding-top: 10px;
    margin-top: 10px;
    font-size: 1.2rem;
    font-weight: 700;
    color: #EE7321;
    
  }
  h1, h2, h3 {
    margin: 0;
    
  }
  h2 {
    font-size: 2.3rem;
  }
  h3 {
    margin: 10px;
    text-align:center;
    padding: 5px;
    padding-bottom: 40px;
    font-size: 1.5rem;
    font-weight: 600;
  }
  .final {
    text-align: center;
    padding: 20% 0;
  }
  .final h2 {
    font-weight: 700;
    font-size: 1.8rem;
  }
  .final h3 {
    color: #A4A7AC;
    font-size: 1.4rem;
    font-weight: 600;
    
  }
  .final button {
    margin-top: 20px;
  }
  input {
    background-color: rgba(215, 229, 230, 0.8);
    border: none;
    border-radius: 4px;
    width: 75%;
    font-size: 1.1rem;
    padding: 10px 22px;
    color: #F0F0F0;
    font-family: 'Nunito', sans-serif;
    font-weight: 700;
    transition: background-color .15s ease;
    
  }
  input::-webkit-input-placeholder {
    color: rgba(133, 162, 206, 0.5);
  }
  input:focus {
    background-color: #021333;
  }
  .pattern::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    /* background: url(assets/pattern.svg); */
    background-size: 35%;
    opacity: 0.1;
    z-index: -1;
  }
  @media screen and (min-width: 650px) {
    .final {
      padding: 8% 0;
    }
    .pattern::before {
      background-size: 18%;
    }
  }
  .hero .logo {
    margin-bottom: 20%;
  }
  @media screen and (min-width: 950px) {
    .hero .logo {
      margin-bottom: 10%;
    }
  }
  div[class^="card"],
div[class*=" card"] {
  /* border: 2px solid black; */
  padding: 5px;
  /* color:grey; */
  background-color: rgb(255, 250, 250);


}
</style>