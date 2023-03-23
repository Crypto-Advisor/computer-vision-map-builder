import cv2 as cv
import pathlib

cascade_path = pathlib.Path(cv.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"

clf = cv.CascadeClassifier(str(cascade_path))


camera = cv.VideoCapture(1)

while camera.isOpened():
    _, frame = camera.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = clf.detectMultiScale(
        gray, 
        scaleFactor=1.1, 
        minNeighbors=4,
        minSize=(30, 30),
        flags=cv.CASCADE_SCALE_IMAGE
    )
    
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
        
    cv.imshow("Face Detection", frame)
    
    if cv.waitKey(1) == ord("q"):
        break

camera.release()
cv.destroyAllWindows()

