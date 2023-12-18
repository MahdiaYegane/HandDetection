import numpy as np
import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
from matplotlib import pyplot as plt


cap=cv.VideoCapture(0)
detector=HandDetector(detectionCon=0.5,maxHands=1)

while True:
    rec,frame=cap.read()
    hand,frame=detector.findHands(frame)
    cv.imshow("i",frame)
    keyExit=cv.waitKey(5)& 0xFF
    if keyExit==27:
        break
    
cv.destroyAllWindows()
cap.release()

