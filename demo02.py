import requests
import os
from lxml import etree  # Import lxml module for handling DOM parsing

# Define headers to simulate a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36'
}

# Webpage URL
url = "https://www.soogif.com/gif/83205-1-0-0.html"

# Send a request to the webpage
htmlText = requests.get(url, headers=headers, timeout=15).text

# Parse the HTML text to find all thumbnail links
htmlDom = etree.HTML(htmlText)
imgUrlList = htmlDom.xpath('//a[@class="image-item"]/@href')

# Create a folder named 'img' if it doesn't exist
if not os.path.exists('img'):
    os.makedirs('img')

# Initialize a counter
download_count = 0

# Iterate through the thumbnail links
for url in imgUrlList:
    if download_count >= 10:  # Stop after downloading 10 images
        break

    # Send a request to the detail page of each thumbnail
    detailHtmlText = requests.get("https://www.soogif.com/" + url, headers=headers, timeout=15).text

    # Parse the detail page HTML to find the main image URL
    detailHtml = etree.HTML(detailHtmlText)
    src = detailHtml.xpath('//img[@id="display-image"]/@src')[0]

    # Download the image using the extracted URL
    imgRes = requests.get(src, headers=headers, timeout=3)
    imgName = src.split('/')[-1]

    # Save the image in the 'img' folder
    with open(os.path.join('img', imgName), 'wb') as f:
        f.write(imgRes.content)

    print(url + " downloaded successfully")
    download_count += 1  # Increment the counter
