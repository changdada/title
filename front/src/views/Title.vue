<template>
  <div class="container">
    <div><Header/></div>
  <div id="implement">

    <!-- 标题 -->
    <div class="title">
      <!-- 输入文字 -->
      <div class="title1">
<!--        <div class="title1_1">-->
<!--          输入内容-->
<!--        </div>-->
        <div class="title1_2">

          <quill-editor ref="text" style="height: 550px" v-model="content" class="editor"/>
        </div>


      </div>

      <div class="title3">
        <el-button type="primary" class="buttons" @click="title_ai_sql" :loading="loading" v-if="get_login_id">
          {{ buttonText }}
        </el-button>
        <el-button type="primary" class="buttons" @click="title_ai()" :loading="loading" v-else>
          {{ buttonText }}
        </el-button>
        <div  style="margin-top: 20px; height: 550px;">

          <el-collapse-transition>
            <div v-show="show3">
              <div class="transition-box">
                标题：{{ title}}
             </div>

              <div class="transition-box2">
                摘要：{{ abstract }}
              </div>
            </div>
          </el-collapse-transition>
        </div>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
import Header from "../../components/Header";
import axios from 'axios';
export default {

  name: "Title",
  components: {Header},
  component:{Header},


  data:function (){
    return{
      message:'已登陆',
      buttonText:'点击生成',
      loading:false,
      maxLength:10000,
      // 当前文字数量
      nowLength:0,
      login_id:'',
      content:'',
      title:'',
      abstract:'',
      show3: false,
      editorOption: {},
    }
  },
  watch: {
    content:{
      handler(newVal, oldVal){
        this.nowLength = newVal.length
      },
      immediate: true
    }
  },



  methods:{
    exit_login(){
      alert("您已退出登录")

      this.$router.push({
          path: '/',
        }
      )
    },
    title_ai(){
      this.buttonText="生成中"
      this.loading=true
      // document.getElementById('btn1').disabled=true
      const FPath = 'http://localhost:5555/api/news-title-generate'
      axios.post(FPath,{content:this.content}
      ).then(response => {
        this.msg = response.data

        this.title = response.data['title']
        this.abstract = response.data['abstract']
        this.buttonText="点击生成"
        this.loading=false
        this.show3=true
        // document.getElementById('btn1').disabled=false
      }).catch(() => {
        alert("Error");
      })
    },
    title_ai_sql(){
      this.buttonText="生成中"
      this.loading=true
      // document.getElementById('btn').disabled=true
      const FPath = 'http://localhost:5555/api/generate_sql'
      axios.post(FPath,{content:this.content}
      ).then(response => {
        this.msg = response.data
        this.title = response.data['title']
        this.abstract = response.data['abstract']
        this.buttonText="点击生成"
        this.loading=false
        this.show3=true
        // document.getElementById('btn').disabled=false
      }).catch(() => {
        alert("Error");
      })
    },

  },
  computed: {
    get_login_id() {
      this.login_id = sessionStorage.getItem('Login_id')
      if (this.login_id == 1) {
        return true
      } else return false
    }
  }
}
</script>

<style>
*{
  margin: 0px;
  padding: 0px;
}
.transition-box {
  margin-top: 5px;
  width: 400px;
  height: 100px;
  border-radius: 4px;
  background-color: #eeeeee;
  text-align: left;
  color: #000000;
  padding: 40px 20px;
  box-sizing: border-box;
  margin-right: 20px;
}
.transition-box2 {
  margin-top: 20px;
  width: 400px;
  height: 380px;
  border-radius: 4px;
  background-color: #FCE1E5;
  text-align: left;
  color: #000000;
  padding: 40px 20px;
  box-sizing: border-box;
  margin-right: 20px;
}
.buttons{
  width: 200px;
  height: 40px;
  margin-top: 5px;
  margin-right: 220px;
}
</style>
<style scoped >
input[type=text], textarea {
  outline: none;
  padding: 5px 0px 10px 3px;
  /* margin: 5px 1px 3px 0px; */
  /* border: 2px solid #ddd; */
  box-sizing: border-box;
}

