#coding:utf-8

# #--------------------------------------------------
# import urllib

# url = "http://blog.csdn.net/omenglishuixiang1234"
# html = urllib.urlopen(url)
# content = html.read()
# print content
# #--------------------------------------------------

# #--------------------------------------------------
# import urllib2

# url = "http://blog.csdn.net/omenglishuixiang1234"
# req = urllib2.Request(url)
# req.add_header("User-Agent","Mozilla/5.0(X11;Ubuntu;Linux x86_64; rv:47.0)Gecko/20100101 Firefox/47.0")
# req.add_header("GET",url)
# req.add_header("Host","blog.csdn.net")
# req.add_header("Referer","http://blog.csdn.net/")

# html = urllib2.urlopen(req)
# print html.read()
# #--------------------------------------------------


import urllib2
import random

url = "http://blog.csdn.net/omenglishuixiang1234"
host = "blog.csdn.net"
referer = "http://blog.csdn.net/"

def get_page_content(url,host,referer):
    """
    @获取403禁止访问的页面
    """
    my_headers = [
        "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9B176 MicroMessenger/4.3.2",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:27.0) Gecko",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/50.0.2661.102 Chrome/50.0.2661.102 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.3.19 NetType/WIFI Language/zh_CN",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 UBrowser/5.6.13381.205 Safari/537.36",
        "Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; MI 2 Build/LRX22G) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.9.10.788 U3/0.8.0 Mobile Safari/534.30",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13E238 Safari/601.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13F69 Safari/601.1"
    ]
    random_header = random.choice(my_headers)
    req = urllib2.Request(url)
    req.add_header("User-Agent",random_header)
    req.add_header("Host",host)
    req.add_header("Referer",referer)
    req.add_header("GET",url)
    content = urllib2.urlopen(req).read()
    # print random_header
    return content
    
print get_page_content(url,host,referer)