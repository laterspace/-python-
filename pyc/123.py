#!/usr/bin/python
# -*- coding: UTF-8 -*-



# 导入Python SQLITE数据库模块
import sqlite3

# 创建/打开数据库 
cx = sqlite3.connect("E:/test1.db")
# 游标对象
cu=cx.cursor()

# 如果数据表已经存在使用 execute() 方法删除表。
cu.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql="""CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
cu.execute(sql) # 建表

# 插入数据
""" for t in[(0,10,'abc','Yu'),(1,20,'cba','Xu')]:
    cx.execute("insert into catalog values (?,?,?,?)", t) """
insertsql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""



try:
   # 执行sql语句
   cu.execute(insertsql)
   # 提交到数据库执行
   cx.commit() # 提交生效
except:
   # Rollback in case there is any error
   cx.rollback()
         

#cx.commit() # 提交生效







sql3 = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > %s" % (1000)
try:
   # 执行SQL语句
   cu.execute(sql3)
   # 获取所有记录列表
   results = cu.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      # 打印结果
      print  ("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
             (fname, lname, age, sex, income ))
except:
   print ("Error: unable to fecth data")


""" cu.execute("select * from catalog") 
data = cu.fetchall()

print ("Database version : " ,data)

#修改
cu.execute("update catalog set name='Boy' where id = 0")
cx.commit()


for item in cu.fetchall():
     for element in item:
         print (element,)
      """


""" data2 = cu.fetchall()

print ("修改Database version : " ,data2) """

cx.close()  # close db


""" # 导入Python SQLITE数据库模块
import sqlite3

# 创建/打开数据库 
cx = sqlite3.connect("E:/test.db")

# 游标对象
cu=cx.cursor()


#sql="create table catalog (id integer primary key,pid integer,name varchar(10) UNIQUE,nickname text NULL)"
#cu.execute(sql) # 建表

# 插入数据
#for t in[(0,10,'abc','Yu'),(1,20,'cba','Xu')]:
 #   cx.execute("insert into catalog values (?,?,?,?)", t)


#cx.commit() # 提交生效



cu.execute("select * from catalog") 



data = cu.fetchall()

print ("Database version : " ,data)

#修改
cu.execute("update catalog set name='Boy' where id = 0")
cx.commit()


for item in cu.fetchall():
     for element in item:
         print (element,)
     


"""
# data2 = cu.fetchall()

#print ("修改Database version : " ,data2) 

#cx.close()  # close db """

""" import re
pattern= re.compile(r'\d*',re.M|re.I)
line="fa122sdf445adfsf565as"
m=pattern.findall(line,2)
m1=pattern.match(line,2,10)
print (m)
print(m1.span())


re.sub(pattern, "1", line, count=0, flags=0) """

""" import re
re.match(pattern, string, flags=0)   # 有局限性，不适用全部，一招货
re.search(pattern, string, flags=0)     # 无法限制次数
re.sub(pattern, repl, string, count=0, flags=0)     # 无法定点开始
re.compile(pattern[, flags])
findall(string[, pos[, endpos]])    # 可以
re.finditer(pattern, string, flags=0) """


""" import re
print ("1 ",re.split('\W+', 'runoob, runoob, runoob.'))

print ("2 ",re.split('(\W+)', ' runoob, runoob, runoob.') )

print ("3 ",re.split('\W+', ' runoob, runoob, runoob.', 1) )

 
print ("4 ",re.split('a*', 'hello world'))   # 对于一个找不到匹配的字符串而言，split 不会对其作出分割
 """



""" import re
 
it = re.finditer(r"\d+","12a32bc43jf3") 
for match in it: 
    print (match.group() ) """


""" 
import re
 
pattern = re.compile(r'\d+')   # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)
 
print(result1)
print(result2) """






""" import re
pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
m = pattern.match('Hello World Wide Web')
print (m)                               # 匹配成功，返回一个 Match 对象

print (m.group(0) )                           # 返回匹配成功的整个子串

print (m.span(0) )                            # 返回匹配成功的整个子串的索引

print (m.group(1))                            # 返回第一个分组匹配成功的子串

print (m.span(1))                             # 返回第一个分组匹配成功的子串的索引

print (m.group(2))                            # 返回第二个分组匹配成功的子串

print (m.span(2))                             # 返回第二个分组匹配成功的子串

print (m.groups())                            # 等价于 (m.group(1), m.group(2), ...)

print (m.group(3) )     """                       # 不存在第三个分组