input[type=text]:focus, textarea:focus {
  box-sizing: border-box;
  box-shadow: 0 0 5px rgb(72, 37, 228);
  padding: 5px 0px 10px 3px;
  /* margin: 5px 1px 3px 0px; */
  border: 2px solid rgba(72, 37, 228, 1);
}
#implement{
  width: 100%;
  height: 93.4vh;
  background: #fff;
  /*background: -webkit-linear-gradient(to right, #cac849, #7ec6bc);*/
  /*background: linear-gradient(to right, #cac849, #7ec6bc);*/


}
.title{
  /* font-size:20px; */
  display: flex;
  flex-direction:row;
  justify-content:space-around;
  align-items:center
}
.title1,
.title2,
.title3{
  display: flex;
  flex-direction: column;
  align-items:center;
  justify-content:space-around;
}
.title1{
  border: 0px;
  flex: 5;
  width: 500px;
  height: 90vh;
  /* background: red; */
}
.title2{
  position: relative;
  left: -5vw;
  height: 90vh;
  flex:1;
}
.title3{
  margin-top: 20px;
  margin-left: 30px;
  position: relative;
  /*right: 5vw;*/
  /*left: -5vw;*/
  border: 0px;
  height: 90vh;
  /* background: green; */
  flex:4;


}
.title1_1,
.title3_1{
  font-family:"Microsoft YaHei";
  font-size: 1.5125rem;
  text-shadow: 10px 5px 2px #ffffff;
  position: relative;
  top:20px;
  box-sizing: border-box;
  padding:5px 150px 5px;
}
.title1_2{
  /* background: green; */
  margin-top: 30px;
  margin-left: 100px;
  background: #FAFAFA;
  width: 60vw;
  height: 90vh;
}
.title3_2{
  /* background: green; */
  width: 30vw;
  height: 65vh;

  display: flex;
  flex-direction: column;
  align-items:center;
  justify-content:space-around;
}
#this_item{
  /* background: rgb(218, 100, 5); */
  width: 30vw;
  height: 10vh;
}
#this_content{
  /* background: rgb(128, 0, 128); */
  width: 30vw;
  height: 50vh;
}
.text{
  font-family:"Microsoft YaHei";
  color: rgb(56, 56, 56);
  background: #36363600;
  box-sizing: border-box;
  padding: 5px 0px 10px 3px;
  resize:none;
  font-size: 17px;
  width: 100%;
  height: 100%;
  /* margin-left: 10vw;
  margin-top: 5vh; */
}
#this_content .text,
#this_item .text{
  cursor: not-allowed;
}
/* 查询按钮 */
.el-button--bblue {
  color: rgb(148, 197, 238);
  background-color: rgb(240, 248, 255);
  border-color: rgb(148, 197, 238);
}

.el-button--bblue:hover {
  color: rgb(240, 248, 255);
  background-color: rgb(148, 197, 238);
  border-color: rgb(148, 197, 238);
}
#btn{
  cursor: pointer;
  /*border: 1.5px solid rgba(43, 43, 43, 0.575);*/
  /*color: white;*/
  color: rgb(240, 248, 255);
  background-color: rgb(52,88,255);
  border-color: rgb(52,88,255);

   /*background: #0074D9;*/
  /*background: -webkit-linear-gradient(to right, #cac84993, #7ec6bc93);*/
  /*background: linear-gradient(to right, #cac84993, #7ec6bc93);*/
  border-radius: 10px;
  font-size: 20px;
  width: 180px;
  height: 55px;
  padding: 5px 10px 5px;
  box-sizing: border-box;
}
#btn:hover{
  font-size: 23px;
  color: rgb(52,88,255);
  background-color: rgb(240, 248, 255);
  border-color: rgb(52,88,255);
  /* background: rgba(207, 155, 43, 0.685); */
  /*background: -webkit-linear-gradient(to right, #f8f53ac0, #5bccbdd7);*/
  /*background: linear-gradient(to right, #f8f53ac0, rgba(85, 202, 187, 0.808));*/
}
#btn:active{
  border: 2.5px solid rgba(61, 61, 61, 0.753);
}

#btn1{
  cursor: pointer;
  color: rgb(240, 248, 255);
  background-color: #0074D9;
  border-color: #0074D9;
  border-radius: 10px;
  font-size: 20px;
  width: 180px;
  height: 55px;
  padding: 5px 10px 5px;
  box-sizing: border-box;
}
#btn1:hover{
  font-size: 23px;
  color: #0074D9;
  background-color: rgb(240, 248, 255);
  border-color: #0074D9;
}
#btn1:active{
  border: 2.5px solid rgba(61, 61, 61, 0.753);
}

.textCount{
  display: flex;
  justify-content:flex-end
}
</style>
