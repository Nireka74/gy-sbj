import requests

# 发送请求
# get无参数请求

# r = requests.request("GET","http://mall.yansl.com:8080/prefrenceArea/listAll")
# print(r.text)

# get query参数请求

# para = {"accountName": "sp777"}
# r = requests.request("GET","http://192.168.1.151:8084/acc/getAccInfo",params=para)
# print(r.request.url)
# print(r.text)

# get path数据

# r = requests.request("GET", "http://mall.yansl.com:8080/order/{id}".format(id=12))
# print(r.request.url)
# print(r.text)

# r = requests.request("GET", "http://192.168.1.151:8084/acc/getAllAccs/{pageNum}/{pageSize}".format(pageNum=1, pageSize=3))
# print(r.request.url)
# print(r.text)

# 下载文件



