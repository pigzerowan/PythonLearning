# /usr/bin/python
#-*- coding:utf-8 -*-
import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.*?\.jpg)" size'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    i = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg'%i)
        i+=1

html =  getHtml("https://tieba.baidu.com/p/5008707773")
print getImg(html)

