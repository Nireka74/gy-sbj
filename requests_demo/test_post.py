import requests

#post path数据
# header = {"token": "eyJ0aW1lT3V0IjoxNTk0MjY1MzIzMDcxLCJ1c2VySWQiOjI0MTI5LCJ1c2VyTmFtZSI6IjI5MHJnayJ9"}
# data = {
#   "balance": 1111
# }
# r = requests.request("POST","http://192.168.1.151:8084/acc/changeBalance/{accountId}".format(accountId=24107),headers=header,json=data)
# print(r.request.url)
# print(r.text)


# post键值对参数
# header = {"token": "eyJ0aW1lT3V0IjoxNTk0MjY0MDM1NTczLCJ1c2VySWQiOjI0ODEsInVzZXJOYW1lIjoiNDYwdWd6In0="}
# data = {"userName":"460ugz"}
# r = requests.request("POST", "http://192.168.1.151:8084/user/lock", data=data, headers=header)
# print(r.request.body)
# print(r.request.url)
# print(r.text)


# post json类型数据
# data = {
#   "pwd": "123456gh",
#   "userName": "sp777"
# }
# r = requests.request("POST", "http://192.168.1.151:8084/login",json=data)
# print(r.request.body)
# print(r.request.headers)
# print(r.text)

# data 和 header 两个关键字可以传任意数据类型的请求
# data 可以接收两种类型数据，一种字典格式先转成键值对类型，然后放入正文，一种字符串类型，直接放入正文里面。
# header = {"Content-Type":"application/json"}
# import json
# data = {
#   "pwd": "123456gh",
#   "userName": "sp777"
# }
# r = requests.request("POST", "http://192.168.1.151:8084/login",data=json.dumps(data),headers=header)
# print(r.request.body)
# print(r.request.headers)
# print(r.text)

# 下载文件
# header = {"token": "eyJ0aW1lT3V0IjoxNTk0MjY3MTU5MjEyLCJ1c2VySWQiOjI0MTQxLCJ1c2VyTmFtZSI6InlzYTE1NCJ9"}
# r = requests.request("GET", "http://192.168.1.151:8084/product/downRepertoryTemplate",headers=header)
# print(r.content)
# with open("aaa.xls","wb")as f:
#     f.write(r.content) # 获取响应数据中的二进制数据写入相应文件

# 上传文件
# f = open("aaa.xls","rb")
# file = {"file":f}
# header = {"token": "eyJ0aW1lT3V0IjoxNTk0Mjc3NTU4OTI1LCJ1c2VySWQiOjI0MTk5LCJ1c2VyTmFtZSI6IjE2MG1rbSJ9"}
# r = requests.request("POST","http://192.168.1.151:8084/product/uploaProdRepertory",files=file,headers=header)
# f.close()
# print(r.text)








