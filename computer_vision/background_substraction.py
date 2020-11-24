import cv2 as cv

cap = cv.VideoCapture(1)
mask = cv.createBackgroundSubtractorMOG2(history=105)

while True:
    ret, frame = cap.read()
    if ret:
        bgmask = mask.apply(frame)
        cv.imshow('bg example',bgmask)
        if cv.waitKey(1) == ord('q'):
            break
    else:
        print('camera not working')
        break
cap.release()
cv.destroyAllWindows()
