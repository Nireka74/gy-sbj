# import requests
# api_url = 'http://192.168.1.151:8084'
#
#
# data = {
#   "pwd": "qq1234",
#   "userName": "KDS123"
# }
# r = requests.request("POST", f"{api_url}/login", json=data)
#
# # 获取请求方法
# print(r.request.method)
# # 获取请求url
# print(r.request.url)
# # 获取请求头
# print(r.request.headers)
# # 获取请求正文
# print(r.request.body)
#
# # 获取响应状态码
# print(r.status_code)
# # 获取响应头
# print(r.headers)
# # 获取响应正文
# # 获取正文中编码后的结果，一般用在响应断言
# print(r.text)
# # 获取响应中的原始数据，一般用于下载文件
# print(r.content)
# # 获取响应的json数据（字典），一般用来提取响应数据
# print(r.json())




import random

# 随机生成手机号码和名字
class random_pn():

    def phone(self):
        prelist=["130","131","132","133","134","135","136","137","138","139","147","150","151","152","153","155","156","157","158","159","186","187","188"]
        return random.choice(prelist)+"".join(random.sample("0123456789",8))

    def name(self):
        xing='abcdefjhijklmnopqrst'
        ming='01234567879'
        X="".join(random.sample(f"{xing}",5))
        M="".join(random.choice(ming) for i in range(5))
        return X+M

a = random_pn()
print(a.name())

