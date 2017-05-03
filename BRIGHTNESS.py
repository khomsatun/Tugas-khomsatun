import numpy as np
import cv2

cap = cv2.VideoCapture(0)
print(cap.isOpened())

while(True):
    #Capture frame by frame
    ret, frame = cap.read()
    BRIGHTNESS = cv2.addWeighted(frame,2.0, np.zeros(frame.shape, frame.dtype), 0, 40)
    cv2.imshow('webcam',BRIGHTNESS)
    if cv2.waitKey(1) & 0xFF == ord ('m'):
        break

cap.realease()
cv2.destroyAllwindows()

