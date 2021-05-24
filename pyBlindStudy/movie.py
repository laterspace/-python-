#!/usr/bin/python
# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup

#for i in range(10):
res = requests.get("https://movie.douban.com/chart")  # 发送get请求
html = res.text#将获取到的网页信息以字符串的形式存入变量html中
soup = BeautifulSoup(html, "html.parser")#用BeautifulSoup将网页信息html解析成人们看得懂的语言,解释器是html.parser
items = soup.find_all("div", class_="item")#提取所有的电影名，序号，链接，推荐语，评分的数据

for item in items:
        dym_0 = item.find("span", class_="title")  # 标签包含电影名
        dym_1 = dym_0.text  # 去掉标签，提取电影名
        xh_0 = item.find("em", class_="")# 标签包含序号
        xh_1 = xh_0.text
        pf_0 = item.find("span", class_="rating_num")# 标签包含评分
        pf_1 = pf_0.text
        print(xh_1,dym_1, pf_1)#打印序号，电影名，评分

        tjy_0 = item.find("span",class_ = "inq")# 标签包含推荐语
        if tjy_0:#打印非空的推荐语，否则报错
            print(tjy_0.text)

        lj_0 = item.find("a")
        print(lj_0['href'] + "\n")#提取lj_0["a"]属性的值。即 将 <a href="网址">中，属性a的值href提取出来并打印。
