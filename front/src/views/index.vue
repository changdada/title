<template>
  <div>

    <div><Header/></div>
    <div id="backImage">
      <div class="msg1">智能创作平台</div>
      <div class="msg2">更懂你的智能创作助手</div>
      <button id="btn1" @click="gotitle">
        立即使用
      </button>
    </div>
    <div id="content_1">
      <div class="left">
        <ul>
          <li>自动创作</li>
          <li>自动生成多样内容，快速高效</li>
          <li>用户可以通过接入数据，快速实现自动生成文章标题和摘要的能力。同时支持历史查询、信息修改等多种能力。</li>
          <li>
            <button id="btn2" @click="tohelp">了解更多</button>
          </li>
        </ul>
      </div>
      <div class="right">
        <img class='img' src="../assets/flower.png" alt="">
      </div>
    </div>
    <div id="content_3">
      <div class="con3_1">让创作变得更简单</div>
      <div class="con3_2">
        <!-- 第一块 -->
        <div >
          <ul>
            <li>领先的语言生成技术</li>
            <li>基于深度学习，提供领先的深度理解能力与语言生成技术</li>
          </ul>
        </div>
        <!-- 第二块 -->
        <div>
          <ul>
            <li>一站式创作能力提供</li>
            <li>内置丰富数据、索材，融合多种自然语言处理能力</li>
          </ul>
        </div>
        <!-- 第三块 -->
        <div>
          <ul>
            <li>超低门槛的使用体验</li>
            <li>无需配置、生成快速，零代码基础也可以轻松使用</li>
          </ul>
        </div>
      </div>
    </div>
    <div id="content_2">
      <div class="flex1">
        <ul>
          <li>关于我们</li>
          <li>智能创作平台，集合领先的自然语言处理技术</li>
          <li>拥有丰富的自动创作和辅助创作能力</li>
          <li>更懂你的智能创作助手</li>
        </ul>
      </div>
      <div class="flex2">
        <ul>
          <li>开发资源</li>
          <li>技术论坛文档中心</li>
          <li>常见问题</li>
        </ul>
      </div>
      <div class="flex3">
        <ul>
          <li>服务支持</li>
          <li>QQ支持群: 1234567</li>
          <li>客服电话: 1001-111-111</li>
          <li>邮箱：123456789@jlict.deu.cn</li>
        </ul>
      </div>
      <div class="flex4">
        <img src="../assets/link.jpg" alt="">
        <div class="message">微信公众平台</div>
      </div>
    </div>
    <div id="content_4">
      Copyright © 2022 吉林化工学院 版权所有
    </div>
  </div>

