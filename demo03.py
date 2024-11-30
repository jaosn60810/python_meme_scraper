import requests  # Import requests module for handling HTTP requests
import os  # Import os module for file handling
from lxml import etree  # Import lxml module for DOM parsing

# Define request headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36'
}

# Counter to limit total downloads
total_downloads = 0

# Create an 'img' folder if it doesn't exist
if not os.path.exists('img'):
    os.makedirs('img')

# Function to download images from a given page
def getImages(page):
    global total_downloads  # Access the global counter
    if total_downloads >= 10:  # Stop downloading if the limit is reached
        return

    # Webpage URL
    url = f"https://www.soogif.com/gif/83205-{page}-0-0.html"
    # Send a request to the webpage
    htmlText = requests.get(url, headers=headers, timeout=5).text
    # Parse the HTML to find all thumbnail links
    htmlDom = etree.HTML(htmlText)
    imgUrlList = htmlDom.xpath('//a[@class="image-item"]/@href')

    # Iterate through the thumbnail links
    for url in imgUrlList:
        if total_downloads >= 10:  # Stop downloading if the limit is reached
            return

        # Send a request to the detail page of each thumbnail
        detailHtmlText = requests.get("https://www.soogif.com/" + url, headers=headers, timeout=15).text
        # Parse the detail page to find the main image URL
        detailHtml = etree.HTML(detailHtmlText)
        src = detailHtml.xpath('//img[@id="display-image"]/@src')[0]

        # Extract the file name from the URL
        imgName = src.split("/")[-1]
        # Send a request to fetch the image
        imgRes = requests.get(src, headers=headers, timeout=3)

        # Save the image in the 'img' folder
        with open(os.path.join('img', imgName), "wb") as f:
            f.write(imgRes.content)

        print(f"Downloaded: {imgName}")
        total_downloads += 1  # Increment the counter

# Download images by iterating through pages
for i in range(1, 2):
    if total_downloads >= 10:  # Stop downloading if the limit is reached
        break
    getImages(i)  # Call the function to download images
