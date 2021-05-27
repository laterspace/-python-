#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
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
 
print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print( "Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)
 
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
 
"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)

emp1.age = 7  # 添加一个 'age' 属性
emp1.age = 8  # 修改 'age' 属性
print(emp1.age)
del emp1.age  # 删除 'age' 属性

print(hasattr(emp1, 'age'))    # 如果存在 'age' 属性返回 True。
#print(getattr(emp1, 'age')  )  # 返回 'age' 属性的值
print(setattr(emp1, 'age', 8)) # 添加属性 'age' 值为 8
print(delattr(emp1, 'age'))    # 删除属性 'age' """




""" class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg

try:
    raise Networkerror("Bad hostname")
except Networkerror as e:
    print (e.args) """



""" # 定义函数
def mye( level ):
    if level < 1:
        raise Exception ("Invalid level!") 
        # 触发异常后，后面的代码就不会再执行
try:
    mye(0)            # 触发异常
except Exception as err:
    print (1,err)
else:
    print (2) """



""" # 定义函数
def temp_convert(var):
    try:
        return int(var)
    except ValueError, Argument:
        print "参数没有包含数字\n", Argument

# 调用函数
temp_convert("xyz") """

""" x="a"
y="b"
# 换行输出
print x
print y

print ('---------')
# 不换行输出
print x,
print y,

# 不换行输出
print x,y """

""" if expression : 
   suite 
elif expression :  
   suite  
else :  
   suite """