#!/usr/bin/python
# -*- coding: UTF-8 -*-


import urllib.request
from bs4 import BeautifulSoup
import os
import re

def get_html(url):
    request=urllib.request.Request(url)
    header={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47',
    }
    request.add_header=header


    response=urllib.request.urlopen(request)
    html=response.read()
    return html

def get_contents(url):
    html=get_html(url).decode('gb2312','ignore')#解码

    soup=BeautifulSoup(html,'lxml')#解析成文档树
    
    
    Contents=soup.find_all('div',attrs={'id':'content'})#全搜索文档数

    Contents_soup = BeautifulSoup(str(Contents), 'lxml')#再次解析成文档数
    numbers = len(Contents_soup.dl.contents)
    print(numbers)

    return Contents_soup
    
    





def get_chapter():
    pass


def save():
    pass


if __name__ == '__main__':
    targetUrl ="https://www.bqkan8.com/1_1094/5433843.html"
    
    get_contents(targetUrl)
    print(" OVER")