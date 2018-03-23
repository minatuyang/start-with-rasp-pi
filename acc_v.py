from init.iot10086 import Iot10086
import logging  
import os
import warnings
import datetime
import imutils
import time
import cv2
import socket
import numpy

def acc_video():
    warnings.filterwarnings("ignore")
    
##    print datetime.datetime.now()
##    print "socket loading......"
##    address=('192.168.1.8',8002)
##    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
##    sock.connect(address)
##    print "socket ready"

    print '\n'
    print datetime.datetime.now()
    print "OneNet loading......"
    apikey ='XkNWn=bzWQ2hF1BtWDncnwjrtd0='
    apiurl='http://api.heclouds.com/devices/25686644/datapoints'
    iot = Iot10086(apikey,apiurl)
    print "OneNet ready"

    encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]#encode initial
    avg=None
    people=0
    temp=0
    tim_i=0

    print datetime.datetime.now()
    print "complete"
    print '\n'
    
    cap = cv2.VideoCapture("vtest.avi")
    
    while True:
        ret, frame = cap.read()
        people=0
        
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        gray=cv2.GaussianBlur(gray,(21,21),0)

        if avg is None:#initial the avg
            print "creating background model..."
            avg=gray.copy().astype("float")
            continue
        cv2.accumulateWeighted(gray,avg,0.5)
        frameDelta=cv2.absdiff(gray,cv2.convertScaleAbs(avg))

        ret,thresh=cv2.threshold(frameDelta,5,255,
                                 cv2.THRESH_BINARY)#5 for deltathresh
        thresh=cv2.dilate(thresh,None,iterations=2)
        (cnts,a,b)=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,
                                  cv2.CHAIN_APPROX_SIMPLE)
        
        for c in a:#counting the contours
            if cv2.contourArea(c)<5000:#5000 for minarea
                continue
            (x,y,w,h)=cv2.boundingRect(c)#draw the rectangle
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            people=people+1#count number
        print people

        timestamp=datetime.datetime.now()#putText
        ts=timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
        cv2.putText(frame,str(people),(10,20),
                    cv2.FONT_HERSHEY_SIMPLEX,0.35,(255,255,255),1)
        cv2.putText(frame,ts,(10,frame.shape[0]-1),
                    cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1)

        if tim_i==10:#post Onenet,freq=10loop per text
            tim_i=0;
            iot_post_status=iot.set_data("current_num",people)
            print datetime.datetime.now()
            print iot_post_status
        tim_i+=1

##        result, imgencode = cv2.imencode('.jpg',frame,encode_param)#post socket
##        data=numpy.array(imgencode)
##        stringData = data.tostring()
##        sock.send(str(len(stringData)).ljust(16));
##        sock.send(stringData);
        cv2.imshow('123',frame)
        key = cv2.waitKey(100)&0xff#esc exit
        if key==27:
            break

    #sock.close()    
    cv2.destroyAllWindows()
    
def main():
    acc_video()
if __name__=="__main__":
    main()
