import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.avi')
 
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
back = cv2.createBackgroundSubtractorGMG()
 
while(1):
ret, frame = cap.read()
 
mask = back.apply(frame)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

cv2.imshow('frame',fgmask)
k = cv2.waitKey(30) & 0xff
if k == 27:
   break
cap.release()
cv2.destroyAllWindows()
