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
import urllib2
import urllib
import json
import jsonpath
from init.facepp import FacePP
def facepp_video():
    warnings.filterwarnings("ignore")

    cap = cv2.VideoCapture("vtest.avi")

    http_url='https://api-cn.faceplusplus.com/humanbodypp/beta/detect'
    key = "oTuSwUW0h1vEUp57MHCsvfjp3-dg7U_f"
    secret = "FMmBi2OnH4pv3JC4GlMyDREuFeRx3Pub"
    boundary = '----------%s' % hex(int(time.time() * 1000))
    fpp=FacePP(http_url,key,secret,boundary)

    while True:
        ret, frame = cap.read()
        image = imutils.resize(frame,1080,2000)
        cv2.imwrite('temp.JPG',image)
        
        req=fpp.init('temp.JPG')
        (width_list,top_list,height_list,left_list)=fpp.receive(req)
        
        if width_list==False or width_list==0:
            continue
        
        for i in range(0,len(width_list)):
            image=cv2.rectangle(image,
                                (left_list[i],top_list[i]),
                                (left_list[i]+width_list[i],
                                 top_list[i]+height_list[i]),
                                (0,255,0),
                                2)
        cv2.imshow("After NMS",image)
            
        if cv2.waitKey(100)==27:
            break

    cap.release()
    cv2.destroyAllWindows()

def main():
    facepp_video()
if __name__=="__main__":
    main()
