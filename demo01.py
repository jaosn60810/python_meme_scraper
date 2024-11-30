import requests  # Import the requests module to handle HTTP requests
import os  # Import the os module for handling file storage

# Define headers to simulate a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36'
}

# Paste the image URL
src = "http://img.soogif.com/0Hy0iUj4T0hwELRUd5umISJJUkOOI7OM.gif"

# Define the file name based on the image URL
imgName = src.split('/')[-1]

# Fetch the image data
imgRes = requests.get(src, headers=headers, timeout=3)

# Save the image to the local system
with open(imgName, 'wb') as f:
    f.write(imgRes.content)

print("Download successful")
