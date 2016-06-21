#coding:utf-8

import re
import urllib


def get_urlContent(url):
    """
    @url 传值进来需要处理的参数
    该函数用来获取页面的类容
    """
    html = urllib.urlopen(url)
    content = html.read()
    html.close()
    return content

def get_images(info):
    """
    获取贴吧发帖图片
    <img class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=d669afad34d12f2ece05ae687fc3d5ff/45889e510fb30f24ef222279ca95d143ad4b0315.jpg" pic_ext="jpeg" changedsize="true" height="746" width="560">
    """
    regex = r'class="BDE_Image" src="(.+?\.jpg)"'
    pat = re.compile(regex)
    image_code = re.findall(pat, info)
    
    i = 1
    for image_url in image_code:
        print image_url
        urllib.urlretrieve(image_url, '%s,jpg' % i)
        i += 1
    
    
page_content = get_urlContent("http://tieba.baidu.com/p/2772656630")
print get_images(page_content)