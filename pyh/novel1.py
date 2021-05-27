#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib.request
import re


#流程
#获取主页面源代码
#获取章节超链接
#获取小说内容
#下载小说


#定义函数
def getNovelContent():

    #获取主页面源码 byte
    url='https://www.bqkan8.com/74_74297/'
    req =urllib.request.Request(url)
    header={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47',
    
    #'Accept': '*/*',
    #'Accept-Language': 'en-US,en;q=0.8',
    #'Cache-Control': 'max-age=0',
    #'Connection': 'keep-alive'
    
    }
    req.add_header=header
    html=urllib.request.urlopen(req).read()
    #print(html)
    
    #状态码 200
    #print(html.status)

    #解码（没解码之前，一堆看不懂符号）
    html=html.decode('gbk')
    #print(html)

    regx=r'<dd><a href="(.*?)" one-link-mark="yes">(.*?)</a></dd>'
    urls=re.findall(regx, html)
    print(urls)



getNovelContent()