import cv2 as cv
import numpy as np

filename = 'image_editing/cubes.png'
img = cv.imread(filename)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = np.float32(gray) 
dst = cv.cornerHarris(gray,5,3,.2)
dst = cv.dilate(dst,None)
img[dst>0.02 *dst.max()] = [0,0,255] # color all pixels red that are corner pixed based on threshold
cv.imshow('corner detection',img)
cv.waitKey(0)