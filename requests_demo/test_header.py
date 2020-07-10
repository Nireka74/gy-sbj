import requests

# 请求头需要加token的请求
header = {"token": "eyJ0aW1lT3V0IjoxNTk0MjYzMTczMzE4LCJ1c2VySWQiOjI0MTA4LCJ1c2VyTmFtZSI6Ijk1NG9mcyJ9"}
r = requests.request("GET", "http://192.168.1.151:8084/acc/getAllAccs/{pageNum}/{pageSize}".format(pageNum=1, pageSize=3),headers=header)
print(r.request.url)
print(r.request.headers)
print(r.text)

