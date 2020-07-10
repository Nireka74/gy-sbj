
# post无参数

# post键值对参数
import requests

def test_post_form_data():
    header = {"token":"eyJ0aW1lT3V0IjoxNTk0MjYyNTg4MDYwLCJ1c2VySWQiOjkxLCJ1c2VyTmFtZSI6Inpob25neng4OSJ9"}
    data = {"userName":"xuepl123"}
    r = requests.request("POST","http://192.168.1.151:8084/user/lock" , data=data,headers = header) # data参数关键字可以把字典类型的数据转成键值对类型，再存入请求正文中
    print(r.request.body) # 获取请求正文的数据
    print(r.text)


# post json数据

def test_post_json_1():
    data= {
      "pwd": "6esDTQ0z",
      "userName": "zhongzx89"
    }

    r = requests.request("POST","http://192.168.1.151:8084/login",json=data) # json 参数关键字把字典类型数据转成json字符串，并忘请求头中添加content-type：application/json

    print(r.request.body)
    print(r.request.headers)
    print(r.text)

def test_post_json_2():
    data= {
      "pwd": "6esDTQ0z",
      "userName": "zhongzx89"
    }

    header = {
    'Content-Type': 'application/json'
    }
    import json

    r = requests.request("POST","http://192.168.1.151:8084/login",data=json.dumps(data),headers = header) # json 参数关键字把字典类型数据转成json字符串，并忘请求头中添加content-type：application/json
    '''
    data可以接收两种类型的数据，字典：先转成键值对类型，然后再放入正文，一种字符串类型：直接放入正文里边
    '''

    print(r.request.body)
    print(r.request.headers)
    print(r.text)


# post上传文件
def test_post_upload():
    f = open("aaa.xls",'rb')
    file = {"file":f}
    header = {"token":"eyJ0aW1lT3V0IjoxNTk0Mjc2NjM4MzcxLCJ1c2VySWQiOjI0MTY2LCJ1c2VyTmFtZSI6IkZrSlI3UiJ9"}
    r = requests.request("POST","http://192.168.1.151:8084/product/uploaProdRepertory",files=file,headers=header)
    f.close()
    print(r.text)


# if __name__ == '__main__':
#     post_form_data()
#     post_json_1()
#     post_json_2()
#     post_upload()


