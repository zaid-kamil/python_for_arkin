from PIL import Image
import os

path = 'E:/office'

content = os.listdir(path)
images = []
# filter only images
for item in content:
    if item.lower().endswith('.jpg') or item.lower().endswith('.png') or item.lower().endswith('.jpeg'):
        images.append(item)

# resize all images and store it in folder
storage = 'resized_images'

for file in images:
    address = path + '/' + file
    saveaddr = storage + '/' + file
    img = Image.open(address)
    img.thumbnail((64,64))
    img.save(saveaddr)
