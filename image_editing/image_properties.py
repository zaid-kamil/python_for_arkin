from PIL import Image,ImageFilter

img = Image.open('function_based_coding/images/tank1.png')
print(img.size) # tuple
print(img.filename)
print(img.mode)
print(img.format)
print(img.height)
print(img.width)
