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


# 登录
def test_login(d):
    data = {
      "pwd": d["pwd"],
      "userName":  d["username"]
    }
    r = requests.request("POST", QA_BASE_URL+'/login',json=data)
    print(r.text)

    d["token"]= (r.json()["data"]["token"])

# 创建产品

def test_add_product(d):
    header = {"token": d["token"]}
    data = {
      "brand": "阿迪",
      "colors": [
        "红色","黑色"
      ],
      "price": 200,
      "productCode": "23ab",
      "productName": "书包",
      "sizes": [
        "s","m"
      ],
      "type": "配饰"
    }
    r = requests.request("POST", QA_BASE_URL+"/product/addProd", json=data, headers=header)
    print(r.text)
    assert "2000" in r.text

