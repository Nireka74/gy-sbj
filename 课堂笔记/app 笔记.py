from flask import Flask, request, jsonify
import re

from tools.mysql_tool import mysql_db

app = Flask(__name__)


# 注册功能
@app.route('/signup',methods=["POST"])
def hello_world():
    req = request.json

    # 用户名 长度内容
    username = req['username'] # 获取请求数据中的用户名
    r_username = re.compile("^[\w]{6,10}$") # 编译用户名校验的正则

    if(len(r_username.findall(username)) == 0): # 判断用户名是否符合正则，如果不符合返回
        return jsonify({"code":"9999","msg":"用户名必须是6-10位的数字、字母、下划线","data":None}) # jsonify响应返回json数据

    # 密码长度内容
    password = req['password']  # 获取请求数据中的密码
    r_password = re.compile("^[a-zA-Z\d]{8,12}$")  # 编译密码校验的正则
    if (len(r_password.findall(password)) == 0):  # 判断密码是否符合正则，如果不符合返回
        return jsonify({"code": "9999", "msg": "密码必须是8-12位的数字、字母", "data": None})  # jsonify响应返回json数据
    # 用户是否存在验证
    mydb = mysql_db('192.168.1.161', 'stu', 'stu123', 'stuTest') # 实例化mysql工具类
    res = mydb.select_execute("SELECT id FROM `test_user` WHERE username = '{}';".format(username)) # 执行查询sql语句
    if(len(res) != 0): # 判断查询结果非空
        return jsonify({"code": "9999", "msg": "用户名已存在", "data": None})
    # 密码是否一致验证
    repassword = req['repassword'] # 获取重复密码
    if(password != repassword): # 判断密码和重复密码是否一致
        return jsonify({"code": "9999", "msg": "两次密码输入不一致", "data": None})

    # 插入数据到数据库
    res = mydb.update_execute("INSERT INTO `test_user` (username,PASSWORD) VALUE('{}','{}');".format(username,password)) # 把用户名和密码添加到数据库中
    if res: # 对插入结果进行判断
        return jsonify({"code": "0000", "msg": "注册成功", "data": req})
    else:
        return jsonify({"code": "9999", "msg": "注册失败", "data": req})



if __name__ == '__main__':
    app.run()
