import numpy as np
import cv2

cap = cv2.VideoCapture(0)
print(cap.isOpened())

while(True):
    #Capture frame by frame
    ret, frame = cap.read()
    SKALA_ABU=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('webcam', 255-SKALA_ABU)
    if cv2.waitKey(1) & 0xFF == ord ('m'):
        break

cap.realease()
cv2.destroyAllwindows()

