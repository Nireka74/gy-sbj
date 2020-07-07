# l = ["果芽","老干妈","腾讯","百度","阿里"]
# if ("果芽" in l):
#     print("合作方")
# else:
#     print("非合作方")
#
# """
# 成绩评定： 0-59分 不及格 60-70 及格 71-80 良好 81-100 优秀
# 编写程序实现下列需求，给定任意成绩，程序运行之后输出该成绩的级别
# 例如：59分，程序打印出"不及格"
#
# """
#
# score_l = [40,70,90,20,87,38,29,30,68,98] # 可迭代对象
#
# for score in score_l:
#     if(score > 0 and score < 60):
#         print("不及格")
#     elif(score >= 60 and score <= 70):
#         print("及格")
#     elif(score >= 71 and score <= 80):
#         print("良好")
#     elif(score >= 81 and score <= 100):
#         print("优秀")
#     else:
#         print("请输入正确的成绩")



'''
if():
    代码块
elif():
    代码块
else:
    代码块
'''

# 100以内数的和 不算100
# s = 0
# for i in range(100):
#     s = s + i
# print(s)


# range()
# 第一个参数：起始数据 默认值为0
# 第二个参数：代表结束值，不包含边界
# 第三个参数：步长（增量） 默认值为1
#
# for i in range(1,100,2):
#     print(i)
#
# for i in range(100,0,-1):
#     print(i)

# 求出10*9*8.。。*1 的结果 10的阶乘  10!
# s = 1
# for i in range(10,0,-1):
#     s *= i
# print(s)

# 猜数字，

#
# a=29
#
# while True:
#     b = int(input("请输入数字"))
#     if b > a :
#         print("大了")
#     elif(b < a):
#         print("小了")
#     else:
#         print("猜对了")
#         break


'''
break 终止循环
continue 跳过本次循环
'''


# 找出100以内可以被3整除的数字

# for i in range(1,100):
#     if (i % 3 != 0):
#         continue
#     print(i)



#
#
#
# def level(score):
#     if (score > 0 and score < 60):
#         print("不及格")
#     elif (score >= 60 and score <= 70):
#         print("及格")
#     elif (score >= 71 and score <= 80):
#         print("良好")
#     elif (score >= 81 and score <= 100):
#         print("优秀")
#     else:
#         print("请输入正确的成绩")
#
# level(50)
# level(80)
#
# print("要不要叫家长？")



#(a+b)**2
# a ** 2 + b ** 2 + 2 * a * b
#
# a = 10
# b = 20
#
# print(a,"** 2 + ",b,"** 2 + ","2 * ",a," * ", b)



# # 定义一个求两个数商和余数的方法 方法定义
# def shang_yu(a,b): # a,b形参
#     if(b == 0):
#         print("除数不能为0")
#     else:
#         print("商：", a // b, ",余数：", a % b)
#
# shang_yu(10,2) # 方法调用 10,2实参
# shang_yu(20,3)
# shang_yu(20,0)

# 一个接口的功能是一样的。不同的人传不同的数据，给到处理结果不一样。


#
# def shang_yu(a,b): # a,b形参 a=20 b = 2
#     if(b == 0):
#         return None  # return 返回值
#     else:
#         return (a//b,a%b)# (10,0)




# res = shang_yu(20,2) # 按照位置传参

# res = shang_yu(b=2,a=20) # 按照关键字传实参
# res = shang_yu(20,b=2)
#
# if res is None:
#     print(res)
#     print("参数错误")
# else:
#     print(res)
#     print("商为：",res[0],"余数为：",res[1])
#
#
# def sm(a,b=2): # 定义关键字形参,给参数b设置默认值
#     return a+b
#
# print(sm(2))

#
# c = 1,2,3,4
# a,*b = (1,2,3,4)
#
# print(b)
#
# def sum1(name,*args,**kwargs): # *args接收动态位置参数，**kwargs 接收动态关键字参数
#     print(kwargs)
#     print(name)
#     s = 0
#     for i in args:
#         s+=i
#     return s
# print(sum1(1,2,3,56,7,8,9,0,3,3,4,4,7))
# print(sum1(name="薛小磊"))




# a = 10 # 全局变量
# print(a)
#
# def aaa():
#     b = 13 # 局部变量
#     global a
#     a = 12
#
#
# aaa()
# print(a)



# 面向对象
# # 定义类
# class calc():
#     a=None
#     b=None
#     res=None
#     def input(self,a,b):
#         self.a=a
#         self.b=b
#
#     def sum(self):
#         self.res = self.a + self.b
#
#     def div(self):
#         self.res = self.a / self.b
#
#     def get_result(self):
#         print(self.res)
#
#
# c = calc() # 类的实例化 c对象 实例
#
# c.input(10,20)
# print(c.a)
# # c.sum()
# # c.get_result()
# # c.div()
# # c.get_result()
#
# d = calc()
# d.input(29,39)
# print(d.a)

# 类变量
# 实例变量
# 局部变量

class calc():
    res = None # 类的所有实例共享

    def __init__(self,a,b): # 魔法函数，类实例化的时候调用，又称构造方法
        self.a=a # 实例变量，只有当前对象可用
        self.b=b
        c = 10

    def sum(self): # 实例方法
        self.c = 10
        self.res = self.a + self.b

    def div(self):
        self.res = self.a / self.b

    def get_result(self):
        print(self.res)

    @classmethod
    def get_res(cls): # 类方法定义：必须添加名字为@classmethod的装饰器，第一个参数名 cls cls代表当前类本身
        print(cls.res)

    @staticmethod
    def static(): # 静态方法定义：必须使用@staticmethod装饰器，无默认参数
        print("我是静态方法")



c = calc(29,39) # 通过对象去操作实例变量
c.a = 100
print(c.a)

calc.res = 1000 # 通过类名去操作类变量
calc.get_res() # 类方法在使用的时候，通过类名调用。不需要实例化

calc.static() # 通过类名调用