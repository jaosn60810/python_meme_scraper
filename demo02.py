import requests
import os
from lxml import etree  # Import the lxml module to process the DOM

# Set headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36'
}

# URL of the webpage containing GIFs
webpage_url = "https://tenor.com/zh-TW/search/meme-gifs"

# Create a folder named 'img' if it doesn't already exist
if not os.path.exists('img'):
    os.makedirs('img')

# Send a request to the webpage
response_text = requests.get(webpage_url, headers=headers, timeout=15).text

# Parse the HTML content of the webpage
html_dom = etree.HTML(response_text)

# Find all thumbnail links
thumbnail_links = html_dom.xpath('//figure[@class="UniversalGifListItem clickable"]/a/@href')

print(thumbnail_links)

# Counter to limit downloads to 10
download_count = 0
max_downloads = 10

# Iterate through all the thumbnail links
for link in thumbnail_links:
    if download_count >= max_downloads:
        break  # Stop if the limit is reached

    # Construct the full URL for the thumbnail detail page
    detail_page_url = "https://tenor.com/" + link
    
    # Send a request to the thumbnail detail page
    detail_response_text = requests.get(detail_page_url, headers=headers, timeout=15).text

    # Parse the detail page HTML to find the actual image source
    detail_html_dom = etree.HTML(detail_response_text)
    image_src = detail_html_dom.xpath('//div[@class="Gif"]/img/@src')[0]

    # Download the image using the source URL
    image_response = requests.get(image_src, headers=headers, timeout=3)
    
    # Extract the image file name from the URL
    image_name = image_src.split('/')[-1]
    
    # Save the image in the 'img' folder
    image_path = os.path.join('img', image_name)
    with open(image_path, 'wb') as file:
        file.write(image_response.content)
    
    print(f"Downloaded successfully: {image_name}")

    # Increment the counter
    download_count += 1
