#coding:utf8
#url获取数据

import urllib

# print dir(urllib)
# print help(urllib.urlopen)

url = "http://www.iplaypython.com/"
html = urllib.urlopen(url)
# print html.read().decode('gbk').encode('utf-8') #乱码转换
print html.info() #获取头部信息
# print html.getcode() #获取状态

#print html.geturl()#获取传值的url
#下载网页到本地
# urllib.urlretrieve(url,"/mypc/www/python/web1/abc.html")

urllib.close()