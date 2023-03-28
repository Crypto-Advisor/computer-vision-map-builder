import cv2 as cv
import pathlib

#load the model
net = cv.dnn.readNet("dnn_model/yolov4-tiny.weights", "dnn_model/yolov4-tiny.cfg")
model = cv.dnn_DetectionModel("dnn_model/yolov4-tiny.weights", "dnn_model/yolov4-tiny.cfg")
model.setInputParams(size=(320, 320), scale=1/255)

#load the classes
classes = []
with open("dnn_model/classes.txt", "r") as f:
    classes = f.read().splitlines()

#load the camera
camera = cv.VideoCapture(0)

while camera.isOpened():
    #get camera frame
    _, frame = camera.read()

    #pass the frame to the model
    (class_ids, scores, bboxes) = model.detect(frame)
    
    #display the output as a box around the object
    for class_id, score, bbox in zip(class_ids, scores, bboxes):
        cv.putText(frame, classes[class_id], (bbox[0], bbox[1] - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv.rectangle(frame, bbox, (255, 255, 0), 2)
    
    #display the frame
    cv.imshow("Collision Detection", frame)
    
    #quit the program if q is pressed
    if cv.waitKey(1) == ord("q"):
        break

#release the camera and close all windows
camera.release()
cv.destroyAllWindows()