""" import re
pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
print (m)

m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
print (m)

m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
print (m)                                       # 返回一个 Match 对象

print(m.group(0) )  # 可省略 0

print(m.start(0))   # 可省略 0
print(m.end(0) )    # 可省略 0
print(m.span(0) )   # 可省略 0 """




""" import re
 
# 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)
 
s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s)) """


 
""" import re
 
phone = "2004-959-559 # 这是一个国外电话号码"
 
# 删除字符串中的 Python注释 
num = re.sub(r'#.*$', "", phone)
print ("电话号码是: ", num)
 
# 删除非数字(-)的字符串 
num = re.sub(r'\D', "", phone)
print ("电话号码是 : ", num) """



""" import re
 
line = "Cats are smarter than dogs";
 
matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print ("match --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")
 
matchObj = re.search( r'dogs', line, re.M|re.I)
if matchObj:
   print ("search --> searchObj.group() : ", matchObj.group())
else:
   print ("No match!!") """


""" import re
 
line = "Cats are smarter than dogs";
 
searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if searchObj:
   print ("searchObj.group() : ", searchObj.group())
   print ("searchObj.group(1) : ", searchObj.group(1))
   print ("searchObj.group(2) : ", searchObj.group(2))
else:
   print ("Nothing found!!") """


 
""" import re
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配
 """


""" import re
 
line = "Cats are smarter than dogs"
 
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!") """


""" import re
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配
 """


""" 类的方法的参数self，就只在方法中出现，默默的默默付出
class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量
 
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print (self.__secretCount)
 
counter = JustCounter()
counter.count()
counter.count()
print (counter.publicCount)
print (counter._JustCounter__secretCount)  # 报错，实例不能访问私有变量
 """
 
""" class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b
 
   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)
 
v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)
print ("没有str：" , type(v1))
print ("有str：", type(str(v1))) """




""" class Parent:        # 定义父类
   parentAttr = 100
   def __init__(self):
      print ("调用父类构造函数")
 
   def parentMethod(self):
      print ('调用父类方法')
 
   def setAttr(self, attr):
      Parent.parentAttr = attr
 
   def getAttr(self):
      print ("父类属性 :", Parent.parentAttr)
 
class Child(Parent): # 定义子类
   def __init__(self):
      print ("调用子类构造方法")
 
   def childMethod(self):
      print ('调用子类方法')
 

class Chil: # 定义子类
        chilz=1

c = Child()          # 实例化子类
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类方法
c.setAttr(200)       # 再次调用父类的方法 - 设置属性值
c.getAttr()          # 再次调用父类的方法 - 获取属性值


print(issubclass(Chil,Parent))

print(isinstance(c,Parent)) """



 
""" class Employee:
   '所有员工的基类'
   empCount = 0
 
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)
 
   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)



class Test:
    def prt(self):
        print(self)
        print(self.__class__)
 
t = Test()
t.prt()

print("---------------")

class Test:
    def prt(runoob):
        print(runoob)
        print(runoob.__class__)
 
t1 = Test()
t1.prt() """



""" # 定义函数
def temp_convert(var):
    try:
        return int(var)
    except ValueError, Argument:
        print ("参数没有包含数字\n", Argument)

# 调用函数
temp_convert("xyz"); """


""" try:
    fh = open("testfile", "w")
    try:
        fh.write("这是一个测试文件，用于测试异常!!")
    finally:
        print ("关闭文件")
        fh.close()
except IOError:
    print ("Error: 没有找到文件或读取文件失败") """


""" try:
    fh = open("testfile", "w")  
    fh.write("这是一个测试文件，用于测试异常!!")
except PermissionError:
   print ("这是一个测试文件，用于测试异常!!")
finally:
    print ("Error: 没有找到文件或读取文件失败") """


""" # 定义函数
def temp_convert(var):
    try:
        return int(var)
    except ValueError, Argument:
        print ("参数没有包含数字\n", Argument)

# 调用函数
temp_convert("xyz") """

