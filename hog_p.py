import logging  
import os
import warnings
import datetime
import imutils
import time
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import cv2

warnings.filterwarnings("ignore")
def hog_picture():
    img=cv2.imread('123.JPG')

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    (rects, weights) = hog.detectMultiScale(img, winStride=(4,4),
                                            padding=(8,8), scale=0.5)
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
    for (xA, yA, xB, yB) in pick:
        cv2.rectangle(img, (xA, yA), (xB, yB), (0, 255, 0), 2)
    while True:
        cv2.imshow("After NMS", img)
        if cv2.waitKey(100)==27:
            break
    cv2.destroyAllWindows() 
def main():
    hog_picture()
if __name__=="__main__":
    main()
