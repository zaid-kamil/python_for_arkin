import cv2

cam = cv2.VideoCapture(1)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,400)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,400)
while True:
    state,frame = cam.read()
    if state:
        framex10 = frame // 10 + 100 # u can do any equation in math on each pixels
        cv2.imshow("Me - the person",frame)
        cv2.imshow("Me - the person 10 times",framex10)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()