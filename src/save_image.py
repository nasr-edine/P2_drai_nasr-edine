import requests
import os 

def dowload_image(image_url):
    current_directory = '../'
    image_dir = "images"
    # image_url = 'http://books.toscrape.com/media/cache/6d/41/6d418a73cc7d4ecfd75ca11d854041db.jpg'

    path = os.path.join(current_directory, image_dir)
    if not os.path.exists(path):
        os.mkdir(path)

    response = requests.get(image_url)
    image_path = os.path.join(path, os.path.basename(image_url))
    file = open(image_path, "wb")
    file.write(response.content)
    file.close()

# dowload_image('http://books.toscrape.com/media/cache/6d/41/6d418a73cc7d4ecfd75ca11d854041db.jpg')