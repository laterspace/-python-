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
    html=get_html(url).decode('gb2312','ignore')
    #parse=html
    soup=BeautifulSoup(html,'lxml')

    Contents=soup.find('div',attrs={'id':'content'})
    #a=Contents.text.strip().split('\xa0'*4)
    download_soup = BeautifulSoup(str(Contents), 'lxml')
    write_flag = True
    with open('123.txt','w') as file:

        for each in download_soup.div.text.replace('\xa0',''):
                    if each == 'h':
                        write_flag = False
                    if write_flag == True and each != ' ':
                        file.write(each)
                    if write_flag == True and each == '\r':
                        file.write('\n')
        file.write('\n\n')
        #f.write(str(a))


    #)
    #print(type(Contents))
    #去掉多余<br/>
    #reg=re.compile(r'(<br/>)*')
    #Contents=Contents.replace(reg,"\n")
    #print(download_soup)





def get_chapter():
    pass


def get_info():
    pass


def save():
    pass


if __name__ == '__main__':
    targetUrl ="https://www.bqkan8.com/1_1094/5433843.html"
    
    get_contents(targetUrl)
    print(" OVER")