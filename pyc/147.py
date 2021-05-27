#!/usr/bin/python
# -*- coding: utf-8 -*-

def f(): pass

print(type(f()))


""" a=[1,2,3,4,5]


print(a[-1:]) """




""" 
# 2
i =int(input("净利润："))
arr=[1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r=0

for idx in range(0,6):
   if i>arr[idx]:
      r+=(i-arr[idx])*rat[idx]
      print((i-arr[idx])*rat[idx])
      i=arr[idx]

print(r)
 """





""" 
# 1
d=[]
for i in range(1,5):
   for j in range(1,5):
      for k in range(1,5):
         if(i!=j) and (j!=k) and (k!=i):
            d.append([i,j,k])
            #print(i,j,k)
print ("总数量：", len(d))
print (d) """
