#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

#html为解析的页面获得html信息,为方便讲解，自己定义了一个html文件

html = """
<html>
<head>
<title>Jack_Cui</title>
</head>
<body>
<p class="title" name="blog"><b>My Blog</b></p>
<li><!--注释--></li>
<a href="http://blog.csdn.net/c406495762/article/details/58716886" class="sister" id="link1">Python3网络爬虫(一)：利用urllib进行简单的网页抓取</a><br/>
<a href="http://blog.csdn.net/c406495762/article/details/59095864" class="sister" id="link2">Python3网络爬虫(二)：利用urllib.urlopen发送数据</a><br/>
<a href="http://blog.csdn.net/c406495762/article/details/59488464" class="sister" id="link3">Python3网络爬虫(三)：urllib.error异常</a><br/>
</body>
</html>
"""

#创建Beautiful Soup对象
s = BeautifulSoup(html,'html.parser')


#print(soup.prettify())
'''
#tag
print(soup.title)
#<title>Jack_Cui</title>
print("-------------")
print(soup.head)
#<head> <title>Jack_Cui</title></head>
print("-------------")
print(soup.a)
#<a class="sister" href="http://blog.csdn.net/c406495762/article/details/58716886" id="link1">Python3网络爬虫(一)：利用urllib进行简单的网页抓取</a>
print("-------------")
print(soup.p)
#<p class="title" name="blog"><b>My Blog</b></p>
'''
""" 
print(type(soup.title))
#<class 'bs4.element.Tag'>

print(soup.name)
print(soup.title.name)
#[document]
#title """


""" print(s.a.attrs)
print(type(s))
print(type(s.title))


print(s.body.contents) """

#for child in s.body.children:
 #    print(child)

#print(s.find_all('a'))


""" import re
for i in s.find_all(re.compile("^b")):
     print(i.name)
print(s.find_all(['title','b']))
#[<title>Jack_Cui</title>, <b>My Blog</b>] """

'''
for tag in s.find_all(True):
     print(tag.name)
'''