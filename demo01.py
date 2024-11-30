import requests #引入requests模块用来处理请求
import os #引入os模块用来存储文件
headers={
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36'
}
#粘贴图片地址
src= "http://img.soogif.com/0Hy0iUj4T0hwELRUd5umISJJUkOOI7OM.gif";
#根据图片地址定义文件名
imgName = src.split('/')[-1]
#获取图片数据
imgRes = requests.get(src,headers=headers,timeout=3)
#将图片保存到本地
with open(imgName,'wb') as f:
    f.write(imgRes.content)
print("下载成功")