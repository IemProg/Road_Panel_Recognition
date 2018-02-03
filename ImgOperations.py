import cv2
import numpy as np
img1 = cv2.imread('Yero team.png',cv2.COLOR_BGR2GRAY)
img = cv2.imread('Yero team.png',cv2.IMREAD_GRAYSCALE)
ret, threshold = cv2.threshold(img,1,255, cv2.THRESH_BINARY)
cv2.imshow('threshold',threshold)
cv2.imshow('IMAGE',img)
cv2.waitKey(0)
cv2.destroAllWindows()