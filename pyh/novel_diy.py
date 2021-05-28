#!/usr/bin/python
# -*- coding: UTF-8 -*-


import urllib.request
from bs4 import BeautifulSoup
import os
from tqdm import tqdm
import re



def get_html(url,charset):
    #发出请求
    request=urllib.request.Request(url)
    header={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47',
    }
    request.add_header=header
    response=urllib.request.urlopen(request)
    html=response.read().decode(charset)#解码
    return html

def get_contents(url,charset):
    #获取内容
    html=get_html(url,charset)

    soup=BeautifulSoup(html,'lxml')#解析成文档树
    
    
    Contents=soup.find_all('div',attrs={'id':'content'})#全搜索文档数

    Contents_soup = BeautifulSoup(str(Contents), 'lxml')#再次解析成文档数
    
    Content_text=Contents_soup.text.replace('\xa0','')#替换多余的符号
    #print (Content_text)
    return Content_text
    
    





def get_chapter(url,charset):
    #获取章节
    html=get_html(url,charset)#.decode('utf-8')
    chapters_Soup=BeautifulSoup(html,'lxml')
    chapter=chapters_Soup.find('div' ,id="list")
    chapters=chapter.find_all('a')
    #chapterDict={}
    """ for chapter_i in chapters:
        link=chapter_i['href']
        #chapterDict={}
        chapterDict[chapter_i.string]=homeUrl+link


        
        #print(chapter_i.string)
    #print(chapterDict) """
    return chapters

def save(filename,content):
    path = 'D:\\UserDataX\\Desktop\\下载小说\\'
    if not os.path.exists(path):
        os.makedirs(path)
    os.chdir(path)

    with open(str(filename)+'.txt','w',encoding='utf-8') as f:
        f.write(filename+'\n\n')
        f.write(content+'\n\n')
        


if __name__ == '__main__':
    #targetUrl ="https://www.bqkan8.com/1_1094/5433843.html"
    ChaptersUrl='https://www.vbiquge.com/15_15338/'
    homeUrl="https://www.vbiquge.com"
    chapters=get_chapter(ChaptersUrl,'utf-8')
    for i in tqdm(chapters):
        link=i['href']#
        chapterName=i.string#标签字符串
        chapterLink=homeUrl+link
        
        charpterText=get_contents(chapterLink,'utf-8')

        save(chapterName,charpterText)
    #get_contents(targetUrl)


    print(" OVER")