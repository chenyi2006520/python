#coding:utf8
#url获取数据

import urllib
import urllib.request

data={}
data["word"] = "java"
url_values=urllib.parse.urlencode(data)
url="https://wap.koudaitong.com/v2/showcase/feature?alias=ijvr26ac&spm=m1464743979558252122565650.autoreply"
full_url=url+url_values
 
data=urllib.request.urlopen(full_url).read()
data=data.decode("UTF-8")
print(data)