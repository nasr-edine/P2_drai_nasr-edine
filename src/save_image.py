import requests
import os


def dowload_image(image_url, session):
    current_directory = '../'
    image_dir = "images"
    path = os.path.join(current_directory, image_dir)
    if not os.path.exists(path):
        os.mkdir(path)
    response = requests.get(image_url)
    # response = session.get(image_url)
    image_path = os.path.join(path, os.path.basename(image_url))
    file = open(image_path, "wb")
    file.write(response.content)
    file.close()
