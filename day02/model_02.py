# from excise import model_01

# print(model_01.a)
# print(model_01.name())
# print(model_01.Test.name)

# from excise.model_01 import a as model_01_a,name as model_01_name,Test as model_01_Test

# print(model_01_a)
# print(model_01_name())
# print(model_01_Test.name)


a = '我是model_02中的变量a'

def name():
    print('我是model_02中的方法name')


class Test():
    name = '我是model_02中的Test类变量'

if __name__ == '__main__':
    name()
    print(Test.name)
