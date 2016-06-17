#coding:utf8
#导入库文件
import re

#设置URL
testUrl = "http://www.iranshao.com"
total_page = 20;

fileTxt = open('iranshao.txt','r')
fileNeiRong = fileTxt.read()
fileTxt.close()

#抓取标题 如果知道了明确目标，就使用search。可大大提高效率，如果是全文搜索推荐使用findall
title = re.search('<title>(.*?)</title>',fileNeiRong,re.S).group(1)
print(title)

#爬取链接
links = re.findall('href="(.*?)"',fileNeiRong,re.S)
for each in links:
    print(each)
    
#抓取部分文字，先抓大再抓小，比如部分文字存在ul li中间 先获取ul 再获取li，如果页面多个ul，可以循环处理，也可直接[0]下标获取 