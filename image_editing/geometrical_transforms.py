from PIL import Image

img = Image.open('image_editing/batman.jpg')
img.show()

# simple transform
img.rotate(45).show()
img.rotate(45,fillcolor='white').show()

# transposing an image
img.transpose(Image.FLIP_LEFT_RIGHT).show()
img.transpose(Image.FLIP_TOP_BOTTOM).show()
img.transpose(Image.ROTATE_90).show()
img.transpose(Image.ROTATE_180).show()
img.transpose(Image.ROTATE_270).show()

# make img black and white
img.convert('L').show()