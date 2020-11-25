import cv2 as cv

face_cascade = cv.CascadeClassifier()
smile_cascade = cv.CascadeClassifier()
if not face_cascade.load('computer_vision/models/face1.xml'):
    print('could not load the AI face model')
if not smile_cascade.load('computer_vision/models/smile.xml'):
    print('could not load the AI smile model')

def detect_n_display(frame):
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    gray = cv.equalizeHist(gray)

    faces = face_cascade.detectMultiScale(gray)
    for (x,y,w,h) in faces:
        center = (x + w//2, y+ h//2)
        frame = cv.ellipse(frame,center,(w//2,h//2),0,0,360,(0,255,255),3)
    
        faceROI = gray[y:y+h,x:x+w]
        coloredROI = frame[y:y+h,x:x+w]
        smile = smile_cascade.detectMultiScale(faceROI,1.8,20)
        for (sx,sy,sw,sh) in smile:
            cv.rectangle(coloredROI,(sx,sy),((sx+sw),sy+sh),(0,255,0),3),
    
    cv.imshow("yop",frame)

cap = cv.VideoCapture(1)
while True:
    ret, frame = cap.read()
    if ret:
        detect_n_display(frame)
        if cv.waitKey(1) == ord('q'):
            break
    else:
        print('camera not working')
        break
cap.release()
cv.destroyAllWindows()