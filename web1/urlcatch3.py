#coding:utf8

# #-------------------------------------------------------
# import sys
# import time
# import urllib

# url = "http://www.bisaiw.com/"
# info =  urllib.urlopen(url).info()
# print info
# print info.getparam('charset')

#-------------------------------------------------------

# import urllib
# import chardet #字符集检测

# url = "http://www.iplaypython.com/"
# html = urllib.urlopen(url).read()
# result = chardet.detect(html)
# result2 = chardet.detect("我是中文")
# print result
# print result['encoding']
# print result2
#-------------------------------------------------------

import urllib
import chardet #字符集检测

def automatic_detec(url):
    """获取站点的字符集"""
    content = urllib.urlopen(url).read()
    result = chardet.detect(content)
    encoding = result["encoding"]
    return encoding
    
urls = [
    "http://www.qq.com",
    "http://wwww.bisai.cn",
    "http://www.163.com",
    "http://www.12306.cn",
    "http://www.z.com",
    "http://www.jd.com"
]

for url in urls:
    print url , automatic_detec(url)