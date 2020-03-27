import {initializeApp} from 'firebase';
const app = initializeApp({
    apiKey: "AIzaSyAEEO1frXfzyL6MCkRvgGz7qURfsTLajRc",
    authDomain: "covid-19-fake-news-detector.firebaseapp.com",
    databaseURL: "https://covid-19-fake-news-detector.firebaseio.com",
    projectId: "covid-19-fake-news-detector",
    storageBucket: "covid-19-fake-news-detector.appspot.com",
    messagingSenderId: "401417810179",
    appId: "1:401417810179:web:b5c7dac2f172bfdc11f936",
    measurementId: "G-59YT063WPN"
});

export const db = app.database();
