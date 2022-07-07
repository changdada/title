<template>
  <div class="container">
    <div><Header/></div>
    {{get_title}}
    <div class="tab-container">

      <el-table
        v-loading="loading"
        element-loading-text="拼命加载中"
        element-loading-spinner="el-icon-loading"
        element-loading-background="rgba(0, 0, 0, 0.8)"
        :data="pvData.slice((currentPage - 1) * pagesize, currentPage * pagesize)"
        border
        fit
        highlight-current-row
        style="width: 100%"

      >
        <el-table-column type="expand">
        <template slot-scope="props">
          <el-form label-position="left" inline class="demo-table-expand">
            <el-form-item label="日期">
              <span>{{ props.row.time }}</span>
            </el-form-item>
            <el-form-item label="标题">
              <span>{{ props.row.title }}</span>
            </el-form-item>
            <el-form-item label="摘要">
              <span>{{ props.row.abstract }}</span>
            </el-form-item>
            <el-form-item label="内容">
              <span  v-html="props.row.content">{{ props.row.content }}</span>
            </el-form-item>


          </el-form>
        </template>
        </el-table-column>

        <el-table-column prop="time" label="日期"  sortable
                         width="180"
                         column-key="date" ></el-table-column>
        <el-table-column prop="title" label="标题" ></el-table-column>
        <el-table-column prop="abstract" label="摘要" width="600px" :formatter="stateFormat"></el-table-column>
<!--        <el-table-column prop="content" label="内容" :formatter="stateFormat"></el-table-column>-->
        <el-table-column
          align="center" label="删除" width="100px">

          <template slot-scope="scope">

            <el-button
              size="mini"
              type="danger"
              @click="handleDelete(scope.$index, scope.row)">Delete</el-button>
          </template>
        </el-table-column>
      </el-table>

      <el-pagination
        style="margin: 12px 0px"
        background
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-sizes="[5, 10, 20, 40]"
        :page-size="pagesize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="pvData.length"
      >
      </el-pagination>


  </div>
  </div>
</template>

<script>
import Header from "../../components/Header";
import axios from 'axios';
export default {
  data() {
    return {
      // 分页
      currentPage: 1, //初始页
      pagesize: 10, //    每页的数据
      total: 0,
      pvData: [],


    };
  },

  created() {
    this.getQuerycheckList();
  },
  computed:{
    get_title(){
      axios.defaults.withCredentials=true
      const FPath = 'http://localhost:5555/api/select_title'

      axios.post(FPath).then(res =>{

        this.pvData = res.data;
        console.log(this.pvData)
      }).catch(() => {
        alert("Error");
      })
    }
  },
  methods: {
    // 初始页currentPage、初始每页数据数pagesize和数据data
    handleSizeChange: function (size) {
      this.pagesize = size;
      console.log(this.pagesize); //每页下拉显示数据
    },
    handleCurrentChange: function (currentPage) {
      this.currentPage = currentPage;
      console.log(this.currentPage); //点击第几页
    },
    stateFormat(row, column, cellValue) {
      if (!cellValue) return ''
      if (cellValue.length > 40) {       //最长固定显示10个字符
        return cellValue.slice(0, 40) + '...'
      }
      return cellValue
    },

    //查询题目列表信息接口
    getQuerycheckList() {
      const params = {
        organId: 1,
        userOrganId: 1,
        authority: 0,
        page: 1,
        rows: 5,
        isPagination: false,
      };
      const FPath = 'http://localhost:5555/api/select_title'
      axios.get(FPath).then(res =>{
        console.log("查询题目列表信息", res);
        this.pvData = res.data;
      }).catch(() => {
        alert("Error");
      })
    },
    handleDelete(index, row) {
      console.log(index, row);
      console.log(row.id)
      const FPath = 'http://localhost:5555/api/delete_title'
      axios.post(FPath,{'id':row.id}).then(res =>{
        console.log("删除标题", res);
        location.reload()
      }).catch(() => {
        alert("Error");
      })
    },
  },

  loading: true
};
</script>
<style>
.tab-container {
  height:100vh;
  margin: 40px;

}
.demo-table-expand {
  font-size: 0;
}
.demo-table-expand label {
  width: 90px;
  color: #99a9bf;
}
.demo-table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 100%;
}
</style>
