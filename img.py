import os
from PIL import Image
from random import randint
#git_path = "https://raw.githubusercontent.com/workthe1/image_repository/refs/heads/main/"
path = 'image'
def open_image(img):
    if os.path.isfile(img):
        with open(img, 'rb') as image_file:
            image = Image.open(image_file)
            image.show()


def image_path():
    img_path = []
    i = 0
    for file_name in os.listdir(path):
        for file in os.listdir(os.path.join(path, file_name)):
            img_path.append(os.path.join(path, file_name, file))
            i += 1
    return img_path,i


if __name__ == '__main__':
    path,i = image_path()
    num = randint(0,i)
    open_image(path[num])




