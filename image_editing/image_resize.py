from PIL import Image

original = Image.open('image_editing/batman.jpg')
original.show()
print(f'original size: {original.size}')
y = original.height // 2 # need it as integers
x = original.width // 2
half_img = original.resize((x,y))
half_img.show()
small_img = original.resize((100,100))
small_img.show()
mega_img = original.resize((original.width*5, original.height*5))
mega_img.show()
print(mega_img.size)


