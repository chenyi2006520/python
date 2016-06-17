#coding:utf8

# #-------------------------------------------------------
# import sys
# import time
# import urllib

# url = "http://www.bisaiw.com/"
# info =  urllib.urlopen(url).info()
# print info
# print info.getparam('charset')

# #-------------------------------------------------------

import urllib
import chardet #字符集检测

url = "http://www.iplaypython.com/"
html = urllib.urlopen(url).read()
result = chardet.detect(html)
result2 = chardet.detect("我是中文")
print result
print result['encoding']
print result2
    

