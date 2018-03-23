# -*- coding: utf-8 -*-
import urllib2
import urllib
import time
import json
import jsonpath
import cv2
import datetime
from init.facepp import FacePP
def facepp_picture():
    print datetime.datetime.now()
    http_url='https://api-cn.faceplusplus.com/humanbodypp/v1/detect'
    key = "oTuSwUW0h1vEUp57MHCsvfjp3-dg7U_f"
    secret = "FMmBi2OnH4pv3JC4GlMyDREuFeRx3Pub"
    image=cv2.imread('123.JPG')
    boundary = '----------%s' % hex(int(time.time() * 1000))

    fpp=FacePP(http_url,key,secret,boundary)
    req=fpp.init('123.JPG')
    (width_list,top_list,height_list,left_list)=fpp.receive(req)

    if width_list==False or width_list==0:
        print 'error'
    else:
        for i in range(0,len(width_list)):
            image=cv2.rectangle(image,(left_list[i],top_list[i]),
                                (left_list[i]+width_list[i],
                                 top_list[i]+height_list[i]),
                                (0,255,0),
                                2)
        print datetime.datetime.now()
        while True:
            cv2.imshow("123",image)
            key = cv2.waitKey(1)&0xff
            if key==27:
                break
        cv2.destroyAllWindows()
        
def main():
    facepp_picture()
if __name__=="__main__":
    main()
