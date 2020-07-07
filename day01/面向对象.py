# 面向对象
# class calc():
#     a = None
#     b = None
#     res = None
#
#     def input(self, a, b):
#         self.a = a
#         self.b = b
#     def sum(self):
#         self.res = self.a + self.b
#     def div(self):
#         self.res = self.a / self.b
#     def minus(self):
#         self.res = self.a - self.b
#     def get_result(self):
#         print(self.res)
#
# c = calc()
#
# c.input(10, 20)
# c.sum()
# c.get_result()
# c.div()
# c.get_result()
# c.minus()
# c.get_result()


# 类变量
# 实例变量
# 局部变量
# class calc():
#     res = None # 类变量，类的所有实例共享
#     def __init__ (self,a,b): #魔法函数，类实例化的时候使用，又称构造方法
#         self.a = a # 实例变量，只有当前对象可用
#         self.b = b
#            c = 10 #局部变量
#     def sum(self): # 实例方法
#         self.res = self.a + self.b
#     def div(self):
#         self.res = self.a / self.b
#     def minus(self):
#         self.res = self.a - self.b
#     def get_result(self):
#         print(self.res)

# @classmethod
# def get_res(cls):  # 类方法定义：必须添加名字为@classmethod的装饰器，第一个参数名 cls ，cls代表当前类本身。
#     print(cls.res)
# calc.get_res() # 类方法在使用的时候，通过类名调用。不需要实例化


# def sum(self): # 实例方法：不需要装饰器，实例方法通常会用类对象直接调用，最少包含一个self参数。
# c.sum() #类对象直接调用

# @staticmethod
# def static():  # 静态方法定义：必须使用@staticmethod装饰器，无默认参数
#     print("我是静态方法")
# calc.static() # 静态方法通过类名调用

# c = calc(15,10) # 通过对象去操作实例变量
# c.a = 100  # 通过对象去操作实例变量
# calc.res = 1000 # 通过类名去操作类变量
# c.div()
# c.get_result()

# 九九乘法表
# 顺序
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,'x',i,'=',i*j,end='\t')
#     print()
# 倒叙
# for i in range(9,0,-1):
#     for j in range(i,0,-1):
#         print(j,'x',i,'=',i*j,end='\t')
#     print()

# 冒泡排序
# l = [1,52,12,451,23,65,54,11,33,52,42,21,15,78,98]
#
# length = len(l) # 统计列表长度
# for i in range(length-1,0,-1): #通过长度求索引的列表，以i来命名索引的列表
#     for j in range(i): # 通过索引位置比较大小
#         if(l[j] > l[j+1]):
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)

# A = [12.21,11,41,2,3,6,56,15,52,21,11,2,3,32,89,12345]
# length = len(A)
# for i in range (length-1,0,-1):
#     for j in range(i):
#         if(A[j]>A[j+1]):
#             A[j],A[j+1] = A[j+1],A[j]
# print(A)

#类的封装
# class aaa():
#类变量
    # pub_res = '公有变量'
    # _pri_res = '私有变量'
    # __pri_res = '私有变量2'
#类变量通过类直接调用，双下划线私有变量不能调用。单下划线私有变量能调用，不能修改。
# print(aaa.pub_res)
# print(aaa._pri_res)

# class aaa():
    # 实例方法
    # def pub_function(self):
    #     print('公有方法')
    # def _pri_function(self):
    #     print('私有方法')
    # def __pri_function(self):
    #     print('私有方法2')
#实例方法通过对象调用
# print(aaa().pub_function())
# print(aaa()._pri_function())


#类的继承
# class Woman():
#     money =1000000
#     house =10
#     __yi_wu = '裙子'
#
#     def __init__(self,a):
#         self.a = a
#
#     def skill(self):
#         print('吃喝玩乐')

# w = Woman(123)
# print(w.a)

# class Man(Woman):
#     hobby = '花钱'
#     def __init__(self,a):
#         super().__init__(a)
#
#     def skill(self):
#         print('吃喝玩乐2566')# 方法重写
#         super().skill()
#
# m = Man(123)
# print(m.skill())
# print(Man.money)
# print(m.house)
# print(m.hobby)
# m.skill()
# print(m.a)



