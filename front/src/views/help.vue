<template>
  <div>
    <div><Header/></div>

    <div style="margin-top: 30px;margin-right: 200px;margin-left: 200px">
      <h1>帮助文档</h1>
      <el-divider></el-divider>
      <p class="title1">产品介绍</p>

      <p style="text-align: left"> Hi，您好，欢迎使用智能创作服务平台，旨在成为更懂你的智能创作助手。平台提供如下功能：自动生成标题、自动生成摘要、历史查看。 自动生成标题：可通过输入文章、快速实现自动生成标题的能力。自动生成标题：可通过输入文章、快速实现自动生成标题的能力。历史查看：提供用户登录后可对已生成的标题及摘要进行查看及删除。</p><br>
      <p style="text-align: left;">接下来，您只需快速浏览以下介绍，即可完成您内容创作需求。</p><br>
      <el-divider></el-divider>
      <p class="title1">登录</p>

      <p style="text-align: left">登录智能创作平台首页，点击右上角登录，输入相应的账号密码即可登录</p><br>
      <el-image :src="require('../assets/denglu.jpg')" style="width: 650px; height: 400px"></el-image><br>
      <el-divider></el-divider>
      <p class="title1">注册</p>

      <p style="text-align: left">若没有账号，可点击立即注册进行账号的注册</p><br>
      <el-image :src="require('../assets/zhuce.jpg')" style="width: 650px; height: 400px"></el-image>
      <el-divider></el-divider>
      <p class="title1">标题及摘要生成</p>

      <p style="text-align: left">在首页点击立即使用即可进入，进入后在左侧的文本框内输入文章，点击立即生成便可生成此文章的标题及摘要,若未登录则只能生成，并不可保存查看，登陆后便可在历史记录中进行已生成的标题及摘要，也可进行删除操作</p><br>
      <el-image :src="require('../assets/shengcheng2.jpg')" style="width: 650px; height: 400px"></el-image>
      <el-divider></el-divider>
      <p class="title1">历史查看</p>

      <p style="text-align: left">若登录，点击右上角历史记录便可进行查看，点击每条记录也可查看详细内容，并且可进行删除操作。</p><br>
      <el-image :src="require('../assets/lishi2.jpg')" style="width: 650px; height: 400px"></el-image>
      <el-divider></el-divider>
      <p class="title1">个人信息管理</p>

      <p style="text-align: left">若登录，点击右上角个人中心便进行查看，可进行信息的修改，包括账号、邮箱、电话及密码。</p><br>
      <el-image :src="require('../assets/geren.jpg')" style="width: 650px; height: 400px;margin-bottom: 50px"></el-image>
<!--      <el-image :src="require('../assets/title2.jpg')" style="width: 921px; height: 475px">-->
<!--        <div slot="placeholder" class="image-slot">-->
<!--          加载中<span class="dot">...</span>-->
<!--        </div>-->
<!--      </el-image>-->
    </div>
  </div>
</template>

<script>
export default {
  name: "help"
}
</script>

<style scoped>
.title1{
  text-align: left;
  font-size: 20px;
  line-height: 24px;
  font-weight: 700;
  display: block;
  margin-bottom: 15px;
}
</style>
