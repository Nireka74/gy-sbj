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
class Woman():
    money =1000000
    house =10
    __yi_wu = '裙子'

    def __init__(self,a):
        self.a = a

    def skill(self):
        print('吃喝玩乐')

# w = Woman(123)
# print(w.a)

# class Man(Woman):
#     hobby = '花钱'
#     def __init__(self,a):
#         super().__init__(a)
#
#     def skill(self):
#         print('白嫖')# 方法重写
#         super().skill()
#
# m = Man(123)
# print(m.skill())
# print(Man.money)
# print(m.house)
# print(m.hobby)
# m.skill()
# print(m.a)


