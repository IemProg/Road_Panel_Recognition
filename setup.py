import cv2
import numpy as np
import serial
import threading
from time import sleep
stop_Cascade = cv2.CascadeClassifier('stop_sign.xml')
speed_Cascade = cv2.CascadeClassifier('haarCascade.xml')
yield_Cascade = cv2.CascadeClassifier('yield.xml')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Alert.avi', fourcc, 10.0, (640,480))
#ser = serial.Serial("COM6", 9600, timeout=1)

cap = cv2.VideoCapture(0)

speed_Sign = False
stop_Sign = False
yeild_Sign = False
"""def process():
     while True:
         print ('f')
         global stop_Sign
         if  stop_Sign:
             print("Stop ahead")
             ser.write(b's')
             ser.flush()
         else :
             ser.write(b'x')
             print ("dfdg")

s=threading.Thread(target=process)
s.start()
"""
def read():
    while True:
        data = ser.read(9999)
        if len(data) > 0:
            print 'Got:', data

        sleep(0.5)
        print 'not blocked'

while True:
        ser = serial.Serial("COM6", 9600, timeout=1)
        if ser.isOpen():
            ser.close()
        ser.open()
        t1 = threading.Thread(target=read, args=())
        t1.start()

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
            stop_Sign = True
            if data[0] == "j":
                print("Stop ahead")
                ser.write('s')
        for(ex,ey,ew,eh) in speed :
            cv2.rectangle(img, (ex, ey), (ex + ew, ey + eh), (100, 100, 0), 2)  # draw the rectangle around the yield sign
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, 'Watch your speed"SPEED LIMIT"', (ex, ey), font, 1, (0, 0, 255), 3,cv2.LINE_AA)  # write in front of the detected object                speed_Sign = True
            if speed_Sign:
                print("Watch your speed'SPEED LIMIT'")
                ser.write('w')

        for(gx,gy,gw,gh) in yield_sign :
            cv2.rectangle(img, (gx, gy), (gx + gw, gy + gh), (100, 100, 0), 2)  # draw the rectangle around the yield sign
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, 'Yield', (gx, gy), font, 1, (0, 0, 255), 3,cv2.LINE_AA)  # write in front of the detected object
            yeild_Sign = True
            if yeild_Sign and data =="j" :
                print("Yield Ahead")
                ser.write('y')

        cv2.imshow('img',img)
        out.write(img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
        ser.close()

cap.release()
out.release()
cv2.destroyAllWindows()


