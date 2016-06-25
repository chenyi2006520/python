#coding:utf-8

import urllib
from bs4 import BeautifulSoup

def get_pageContent(url):
    """获取页面内容"""
    html = urllib.urlopen(url)
    content = html.read()
    html.close()
    return content
    
    
def get_imageContent(info):
    """抓取贴吧页面的图片"""
    soup = BeautifulSoup(info,"lxml")
    all_image = soup.find_all('img',class_="BDE_Image")
    
    x = 1
    for img in all_image:
        print img['src']
        image_name = "%s.jpg" % x
        #urllib.urlretrieve(img['src'],image_name)
        x += 1
        
        
page_content = get_pageContent("http://tieba.baidu.com/p/2772656630")
get_imageContent(page_content)
# print page_content