import cv2 as cv
import numpy as np
cap = cv.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if ret:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        gray = np.float32(gray) 
        dst = cv.cornerHarris(gray,5,3,.2)
        dst = cv.dilate(dst,None)
        frame[dst>0.02 *dst.max()] = [0,255,255] # color all pixels red that are corner pixed based on threshold
        cv.imshow('corner detection',frame)
        if cv.waitKey(1) == ord('q'):
            break
    else:
        print('camera not working')
        break
cap.release()
cv.destroyAllWindows()