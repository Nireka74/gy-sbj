import requests
from config.env_config import QA_BASE_URL
from ramdom_tools.random_tool import random_tell, random_pwd ,random_string

ip_url = "http://192.168.1.151:8084"
a = 1
#注册
def test_signup():
    pwd = random_pwd()

    data = {
      "phone": random_tell(),
      "pwd": pwd,
      "rePwd": pwd,
      "userName": "sp"+random_string('0123456789',3)
    }
    r = requests.request("POST", QA_BASE_URL+'/signup',json=data)
    print(r.text)
    print(r.request.body)


#登录
def test_login():
    data = {
      "pwd": "123456gh",
      "userName": "sp777"
    }
    r = requests.request("POST", QA_BASE_URL+'/login',json=data)
    print(r.text)

    global a
    a = (r.json()["data"]["token"])

test_login()


#冻结-全字段正常流
def test_lock_normal():
    header = {"token": f"{a}"}
    data = {"userName":"904xdr"}
    r = requests.request("POST", f"{ip_url}/user/lock", data=data, headers=header)
    print(r.text)
    assert "冻结成功" in r.text

#冻结-异常流用户名已冻结
def test_lock_normal():
    header = {"token": f"{a}"}
    data = {"userName":"904xdr"}
    r = requests.request("POST", f"{ip_url}/user/lock", data=data, headers=header)
    print(r.text)
    assert "该用户已被冻结" in r.text


#冻结-异常流用户名为空
def test_lock_unnormal():
    header = {"token":f"{a}"}
    data = {"userName":""}
    r = requests.request("POST", f"{ip_url}/user/lock", data=data, headers=header)
    print(r.text)
    assert "该用户不存在" in r.text
#冻结-异常流用户名不存在
def test_lock_unnormal():
    header = {"token":f"{a}"}
    data = {"userName":"mkj256"}
    r = requests.request("POST", f"{ip_url}/user/lock", data=data, headers=header)
    print(r.text)
    assert "该用户不存在" in r.text

#解冻-全字段正常流
def test_unlock_normal():
    header = {"token":f"{a}"}
    data = {"userName":"517ugg"}
    r = requests.request("POST", f"{ip_url}user/unLock", data=data, headers=header)
    print(r.text)
    assert "解冻成功" in r.text

#解冻-异常流该用户已经解冻
def test_unlock_unnormal():
    header = {"token":f"{a}"}
    data = {"userName":"517ugg"}
    r = requests.request("POST", f"{ip_url}user/unLock", data=data, headers=header)
    print(r.text)
    assert "该用户已经解冻" in r.text

#解冻-异常流该用户不存在
def test_unlock_unnormal():
    header = {"token":f"{a}"}
    data = {"userName":"256kjn"}
    r = requests.request("POST", f"{ip_url}user/unLock", data=data, headers=header)
    print(r.text)
    assert "该用户不存在" in r.text

#解冻-异常流该用户为空
def test_unlock_unnormal():
    header = {"token":f"{a}"}
    data = {"userName":""}
    r = requests.request("POST", f"{ip_url}user/unLock", data=data, headers=header)
    print(r.text)
    assert "该用户不存在" in r.text






# 注册
d = {}
def test_signup1():
    d["pwd"]= random_pwd()
    d["username"]= "sp" + random_string('0123456789', 3)

    data = {
        "phone": random_tell(),
        "pwd": d["pwd"],
        "rePwd": d["pwd"],
        "userName": d["username"]
    }
    r = requests.request("POST", QA_BASE_URL + '/signup', json=data)
    print(r.text)
    print(r.request.body)
    assert "注册成功" in r.text



# 登录
def test_login1():
    data = {
        "pwd": d["pwd"],
        "userName": d["username"]
    }
    r = requests.request("POST", QA_BASE_URL + '/login', json=data)
    print(r.text)
    d["token"] = (r.json()["data"]["token"])
    assert "登录成功" in r.text

#冻结
def test_lock_normal1():
    header = {"token": d["token"]}
    data = {"userName":d["username"]}
    r = requests.request("POST", QA_BASE_URL +"/user/lock", data=data, headers=header)
    print(r.text)
    assert "冻结成功" in r.text