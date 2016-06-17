#coding:utf8
#水电费水电费
import sys
import urllib
import time

# print dir(urllib)

"""
1.传入网址，网址的类型一定是字符串
2.传入本地的网页保存路径和文件名
3.一个函数的调用，我们可以任意来定义这个函数的行为，
但是一定要保证这个函数有3个参数。
(1).到目前位置传递的数据块数量
(2).是每个数据块的大小，单位的byte字节
(3).远程文件的大小。(有时候返回-1)
"""

def urlCallbak(a,b,c):
    """
    @a: xxxx
    @b: xxxx
    @c: xxxx
    """
    down_progress = 100.0 * a * b / c
    if down_progress > 100 :
        down_progress = 100
    # time.sleep(0.5)
    print "%.2f%%" % down_progress,
    

print "请输入要处理的地址："
url = sys.stdin.readline()
while url:
    if url == "quit":
        break
    urllib.urlretrieve(url,'/mypc/www/python/web1/urlcatch2.html',urlCallbak)
    print "请输入要处理的地址："
    url = sys.stdin.readline()