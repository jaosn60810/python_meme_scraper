import requests 
import os 
from lxml import etree 
headers={ 
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36'
}
def getImages(page): 
    url= f"https://www.soogif.com/gif/83205-{page}-0-0.html" 
    htmlText = requests.get(url,headers=headers,timeout=15).text;
    htmlDom = etree.HTML(htmlText);
    imgUrlList = htmlDom.xpath('//a[@class="image-item"]/@href') 
    for url in imgUrlList:
        detailHtmlText = requests.get("https://www.soogif.com/"+url,headers=headers,timeout=15).text
        detailHtml = etree.HTML(detailHtmlText)
        src = detailHtml.xpath('//img[@id="display-image"]/@src')[0]
        imgRes = requests.get(src,headers=headers,timeout=3)
        imgName = src.split('/')[-1]
        with open(imgName,'wb') as f:
            f.write(imgRes.content)
        print(url+"下载成功")

for i in range(1,5):
    getImages(i);