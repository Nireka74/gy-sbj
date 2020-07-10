import requests
from config.env_config import QA_BASE_URL
from ramdom_tools.random_tool import random_tell, random_pwd ,random_string
import pytest



@pytest.fixture(scope="module")
def d():
    a={}
    a["pwd"] = random_pwd()
    a["username"] = "sp" + random_string('0123456789', 3)
    return a



# 注册
from test_pytest.conftest import d1


def test_signup(d):
    data = {
      "phone": random_tell(),
      "pwd":d["pwd"] ,
      "rePwd": d["pwd"],
      "userName": d["username"]
    }
    r = requests.request("POST", QA_BASE_URL+'/signup',json=data)
    print(r.text)
    print(r.request.body)


#登录
def test_login(d):
    data = {
      "pwd": d["pwd"],
      "userName":  d["username"]
    }
    r = requests.request("POST", QA_BASE_URL+'/login',json=data)
    print(r.text)

    # d["token"]= (r.json()["data"]["token"])




#冻结-全字段正常流
def test_lock_normal(d):
    header = {"token": d["token"]}
    data = {"userName":"lst32248"}
    r = requests.request("POST", QA_BASE_URL+"/user/lock", data=data, headers=header)
    print(r.text)
    assert "冻结成功" in r.text


#解冻-全字段正常流
def test_unlock_normal(d):
    header = {"token":d["token"]}
    data = {"userName":d["username"]}
    r = requests.request("POST", QA_BASE_URL+"/user/unLock", data=data, headers=header)
    print(r.text)
    assert "解冻成功" in r.text






