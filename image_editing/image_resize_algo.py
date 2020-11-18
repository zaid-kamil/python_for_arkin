from PIL import Image

img = Image.open('image_editing/batman2.jpg')
img.show()
x1 = img.width * 2
y1 = img.height * 2

img.resize((x1,y1)).show()
img.resize((x1,y1), Image.LINEAR).show()
img.resize((x1,y1), Image.ANTIALIAS).show()
img.resize((x1,y1), Image.ADAPTIVE).show()

img.resize((x1,y1)).save('batman_3.gif')