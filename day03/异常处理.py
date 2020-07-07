# 异常处理
# def div(a,b):
#     return a/b
#
# print(div(10,0))

# def div(a,b):
#     try:
#         print( a/b)
#     except ZeroDivisionError:
#         print('division by zero')
#     else:
#         print('除法执行成功')
#     finally:
#         print('不管是否成功都会打印')
# print(div(10,0))

# f = open('bbb.txt','r')
# f.readlines()
# f.close()

# try:
#     f = open('bbb.txt', 'r')
#     f.readlines()
#     f.close()
# except:
#     print('文件不存在')

# 自定义异常
# class CustomExcaption(Exception):
#     def __init__(self, value='值不能为零'):
#         self.value = value
#     def __str__(self):
#         return self.value
#
#
# a = 0
# try:
#     if a == 0:
#         print('a ={} 触发异常'.format(a))
#         raise CustomExcaption
#     print('a ={} 未触发异常'.format(a))
# except CustomExcaption as e:
#     print(e)
