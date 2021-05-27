import urllib.request
import os


response = urllib.request.urlopen("http://placekitten.com/200/300")
html = response.read()
#f=open("1.jpg","wb")
with open("2.jpg","wb") as f:
    f.write(html)
