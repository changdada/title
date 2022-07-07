<template>
  <div id="app">

    <!-- <img src="./assets/logo.png"> -->
<!--    <div><Header/> </div>-->
    <router-view/>

  </div>
</template>

<script>
// import Header from "../components/Header";
export default {
  name: 'App',
  // components:{Header},
}
</script>

<style>
body,html{
  padding: 0;
  margin: 0;
  /*background-image: url("./views/img/background3.jpeg");*/



}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 0;
  width: 100%;
  padding: 0;
}
</style>
