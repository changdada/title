
"""
    文件说明:
    构建web服务文件
"""

from gevent import monkey
monkey.patch_all()
from flask import Flask, request, render_template,session,make_response
from flask_session import Session
import datetime
from datetime import timedelta
from flask_cors import CORS
import argparse
from gevent import pywsgi
from generate_title import predict_one_sample
from generate_abstract import predict_one_abstract
import torch
from model import GPT2LMHeadModel
from transformers import BertTokenizer
import os

import json


from flask_sqlalchemy import SQLAlchemy
import pymysql
import traceback
pymysql.install_as_MySQLdb()


def set_args():
    """设置所需参数"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--device', default='0', type=str, help='设置预测时使用的显卡,使用CPU设置成-1即可')
    parser.add_argument('--output_dir', default='output_dir/checkpoint-139805', type=str, help='模型文件路径')
    parser.add_argument('--vocab_path', default='vocab/vocab.txt', type=str, help='词表，该词表为小词表，并增加了一些新的标记')
    parser.add_argument('--batch_size', default=3, type=int, help='生成标题的个数')
    parser.add_argument('--generate_max_len', default=32, type=int, help='生成标题的最大长度')
    parser.add_argument('--repetition_penalty', default=1.2, type=float, help='重复处罚率')
    parser.add_argument('--top_k', default=5, type=float, help='解码时保留概率最高的多少个标记')
    parser.add_argument('--top_p', default=0.95, type=float, help='解码时保留概率累加大于多少的标记')
    parser.add_argument('--max_len', type=int, default=512, help='输入模型的最大长度，要比config中n_ctx小')
    parser.add_argument('--http_id', type=str, default="localhost", help='ip地址')
    parser.add_argument('--port', type=int, default=5555, help='端口号')
    return parser.parse_args()

def set_args_abstract():
    """设置所需参数"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--device', default='0', type=str, help='设置预测时使用的显卡,使用CPU设置成-1即可')
    parser.add_argument('--output_dir', default='output_dir/checkpoint-139805', type=str, help='模型文件路径')
    parser.add_argument('--vocab_path', default='vocab/vocab.txt', type=str, help='词表，该词表为小词表，并增加了一些新的标记')
    parser.add_argument('--batch_size', default=3, type=int, help='生成标题的个数')
    parser.add_argument('--generate_max_len', default=128, type=int, help='生成摘要的最大长度')
    parser.add_argument('--repetition_penalty', default=1.2, type=float, help='重复处罚率')
    parser.add_argument('--top_k', default=5, type=float, help='解码时保留概率最高的多少个标记')
    parser.add_argument('--top_p', default=0.95, type=float, help='解码时保留概率累加大于多少的标记')
    parser.add_argument('--max_len', type=int, default=512, help='输入模型的最大长度，要比config中n_ctx小')
    parser.add_argument('--http_id', type=str, default="localhost", help='ip地址')
    parser.add_argument('--port', type=int, default=5555, help='端口号')
    return parser.parse_args()


