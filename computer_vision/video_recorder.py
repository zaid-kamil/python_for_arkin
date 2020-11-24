import cv2 as cv

cap = cv.VideoCapture(1)

# define the video settings
codec = cv.VideoWriter_fourcc(*'DIVX')
out = cv.VideoWriter('output.avi',codec, 24, (640,480))

while True:
    ret, frame = cap.read()
    if ret:
        cv.imshow("video",frame)
        out.write(frame)
        if cv.waitKey(1) == ord('q'):
            break
    else:
        print('cant recieve the frame from camera')
        break
cap.release()
out.release()
cv.destroyAllWindows()