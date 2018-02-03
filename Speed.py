import cv2
import numpy as np


stop_Cascade = cv2.CascadeClassifier('stop_sign.xml')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('stop sign.avi', fourcc, 10.0, (640,480))

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    stop = stop_Cascade.detectMultiScale(gray,1.3,5)#detect the stop sign
    for(x,y,w,h) in stop :
        cv2.rectangle(img,(x,y),(x+w,y+h),(100,100,0) , 2) # draw the rectangle around the yield sign
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'Stop',(x , y), font,1 ,(0,0,255), 2 , cv2.LINE_AA) #write in front of the detected object

    cv2.imshow('img',img)
    out.write(img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
out.release()
cv2.destroyAllWindows()


