import cv2
import numpy as np
import serial
import threading
import time

stop_Cascade = cv2.CascadeClassifier('stopsign_classifier.xml')
speed_Cascade = cv2.CascadeClassifier('haarCascade.xml')
yield_Cascade = cv2.CascadeClassifier('yield.xml')
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('Alert.avi', fourcc, 10.0, (640,480))
ser = serial.Serial("COM6", 9600, timeout=1)

cap = cv2.VideoCapture(0)
stop_sign=False
speed_sign=False
yield_sign=False

while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #Detecing the pannels
        stop = stop_Cascade.detectMultiScale(gray,1.3,5)#Part of detection
        speed = speed_Cascade.detectMultiScale(gray, 1.3, 5)
        yield_sign = yield_Cascade.detectMultiScale(gray, 1.3, 5)
        for(x,y,w,h) in stop :
            cv2.rectangle(img,(x,y),(x+w,y+h),(100,100,0) , 2) # draw the rectangle around the yield sign
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,'Stop',(x , y), font,1 ,(0,0,255), 2 , cv2.LINE_AA) #write in front of the detected object
            stop_sign =True
            if stop_sign:
                print("Stop Ahead")
                ser.write('t')
        for(ex,ey,ew,eh) in speed :
            cv2.rectangle(img, (ex, ey), (ex + ew, ey + eh), (100, 100, 0), 2)  # draw the rectangle around the yield sign
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, 'Watch your speed"SPEED LIMIT"', (ex, ey), font, 1, (0, 0, 255), 3,cv2.LINE_AA)  # write in front of the detected object
            speed_sign=True
            if speed_sign:
                print("Speed Limit")
                ser.write('s')
        for(gx,gy,gw,gh) in yield_sign :
            cv2.rectangle(img, (gx, gy), (gx + gw, gy + gh), (100, 100, 0), 2)  # draw the rectangle around the yield sign
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, 'Yield', (gx, gy), font, 1, (0, 0, 255), 3,cv2.LINE_AA)  # write in front of the detected object
            yeild_Sign = True
            if yeild_Sign:
                print("Yield Ahead")
                ser.write('Y')


        cv2.imshow('img',img)
        # out.write(img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
cap.release()
# out.release()
cv2.destroyAllWindows()