</template>
<script>
import Header from "../../components/Header";
export default {
  data(){
    return {

    }
  },
  component:{Header},
  watch: {
  },
  methods: {
    gotitle(){
      this.$router.push({
        path: 'Title',
      },)
    },
    tohelp(){
      this.$router.push({
        path: '/help',
      },)
    }

  }
}
</script>
<style>
*{
  margin: 0px;
  padding: 0px;
}
</style>
<style scoped >
ul li{
  list-style:none;
}
#backImage{
  background-image: url("../assets/bg.jpg");
  background-size: 100% 80%;
  background-position-y: -30px;
  width: 100%;
  height: 80vh;
}
.msg1,
.msg2{
  position: absolute;
  color: white;
}
.msg1{
  font-weight: 1000;
  font-size: 40px;
  left: 18%;
  top:30%
}
.msg2{
  font-weight: 500;
  font-size: 24px;
  left: 18%;
  top:40%
}
#btn1{
  cursor: pointer;
  border: 1.5px solid white;
  border-radius: 5px;
  background: rgba(255, 0, 0, 0);
  color: white;
  font-size: 18px;
  width: 8vw;
  height: 36px;
  position: relative;
  right: 20%;
  top:57%
}
#btn1:hover{
  background: white;
  color: black;
}
/* ----------------#content_1 ------------------------*/
#content_1{
  width: 100%;
  height: 45vh;
  background: white;
  display:flex
}
#content_1 ul{
  margin: 50px 50px 50px 200px ;
}
#content_1 .left{
  flex: 4;
  /* background: rgb(185, 179, 179); */
}
#content_1 .right{
  flex: 3;
  /* background: rgb(108, 138, 108); */

}
#content_1 ul li:nth-child(1){
  font-size: 25px;
  font-weight: 1000;
}
#content_1 ul li:nth-child(2){
  margin-top: 8px;
  font-size: 19px;
  font-weight: 600;
}
#content_1 ul li:nth-child(3){
  color: rgb(36, 36, 36);
  margin-top: 15px;
  display: inline-block;
  width: 27vw;
  font-size: 15px;
}
.right img{
  position: relative;
  top:8%;
}
#btn2{
  cursor: pointer;
  border: 1.5px solid rgb(141, 141, 141);
  border-radius: 5px;
  background: rgba(255, 0, 0, 0);
  color: black;
  font-size: 17px;
  width: 8vw;
  height: 36px;
  position: relative;
  /* left: 200px; */
  top:20px
}
#btn2:hover{
  color:white;
  border: 1.5px solid rgb(52,88,255);
  background: rgb(52,88,255);
}
/* ----------------#content_2 ------------------------*/
#content_2{
  width: 100%;
  height: 45vh;
  background: rgb(25,25,25);
  display:flex
}
#content_2 .flex1{
  flex: 2;
  /* background: red; */

}
#content_2 .flex2{
  flex: 1;
  /* background: rgb(123, 255, 0); */

}
#content_2 .flex3{
  flex: 1;
  /* background: rgb(0, 17, 255); */
}
#content_2 .flex4{
  flex: 1;
  /* background: rgb(255, 0, 212); */
}
#content_2 .flex4 img{
  margin-top: 50px;
  margin-left: 42px;
  width:12vw;
}
#content_2 .flex4 .message{
  padding-left:58px ;
  padding-top: 12px;
  color: white;
  font-size: 16px;
}
#content_2 ul{
  margin: 50px 2px 10px 60px ;
}
#content_2 .flex1 ul li,
#content_2 .flex2 ul li,
#content_2 .flex3 ul li{
  font-size: 15px;
  color: white;
  padding: 5px 0 5px;
}
#content_2 .flex1 ul li:nth-child(1),
#content_2 .flex2 ul li:nth-child(1),
#content_2 .flex3 ul li:nth-child(1){
  font-size: 18px;
  color: white;
  font-weight: 600;
  padding-bottom: 15px;
}
/* ----------------#content_3 ------------------------*/
#content_3{
  width: 100%;
  height: 45vh;
  background: rgb(249,246,247);
  /* display:flex */
}
#content_3 .con3_1{
  position: relative;
  top:28px;
  width: 100%;
  height: 6vh;
  /* background: rgba(105, 198, 201, 0.801); */
  display: flex;
  font-size: 32px;
  justify-content:center;
  align-items:center

}
#content_3 .con3_2{
  width: 100%;
  height: 39vh;
  /* background: rgba(201, 105, 105, 0.801); */
  display: flex;
}
#content_3 .con3_2 div{
  flex: 1;
  display: flex;
  justify-content:center;
  align-items:center
}
#content_3 .con3_2 div ul li:nth-child(1){
  margin-bottom:25px;
  font-size:22px;
  font-weight: 400;
  color:rgb(50,50,50);
}
#content_3 .con3_2 div ul li:nth-child(2){
  width: 20vw;
  color:rgb(165,160,170);
  font-size: 15px;
}
/*--------------- content_4---------------- */
#content_4{
  width: 100%;
  height: 6vh;
  background: rgb(0,0,0);
  display: flex;
  color:white;
  font-size: 13px;
  justify-content:center;
  align-items:center
}
</style>




