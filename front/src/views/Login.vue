<template>
<div>
  <div><Header/></div>

  <div id="login">

    <div id="left">
<!--      <div class="left1"><a href=""><img src="../assets/logo1.png" alt=""></a></div>-->
      <div class="left2">智能创作平台</div>
      <div class="left3">自动生成标题，摘要 - 实现标题，摘要的自动生成，准确、及时、高效。<br>
        使用场景 - 新闻，论文标题及摘要的快速生成<br>
        操作简单 - 零基础也可快速使用</div>
      <div class="left4"></div>
      <div class="left5"><img src="../assets/bg.jpg" alt=""></div>
      <div class="left6">
<!--        <div class="small1">2022 jlict<a href="">使用前必读</a>&nbsp;&nbsp;<a href="">增值电信业务经营许可证:  B1.B2-20100266</a></div>-->
        <div class="small2">Copyright © 2022 吉林化工学院 版权所有&nbsp;&nbsp;&nbsp;</div>
      </div>
    </div>
    <div id="right">
      <div class="right1">账号登录</div>
      <div id="user" v-if="isUser">请您输入手机号/用户名/邮箱</div>
      <div id="pass" v-if="isPass">请您输入密码</div>
      <div class="right2"><input  v-model="name" type="text" name="" id="" placeholder="手机号/用户名/邮箱"></div>
      <div class="right3"><input v-model="pwd" type="password" name="" id="" placeholder="密码"></div>
      <div class="right4" @click="login()">登录</div>
      <router-link class="right5" to="/Register">立即注册</router-link>
    </div>
  </div>
</div>
</template>

<script>
import Header from "../../components/Header";
import axios from 'axios';

export default {
  name: "Login",

  data:function (){
    return{
      name:'',
      pwd:'',


    }
  },
  components:{Header},
  created() {
    this.fetchData()
  },

  methods:{
    fetchData() {
      getmsg().then(response => {
        this.msg = response.data.msg
        console.log(response.data)
      }).catch(() => {
        alert("Error");
      })
    },
    register(){  this.$router.push("Register")},

    // getParams: function () {
    //         // 取到路由带过来的参数
    //         var routerParams = this.$route.query.list;
    //         this.user_list = routerParams;
    // },
    login(){
        const FPath = 'http://localhost:5555/api/login'
        var flag=0;
          axios.defaults.withCredentials=true
          axios.post(FPath,{names:this.name,pwd:this.pwd}
      ).then(response => {
            withCredentials: true
          this.msg = response.data
            flag = this.msg
            if(flag==1){
              //可以跳转到主页
              // this.$router.push("Homepage");
              this.$router.push({
                  path: 'Title',
                },
                sessionStorage.setItem('Login_id', 1),
              console.log("good")
              )
            }
            else{
              console.log(flag)
              this.$message({
                message: '用户名或密码错误，请重新输入！',
                type: 'warning'
              });
              }
          // console.log(flag)
        }).catch(() => {
          alert("Error");
        })


    }

  },


}
</script>

<style>
*{
  margin: 0px;
  padding: 0px;
}

</style>
<style scoped >
#login{
  width: 100%;
  height: 93vh;
  display: flex;

}
a{
  text-decoration:none;
  line-height: 24px;
  font-size: 12px;
  color: #848b99;
  font-weight: 400;
}
/* -----------------------left----------------------- */
#left{
  flex: 500;
  background: rgb(235,237,244);
  display: flex;
  flex-direction: column;
  justify-content:center;
  align-items:center;
}
.left1{
  padding: 24px;
}
.left1 a img{
  width: 109px;
  height: 28px;
  position: relative;
  left: -280%;
  bottom: 235%;
}
.left2{
  text-align: center;
  /* margin-top: 160px; */
  font-size: 28px;
  color: #191a24;
  width: 100%;
}
.left3{
  display: block;
  width: 60%;
  margin-top: 37px;
  margin-left: 5%;
  font-size: 14px;
  color: #545b66;
  letter-spacing: 0;
  line-height: 28px;
  text-align: left;
}
.left4{
  margin-top: 5%;
  /* margin-left: 140px; */
  width: 65%;
  border-bottom: 0.8px solid rgb(204, 204, 204);
}
.left5 img{
  height: 120px;
  /* margin-left: 171px; */
  margin-top: 53px;
}
.left6{
  position: relative;
  bottom: -8%;
  text-align: center;
  width: 100%;
  line-height: 24px;
  font-size: 12px;
  color: #848b99;
  letter-spacing: 0;
  font-weight: 400;
}
/* -----------------------right----------------------- */
#user,
#pass{
  position: absolute;
  line-height: 30px;
  font-size: 12px;
  color: #f28281;
  bottom: 61%;
  right: 24%;
}
#pass{
  right: 30%;
}
#right{
  flex:393;
  background: rgb(246,247,250);
  display: flex;
  flex-direction: column;
  justify-content:space-around;
  align-items:center;
}
.right1{
  margin-top: 32%;
  position: relative;
  bottom:5px
}
.right2 input,
.right3 input{
  width: 358px !important;
  border: 1px solid #c5ccdb;
  margin-top: 1px;
  border-radius: 4px;
  padding: 4px 12px !important;
  box-sizing: border-box;
  height: 36px !important;
  outline: none;
  font-weight: inherit;
}
.right2 input:hover,
.right3 input:hover{
  border: 1px solid #2468f2;
}
.right4 {
  display: block;
  margin-top: 0;
  width: 360px;
  line-height: 40px;
  background: #2468F2;
  /* background-image: -webkit-linear-gradient(top, #2468f2, #2468f2); */
  font-size: 14px;
  color:white !important;
  text-align: center;
  border: none;
  box-shadow: none;
  border-radius: 4px;
  outline: none;
  cursor: pointer;
}
.right5{
  cursor: pointer;
  color: #848b99;
  font-size: 14px;
  margin-bottom: 32%;
}

</style>
