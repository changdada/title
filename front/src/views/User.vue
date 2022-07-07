<template>

  <div class="container">
    <div><Header/> </div>
    {{user_message}}
    <div style="margin: 20px;"></div>
    <div class="users">
    <el-form :label-position="right" label-width="60px" class="form">
      <a>个人信息</a><br><br>
      <el-form-item label="账号:" >
        <el-input v-model="name" :disabled='isDisabled'></el-input>
      </el-form-item>

      <el-form-item label="邮箱:" >
        <el-input v-model="email" :disabled='isDisabled'></el-input>
      </el-form-item>
      <el-form-item label="手机:">
        <el-input v-model="phone"  :disabled='isDisabled'></el-input>
      </el-form-item>
      <el-form-item label="原密码:" v-if='iff'>
        <el-input v-model="pwd"  :disabled='isDisabled_pwd'></el-input>
      </el-form-item>
      <el-form-item label="新密码:" v-if='iff'>
        <el-input v-model="new_pwd"  :disabled='isDisabled_pwd'></el-input>
      </el-form-item>
      <el-form-item label="确认密码:" v-if='iff'>
        <el-input v-model="new_pwd1" ></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="message">修改信息</el-button>
        <el-button type="primary" @click="pwdd">修改密码</el-button>
        <el-button @click="update_message" v-if="message_up">确认</el-button>
        <el-button @click="update_pwd" v-if="pwd_up">确认</el-button>
        <el-button @click="down" v-if='cancel'>取消</el-button>
      </el-form-item>
    </el-form>

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
      new_pwd:'',
      new_pwd1:'',
      email:'',
      phone:'',
      isDisabled:true,
      iff:false,
      isDisabled_pwd:true,
      message_up:false,
      pwd_up:false,
      cancel:false


    }
  },
  components:{Header},
  created() {
    this.fetchData()
  },

  computed:{

    user_message(){
      axios.defaults.withCredentials=true
      const FPath = 'http://localhost:5555/api/user'
      axios.post(FPath).then(response =>{
        this.msg = response.data
        this.name  =this.msg['name']
        sessionStorage.setItem('name', this.name),
        this.pwd = this.msg['pwd']
        sessionStorage.setItem('pwd', this.pwd),
        this.email = this.msg['email']
        sessionStorage.setItem('email', this.email),
        this.phone = this.msg['phone']
        sessionStorage.setItem('phone', this.phone),

        console.log(this.msg['name'])
      }).catch(() => {
        alert("Error");
      })
    },
    register(){  this.$router.push("Register")},


  },
  methods:{
    message(){
      this.isDisabled=false
      this.isDisabled_pwd=true
      this.iff=false
      this.message_up=true
      this.cancel=true
      this.pwd_up=false
    },
    pwdd(){
      this.isDisabled_pwd=false
      this.isDisabled=true
      this.iff=true
      this.pwd_up=true
      this.cancel=true
      this.message_up=false
      this.pwd=''

    },
    update_message(){
      this.pwd_up=false
      if (this.name === '' || this.email === '' || this.phone === ''){
        this.$message({
          message: '信息不能为空！',
          type: 'warning'
        });
      }
      else {
        axios.defaults.withCredentials=true
        const FPath = 'http://localhost:5555/api/update_message'
        axios.post(FPath,{'name':this.name,'email':this.email,'phone':this.phone}).then(response =>{
          this.msg = response.data
          console.log("修改成功")
          this.$message({
            message: '修改成功',
            type: 'success'
          });
          this.isDisabled=true
          this.message_up=false
          this.cancel=false
          location.reload()
        }).catch(() => {
          alert("Error");
        })


      }
    },
    update_pwd(){
      this.message_up=false

      if (this.pwd === '' || this.new_pwd1 === '' || this.new_pwd===''){
        this.$message({
          message: '密码不能为空！',
          type: 'warning'
        });
      }
      else {
        if(this.new_pwd === this.new_pwd1){
          axios.defaults.withCredentials=true
          const FPath = 'http://localhost:5555/api/update_pwd'
          axios.post(FPath,{'pwd':this.pwd,'new_pwd':this.new_pwd}).then(response =>{
            this.msg = response.data
            if(this.msg === 'success'){
              this.$message({
                message: '修改成功',
                type: 'success'
              });
              this.pwd_up=false
              this.iff=false
              this.cancel=false
              const Path = 'http://localhost:5555/api/quit'
              axios.post(Path)
              window.sessionStorage.clear();
              this.$router.push({
                path: '/',
              },)
            }
            else {
              this.$message({
                message: '原密码不正确！',
                type: 'error'
              });
            }
          })
            .catch(() => {
            alert("Error");
          })


        }
        else {
          this.$message({
            message: '两次密码不相同！',
            type: 'warning'
          });
        }
      }
    },

    down(){
      this.isDisabled=true
      this.isDisabled_pwd=true
      this.iff=false
      this.pwd_up=false
      this.message_up=false
      this.cancel=false
      this.pwd = sessionStorage.getItem('pwd')
      this.name = sessionStorage.getItem('name')
      this.email = sessionStorage.getItem('email')
      this.phone = sessionStorage.getItem('phone')

    }

  },




}
</script>



<style scoped>
.users{
  display: flex;

  flex-direction: column;
  justify-content:center;
  align-items:center;
}

.form{
  width: 500px;


}





</style>

