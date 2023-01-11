import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont

# You can use as test URL:
# https://www.instagram.com/p/CnQY4y7K1zQ/?utm_source=ig_web_copy_link

def repost(url):
    # Fetch the page source code
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Extract the image URL
    image_url = soup.find('meta', property='og:image')['content']

    # Prompt the user for permission
    permission = input('Do you have permission from the owner to repost this image? (y/n)')

    if permission.lower() == 'y':
        # Download the image
        image = requests.get(image_url, stream=True)
        with open('repost.jpg', 'wb') as out_file:
            out_file.write(image.content)
        print('Image saved as repost.jpg')
    else:
        print('Cancelling repost')

url = input('Enter the URL of the post:')
repost(url)

# Open the image
image = Image.open("repost.jpg")

# Create an ImageDraw object
draw = ImageDraw.Draw(image)

# Set font and font size
font = ImageFont.load_default()

# Position for the repost icon
x, y = 10, image.height - 30

# Draw the repost icon text
draw.text((x, y), "repost", font=font, fill=(255, 255, 255))

# Save the image with the repost icon
image.save("reposted.jpg")

