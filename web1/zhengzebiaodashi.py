#coding:utf8
#百度

import re

a='sdcsdvdsv23423fsdf4ddsv34r345'
b=re.findall('(\d+)',a)
print(b)
print("百度")