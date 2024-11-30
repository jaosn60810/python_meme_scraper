import requests #引入requests模块用来处理请求
import os #引入os模块用来存储文件
from lxml import etree #引入lxml模块，用来处理DOM
#定义请求头
headers={
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36'
}
def getImages(page):
    #网页地址
    url= f"https://www.soogif.com/gif/83205-{page}-0-0.html"
    #想网页发送请求
    htmlText = requests.get(url,headers=headers,timeout=5).text;
    #在网页文本中找到所有缩略图
    htmlDom = etree.HTML(htmlText);
    imgUrlList = htmlDom.xpath('//a[@class="image-item"]/@href');
    #遍历缩略图
    for url in imgUrlList:
        #想缩略图的链接发送请求
        detailHtmlText = requests.get("https://www.soogif.com/"+url,headers=headers,timeout=15).text
        #找到所有图片地址
        detailHtml = etree.HTML(detailHtmlText)
        src=detailHtml.xpath('//img[@id="display-image"]/@src')[0]
        #有了地址，以下内容与demo1相同
        #根据图片地址定义文件名
        imgName=src.split("/")[-1];
        #获取图片数据
        imgRes = requests.get(src,headers=headers,timeout=3);
        #将图片保存到本地
        with open(imgName,"wb") as f:
            f.write(imgRes.content);
        print("下载成功");

#通过页码获取图片
for i in range(1,2001):
    getImages(i); #调用函数，爬取图片