<template>
<div>
  <div><Header/></div>

  <div style="margin-top: 30px;margin-right: 200px;margin-left: 200px">
    <h1>能力介绍</h1>

    <p class="title1">&nbsp;&nbsp;&nbsp;功能简介</p>

     <p> 结合传统语义特征和深度学习模型，充分考虑段落分布和篇章结构，准确计算新闻语句重要性，自动生成新闻标题并自动抽取关键信息并形成摘要结果。</p><br>
    <p style="text-align: left;">登录可进行历史标题及摘要的的查询操作</p><br>
    <el-image :src="require('../assets/title2.jpg')" style="width: 921px; height: 475px">
      <div slot="placeholder" class="image-slot">
        加载中<span class="dot">...</span>
      </div>
    </el-image>
  </div>
</div>
</template>

<script>
export default {
  name: "power"
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