""" try:
    fh = open("testfile", "w")
    try:
        fh.write("这是一个测试文件，用于测试异常!!")
    finally:
        print ("关闭文件")
        fh.close()
except IOError:
    print ("Error: 没有找到文件或读取文件失败") """


""" try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
finally:
    print ("Error: 没有找到文件或读取文件失败")
 """

""" try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
finally:
    print ("Error: 没有找到文件或读取文件失败")
 """

##异常##
""" try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print ("Error: 没有找到文件或读取文件失败")
else:
    print ("内容写入文件成功")
    fh.close() """





""" 
import os
 
# 给出当前的目录
print (os.getcwd())
"""  """ """

""" fo = open("foo.txt", "w")
a1=dir(fo)

print(a1) """






""" # 打开一个文件
fo = open("foo.txt", "w")
print ("文件名: ", fo.name)
print ("是否已关闭 : ", fo.closed)
print ("访问模式 : ", fo.mode)
print(type(fo))
#print ("末尾是否强制加空格 : ", fo.softspace)



# 关闭打开的文件
fo.close( """
 
""" str = input("请输入：")
print ("你输入的内容是: ", str) """

""" from package0.runoob1 import runoob1
from package0.runoob2 import runoob2

runoob1()
runoob2() """






""" Money = 2000
def AddMoney():
   # 想改正代码就取消以下注释:
   global Money
   Money = Money + 1
 
print (Money)
AddMoney()
print (Money) """

""" m=[5,9]  
m.append(7)
#m+=[6] 
print(m) """



""" total = 0 # 这是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
   #返回2个参数的和."
   total = arg1 + arg2 # total在这里是局部变量.
   print ("函数内是局部变量 : ", total)
   return total
 
#调用sum函数
sum( 10, 20 )
print ("函数外是全局变量 : ", total) """

""" total = 1

def sum( arg1,arg2):
    total = arg1+ arg2
    print("函数内局部变量:",total)
    return total
sum(20,10)
print("函数外全局变量：",total) """


""" ##return 语句##
def sum(arg1,arg2):
    total =arg1+arg2
    print("函数内:",total)
    return total

total = sum(10,10) """



""" ##匿名函数##
# 可写函数说明
sum = lambda arg1, arg2: arg1+arg2
#sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("相加后的值：", sum(10,20))
print("相加后的值：", sum(50,20)) """

""" # 可写函数说明
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return
 
# 调用printinfo 函数
printinfo( 10 )
printinfo( 70, 60, 50 ) """




"""  
#可写函数说明
def printinfo( name, age ):
   "打印任何传入的字符串"
   print ("Name: ", name)
   print ("Age ", age)
   return
 
#调用printinfo函数
printinfo( age=50, name="miki" ) """

 
""" a = "hello"
b = "Python"
 
print ("a + b 输出结果：", a + b )
print ("a * 2 输出结果：", a * 2) 
print ("a[1] 输出结果：", a[1] )
print ("a[1:4] 输出结果：", a[1:4]) 
 
if( "H" in a) :
    print ("H 在变量 a 中" )
else :
    print ("H 不在变量 a 中" )
 
if( "M" not in a) :
    print ("M 不在变量 a 中") 
else :
    print ("M 在变量 a 中")
 
print (r'\n')
print (R'\n')
 """


"""  
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"

for i in tup1 :
   dict1 = dict.fromkeys(tup1[i], tup2[i])

print (dict1) """


""" 
for i in tup3:
   print(i)

# 创建一个新的元组
tup4 = tup1 + tup2
print (tup4) """

""" dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
 
#del dict['Age']
dict['School'] = "RUNOOB" # 添加
dict.clear()
 
#print ("dict['Age']: ", dict['Age'])
#print ("dict['School']: ", dict['School'])

for i in dict:
   print (dict[i]) """


""" import time
 
localtime = time.asctime(time.localtime(time.time()))
print ("本地时间为 :", localtime) """

""" import calendar
 
cal = calendar.month(2016, 1)
print ("以下输出2016年1月份的日历:")
print (cal) """

""" import datetime
i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second) """

""" def ChangeInt( a ):
    a = 10
 
b = 2
ChangeInt(b)
print (b) """

print("运行成功")