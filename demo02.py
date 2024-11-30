import requests
import os
from lxml import etree #引入lxml模块，用来处理DOM
headers={
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36'
}
#网页地址
url= "https://www.soogif.com/gif/83205-1-0-0.html"
#向网页发送请求
htmlText = requests.get(url,headers=headers,timeout=15).text;
#在网页文本中找到所有缩略图
htmlDom = etree.HTML(htmlText);
imgUrlList = htmlDom.xpath('//a[@class="image-item"]/@href') 
#遍历缩略图
for url in imgUrlList:
    #向缩略图的链接发送请求
    detailHtmlText = requests.get("https://www.soogif.com/"+url,headers=headers,timeout=15).text
    #找到所有图片地址，然后根据demo1的思路下载图片
    detailHtml = etree.HTML(detailHtmlText)
    src = detailHtml.xpath('//img[@id="display-image"]/@src')[0]
    imgRes = requests.get(src,headers=headers,timeout=3)
    imgName = src.split('/')[-1]
    with open(imgName,'wb') as f:
        f.write(imgRes.content)
    print(url+"下载成功")