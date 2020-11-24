from PIL import Image
img = Image.open('image_editing/batman.jpg')
bg = Image.open('image_editing/bg.jpg')

bg = bg.resize(img.size)

Image.blend(img,bg,.9).show()
