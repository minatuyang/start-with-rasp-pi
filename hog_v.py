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
def hog_video():
    cap = cv2.VideoCapture("vtest.avi")

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    while True:
        ret, frame = cap.read()
        image=frame
        #cv2.imshow("capture",image)
        orig = image.copy()
        (rects, weights) = hog.detectMultiScale(image, winStride=(4,4),
                                                padding=(8,8), scale=0.5)
        rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
        pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
        
        for (xA, yA, xB, yB) in pick:
                cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

        cv2.imshow("After NMS", image)

        if cv2.waitKey(100)==27:
            break


    cap.release()
    cv2.destroyAllWindows() 
def main():
    hog_video()
if __name__=="__main__":
    main()
