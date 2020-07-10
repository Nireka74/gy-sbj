# open 打开模式：r 读取 w 清空写入 a追加写入 b二进制模式
# 写入
#f = open('sp.txt','w',encoding ="utf-8")
# f.write('全世界最可爱的是谁？\n沈毕君')
# f.write('asdasd\nsdad\nsdasda\n') #write写入内容至打开的文件，仅限字符串
#f.writelines(['12234\n','agshhdj\n','ghjnkkm\n'])#write写入内容至打开的文件，可以字符转也可以序列
#print(f.writable())#判断是否能写入
#f.close()

#  读取
# f = open('sp.txt','r',encoding ="utf-8")
# print(f.read())# 默认读取全部数据
# print(f.read(10))#读取指定大小的数据
# print(f.readline())#按行读取，读取一行
# print(f.readlines())#按行读取，读取所有行
# f.close()


#字符串常见操作

# 数字转字符串
# a = 12
# b = '235678'
# print(str(a)+b)
# 字符串转数字
# a = 123
# b = '235678'
# print(a+int(b))

#字符串转有序的列表，元祖，集合
# a = '12345678945'
# print(list(a))
# print(tuple(a))
# print(set(a))

#读取字符串
a = 'abcdefghijklmnop'
#print(a[0])
#print(a[2:-1])
#print(a[3:-2:2])
print(a[-1:1:-1])

#前后去空格
# s ='   aaa www  '
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())

#字符串按对应符号分隔
# l='asda:jkkk231:sd'
# print(l.split(':'))

# replace替换，使用一个上下文管理器
# with open('sp.txt','r') as f:
#     lines = f.readlines()
#     print(lines)
#     for i in lines:
#         print(i.replace('\n',''),end='\t') #print默认带一个换行

#查找字符串中的摸个字符的位置 find
# c ='sdsaf/sdfakfjdh'
# print(c.find('/'))

#格式化
## 占位符格式化
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d X %d = %d'%(j,i,i*j),end='\t')
#     print()

## .format格式化
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{} X {}= {}'.format(j,i,i*j),end='\t')
#     print()

#列表常见操作

#修改列表
# l=[1,20,32,12,5]
#l[0]=32
#print(l)
# l[2:4]= 44,22
# print(l)
# l =['cd','aa','bb','ddc']
# l[0]= 'dd'
# print(l)
# l[2:4]= '尼玛','我'
# print(l)

#新增数据
# l= ['cd', 'aa', '尼玛', '我']
# l.append('沈小君')
# l.extend({'sp','朝珠','曹尼玛'})
# l.insert(2,'小可爱')
# print(l)

#删除数据
##pop 根据下标删除
# l= ['cd', 'aa', '尼玛', '我']
# print(l.pop(1))
# print(l)
# print(l.pop())#默认弹出最后一个
# print(l)
##remove 根据内容删除
# l= ['cd', 'aa', '尼玛', '我']
# l.remove('cd')
# print(l)
#列表里有布尔值时使用pop下标删除
##clear清空列表
# l= ['cd', 'aa', '尼玛', '我']
# l.clear()
# print(l)

#对列表数据排序
# a =[1,2,56,32,65,99,100,231,321,4,44]
# a.sort()
# a.sort(reverse=False)
# a.sort(reverse=True)
# print(a)

#字典的常见操作
##遍历字典
# d = {"name":"小明","age":18,"sex":"男"}
# for key in d:
# 	print(d[key])
# for k,v in d.items():
#     print(k,v)
##修改value
# d = {"name":"小明","age":18,"sex":"男"}
# d['name'] = '小红'
# print(d)

##新增一对值
# d = {"name":"小明","age":18,"sex":"男"}
# d['addr'] = '果芽软件'
# print(d)

##新增多对值
# d = {"name":"小明"}
# d.update(爱好="发呆",学历='本科')# key不加引号
# print(d)

##删除一对值
# d = {"name":"小明","age":18,"sex":"男"}
# d.pop('age')
# print(d)


##清空整个字典
# d.clear()
# print(d)