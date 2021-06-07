#-*- coding:utf-8 -*-
import sys
reload(sys)
#sys.setdefaultencoding("gbk")

from re import findall
import requests
import re
from urllib import urlopen

from bs4 import BeautifulSoup


def modifyip(tfile,sstr,rstr):

    try:

        lines=open(tfile,'r').readlines()

        flen=len(lines)-1

        for i in range(flen):

            if sstr in lines[i]:

                lines[i]=lines[i].replace(sstr,rstr)

        open(tfile,'w').writelines(lines)

        

    except Exception as e:

        print (e)



url = 'http://mp.weixin.qq.com/s/d2dOqNN1ITxN3pSr0VP3uQ'
content = urlopen(url).read()
f1 = open('p.htm','wb')
f1.write(content)
f1.close()
#f2=file('pic.txt','wb')

import os
import math       
altxt = open('p.htm').read()
pattern = ''
#out = re.sub(pattern,' ', altxt)
listpp=re.split(r')
f1 = open('p1.htm','a+')
for i in listpp:
   print listpp.index(i)
   if (listpp.index(i)+2)%2  == 0:
     print i
   
     f1.write(i)
     
f1.close()

altxt = open('p1.htm').read()
pattern = ''
#out = re.sub(pattern,' ', altxt)
listpp=re.split(r'<|>',altxt)
f1 = file('p2.htm','a+')
for i in listpp:
   print listpp.index(i)
   if (listpp.index(i)+2)%2  == 0:
     print i

     f1.write(i+chr(10))
     
f1.close()

#f4=open('p2.htm','r+')
#altxt = f4.read()
#altxt =  altxt.replace('head','')
#print altxt
#f4.write(altxt)
#f4.close()

for i in range(10):

 with open('p2.htm','r+') as f:
    t = f.read()
    t = t.replace('/head', '')
    t = t.replace('head', '')
    t = t.replace('/body', '')
    t = t.replace('body', '')
    t = t.replace('/html', '')
    t = t.replace('html', '')
    #t = t.replace(' ', '')

   #读写偏移位置移到最开始处
    f.seek(0, 0)    
    f.write(t)



def delblankline(infile,outfile):
    infopen = open(infile,'r')
    outfopen = open(outfile,'w')
    lines = infopen.readlines()
    for line in lines:
        if line.split():
            outfopen.writelines(line)
        else:
            outfopen.writelines("")
    infopen.close()
    outfopen.close()
    
delblankline("p2.htm","p3.txt")

pattern = ' data-src="(.+?)"'
pattern1 = ' data-src="(.+?)"'

content = open('p.htm').read()
result = findall(pattern, content)
#print result


#content = open('p.htm').read()
#pattern1 = ' data-src="(.+?)"'
#result1 = findall(pattern1, content)
#for index, item in enumerate(result):

for index, item in enumerate(result):
    
    
    if not str(item).find('png')==-1:
         data = urlopen(str(item)).read()
         #f2.write(str(item)+'"  />'+'python <wbr>把微信公众号的文章下载下来，并正常显示图片,抽取文本')
         modifyip('p.htm',' data-src="'+str(item),' src="'+str(index)+'.png" ')
        
         f = file(str(index)+'.png',"wb")
         f.write(data)
         f.close()

    if not str(item).find('jpeg')==-1:
         data = urlopen(str(item)).read()
         
         modifyip('p.htm',' data-src="'+str(item),' src="'+str(index)+'.jpg" ')
         
         f = file(str(index)+'.jpg',"wb")
         f.write(data)
         f.close()

    if not str(item).find('gif')==-1:
         data = urlopen(str(item)).read()
         
         modifyip('p.htm',' data-src="'+str(item),' src="'+str(index)+'.gif" ')
         
         f = file(str(index)+'.gif',"wb")
         f.write(data)
         f.close()  

 



os.remove('p1.htm')
os.remove('p2.htm')

html="""
下面的程序，可以下载图片，但是不可以放入链接，其实也可以放入链接，但是无法打开，是因为什么原因无法打开呢？
 是否可以将img的内容一项一项地删除，而找到问题的原因呢？试一下。
原因找到了，当把data-src="6.jpg"改为src="6.jpg"之后， 就可以正常显示图片了。
现在的问题是，怎么修改程序？

下面这一行主要是替换，将p.htm中data-src="6.jpg"改为src="6.jpg"，str(item) 代表是图片的网址，

它前面是' data-src="', 那么加上图片的网址str(item)，就是' data-src="'+str(item)，
更改为' src="'+' src="'+str(index)+'.jpg" '即可，
其中' src="'+str(index)+'.jpg" ' 是 本地的新图片。

仔细看一下， 其实 也可以用于上面一部分的处理。
修改一下，执行试试。


         #modifyip('p.htm',' data-src="'+str(item),' src="'+str(index)+'.jpg" ')  


以下三行主要是写图片，这段程序没问题。
         f = file(str(index)+'.jpg',"wb")
         f.write(data)
         f.close()

"""