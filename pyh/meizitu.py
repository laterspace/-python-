#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import urllib.request
from bs4 import BeautifulSoup




"""def Download(url,picAlt,name):
    path = 'D:\\pythonD爬虫妹子图\\'+picAlt+'\\'
    if not os.path.exists(path):
        os.makedirs(path)
    urllib.request.urlretrieve( url, '{0}{1}.jpg'.format(path, name)) 
 
header = {
    "User-Agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive'
    }

def run(targetUrl, beginNUM ,endNUM):
    req = urllib.request.Request(url=targetUrl,headers=header)
    response = urllib.request.urlopen(req)
    html = response.read().decode('gb2312','ignore')
    soup = BeautifulSoup(html, 'html.parser')
    Divs = soup.find_all('div',attrs={'id':'big-pic' })
    nowpage = soup.find('span',attrs={'class':'nowpage'}).get_text()
    totalpage= soup.find('span',attrs={'class':'totalpage'}).get_text()
    if beginNUM ==endNUM :
        return
    for div in Divs:
        beginNUM = beginNUM+1
 
        if div.find("a") is None :
            print("没有下一张了")
            return
        elif div.find("a")['href'] is None or div.find("a")['href']=="":
            print("没有下一张了None")
            return
        print("下载信息：总进度：",beginNUM,"/",endNUM," ，正在下载套图：(",nowpage,"/",totalpage,")")
 
        if int(nowpage)<int(totalpage):
            nextPageLink ="http://www.mmonly.cc/mmtp/qcmn/" +(div.find('a')['href'])
        elif int(nowpage)==int(totalpage):
            nextPageLink = (div.find('a')['href'])
 
        picLink = (div.find('a').find('img')['src'])
        picAlt = (div.find('a').find('img'))['alt']
        print('下载的图片链接:',picLink)
        print('套图名：[ ', picAlt , ' ] ')
        print('开始下载...........')
        Download(picLink,picAlt, nowpage)
        print("下载成功！")
        print('下一页链接:',nextPageLink)
        run(nextPageLink,beginNUM ,endNUM)
        return
 

if __name__ == '__main__':
    targetUrl ="http://www.mmonly.cc/mmtp/qcmn/237269.html"
    run(targetUrl,beginNUM=0,endNUM=70)
    print(" OVER")
    
 """




















def saveImg(url,picAlt,name):
    path="D:\\爬虫妹子图2\\"+picAlt+"\\"
    if not os.path.exists(path):
        os.makedirs(path)
    urllib.request.urlretrieve(url,'{0}{1}.jpeg'.format(path, name))

header={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47',
    
    #'Accept': '*/*',
    #'Accept-Language': 'en-US,en;q=0.8',
    #'Cache-Control': 'max-age=0',
    #'Connection': 'keep-alive'
    
}



def Download(targetUrl,beginNum,endNum):

    #请求对象，参数两者写法
    #- a（b=1，a=2，c=3）写成a（b=1，c=3）是对的，也就是带上对应参数名，不带上，直接写上变量会出错
    req=urllib.request.Request(targetUrl)
    req.add_header=header



    response=urllib.request.urlopen(req)
    html=response.read().decode('gb2312','ignore')
    #print(html)
    soup=BeautifulSoup(html,'html.parser')  #网页解析（BeatifulSoup解析库），生成Beatifulsoup对象
    Divs=soup.find_all('div',attrs={'id':'big-pic'})    #搜索为标签div,属性为'id':'big-pic'，并生成的列表
    nowpage=soup.find('span',attrs={'class':'nowpage'}).get_text()
    totalpage=soup.find('span',attrs={'class':'totalpage'}).get_text()
    if beginNum==endNum:
        return
    for div in Divs:
        beginNum+=1

        if div.find('a') is None:
            print('没有下一张')
            return
        elif div.find('a')['href'] is None or div.find('a')['href']=="":
            print('没有下一张none')
            return
        print("下载信息：总进度：",beginNum,"/",endNum," ，正在下载套图：(",nowpage,"/",totalpage,")")

        if int(nowpage)<int(totalpage):
            nextPageLink="http://www.mmonly.cc/mmtp/qcmn/" +(div.find('a')['href'])
        elif int(nowpage)==int(totalpage):
            nextPageLink = (div.find('a')['href'])

        picLink = (div.find('a').find('img')['src'])    #图片链接
        picAlt = (div.find('a').find('img'))['alt'] #套图名
        print('下载的图片链接:',picLink)
        print('套图名：[ ', picAlt , ' ] ')
        print('开始下载...........')
        saveImg(picLink,picAlt, nowpage)
        print("下载成功！")
        print('下一页链接:',nextPageLink)
        Download(nextPageLink,beginNum ,endNum)
        return

if __name__ == '__main__':
    targetUrl ="http://www.mmonly.cc/mmtp/qcmn/237269.html"
    Download(targetUrl,beginNum=0,endNum=70)
    print(" OVER")
    

