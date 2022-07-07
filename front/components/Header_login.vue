<template>
  <div>
    <div class="header">
      <div class="box">
        <h1>
          <img src="../src/assets/logo1.png">
          <span>智能创作平台</span>
        </h1>
        <nav>
          <router-link active-class="active" to="/index">首页</router-link>
          <router-link active-class="active" to="/ask">能力介绍</router-link>
          <router-link active-class="active" to="/community">帮助文档</router-link>
        </nav>
      </div>
      <div class="box">
        <nav>
          <router-link active-class="active" to="/Login">历史记录</router-link>
          <router-link active-class="active" to="/User" @click="user">个人中心</router-link>
<!--          <button @click="users">个人</button>-->
        </nav>
      </div>
    </div>
    <div class="contents">
      <div class="content">
        <!--指定组件的位置-->
        <router-view></router-view>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "Header_login",
  methods:{
    users(){
      const FPath = 'http://localhost:5555/api/user'
      axios.post(FPath).then(response =>{
        this.msg = response.data
        console.log(this.msg['name'])
      }).catch(() => {
        alert("Error");
      })
    }
  }
}


</script>

<style scoped>
.header{
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 50px;
  background-color:#292c2f;
  color: #ffffff;

  /*吸顶效果*/
  /* position: sticky;
   position: -webkit-sticky;    !*兼容 -webkit 内核的浏览器*!
   top: 0px;                    !*必须设一个值，否则不生效*!*/

}
.box{
  display: flex;
  align-items: center;
}
h1{
  display: flex;
  align-items: center;
  font: normal 28px Cookie, Arial, Helvetica, sans-serif;
  padding: 0px 20px;
}
img{
  width: 40px;
  height: 40px;
}

nav {
  display: flex;
  align-items: center;
  margin: 0px 60px;
  font:16px Arial, Helvetica, sans-serif;
}
nav a{
  padding: 0 15px;
  width: 80px;
  text-decoration:none;
  color: #ffffff;
  font-size: 16px;
  font-weight: normal;
  opacity: 0.9;
}

nav a:hover {
  opacity: 1;
}

.active {
  color: #608bd2;
  pointer-events: none;
  opacity: 1;
}

/*搜索框*/

.text{
  height: 22px;
  font-size: 14px;
  border: 1px solid #ccc;
  padding: 3px 16px;
  border-bottom-left-radius: 20px;
  border-top-left-radius: 20px;
}
.text:focus{
  outline: none;
  border-color: rgba(82, 168, 236, 0.8);
  box-shadow: inset 0 2px 2px rgba(0, 0, 0, 0.075), 0 0 8px rgba(82, 168, 236, 0.6);
}
.button{
  width: 60px;
  height: 30px;
  font-size: 14px;
  margin-right: 35px;
  border: 1px solid #608bd2;
  background-color: #608bd2;
  border-top-right-radius: 20px;
  border-bottom-right-radius: 20px;
}

.contents{
  display: flex;
  justify-content: center;
}
.content{
  display: flex;
  width: 100%;
  height: 100%;
  /*background-color: #f0f2f3;*/
}
</style>

