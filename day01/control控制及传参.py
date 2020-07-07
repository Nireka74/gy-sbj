# 条件控制
# score = 59
# if ( score < 0):
#     print('请输入正确的成绩')
# if (score >= 0 and score <= 59):
#     print('不及格')
# if (score >= 60 and score <= 70):
#     print('及格')
# if (score >= 71 and score <= 80):
#     print('良好')
# if (score >= 81 and score <= 100):
#     print('优秀')

# score_1 = [80,10,25,99,100,71]
# for score in score_1:
#  score = int(input('请输入正确成绩'))
#     if (score >= 0 and score <= 59):
#         print('不及格')
#     elif (score >= 60 and score <= 70):
#         print('及格')
#     elif (score >= 71 and score <= 80):
#         print('良好')
#     elif (score >= 81 and score <= 100):
#         print('优秀')
#     else:
#         print('请输入正确的成绩')

# 循环控制
# s = 1
# for i in range(10,0,-1):
#    s *= i
# print(s)

# flag = True
# a = 32
# while flag:
#     b = int(input("请输入数字"))
#     if b > a:
#         print("大了")
#     elif b < a:
#         print("小了")
#     else:
#         print("答对了")
#         flag = False
#
# 终止循环 break，continue
#
# a = 32
# while True:
#     b = int(input("请输入数字"))
#     if b > a:
#         print("大了")
#     elif b < a:
#         print("小了")
#     else:
#         print("答对了")
#         break

# 请找出100以内被2整除的数
# for i in range(1,101):
#     if (i % 2 != 0):
#         continue
#     print (i)

# def 方法定义和调用
# 定义一个两个数取余和商的方法
# def shang_yu(a,b): #行参
#     if b == 0:
#         print('除数不能为零')
#     else:
#         print('商',a // b,'余',a % b)
# shang_yu(10,3) #实参
# shang_yu(20,0)

# 方法传参，return提供返回值,给返回值提供解决方案

# def shang_yu(a,b):
#     if (b == 0):
#         return None
#     else:
#         return(a // b,a % b)

# res = shang_yu(30,0) #按照位置传参
# res = shang_yu(b = 20,a = 10) #按照关键字传参
#
# if res is None:
#     print('参数错误')
# else:
#     print ('商:',res[0],'余:',res[1])

#传参

#定义关键字形参，给参数b设置默认值,默认值在后面 (必选参数)

# def sm(a,b=2):
#     return a+b
# print(sm(2))

# 传参个数不确定，*args设置动态位置参数(可变参数)，**kwargs接收动态位置参数(关键字参数)

# args 多余的值以元祖的方式呈现
# def sum1(*args):
#     s = 0
#     for i in args:
#         s+=i
#     return s
# print(sum1(1,23,25,36,89,54,65.5))

# kwargs 多余的值以字典的方式呈现
# def sum1(name,**kwargs):
#     print(kwargs)
#     print(name)
# print(sum1(name='小可爱'))
#
# def person(name, age, **kwargs):
#     print('name:', name, 'age:', age, kwargs)
#     return
# print(person('沈小君',18,职位='测试'))