import cv2
from random import randrange

#pre trained face data 
trained_face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#import image and then change it to black and white
#img = cv2.imread("MSM.png")
#instead of picture using live video
cap = cv2.VideoCapture(1)


while True:
    successful_frame_read, frame = cap.read()
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face.detectMultiScale(grayscaled_img)
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 10)

    cv2.imshow("Spiritual Leader", frame)
    key = cv2.waitKey(1)
    if key==81 or key==113:
        break


cap.release()
print("Code Works")