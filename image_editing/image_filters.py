from PIL import Image, ImageFilter
address = input("give me address::")
img = Image.open(address)
img.filter(ImageFilter.CONTOUR).show() # outlines with white
img.filter(ImageFilter.BLUR).show() # blur the image lightly
img.filter(ImageFilter.DETAIL).show() # highlight few pixels in images
img.filter(ImageFilter.EDGE_ENHANCE).show() # enhance the color of edges
img.filter(ImageFilter.FIND_EDGES).show()  # outline with black
img.filter(ImageFilter.SMOOTH).show() # dull pixels to smoothen image
img.filter(ImageFilter.SHARPEN).show() # increase color in pixels
img.filter(ImageFilter.MinFilter(3)).show() # increase black lines width
img.filter(ImageFilter.MaxFilter(3)).show() # increase white lines width
img.filter(ImageFilter.MedianFilter()).show() 
img.filter(ImageFilter.GaussianBlur(10)).show() # blurs image using gaussian eq
img.filter(ImageFilter.GaussianBlur(100)).show() # same as above with different value
img.filter(ImageFilter.EMBOSS).show()