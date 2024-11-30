import requests  # Import the requests module to handle HTTP requests
import os  # Import the os module to handle file operations

# Headers for the HTTP request to mimic a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36'
}

# Paste the image URL
image_url = "https://media.tenor.com/9Sm5usHiEOkAAAAM/cat-meme.gif"

# Extract the file name from the URL
image_name = image_url.split('/')[-1]

# Create a folder named 'img' if it doesn't already exist
if not os.path.exists('img'):
    os.makedirs('img')

# Get the image data
image_response = requests.get(image_url, headers=headers, timeout=3)

# Save the image to the 'img' folder
image_path = os.path.join('img', image_name)
with open(image_path, 'wb') as file:
    file.write(image_response.content)

print("Download successful. Image saved to 'img' folder.")