def start_sever():
    args = set_args()
    args_abstract = set_args_abstract()
    os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
    os.environ["CUDA_VISIBLE_DEVICE"] = args.device
    device = torch.device("cuda" if torch.cuda.is_available() and int(args.device) >= 0 else "cpu")
    # 实例化tokenizer和model
    tokenizer = BertTokenizer.from_pretrained(args.vocab_path, do_lower_case=True)
    model = GPT2LMHeadModel.from_pretrained(args.output_dir)
    model.to(device)
    model.eval()
    print("load model ending!")
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_KEY_PREFIX'] = 'flaskSession:'  # 可以不输入，用来做session的前缀
    app.config['SECRET_KEY'] = os.urandom(24)
    # app.config['session_redis'] == Redis(host="localhost", port="6379")
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

    Session(app=app)


    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/title'
    # 协议：mysql+pymysql
    # 用户名：root
    # 密码：root
    # IP地址：localhost
    # 端口：3306
    # 数据库名：title
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    db = SQLAlchemy(app)
    CORS(app, supports_credentials=True)

    class User(db.Model):



        # 声明表名

        __tablename__ = 'user'

        # 建立字段函数

        id = db.Column(db.Integer, primary_key=True)

        name = db.Column(db.String(255))

        pwd = db.Column(db.String(255))

        email = db.Column(db.String(255))

        phone = db.Column(db.String(255))

    class Ai_title(db.Model):

        # 声明表名

        __tablename__ = 'ai_title'

        # 建立字段函数

        id = db.Column(db.Integer, primary_key=True)

        user_id = db.Column(db.Integer)

        time = db.Column(db.String(255))

        title = db.Column(db.String(255))

        abstract = db.Column(db.String(255))

        content = db.Column(db.String(10000))

    @app.route('/api/login', methods=['Post','Get'])
    def Login():
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        db = pymysql.connect(host="localhost", user="root", password="root", db="title")
        cursor = db.cursor()

        data = request.get_json("pwd")
        name = data['names']
        pwd = data['pwd']
        sql = "select * from user where name='"+name+"' or email = '" + name + "' or phone = '" + name + "' and pwd ='" + pwd + "'"
        try:
            # 执行sql语句
            cursor.execute(sql)

            # results = cursor.fetchall()
            results = cursor.fetchone()
            print(results)
            if results != None:
                flag = 1
                # print(name)
                session['user_id'] = results[0]
                session['results'] = results
                session['name'] = name
                session['pwd'] = pwd
                session['email'] = results[3]
                session['phone'] = results[4]


                return str(flag)
            else:
                flag = 0
                return str(flag)
            # 提交到数据库执行
            db.commit()

        except:
            # 如果发生错误则回滚
            traceback.print_exc()
            db.rollback()
            # 关闭数据库连接
        db.close()



    @app.route('/api/register', methods=['Post'])
    def Register():


        data = request.get_json("pwd")
        name = data['names']
        pwd = data['pwd']
        email = data['email']
        phone = data['phone']
        db1 = pymysql.connect(host="localhost", user="root", password="root", db="title")
        cursor = db1.cursor()
        sql = "select * from user where name='" + name + "'"
        cursor.execute(sql)

        results = cursor.fetchall()
        print(len(results))
        db1.commit()
        if len(results) == 1:
            return "warning"
        else:
            user = User(name=name, pwd=pwd, email=email, phone=phone)
            db.session.add(user)
            return "success"




    @app.route('/api/user',methods=['Post','Get'])
    def user():
        db = pymysql.connect(host="localhost", user="root", password="root", db="title")
        cursor = db.cursor()
        id = session.get('user_id')

        print(id)
        sql = "select * from user where id='" + str(id) + "'"
        # 执行sql语句
        cursor.execute(sql)


        results = cursor.fetchone()

        name = results[1]
        pwd = results[2]
        email = results[3]
        phone = results[4]
        dict = {}
        dict['name'] = name
        dict['pwd'] = pwd
        dict['email'] = email
        dict['phone'] = phone

        # print(pwd)
        # return tuple('name',name),tuple('pwd',pwd),tuple('email',email),tuple('phone',phone)
        return dict

    @app.route('/api/update_message', methods=['Post'])
    def update_message():
        db = pymysql.connect(host="localhost", user="root", password="root", db="title")
        cursor = db.cursor()
        id = session.get('user_id')

        data = request.get_json("pwd")
        name = data['name']
        email = data['email']
        phone = data['phone']
        sql = "update user set name='" + name + "' ,email='" + email + "' ,phone='"+phone+"' where id="+str(id)
        cursor.execute(sql)
        db.commit()
        return "good"

    @app.route('/api/update_pwd', methods=['Post'])
    def update_pwd():
        db1 = pymysql.connect(host="localhost", user="root", password="root", db="title")
        cursor1 = db1.cursor()
        data = request.get_json("pwd")
        pwd = data['pwd']
        sql1 = "select * from user where pwd ='" + pwd + "'"
        cursor1.execute(sql1)
        results = cursor1.fetchall()
        if len(results) >= 1:
            db = pymysql.connect(host="localhost", user="root", password="root", db="title")
            cursor = db.cursor()
            id = session.get('user_id')


            new_pwd = data['new_pwd']
            sql = "update user set pwd='" + new_pwd + "' where id=" + str(id)
            print(sql)
            cursor.execute(sql)
            db.commit()
            return "success"
        else:
            return "error"



    @app.route('/api/generate_sql' ,methods=['POST'])
    def response_requests():

        user_id = session.get('user_id')
        data = request.get_json("pwd")
        content = data["content"]
        print(content)
        titles = predict_one_sample(model, tokenizer, device, args, content)
        abstract = predict_one_abstract(model, tokenizer, device, args_abstract, content)


        title = Ai_title(user_id=user_id, time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') ,title=titles[2], abstract=abstract[2], content=content)
        db.session.add(title)

        dict = {}
        dict['title'] = titles[2]
        dict['abstract'] = abstract[2]
        return dict

    # server = pywsgi.WSGIServer((str(args.http_id), args.port), app)
    # server.serve_forever()

    @app.route('/api/select_title',methods=['Post','Get'])
    def select_title():
        user_id = session.get('user_id')
        print(user_id)
        db = pymysql.connect(host="localhost", user="root", password="root", db="title")
        cursor = db.cursor()
        sql = "select id,time,title,abstract,content from ai_title where user_id = '" + str(user_id)+"'"
        cursor.execute(sql)
        row_headers = [x[0] for x in cursor.description]
        # results = cursor.fetchone()
        results = cursor.fetchall()
        len_select = len(results)
        json_data = []

        for result in results:
            json_data.append(dict(zip(row_headers, result)))
        print(json_data)
        print(json.dumps(json_data))
        return json.dumps(json_data)
        # else:
        #     return 'nice'

    @app.route('/api/delete_title',methods=['Post'])
    def delete_title():
        data = request.get_json("pwd")
        id = data['id']
        db = pymysql.connect(host="localhost", user="root", password="root", db="title")
        cursor = db.cursor()
        sql = "delete from ai_title where id='"+ str(id) +"'"
        cursor.execute(sql)
        db.commit()

        return "success"


    @app.route('/api/news-title-generate', methods=['Post'])
    def response_request():
        # if request.method == 'POST':
        data = request.get_json("pwd")
        content = data["content"]
        print(content)
        titles = predict_one_sample(model, tokenizer, device, args, content)
        abstract = predict_one_abstract(model, tokenizer, device, args_abstract, content)


        title_str = ""
        # for i, t in enumerate(titles):
        #     title_str += "生成的第{}个标题为：{}\n".format(i+1, t)
        dict = {}
        dict['title'] = titles[2]
        dict['abstract'] = abstract[2]
        return dict

    @app.route('/api/quit', methods=['Post'])
    def quits():
        session.clear()
        return "True"
    server = pywsgi.WSGIServer((str(args.http_id), args.port), app)
    server.serve_forever()



    # @app.after_request
    # def af_req(resp):  # 解决跨域session丢失
    #     resp = make_response(resp)
    #     resp.headers['Access-Control-Allow-Origin'] = 'http://localhost:8081'
    #     resp.headers['Access-Control-Allow-Methods'] = 'PUT,POST,GET,DELETE,OPTIONS'
    #     # resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    #     resp.headers[
    #         'Access-Control-Allow-Headers'] = 'Content-Type, Content-Length, Authorization, Accept, X-Requested-With , yourHeaderFeild'
    #     resp.headers['Access-Control-Allow-Credentials'] = 'true'
    #
    #     resp.headers['X-Powered-By'] = '3.2.1'
    #     resp.headers['Content-Type'] = 'application/json;charset=utf-8'
    #     return resp


if __name__ == '__main__':
    start_sever()

