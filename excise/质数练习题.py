# L = []  # 定义一个初始的素数列表
# for n in range(2,101): # 循环100以内的素数n,从2开始,0、1不是素数
#     flag = True  # 设置一个标志位,flag = True代表是素数，flag = Flase代表不是素数
#     for i in range(2,n): # 除以比它小的所有数（不包括1和它本身）,看它是否还有其他因数
#         if n % i == 0:
#             flag = False # 出现一次余数为0就代表可以除尽，即代表这个数为素数，就可以设置flag = False
#             break # 只要第一次出现flag = False，就不用继续往下循环，直接退出整个循环（第二层）
#     if flag == True:
#         L.append(n) # 当flag = True时代表n为素数,追加到素数列表中
# print("100以内的所有素数:",L)


# for i in range(2, 101):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)

# 倒序排列
# L = 'abcdefghijklmnopqrstuvwxyz'
# print(L[::-1])


