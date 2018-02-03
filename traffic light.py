import cv2
import numpy as np

trafficLight_Cascade = cv2.CascadeClassifier('traffic_light.xml')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Traffic lightCedez passage.avi', fourcc, 10.0, (640,480))

cap = cv2.VideoCapture(0)
threshold = 150

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    trafficLight = trafficLight_Cascade.detectMultiScale(gray,1.1,5)


    for (x_pos, y_pos, width, height) in trafficLight :
        roi = gray[y_pos + 10:y_pos + height - 10, x_pos + 10:x_pos + width - 10]
        mask = cv2.GaussianBlur(roi, (25, 25), 0)
        (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(mask)

    # check if light is on
    #  if maxVal - minVal > threshold:
    #     cv2.circle(roi, maxLoc, 5, (255, 0, 0), 2)

        # Red light
        if 1.0 / 8 * (height - 30) < maxLoc[1] < 4.0 / 8 * (height - 30):
            cv2.putText(img, 'Red', (x_pos + 5, y_pos - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)


        # Green light
        elif 5.5 / 8 * (height - 30) < maxLoc[1] < height - 30:
            cv2.putText(img, 'Green', (x_pos + 5, y_pos - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow('img',img)
    out.write(img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
out.release()
cv2.destroyAllWindows()


