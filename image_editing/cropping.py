from PIL import Image, ImageEnhance

img = Image.open('image_editing/batman.jpg')
box = (400,100,800,400)
region = img.crop(box)
region.show()

img.paste(region,(0,0,400,300))
img.show()