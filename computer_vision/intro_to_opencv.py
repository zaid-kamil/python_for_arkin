import cv2

cam = cv2.VideoCapture(1)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,400)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,400)
while True:
    state,frame = cam.read()
    if state:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Me - the person",frame)
        cv2.imshow("Me - the gray person",gray)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()