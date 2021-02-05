import os
import P2_06_codesource


def dowload_image(image_url):
    current_directory = '../'
    image_dir = "images"
    path = os.path.join(current_directory, image_dir)
    if not os.path.exists(path):
        os.mkdir(path)
    response = P2_06_codesource.s.get(image_url)
    image_path = os.path.join(path, os.path.basename(image_url))
    file = open(image_path, "wb")
    file.write(response.content)
    file.close()
