import cv2
import numpy as np

def empty(a):
    pass
cv2.namedWindow("trackBars")
cv2.resizeWindow("trackBars",640,240)
cv2.createTrackbar("Hue Min","trackBars",104,179,empty)
cv2.createTrackbar("Hue Max","trackBars",128,179,empty)
cv2.createTrackbar("Sat Min","trackBars",78,255,empty)
cv2.createTrackbar("Sat Max","trackBars",240,255,empty)
cv2.createTrackbar("Val Min","trackBars",67,255,empty)
cv2.createTrackbar("Val Max","trackBars",255,255,empty)

while True:
    img = cv2.imread('resources/bmw.jpg')
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","trackBars")
    h_max = cv2.getTrackbarPos("Hue Max","trackBars")
    s_min = cv2.getTrackbarPos("Sat Min","trackBars")
    s_max = cv2.getTrackbarPos("Sat Max","trackBars")
    v_min = cv2.getTrackbarPos("Val Min","trackBars")
    v_max = cv2.getTrackbarPos("Val Max","trackBars")
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgFinal = cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("normal", img)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("mask", mask)
    cv2.imshow("res", imgFinal)
    cv2.waitKey(1)
