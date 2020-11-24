from PIL import Image, ImageEnhance

img = Image.open('image_editing/batman.jpg')
img.show()

colorEnc = ImageEnhance.Color(img)

for f in range(-4,5):
    colorEnc.enhance(f).show()

